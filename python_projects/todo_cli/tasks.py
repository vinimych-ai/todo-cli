from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
from datetime import datetime
from typing import List, Optional
import json
import uuid

DATE_FMT = "%Y-%m-%d"

def parse_date(s: Optional[str]) -> Optional[str]:
    """Normalize to YYYY-MM-DD (or None). Raises if invalid."""
    if not s:
        return None
    return datetime.strptime(s, DATE_FMT).strftime(DATE_FMT)

@dataclass
class Task:
    id: str
    title: str
    created_at: str
    due: Optional[str] = None
    tags: List[str] = None
    done: bool = False

    def to_dict(self) -> dict:
        d = asdict(self)
        d["tags"] = d.get("tags") or []
        return d

    @staticmethod
    def from_dict(d: dict) -> "Task":
        return Task(
            id=d["id"],
            title=d["title"],
            created_at=d["created_at"],
            due=d.get("due"),
            tags=d.get("tags") or [],
            done=bool(d.get("done", False)),
        )

class TaskManager:
    def __init__(self, storage: Path):
        self.storage = storage
        self.storage.parent.mkdir(parents=True, exist_ok=True)
        self.tasks: List[Task] = []
        self._load()

    def _load(self) -> None:
        if self.storage.exists():
            with self.storage.open("r", encoding="utf-8") as f:
                data = json.load(f)
            self.tasks = [Task.from_dict(t) for t in data]
        else:
            self.tasks = []

    def _save(self) -> None:
        with self.storage.open("w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.tasks], f, ensure_ascii=False, indent=2)

    # ------- operations -------

    def add(self, title: str, due: Optional[str] = None, tags: Optional[List[str]] = None) -> Task:
        task = Task(
            id=str(uuid.uuid4())[:8],
            title=title.strip(),
            created_at=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            due=parse_date(due) if due else None,
            tags=tags or [],
            done=False,
        )
        self.tasks.append(task)
        self._save()
        return task

    def list(self, status: str = "all") -> List[Task]:
        if status == "open":
            return [t for t in self.tasks if not t.done]
        if status == "done":
            return [t for t in self.tasks if t.done]
        return list(self.tasks)

    def complete(self, task_id: str, done: bool = True) -> Optional[Task]:
        for t in self.tasks:
            if t.id == task_id:
                t.done = done
                self._save()
                return t
        return None

    def delete(self, task_id: str) -> bool:
        before = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.id != task_id]
        if len(self.tasks) != before:
            self._save()
            return True
        return False
