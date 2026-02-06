"""Tests for Project 07: OOP Basics."""

from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from solution import Task, TodoList


class TestTask:
    def test_task_starts_not_done(self):
        task = Task("Read docs")
        assert task.title == "Read docs"
        assert task.done is False

    def test_mark_done_flips_state(self):
        task = Task("Practice")
        task.mark_done()
        assert task.done is True

    def test_blank_title_rejected(self):
        with pytest.raises(ValueError):
            Task("   ")


class TestTodoList:
    def test_add_and_len(self):
        todo = TodoList()
        todo.add_task("A")
        todo.add_task("B")
        assert len(todo) == 2

    def test_complete_task_returns_bool(self):
        todo = TodoList()
        todo.add_task("A")
        assert todo.complete_task("A") is True
        assert todo.complete_task("Missing") is False

    def test_pending_titles(self):
        todo = TodoList()
        todo.add_task("A")
        todo.add_task("B")
        todo.complete_task("A")
        assert todo.pending_titles() == ["B"]

    def test_completion_ratio(self):
        todo = TodoList()
        assert todo.completion_ratio() == 0.0

        todo.add_task("A")
        todo.add_task("B")
        todo.complete_task("A")
        assert todo.completion_ratio() == pytest.approx(0.5)

    def test_aliasing_behavior_for_task_references(self):
        # Invariant: TodoList stores references to Task objects, not copies.
        todo = TodoList()
        task_ref = todo.add_task("Shared object")
        alias = task_ref

        alias.mark_done()

        # Because alias and stored task reference the same object, state changed.
        assert todo.pending_titles() == []
