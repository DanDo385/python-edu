# Project 35: Depth-First Search (DFS)

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow.svg)](../../README.md)
[![Concepts](https://img.shields.io/badge/Concepts-Graphs%2C%20DFS%2C%20Traversal-blue.svg)](../../README.md)

## 🎯 Overview

**Depth-First Search (DFS)** is a fundamental graph traversal algorithm that explores as far as possible along each branch before backtracking. It's one of the most important algorithms in computer science, used for:
- Graph traversal and exploration
- Path finding and connectivity analysis
- Cycle detection in graphs
- Topological sorting
- Solving maze and puzzle problems
- Tree traversals (pre-order, in-order, post-order)

## 🎓 Learning Objectives

By completing this project, you will:
- Master DFS algorithm (recursive and iterative implementations)
- Understand graph representations (adjacency list and matrix)
- Implement path finding algorithms using DFS
- Detect connected components in undirected graphs
- Detect cycles in directed and undirected graphs
- Apply DFS to solve complex graph problems
- Understand DFS vs BFS tradeoffs
- Analyze time and space complexity of graph algorithms

## 📚 Background

### What is Depth-First Search?

DFS is a graph traversal algorithm that explores vertices by going as deep as possible before backtracking.

**Core Idea:**
1. Start at a source vertex
2. Mark it as visited
3. Recursively visit all unvisited neighbors
4. Backtrack when no unvisited neighbors remain
5. Continue until all reachable vertices are visited

**Key Characteristics:**
- **Exploration Strategy:** Goes deep first (hence the name)
- **Data Structure:** Uses a stack (implicit via recursion or explicit)
- **Memory:** O(h) where h is the maximum depth
- **Applications:** Path finding, cycle detection, topological sort

**DFS vs BFS:**

| Aspect | DFS | BFS |
|--------|-----|-----|
| Data Structure | Stack (recursion) | Queue |
| Exploration | Deep first | Level by level |
| Memory | O(h) - height | O(w) - width |
| Path Found | Not shortest | Shortest (unweighted) |
| Applications | Cycle detection, topological sort | Shortest path, level-order |

### Graph Representations

**1. Adjacency List:**
- Dictionary mapping vertex → list of neighbors
- Space: O(V + E)
- Best for sparse graphs
- Efficient neighbor iteration

**2. Adjacency Matrix:**
- 2D array where matrix[i][j] = 1 if edge exists
- Space: O(V²)
- Best for dense graphs
- Fast edge lookup: O(1)

## 💻 Problems

Implement the following in `solution/solution.py`:

### Problem 1: Graph Class Implementation

Implement a Graph class supporting both adjacency list and adjacency matrix representations.

```python
class Graph:
    def __init__(self, num_vertices: int, representation: str = "adjacency_list")
    def add_edge(self, u: int, v: int, directed: bool = False) -> None
    def get_neighbors(self, vertex: int) -> List[int]
    def has_edge(self, u: int, v: int) -> bool
```

**Requirements:**
- Support both "adjacency_list" and "adjacency_matrix" representations
- Handle directed and undirected edges
- Provide methods to query graph structure
- Vertices numbered from 0 to n-1

**Example:**
```python
# Adjacency List
graph = Graph(5, "adjacency_list")
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
# Result: {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}

# Adjacency Matrix
graph = Graph(3, "adjacency_matrix")
graph.add_edge(0, 1, directed=True)
# Result: [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
```

---

### Problem 2: DFS Recursive

Implement DFS using recursion. Return the order vertices were visited.

```python
def dfs_recursive(graph: Graph, start: int) -> List[int]
```

**Algorithm:**
1. Create a visited set
2. Create a result list to store visit order
3. Define recursive helper function:
   - Mark current vertex as visited
   - Add to result
   - Recursively visit all unvisited neighbors
4. Call helper on start vertex
5. Return visit order

**Examples:**
```python
# Linear graph: 0 -> 1 -> 2 -> 3
graph = Graph(4)
graph.add_edge(0, 1, directed=True)
graph.add_edge(1, 2, directed=True)
graph.add_edge(2, 3, directed=True)
dfs_recursive(graph, 0)  # Returns [0, 1, 2, 3]

# Tree structure:
#     0
#    / \
#   1   2
#  /
# 3
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
dfs_recursive(graph, 0)  # Returns [0, 1, 3, 2] or [0, 2, 1, 3]
```

**Complexity:**
- Time: O(V + E) - Visit each vertex once, explore each edge once
- Space: O(V) - Recursion stack + visited set

---

### Problem 3: DFS Iterative

Implement DFS using an explicit stack (iterative approach).

```python
def dfs_iterative(graph: Graph, start: int) -> List[int]
```

**Algorithm:**
1. Create a stack, push start vertex
2. Create visited set and result list
3. While stack is not empty:
   - Pop vertex
   - If not visited:
     - Mark as visited
     - Add to result
     - Push all unvisited neighbors to stack
4. Return visit order

**Examples:**
```python
# Same graphs as DFS recursive
graph = Graph(4)
graph.add_edge(0, 1, directed=True)
graph.add_edge(1, 2, directed=True)
graph.add_edge(2, 3, directed=True)
dfs_iterative(graph, 0)  # Returns [0, 1, 2, 3]
```

**Note:** Visit order may differ from recursive DFS due to stack ordering, but both are valid DFS traversals.

**Complexity:**
- Time: O(V + E)
- Space: O(V) - Explicit stack + visited set

---

### Problem 4: Find Path (DFS-based)

Find a path from source to destination using DFS. Return the path if it exists, otherwise return None.

```python
def find_path_dfs(graph: Graph, start: int, end: int) -> Optional[List[int]]
```

**Algorithm:**
1. Use DFS to explore from start
2. Keep track of current path
3. When destination is reached, return path
4. On backtrack, remove vertex from current path
5. If no path found, return None

**Examples:**
```python
# Connected graph:
# 0 -- 1 -- 3
# |    |
# 2 ---+
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 3)

find_path_dfs(graph, 0, 3)  # Returns [0, 1, 3] (one possible path)
find_path_dfs(graph, 0, 3)  # Could also return [0, 2, 1, 3]
find_path_dfs(graph, 0, 5)  # Returns None (vertex 5 doesn't exist)
```

**Note:** DFS does not guarantee the shortest path. Use BFS for shortest path in unweighted graphs.

**Complexity:**
- Time: O(V + E)
- Space: O(V) - Recursion stack + path storage

---

### Problem 5: Find All Paths

Find all paths from source to destination using DFS.

```python
def find_all_paths_dfs(graph: Graph, start: int, end: int) -> List[List[int]]
```

**Algorithm:**
1. Use DFS with backtracking
2. Maintain current path
3. When destination is reached, add copy of path to results
4. Continue exploring to find all paths
5. Backtrack by removing vertex from path

**Examples:**
```python
# Diamond graph:
# 0 -> 1 -> 3
# |         ^
# +----2----+
graph = Graph(4)
graph.add_edge(0, 1, directed=True)
graph.add_edge(0, 2, directed=True)
graph.add_edge(1, 3, directed=True)
graph.add_edge(2, 3, directed=True)

find_all_paths_dfs(graph, 0, 3)
# Returns [[0, 1, 3], [0, 2, 3]]
```

**Complexity:**
- Time: O(V! · V) in worst case (complete graph)
- Space: O(V) - Recursion depth + path storage

---

### Problem 6: Connected Components

Find all connected components in an undirected graph.

```python
def find_connected_components(graph: Graph) -> List[List[int]]
```

**Algorithm:**
1. Initialize visited set
2. For each unvisited vertex:
   - Start DFS to find all vertices in this component
   - Add component to results
3. Return list of all components

**Examples:**
```python
# Graph with 3 components:
# 0 -- 1    2 -- 3    4
graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(2, 3)

find_connected_components(graph)
# Returns [[0, 1], [2, 3], [4]]
```

**Complexity:**
- Time: O(V + E) - Visit each vertex and edge once
- Space: O(V) - Visited set + recursion stack

---

### Problem 7: Cycle Detection (Undirected Graph)

Detect if an undirected graph contains a cycle.

```python
def has_cycle_undirected(graph: Graph) -> bool
```

**Algorithm:**
1. Use DFS with parent tracking
2. For each vertex, explore neighbors
3. If we visit a vertex that's already visited AND it's not the parent:
   - Cycle detected!
4. If DFS completes without finding cycle, return False

**Examples:**
```python
# Acyclic graph (tree):
# 0 -- 1 -- 2
#      |
#      3
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
has_cycle_undirected(graph)  # Returns False

# Cyclic graph:
# 0 -- 1
# |    |
# 2 ---+
graph = Graph(3)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
has_cycle_undirected(graph)  # Returns True
```

**Complexity:**
- Time: O(V + E)
- Space: O(V)

---

### Problem 8: Cycle Detection (Directed Graph)

Detect if a directed graph contains a cycle.

```python
def has_cycle_directed(graph: Graph) -> bool
```

**Algorithm:**
1. Use DFS with three states for each vertex:
   - White (unvisited)
   - Gray (being processed - in recursion stack)
   - Black (completely processed)
2. If we visit a gray vertex during DFS:
   - Back edge detected → cycle exists!
3. Mark vertices black when DFS completes

**Examples:**
```python
# Acyclic directed graph (DAG):
# 0 -> 1 -> 2
#      ↓
#      3
graph = Graph(4)
graph.add_edge(0, 1, directed=True)
graph.add_edge(1, 2, directed=True)
graph.add_edge(1, 3, directed=True)
has_cycle_directed(graph)  # Returns False

# Cyclic directed graph:
# 0 -> 1 -> 2
#      ^    |
#      +----+
graph = Graph(3)
graph.add_edge(0, 1, directed=True)
graph.add_edge(1, 2, directed=True)
graph.add_edge(2, 1, directed=True)
has_cycle_directed(graph)  # Returns True
```

**Complexity:**
- Time: O(V + E)
- Space: O(V)

---

### Problem 9: Topological Sort (Kahn's Algorithm - DFS-based)

Perform topological sort on a Directed Acyclic Graph (DAG) using DFS.

```python
def topological_sort_dfs(graph: Graph) -> Optional[List[int]]
```

**Algorithm:**
1. Check if graph has cycle (topological sort only works on DAGs)
2. Use DFS to process vertices
3. Add vertices to result in **post-order** (after processing all descendants)
4. Reverse the result to get topological order

**Examples:**
```python
# Course prerequisite graph:
# 0 (Intro) -> 1 (Data Structures) -> 3 (Algorithms)
#               |
#               v
#              2 (Systems)
graph = Graph(4)
graph.add_edge(0, 1, directed=True)  # Intro before DS
graph.add_edge(1, 2, directed=True)  # DS before Systems
graph.add_edge(1, 3, directed=True)  # DS before Algorithms

topological_sort_dfs(graph)
# Returns [0, 1, 2, 3] or [0, 1, 3, 2] (both valid)

# Graph with cycle:
graph = Graph(2)
graph.add_edge(0, 1, directed=True)
graph.add_edge(1, 0, directed=True)
topological_sort_dfs(graph)  # Returns None (cycle detected)
```

**Complexity:**
- Time: O(V + E)
- Space: O(V)

---

### Problem 10: Is Graph Bipartite?

Determine if a graph is bipartite (can be colored with 2 colors such that no adjacent vertices have the same color).

```python
def is_bipartite(graph: Graph) -> bool
```

**Algorithm:**
1. Use DFS with color assignment
2. Color start vertex with color 0
3. Color all neighbors with opposite color (1)
4. If we try to color a vertex that's already colored:
   - Check if color matches expected color
   - If not, graph is not bipartite
5. Repeat for all components

**Examples:**
```python
# Bipartite graph (tree is always bipartite):
# 0 -- 1 -- 2
#      |
#      3
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
is_bipartite(graph)  # Returns True (colors: 0=A, 1=B, 2=A, 3=A)

# Non-bipartite graph (odd cycle):
# 0 -- 1
# |    |
# 2 ---+
graph = Graph(3)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
is_bipartite(graph)  # Returns False (triangle - odd cycle)
```

**Complexity:**
- Time: O(V + E)
- Space: O(V)

---

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest tests/test_project_35.py -v

# Run specific test class
pytest tests/test_project_35.py::TestGraph -v
pytest tests/test_project_35.py::TestDFS -v

# Run with coverage
pytest tests/test_project_35.py --cov=solution --cov-report=html

# Test specific function
pytest tests/test_project_35.py::TestDFS::test_dfs_recursive -v
```

## 📊 Complexity Analysis

| Function | Time Complexity | Space Complexity | Key Technique |
|----------|----------------|------------------|---------------|
| `Graph.__init__` | O(V²) or O(V) | O(V²) or O(V+E) | Initialize representation |
| `add_edge` | O(1) | O(1) | Add edge to graph |
| `dfs_recursive` | O(V + E) | O(V) | Recursive DFS |
| `dfs_iterative` | O(V + E) | O(V) | Stack-based DFS |
| `find_path_dfs` | O(V + E) | O(V) | DFS with path tracking |
| `find_all_paths_dfs` | O(V! · V) worst | O(V) | DFS with backtracking |
| `find_connected_components` | O(V + E) | O(V) | DFS for each component |
| `has_cycle_undirected` | O(V + E) | O(V) | DFS with parent tracking |
| `has_cycle_directed` | O(V + E) | O(V) | DFS with 3-color marking |
| `topological_sort_dfs` | O(V + E) | O(V) | DFS post-order |
| `is_bipartite` | O(V + E) | O(V) | DFS with 2-coloring |

**Note:** V = number of vertices, E = number of edges

## 💡 Hints

<details>
<summary>Hint 1: DFS Recursive vs Iterative</summary>

**Recursive DFS:**
- Uses call stack implicitly
- More concise code
- Natural for tree-like problems

**Iterative DFS:**
- Uses explicit stack
- More control over execution
- Avoids stack overflow for deep graphs
- Visit order may differ from recursive (but still valid)

Both have the same time/space complexity!
</details>

<details>
<summary>Hint 2: Path Finding</summary>

For path finding:
1. Maintain current path during DFS
2. Add vertex to path when visiting
3. Remove vertex when backtracking
4. When destination is found, return copy of path

For all paths:
- Don't stop at first path
- Use backtracking to explore all possibilities
- Make sure to copy the path when adding to results
</details>

<details>
<summary>Hint 3: Cycle Detection</summary>

**Undirected Graph:**
- Track parent to avoid false positives
- If we visit a vertex that's visited AND not parent → cycle!

**Directed Graph:**
- Use 3 colors: White (unvisited), Gray (in stack), Black (done)
- If we visit a Gray vertex → back edge → cycle!
- This detects actual cycles, not just visited vertices
</details>

<details>
<summary>Hint 4: Topological Sort</summary>

Key insight: Add vertices to result in **post-order** (after processing all descendants), then reverse.

Why? A vertex should come after all its dependencies. By adding in post-order and reversing, we ensure this property.

Think of it as: "Finish all children first, then add the parent"
</details>

<details>
<summary>Hint 5: Bipartite Check</summary>

A graph is bipartite if and only if it contains no odd-length cycles.

Use DFS to try 2-coloring:
- Color start with 0
- Color neighbors with 1
- Color their neighbors with 0
- If conflict occurs → not bipartite

This is essentially checking if the graph can be divided into two independent sets.
</details>

## 🔗 Related Concepts

- **Breadth-First Search (BFS)** (Project 36) - Alternative graph traversal
- **Stacks** (Project 16) - Used in iterative DFS
- **Recursion** (Project 05) - Used in recursive DFS
- **Trees** (Projects 28-30) - Special case of graphs
- **Topological Sorting** - DFS application
- **Strongly Connected Components** - Advanced DFS application

## 📖 References

- [Depth-First Search - GeeksforGeeks](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)
- [Graph Traversal - Wikipedia](https://en.wikipedia.org/wiki/Graph_traversal)
- [Introduction to Algorithms (CLRS)](https://en.wikipedia.org/wiki/Introduction_to_Algorithms) - Chapter 22

## 🎓 Key Insights

### When to Use DFS vs BFS

**Use DFS when:**
- Finding ANY path (not necessarily shortest)
- Detecting cycles
- Topological sorting
- Exploring all possibilities (backtracking)
- Memory is limited (DFS uses less for wide graphs)
- Tree traversals (pre-order, in-order, post-order)

**Use BFS when:**
- Finding shortest path (unweighted)
- Level-order traversal
- Finding all nodes at distance k
- Testing bipartiteness (both work, but BFS is more intuitive)

### DFS Templates

**Basic Recursive DFS:**
```python
def dfs(vertex, visited):
    visited.add(vertex)
    process(vertex)  # Do something with vertex
    for neighbor in graph.get_neighbors(vertex):
        if neighbor not in visited:
            dfs(neighbor, visited)
```

**DFS with Path Tracking:**
```python
def dfs(vertex, visited, path):
    visited.add(vertex)
    path.append(vertex)
    if is_goal(vertex):
        return path.copy()
    for neighbor in graph.get_neighbors(vertex):
        if neighbor not in visited:
            result = dfs(neighbor, visited, path)
            if result:
                return result
    path.pop()  # Backtrack
    return None
```

**Cycle Detection (Directed):**
```python
# WHITE = 0 (unvisited)
# GRAY = 1 (in recursion stack)
# BLACK = 2 (done)

def has_cycle(vertex, color):
    color[vertex] = GRAY
    for neighbor in graph.get_neighbors(vertex):
        if color[neighbor] == GRAY:
            return True  # Back edge - cycle!
        if color[neighbor] == WHITE and has_cycle(neighbor, color):
            return True
    color[vertex] = BLACK
    return False
```

### Common Pitfalls

1. **Forgetting to mark as visited** → Infinite loops
2. **Not handling disconnected graphs** → Some vertices never visited
3. **Confusing undirected vs directed cycle detection** → Different algorithms!
4. **Not copying path when storing** → All paths end up the same
5. **Wrong parent check in undirected cycle detection** → False positives

---

**Estimated Time:** 4-5 hours
**Difficulty:** ⭐⭐⭐ Medium
**Prerequisites:** Recursion, stacks, graph theory basics
