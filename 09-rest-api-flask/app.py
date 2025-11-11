"""
Project 09: REST API with Flask - Main Application

Run with: python app.py
Then visit: http://localhost:5000/api/todos
"""

from flask import Flask, jsonify, request
from typing import List, Dict, Optional

app = Flask(__name__)

# In-memory database (for demo purposes)
todos: List[Dict] = [
    {'id': 1, 'title': 'Learn Python', 'completed': False},
    {'id': 2, 'title': 'Build API', 'completed': False}
]
next_id = 3


@app.route('/')
def home():
    """Home endpoint."""
    return jsonify({'message': 'Welcome to Todo API'})


@app.route('/api/todos', methods=['GET'])
def get_todos():
    """Get all todos."""
    return jsonify(todos)


@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id: int):
    """Get single todo by ID."""
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify(todo)


@app.route('/api/todos', methods=['POST'])
def create_todo():
    """Create new todo."""
    global next_id

    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    todo = {
        'id': next_id,
        'title': data['title'],
        'completed': data.get('completed', False)
    }

    todos.append(todo)
    next_id += 1

    return jsonify(todo), 201


@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id: int):
    """Update existing todo."""
    todo = next((t for t in todos if t['id'] == todo_id), None)

    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404

    data = request.get_json()

    if 'title' in data:
        todo['title'] = data['title']
    if 'completed' in data:
        todo['completed'] = data['completed']

    return jsonify(todo)


@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id: int):
    """Delete todo."""
    global todos

    todo = next((t for t in todos if t['id'] == todo_id), None)

    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404

    todos = [t for t in todos if t['id'] != todo_id]

    return '', 204


if __name__ == '__main__':
    print("Starting Flask server on http://localhost:5000")
    print("Try: curl http://localhost:5000/api/todos")
    app.run(debug=True)
