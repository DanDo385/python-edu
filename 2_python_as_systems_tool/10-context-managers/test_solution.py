"""
Project 04: Context Managers - Test Suite
"""

import pytest
import time
import os
from solution import FileManager, Timer, temporary_value


class TestFileManager:
    """Test FileManager context manager."""

    def test_file_manager_reads_file(self, tmp_path):
        # Create a temp file
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello, World!")

        # Test reading with context manager
        with FileManager(str(test_file), 'r') as f:
            content = f.read()

        assert content == "Hello, World!"

    def test_file_manager_closes_file(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("test")

        with FileManager(str(test_file), 'r') as f:
            assert not f.closed

        # File should be closed after exiting context
        assert f.closed


class TestTimer:
    """Test Timer context manager."""

    def test_timer_measures_time(self):
        with Timer() as t:
            time.sleep(0.1)

        assert t.elapsed is not None
        assert 0.09 < t.elapsed < 0.15  # Allow some variance

    def test_timer_starts_at_zero(self):
        timer = Timer()
        assert timer.start is None
        assert timer.elapsed is None


class TestTemporaryValue:
    """Test temporary_value context manager."""

    def test_temporary_value_changes_and_restores(self):
        class Config:
            debug = False

        config = Config()

        assert config.debug is False

        with temporary_value(config, 'debug', True):
            assert config.debug is True

        assert config.debug is False

    def test_temporary_value_with_different_types(self):
        class Settings:
            timeout = 30

        settings = Settings()

        with temporary_value(settings, 'timeout', 60):
            assert settings.timeout == 60

        assert settings.timeout == 30


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
