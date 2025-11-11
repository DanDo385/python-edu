# Project 10: 🤖 Automation & Scripting

> **Automate repetitive tasks**

## 🎯 Skills

- File operations with pathlib
- Running system commands
- CLI arguments with argparse
- Environment variables
- Scheduling tasks

## 📚 Example

```python
from pathlib import Path

# Find all Python files
py_files = list(Path('.').glob('**/*.py'))
```

## 🏃 Run

```bash
python main.py && pytest test_solution.py -v
```

**Status:** ✅ Complete!
