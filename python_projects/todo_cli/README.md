# To-Do CLI (Python OOP + JSON)

A simple command-line To-Do List Manager written in **Python**.  
It demonstrates **object-oriented programming**, **JSON persistence**, and **argparse** CLI design.

---

## Features

- Add tasks with optional due date and tags
- List tasks (all, open, or done)
- Mark tasks as done/undone
- Delete tasks
- Stores data in a JSON file (`data/todo.json`)

---

## Requirements

- Python 3.10+

---

## Installation

```bash
git clone https://github.com/vinimych-ai/todo-cli.git
cd todo-cli
````
___

## Usage

### Add a task

```bash
python todo.py add "Write README" --due 2025-10-10 --tags docs writing
```

### List tasks

```bash
python todo.py list --status all
python todo.py list --status open
python todo.py list --status done
```

### Mark task as done / undone

```bash
python todo.py done <TASK_ID>
python todo.py undone <TASK_ID>
```

### Delete task

```bash
python todo.py delete <TASK_ID>
```

> In the commands above, `<TASK_ID>` is the 8-character id shown by `list` (don’t include the angle brackets).

---

## Example Output

```
ID        Done  Title                          Due        Tags
--------------------------------------------------------------------------------
de8b4212       Write README                    2025-10-10 docs,writing
f17a9c4d  ✔    Refactor parser                              code
```

---

## Project Structure

```
todo_cli/
├─ tasks.py       # Backend logic (Task + TaskManager)
├─ todo.py        # CLI interface (argparse)
├─ data/
│  └─ todo.json   # Auto-created JSON storage
└─ README.md
```

---

## License

MIT License

```

If you want a `.gitignore` too, say the word and I’ll drop a ready-to-paste one.
::contentReference[oaicite:0]{index=0}
```
