# To-Do Manager (CLI + API + Web UI)

A simple Python to-do manager with:
- **Command-line interface (CLI)**
- **Flask REST API**
- **Minimal web UI (HTML/JS)**

Tasks are stored in `data/todo.json`.

---

## Features
- Add, list, complete, undo, and delete tasks
- Filter by **status** (`all`, `open`, `done`)
- Filter by **tag**
- Export tasks to CSV
- REST API endpoints (Flask)
- Simple browser UI (served from Flask)

---

## Requirements
- Python 3.10+
- Install dependencies:
```bash
pip install -r requirements.txt
````

`requirements.txt`:

```
flask>=3.0
```

---

## 📌 CLI Usage

Run commands from the project folder:

```bash
python todo.py add "Write README" --due 2025-10-10 --tags work docs
python todo.py list --status all
python todo.py list --tag work
python todo.py done <TASK_ID>
python todo.py undone <TASK_ID>
python todo.py delete <TASK_ID>
python todo.py export --csv tasks.csv --status all
```

---

## 🌐 API Usage

Start the server:

```bash
python app.py
```

Runs at: `http://127.0.0.1:5000/`

### Endpoints

* `GET /tasks?status=all&tag=work` → list tasks
* `POST /tasks` → add task (JSON body: `{ "title": "...", "due": "YYYY-MM-DD", "tags": ["tag1","tag2"] }`)
* `POST /tasks/<id>/done` → mark done
* `POST /tasks/<id>/undone` → mark not done
* `DELETE /tasks/<id>` → delete task

### PowerShell examples

```powershell
# Add task
Invoke-RestMethod -Method POST -Uri http://127.0.0.1:5000/tasks `
  -ContentType "application/json" `
  -Body (@{ title="API task"; due="2025-10-10"; tags=@("api","demo") } | ConvertTo-Json)

# List tasks
Invoke-RestMethod -Method GET -Uri "http://127.0.0.1:5000/tasks?status=all"

# Mark done
$id = (Invoke-RestMethod -Uri "http://127.0.0.1:5000/tasks?status=all")[0].id
Invoke-RestMethod -Method POST -Uri "http://127.0.0.1:5000/tasks/$id/done"

# Delete
Invoke-RestMethod -Method DELETE -Uri "http://127.0.0.1:5000/tasks/$id"
```

---

## 💻 Web UI

1. Run the API:

```bash
python app.py
```

2. Open in your browser:

```
http://127.0.0.1:5000/
```

The web page lets you:

* Add tasks
* View and filter tasks
* Mark tasks as done/undone
* Delete tasks

---

## 📂 Project structure

```
todo_cli/
├─ tasks.py        # Core Task + TaskManager
├─ todo.py         # CLI interface
├─ app.py          # Flask API + serves web UI
├─ static/
│  └─ index.html   # Browser UI
├─ data/
│  └─ todo.json    # Storage file
├─ tests/
│  └─ test_tasks.py
├─ requirements.txt
└─ README.md
```

```

---

Would you like me to also add a **screenshot section** (with placeholders like `![screenshot](docs/ui.png)`), so you can drop in a picture of your running web UI later?
```
