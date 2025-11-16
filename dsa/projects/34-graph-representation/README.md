# Project 34: Graph Representation

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow.svg)](../../README.md)
[![Concepts](https://img.shields.io/badge/Concepts-Graphs%2C%20Data%20Structures-blue.svg)](../../README.md)

## 🎯 Overview

**Graph Representation** focuses on the fundamental data structures used to represent graphs in computer science. Understanding different graph representations is crucial for:
- Choosing the right data structure for graph algorithms
- Optimizing space and time complexity
- Working with weighted and directed graphs
- Implementing efficient graph operations
- Solving real-world network problems

## 🎓 Learning Objectives

By completing this project, you will:
- Master adjacency list representation
- Implement adjacency matrix representation
- Understand edge list representation
- Work with weighted graphs
- Differentiate between directed and undirected graphs
- Analyze space-time tradeoffs of different representations
- Build a flexible graph class supporting multiple representations
- Apply appropriate representations to different problems

## 📚 Background

### What is a Graph?

A **graph** is a non-linear data structure consisting of:
- **Vertices (V)**: Nodes or points in the graph
- **Edges (E)**: Connections between vertices

**Types of Graphs:**
1. **Undirected Graph**: Edges have no direction (A ↔ B)
2. **Directed Graph (Digraph)**: Edges have direction (A → B)
3. **Weighted Graph**: Edges have associated weights/costs
4. **Unweighted Graph**: All edges have equal weight (or weight 1)

### Graph Representations

**1. Adjacency List**
- Dictionary/array where each vertex maps to a list of neighbors
- **Space**: O(V + E)
- **Best for**: Sparse graphs (E << V²)
- **Edge lookup**: O(degree(v))
- **Neighbor iteration**: O(degree(v))

**2. Adjacency Matrix**
- 2D array where matrix[i][j] = weight if edge exists, 0/∞ otherwise
- **Space**: O(V²)
- **Best for**: Dense graphs (E ≈ V²)
- **Edge lookup**: O(1)
- **Neighbor iteration**: O(V)

**3. Edge List**
- List of all edges (u, v, weight)
- **Space**: O(E)
- **Best for**: Algorithms that process all edges (Kruskal's MST)
- **Edge lookup**: O(E)
- **Neighbor iteration**: O(E)

### Comparison Table

| Operation | Adjacency List | Adjacency Matrix | Edge List |
|-----------|---------------|------------------|-----------|
| Space | O(V + E) | O(V²) | O(E) |
| Add Edge | O(1) | O(1) | O(1) |
| Check Edge | O(degree(v)) | O(1) | O(E) |
| Get Neighbors | O(degree(v)) | O(V) | O(E) |
| Remove Edge | O(degree(v)) | O(1) | O(E) |
| Best For | Sparse graphs | Dense graphs | Edge-based algorithms |

## 💻 Problems

Implement the following in `solution/solution.py`:

### Problem 1: Adjacency List Implementation

Create a graph using adjacency list representation.

```python
class AdjacencyListGraph:
    def __init__(self, num_vertices: int, directed: bool = False)
    def add_edge(self, u: int, v: int, weight: int = 1) -> None
    def remove_edge(self, u: int, v: int) -> None
    def get_neighbors(self, vertex: int) -> List[Tuple[int, int]]
    def has_edge(self, u: int, v: int) -> bool
    def get_degree(self, vertex: int) -> int
```

**Requirements:**
- Support both directed and undirected graphs
- Support weighted edges
- Efficient neighbor iteration
- Handle edge cases (invalid vertices, duplicate edges)

**Example:**
```python
graph = AdjacencyListGraph(4)
graph.add_edge(0, 1, weight=5)
graph.add_edge(0, 2, weight=3)
graph.add_edge(1, 3, weight=2)
# Result: {0: [(1, 5), (2, 3)], 1: [(0, 5), (3, 2)], 2: [(0, 3)], 3: [(1, 2)]}
```

**Complexity:**
- Space: O(V + E)
- add_edge: O(1)
- get_neighbors: O(1) to retrieve, O(degree(v)) to iterate

---

### Problem 2: Adjacency Matrix Implementation

Create a graph using adjacency matrix representation.

```python
class AdjacencyMatrixGraph:
    def __init__(self, num_vertices: int, directed: bool = False)
    def add_edge(self, u: int, v: int, weight: int = 1) -> None
    def remove_edge(self, u: int, v: int) -> None
    def get_neighbors(self, vertex: int) -> List[Tuple[int, int]]
    def has_edge(self, u: int, v: int) -> bool
    def get_degree(self, vertex: int) -> int
```

**Algorithm:**
1. Initialize V×V matrix with 0 (or ∞ for weighted shortest paths)
2. For edge (u, v, w): matrix[u][v] = w
3. For undirected: also set matrix[v][u] = w

**Example:**
```python
graph = AdjacencyMatrixGraph(3)
graph.add_edge(0, 1, weight=4)
graph.add_edge(1, 2, weight=7)
# Result: [[0, 4, 0], [4, 0, 7], [0, 7, 0]]
```

**Complexity:**
- Space: O(V²)
- add_edge: O(1)
- has_edge: O(1)
- get_neighbors: O(V)

---

### Problem 3: Edge List Implementation

Create a graph using edge list representation.

```python
class EdgeListGraph:
    def __init__(self, num_vertices: int, directed: bool = False)
    def add_edge(self, u: int, v: int, weight: int = 1) -> None
    def remove_edge(self, u: int, v: int) -> None
    def get_edges(self) -> List[Tuple[int, int, int]]
    def has_edge(self, u: int, v: int) -> bool
    def sort_edges_by_weight(self) -> List[Tuple[int, int, int]]
```

**Use Cases:**
- Kruskal's MST algorithm (needs sorted edges)
- Bellman-Ford shortest path
- Edge-centric graph algorithms

**Example:**
```python
graph = EdgeListGraph(4)
graph.add_edge(0, 1, weight=10)
graph.add_edge(1, 2, weight=5)
graph.add_edge(2, 3, weight=8)
sorted_edges = graph.sort_edges_by_weight()
# Result: [(1, 2, 5), (2, 3, 8), (0, 1, 10)]
```

**Complexity:**
- Space: O(E)
- add_edge: O(1)
- sort_edges: O(E log E)

---

### Problem 4: Graph Converter

Convert between different graph representations.

```python
def convert_adjacency_list_to_matrix(adj_list: AdjacencyListGraph) -> AdjacencyMatrixGraph
def convert_adjacency_matrix_to_list(adj_matrix: AdjacencyMatrixGraph) -> AdjacencyListGraph
def convert_to_edge_list(graph: Union[AdjacencyListGraph, AdjacencyMatrixGraph]) -> EdgeListGraph
```

**Examples:**
```python
# Adjacency List → Adjacency Matrix
list_graph = AdjacencyListGraph(3)
list_graph.add_edge(0, 1, weight=5)
matrix_graph = convert_adjacency_list_to_matrix(list_graph)

# Adjacency Matrix → Edge List
edge_list = convert_to_edge_list(matrix_graph)
```

**Complexity:**
- List to Matrix: O(V² + E)
- Matrix to List: O(V²)
- To Edge List: O(V²) or O(E) depending on source

---

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest tests/test_project_34.py -v

# Run specific test class
pytest tests/test_project_34.py::TestAdjacencyList -v
pytest tests/test_project_34.py::TestAdjacencyMatrix -v
pytest tests/test_project_34.py::TestEdgeList -v

# Run with coverage
pytest tests/test_project_34.py --cov=solution --cov-report=html
```

## 📊 Complexity Analysis

| Representation | Space | Add Edge | Check Edge | Get Neighbors | Remove Edge |
|----------------|-------|----------|------------|---------------|-------------|
| Adjacency List | O(V+E) | O(1) | O(degree(v)) | O(degree(v)) | O(degree(v)) |
| Adjacency Matrix | O(V²) | O(1) | O(1) | O(V) | O(1) |
| Edge List | O(E) | O(1) | O(E) | O(E) | O(E) |

**When to Use Each:**
- **Adjacency List**: Sparse graphs, need fast neighbor iteration (most common)
- **Adjacency Matrix**: Dense graphs, need fast edge lookup, matrix operations
- **Edge List**: Edge-based algorithms (MST, edge sorting), minimal memory

## 💡 Hints

<details>
<summary>Hint 1: Choosing the Right Representation</summary>

**Sparse Graph (E << V²):** Use Adjacency List
- Example: Social network (average degree << total people)
- Saves memory and faster for DFS/BFS

**Dense Graph (E ≈ V²):** Use Adjacency Matrix
- Example: Complete graph, distance matrix
- Fast edge lookup, good for Floyd-Warshall

**Edge-Centric Algorithm:** Use Edge List
- Example: Kruskal's MST, Bellman-Ford
- Easy to sort edges, process all edges
</details>

<details>
<summary>Hint 2: Weighted Graphs</summary>

For weighted graphs:
- **Adjacency List**: Store tuples (neighbor, weight)
- **Adjacency Matrix**: Store weight instead of 1, use 0 or ∞ for no edge
- **Edge List**: Store triplets (u, v, weight)

Use 0 for "no edge" in connectivity matrices.
Use ∞ for "no edge" in shortest path matrices.
</details>

<details>
<summary>Hint 3: Directed vs Undirected</summary>

**Undirected Graph:**
- Add edge in both directions
- Matrix is symmetric: matrix[u][v] = matrix[v][u]
- Count each edge once in edge list

**Directed Graph:**
- Add edge in one direction only
- Matrix may be asymmetric
- Can have edges u→v and v→u separately
</details>

<details>
<summary>Hint 4: Memory Optimization</summary>

**For Undirected Graphs:**
- Only store lower triangle of adjacency matrix (save 50% space)
- Each edge appears once in adjacency list (not twice)

**For Sparse Graphs:**
- Use dictionary instead of array for adjacency list
- Only allocate space for vertices with edges
</details>

## 🔗 Related Concepts

- **Graph Traversal** (Projects 35-36) - DFS and BFS algorithms
- **Hash Tables** (Projects 21-25) - Used in adjacency list implementation
- **Arrays and Matrices** (Projects 2, 5) - Used in adjacency matrix
- **Sorting** (Projects 6-8) - Used in edge list sorting

## 📖 References

- [Graph Representations - GeeksforGeeks](https://www.geeksforgeeks.org/graph-and-its-representations/)
- [Introduction to Algorithms (CLRS)](https://en.wikipedia.org/wiki/Introduction_to_Algorithms) - Chapter 22
- [Graph Theory - Wikipedia](https://en.wikipedia.org/wiki/Graph_theory)

## 🎓 Key Insights

### Space-Time Tradeoffs

**Adjacency Matrix:**
- ✅ Fast edge lookup O(1)
- ✅ Fast edge addition/removal O(1)
- ✅ Good for dense graphs
- ❌ Wastes space on sparse graphs O(V²)
- ❌ Slow neighbor iteration O(V)

**Adjacency List:**
- ✅ Space efficient for sparse graphs O(V + E)
- ✅ Fast neighbor iteration O(degree(v))
- ✅ Most versatile representation
- ❌ Slower edge lookup O(degree(v))
- ❌ Slightly more complex to implement

**Edge List:**
- ✅ Minimal space O(E)
- ✅ Easy to sort edges
- ✅ Simple to implement
- ❌ Slow for most operations O(E)
- ❌ Not good for graph traversal

### Real-World Applications

1. **Social Networks**: Adjacency List (sparse, millions of users, average degree ~100)
2. **Road Networks**: Adjacency List (sparse, each intersection connects to few roads)
3. **Airline Routes**: Adjacency List (sparse, not all cities connect)
4. **Chess Positions**: Adjacency Matrix (dense, each piece can move to many squares)
5. **Complete Graphs**: Adjacency Matrix (every vertex connects to every other)
6. **Minimum Spanning Tree**: Edge List (Kruskal's needs sorted edges)

### Implementation Best Practices

```python
# Adjacency List with defaultdict
from collections import defaultdict

adj_list = defaultdict(list)  # Auto-creates empty lists
adj_list[0].append((1, 5))    # vertex 1, weight 5

# Adjacency Matrix with infinity for no edge
INF = float('inf')
matrix = [[INF] * n for _ in range(n)]
for i in range(n):
    matrix[i][i] = 0  # Distance to self is 0

# Edge List with named tuples
from collections import namedtuple
Edge = namedtuple('Edge', ['u', 'v', 'weight'])
edges = [Edge(0, 1, 5), Edge(1, 2, 3)]
edges.sort(key=lambda e: e.weight)  # Sort by weight
```

---

**Estimated Time:** 3-4 hours
**Difficulty:** ⭐⭐⭐ Medium
**Prerequisites:** Python basics, OOP, data structures
