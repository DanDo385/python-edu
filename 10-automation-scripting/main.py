"""
Project 10: Automation - Demo
"""

from pathlib import Path
import tempfile
from solution import (
    list_files,
    count_lines,
    backup_file,
    run_command,
    batch_rename
)


def demo_list_files():
    print("=" * 70)
    print("DEMO 1: List Files")
    print("=" * 70)

    # List Python files in current directory
    py_files = list_files(".", "*.py")
    print(f"Found {len(py_files)} Python files:")
    for f in py_files[:5]:  # Show first 5
        print(f"  - {f.name}")
    print()


def demo_count_lines():
    print("=" * 70)
    print("DEMO 2: Count Lines")
    print("=" * 70)

    # Create temp file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5\n")
        temp_file = f.name

    lines = count_lines(temp_file)
    print(f"File has {lines} lines")

    Path(temp_file).unlink()
    print()


def demo_backup():
    print("=" * 70)
    print("DEMO 3: Backup File")
    print("=" * 70)

    # Create temp file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("Important data")
        temp_file = f.name

    # Create backup
    backup_path = backup_file(temp_file, tempfile.gettempdir())
    print(f"Backed up to: {backup_path}")

    # Cleanup
    Path(temp_file).unlink()
    backup_path.unlink()
    print()


def demo_run_command():
    print("=" * 70)
    print("DEMO 4: Run Command")
    print("=" * 70)

    output = run_command(["echo", "Hello from subprocess!"])
    print(f"Command output: {output.strip()}")
    print()


def main():
    print("\n🤖" * 35)
    print("  PROJECT 10: AUTOMATION & SCRIPTING")
    print("🤖" * 35)
    print()

    demo_list_files()
    demo_count_lines()
    demo_backup()
    demo_run_command()

    print("=" * 70)
    print("Key Takeaways:")
    print("1. Use pathlib for modern file operations")
    print("2. subprocess for running system commands")
    print("3. Automate repetitive tasks")
    print("4. Handle errors gracefully")
    print("5. Python excels at automation!")
    print()


if __name__ == "__main__":
    main()
