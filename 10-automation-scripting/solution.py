"""
PROJECT 10: AUTOMATION & SCRIPTING

Automate repetitive tasks with Python scripts.
"""

from pathlib import Path
from typing import List
import subprocess
import shutil


def list_files(directory: str, pattern: str = "*") -> List[Path]:
    """List files matching pattern."""
    path = Path(directory)
    return list(path.glob(pattern))


def count_lines(file_path: str) -> int:
    """Count lines in file."""
    with open(file_path, 'r') as f:
        return len(f.readlines())


def backup_file(file_path: str, backup_dir: str = "backups") -> Path:
    """Create backup of file."""
    source = Path(file_path)
    backup_path = Path(backup_dir)

    # Create backup directory if it doesn't exist
    backup_path.mkdir(exist_ok=True)

    # Copy file to backup directory
    destination = backup_path / source.name
    shutil.copy2(source, destination)

    return destination


def run_command(command: List[str]) -> str:
    """Run system command."""
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout


def batch_rename(directory: str, old_ext: str, new_ext: str):
    """Batch rename files by extension."""
    path = Path(directory)

    for file in path.glob(f"*{old_ext}"):
        new_name = file.with_suffix(new_ext)
        file.rename(new_name)


# AUTOMATION BEST PRACTICES:
# --------------------------
# 1. Use pathlib instead of os.path
# 2. Handle errors gracefully
# 3. Add logging for debugging
# 4. Make scripts idempotent (safe to run multiple times)
# 5. Use argparse for CLI arguments
# 6. Document what the script does
