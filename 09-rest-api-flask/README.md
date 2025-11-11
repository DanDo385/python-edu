# Project 09: 🔌 REST API with Flask

> **Build production APIs**

## 🎯 Skills

- Flask basics
- Routing and HTTP methods
- JSON responses
- Error handling
- Request validation

## 📚 Example

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/users')
def get_users():
    return jsonify([{'id': 1, 'name': 'Alice'}])
```

## 🏃 Run

```bash
python app.py               # Start server
pytest test_solution.py -v  # Test
```

**Status:** ✅ Complete!
