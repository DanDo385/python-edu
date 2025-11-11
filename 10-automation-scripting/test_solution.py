"""
Project 10: Automation - Tests
"""

import pytest
from pathlib import Path
import tempfile
import shutil
from solution import (
    list_files,
    count_lines,
    backup_file,
    run_command,
    batch_rename
)


class TestListFiles:
    def test_list_python_files(self, tmp_path):
        # Create test files
        (tmp_path / "test1.py").touch()
        (tmp_path / "test2.py").touch()
        (tmp_path / "test.txt").touch()

        files = list_files(str(tmp_path), "*.py")
        assert len(files) == 2


class TestCountLines:
    def test_count_lines(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("line1\nline2\nline3")

        count = count_lines(str(test_file))
        assert count == 3


class TestBackupFile:
    def test_backup_creates_file(self, tmp_path):
        source = tmp_path / "original.txt"
        source.write_text("test content")

        backup_dir = tmp_path / "backups"
        backup_path = backup_file(str(source), str(backup_dir))

        assert backup_path.exists()
        assert backup_path.read_text() == "test content"


class TestRunCommand:
    def test_run_echo_command(self):
        output = run_command(["echo", "Hello"])
        assert "Hello" in output


class TestBatchRename:
    def test_batch_rename(self, tmp_path):
        # Create test files
        (tmp_path / "test1.txt").touch()
        (tmp_path / "test2.txt").touch()

        batch_rename(str(tmp_path), ".txt", ".md")

        # Check renamed files exist
        assert (tmp_path / "test1.md").exists()
        assert (tmp_path / "test2.md").exists()
        assert not (tmp_path / "test1.txt").exists()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
