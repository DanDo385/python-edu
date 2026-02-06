"""
Project 09: REST API - Interactive Demo

This demonstrates the API without running a server.
"""

print("""
=" * 70)
PROJECT 09: REST API WITH FLASK
=" * 70)

This project creates a RESTful API with Flask.

ENDPOINTS:
----------
GET    /api/todos           - List all todos
GET    /api/todos/<id>      - Get specific todo
POST   /api/todos           - Create new todo
PUT    /api/todos/<id>      - Update todo
DELETE /api/todos/<id>      - Delete todo

TO RUN:
-------
1. Start server:
   python app.py

2. Test with curl:
   curl http://localhost:5000/api/todos
   curl -X POST http://localhost:5000/api/todos -H "Content-Type: application/json" -d '{"title":"New Todo"}'

3. Or run tests:
   pytest test_solution.py -v

KEY CONCEPTS:
-------------
- RESTful API design
- HTTP methods (GET, POST, PUT, DELETE)
- JSON request/response
- Status codes (200, 201, 404, 400)
- Route parameters
- Request validation

Try it now: python app.py
""")
