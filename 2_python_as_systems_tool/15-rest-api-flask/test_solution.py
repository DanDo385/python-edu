"""
Project 09: REST API - Tests
"""

import pytest
from app import app


@pytest.fixture
def client():
    """Create test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestTodoAPI:
    def test_home(self, client):
        """Test home endpoint."""
        response = client.get('/')
        assert response.status_code == 200
        assert 'message' in response.json

    def test_get_todos(self, client):
        """Test getting all todos."""
        response = client.get('/api/todos')
        assert response.status_code == 200
        assert isinstance(response.json, list)

    def test_get_todo_by_id(self, client):
        """Test getting specific todo."""
        response = client.get('/api/todos/1')
        assert response.status_code == 200
        assert response.json['id'] == 1

    def test_get_nonexistent_todo(self, client):
        """Test 404 for missing todo."""
        response = client.get('/api/todos/999')
        assert response.status_code == 404

    def test_create_todo(self, client):
        """Test creating a todo."""
        response = client.post('/api/todos',
                               json={'title': 'Test Todo'})
        assert response.status_code == 201
        assert response.json['title'] == 'Test Todo'

    def test_create_todo_missing_title(self, client):
        """Test error on missing title."""
        response = client.post('/api/todos', json={})
        assert response.status_code == 400

    def test_update_todo(self, client):
        """Test updating a todo."""
        response = client.put('/api/todos/1',
                              json={'completed': True})
        assert response.status_code == 200
        assert response.json['completed'] is True

    def test_delete_todo(self, client):
        """Test deleting a todo."""
        response = client.delete('/api/todos/1')
        assert response.status_code == 204


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
