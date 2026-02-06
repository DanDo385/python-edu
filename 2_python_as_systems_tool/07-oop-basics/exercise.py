"""
Project 07: OOP Basics

Implement Task and TodoList with core object-oriented behavior.
Run: pytest test_solution.py -v
"""


class Task:
    """Simple task object with mutable completion state."""

    def __init__(self, title: str):
        """
        Create a new task.

        Args:
            title: Non-empty title string.

        Raises:
            TypeError: If title is not a string.
            ValueError: If title is blank after stripping.
        """
        # TODO: Validate and store title; initialize done=False.
        pass

    def mark_done(self) -> None:
        """Mark this task as completed."""
        # TODO: Set done state to True.
        pass


class TodoList:
    """Collection object that owns multiple Task instances."""

    def __init__(self):
        """Initialize an empty todo list."""
        # TODO: Create storage for Task objects.
        pass

    def __len__(self) -> int:
        """Return number of tasks currently stored."""
        # TODO: Return task count.
        pass

    def add_task(self, title: str) -> Task:
        """Create a new task, store it, and return it."""
        # TODO: Create Task, append to internal list, return task.
        pass

    def complete_task(self, title: str) -> bool:
        """
        Mark first matching unfinished task as done.

        Returns:
            True if a task was completed, else False.
        """
        # TODO: Find first unfinished match, mark done, return True/False.
        pass

    def pending_titles(self) -> list[str]:
        """Return titles for tasks that are not done."""
        # TODO: Build and return pending titles.
        pass

    def completion_ratio(self) -> float:
        """
        Return fraction of tasks completed in [0.0, 1.0].

        Convention:
            If list is empty, return 0.0.
        """
        # TODO: Compute done_count / total_count.
        pass


if __name__ == "__main__":
    todo = TodoList()
    todo.add_task("Read chapter 1")
    todo.add_task("Write notes")
    print(todo.pending_titles())
