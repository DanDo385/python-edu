"""
PROJECT 04: CONTEXT MANAGERS - RESOURCE MANAGEMENT

Context managers provide a way to allocate and release resources precisely
when you want to. The most common use is with the 'with' statement.
"""

import time
from contextlib import contextmanager
from typing import Any


class FileManager:
    """Context manager for file operations."""

    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Called when entering 'with' block."""
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block."""
        if self.file:
            self.file.close()
        return False  # Propagate exceptions


class Timer:
    """Context manager that measures execution time."""

    def __init__(self):
        self.start = None
        self.end = None
        self.elapsed = None

    def __enter__(self):
        """Start the timer."""
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Stop the timer and calculate elapsed time."""
        self.end = time.time()
        self.elapsed = self.end - self.start
        return False


@contextmanager
def temporary_value(obj, attr, value):
    """
    Context manager that temporarily changes an attribute.

    Uses the @contextmanager decorator which is simpler than
    writing __enter__ and __exit__ methods.
    """
    # Save original value
    original = getattr(obj, attr)

    try:
        # Set temporary value
        setattr(obj, attr, value)
        yield obj
    finally:
        # Restore original value
        setattr(obj, attr, original)


# HOW CONTEXT MANAGERS WORK:
# --------------------------
# with context_manager as var:
#     # code block
#
# Is equivalent to:
# var = context_manager.__enter__()
# try:
#     # code block
# finally:
#     context_manager.__exit__(exc_type, exc_val, exc_tb)
