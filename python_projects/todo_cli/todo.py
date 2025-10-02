import argparse
from pathlib import Path
from tasks import TaskManager

def print_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    print(f"{'ID':8}  {'Done':4}  {'Title':30}  {'Due':10}  {'Tags'}")
    print("-"*80)
    for t in tasks:
        done = "✔" if t.done else " "
        title = (t.title[:27] + "...") if len(t.title) > 30 else t.title
        due = t.due or ""
        tags = ",".join(t.tags or [])
        print(f"{t.id:8}  {done:4}  {title:30}  {due:10}  {tags}")

def get_manager(storage_arg: str | None):
    storage = Path(storage_arg) if storage_arg else Path("data/todo.json")
    return TaskManager(storage)

def main():
    parser = argparse.ArgumentParser(description="To-Do CLI (OOP + JSON)")
    parser.add_argument("--storage", help="Path to JSON storage (default: data/todo.json)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # add
    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("title", help="Task title")
    p_add.add_argument("--due", help="Due date YYYY-MM-DD")
    p_add.add_argument("--tags", nargs="*", help="Tags, space-separated")

    # list
    p_list = sub.add_parser("list", help="List tasks")
    p_list.add_argument("--status", choices=["all", "open", "done"], default="all")

    # done
    p_done = sub.add_parser("done", help="Mark a task as done")
    p_done.add_argument("id", help="Task id")

    # undone
    p_undone = sub.add_parser("undone", help="Mark a task as NOT done")
    p_undone.add_argument("id", help="Task id")

    # delete
    p_del = sub.add_parser("delete", help="Delete a task")
    p_del.add_argument("id", help="Task id")

    args = parser.parse_args()
    tm = get_manager(args.storage)

    if args.cmd == "add":
        t = tm.add(args.title, due=args.due, tags=args.tags)
        print(f"Added: {t.id} — {t.title}")

    elif args.cmd == "list":
        print_tasks(tm.list(args.status))

    elif args.cmd == "done":
        t = tm.complete(args.id, True)
        print("Updated." if t else "Not found.")

    elif args.cmd == "undone":
        t = tm.complete(args.id, False)
        print("Updated." if t else "Not found.")

    elif args.cmd == "delete":
        ok = tm.delete(args.id)
        print("Deleted." if ok else "Not found.")

if __name__ == "__main__":
    main()
