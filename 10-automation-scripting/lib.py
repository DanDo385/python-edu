"""
Project 10: Automation & Scripting - Practice Stubs
"""

from pathlib import Path
from typing import List
import subprocess


def list_files(directory: str, pattern: str = "*") -> List[Path]:
    """
    List all files matching pattern in directory.

    Example:
        python_files = list_files(".", "*.py")
    """
    # TODO: Use Path.glob() to find matching files
    pass


def count_lines(file_path: str) -> int:
    """
    Count lines in a file.

    Example:
        lines = count_lines("script.py")
    """
    # TODO: Read file and count lines
    pass


def backup_file(file_path: str, backup_dir: str = "backups") -> Path:
    """
    Create backup of file.

    Example:
        backup_path = backup_file("important.txt")
    """
    # TODO: Copy file to backup directory
    pass


def run_command(command: List[str]) -> str:
    """
    Run system command and return output.

    Example:
        output = run_command(["ls", "-la"])
    """
    # TODO: Use subprocess.run() to execute command
    pass


def batch_rename(directory: str, old_ext: str, new_ext: str):
    """
    Rename all files with old_ext to new_ext.

    Example:
        batch_rename(".", ".txt", ".md")
    """
    # TODO: Find files with old_ext and rename them
    pass


if __name__ == "__main__":
    print("Files in current directory:")
    files = list_files(".", "*.py")
    for f in files:
        print(f"  {f}")
