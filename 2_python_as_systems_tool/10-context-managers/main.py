"""
Project 04: Context Managers - Interactive Demo
"""

import time
import tempfile
import os
from solution import FileManager, Timer, temporary_value


def demo_file_manager():
    print("=" * 70)
    print("DEMO 1: FileManager Context Manager")
    print("=" * 70)

    # Create a temp file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tf:
        tf.write("Hello from context manager!")
        temp_file = tf.name

    print("Using FileManager to read file:")
    with FileManager(temp_file, 'r') as f:
        content = f.read()
        print(f"Content: {content}")

    os.unlink(temp_file)
    print("File automatically closed after 'with' block!\n")


def demo_timer():
    print("=" * 70)
    print("DEMO 2: Timer Context Manager")
    print("=" * 70)

    print("Timing a slow operation:")
    with Timer() as t:
        time.sleep(0.5)
        print("Working...")

    print(f"Elapsed time: {t.elapsed:.4f} seconds\n")


def demo_temporary_value():
    print("=" * 70)
    print("DEMO 3: Temporary Value Context Manager")
    print("=" * 70)

    class Config:
        debug = False
        timeout = 30

    config = Config()

    print(f"Original: debug={config.debug}, timeout={config.timeout}")

    with temporary_value(config, 'debug', True):
        print(f"Inside context: debug={config.debug}")

    print(f"After context: debug={config.debug} (restored!)\n")


def main():
    print("\n")
    print("🔒" * 35)
    print("  PROJECT 04: CONTEXT MANAGERS - INTERACTIVE DEMO")
    print("🔒" * 35)
    print("\n")

    demo_file_manager()
    input("Press Enter to continue...")

    demo_timer()
    input("Press Enter to continue...")

    demo_temporary_value()

    print("=" * 70)
    print("Key Takeaways:")
    print("1. Context managers ensure proper resource cleanup")
    print("2. 'with' statement handles setup and teardown")
    print("3. Implement __enter__ and __exit__ for custom managers")
    print("4. @contextmanager decorator simplifies creation")
    print()


if __name__ == "__main__":
    main()
