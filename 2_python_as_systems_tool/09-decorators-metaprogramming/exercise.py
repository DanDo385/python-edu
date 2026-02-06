"""Project 09 exercise entrypoint.

This module re-exports stubs from `lib.py` so the track keeps a consistent
`exercise.py` convention.
"""

from lib import cache, debug, repeat, timer, validate_args

__all__ = ["timer", "repeat", "cache", "validate_args", "debug"]
