from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path
from tasks import TaskManager

# Serve files from ./static at the site root ("/")
app = Flask(__name__, static_url_path="", static_folder="static")
tm = TaskManager(Path("data/todo.json"))

# Home page: serves static/index.html
@app.get("/")
def root():
    return send_from_directory(app.static_folder, "index.html")

# API: list tasks (supports ?status=all|open|done and optional &tag=work)
@app.get("/tasks")
def get_tasks():
    status = request.args.get("status", "all")
    tag = request.args.get("tag")
    tasks = tm.list(status)
    if tag:
        t = tag.lower()
        tasks = [x for x in tasks if any(t == s.lower() for s in (x.tags or []))]
    return jsonify([t.to_dict() for t in tasks])

# API: add task
@app.post("/tasks")
def add_task():
    data = request.get_json(force=True, silent=True) or {}
    title = data.get("title", "").strip()
    if not title:
        return {"error": "title is required"}, 400
    t = tm.add(title, due=data.get("due"), tags=data.get("tags") or [])
    return t.to_dict(), 201

# API: mark done / undone
@app.post("/tasks/<task_id>/done")
def mark_done(task_id):
    t = tm.complete(task_id, True)
    return (t.to_dict(), 200) if t else ({"error": "not found"}, 404)

@app.post("/tasks/<task_id>/undone")
def mark_undone(task_id):
    t = tm.complete(task_id, False)
    return (t.to_dict(), 200) if t else ({"error": "not found"}, 404)

# API: delete
@app.delete("/tasks/<task_id>")
def delete_task(task_id):
    ok = tm.delete(task_id)
    return ({"deleted": True}, 200) if ok else ({"error": "not found"}, 404)

if __name__ == "__main__":
    app.run(debug=True)
