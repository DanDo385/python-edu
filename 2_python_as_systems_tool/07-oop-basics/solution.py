"""
Project 07: OOP Basics - SOLUTION

Reference implementation showing:
- class design with instance state,
- object mutation through methods,
- composition (TodoList owns Task objects).
"""


class Task:
    """Simple task object with mutable completion state."""

    def __init__(self, title: str):
        if not isinstance(title, str):
            raise TypeError("title must be a string")

        cleaned = title.strip()
        if not cleaned:
            raise ValueError("title cannot be blank")

        self.title = cleaned
        self.done = False

    def mark_done(self) -> None:
        # Mutating object state is visible through every reference to this object.
        self.done = True


class TodoList:
    """Collection object that owns Task instances."""

    def __init__(self):
        self.tasks: list[Task] = []

    def __len__(self) -> int:
        return len(self.tasks)

    def add_task(self, title: str) -> Task:
        task = Task(title)
        self.tasks.append(task)
        return task

    def complete_task(self, title: str) -> bool:
        cleaned = title.strip() if isinstance(title, str) else title

        for task in self.tasks:
            if task.title == cleaned and not task.done:
                task.mark_done()
                return True

        return False

    def pending_titles(self) -> list[str]:
        return [task.title for task in self.tasks if not task.done]

    def completion_ratio(self) -> float:
        if not self.tasks:
            return 0.0

        done_count = sum(1 for task in self.tasks if task.done)
        return done_count / len(self.tasks)


if __name__ == "__main__":
    todo = TodoList()
    todo.add_task("Read chapter 1")
    todo.add_task("Write notes")
    todo.complete_task("Read chapter 1")
    print(todo.pending_titles())
    print(todo.completion_ratio())
