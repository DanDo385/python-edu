# Project 38: Topological Sort

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow.svg)](../../README.md)
[![Concepts](https://img.shields.io/badge/Concepts-Graphs%2C%20DAG%2C%20Topological%20Sort-blue.svg)](../../README.md)

## 🎯 Overview

**Topological Sort** is a linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge u→v, vertex u comes before v in the ordering. Essential for:
- Task scheduling with dependencies
- Build systems and package managers
- Course prerequisites
- Compilation order

## 🎓 Learning Objectives

- Understand topological ordering in DAGs
- Implement Kahn's algorithm (BFS-based)
- Implement DFS-based topological sort
- Detect cycles during topological sort
- Solve course schedule problems

## 📚 Background

### What is a DAG?

**Directed Acyclic Graph (DAG):** Directed graph with no cycles.

**Properties:**
- Every DAG has at least one vertex with in-degree 0
- Every DAG has at least one topological ordering
- If graph has cycle → no topological ordering possible

### Applications

- **Build Systems:** Compile files in correct order
- **Package Managers:** Install dependencies first
- **Course Planning:** Take prerequisites before advanced courses
- **Task Scheduling:** Complete tasks in valid order

## 💻 Problems

### Problem 1: Kahn's Algorithm (BFS-based Topological Sort)

Implement Kahn's algorithm using BFS and in-degree tracking.

```python
def kahns_algorithm(graph: Graph) -> Optional[List[int]]
```

**Algorithm:**
1. Compute in-degree for each vertex
2. Add all vertices with in-degree 0 to queue
3. While queue not empty:
   - Dequeue vertex v
   - Add v to result
   - For each neighbor u of v:
     - Decrease in-degree of u
     - If in-degree becomes 0, enqueue u
4. If result contains all vertices, return it; else return None (cycle detected)

**Complexity:** O(V + E)

---

### Problem 2: DFS-based Topological Sort

Implement topological sort using DFS and post-order traversal.

```python
def topological_sort_dfs(graph: Graph) -> Optional[List[int]]
```

**Algorithm:**
1. Use DFS with 3-color marking (white/gray/black)
2. Visit vertices in post-order
3. Reverse the post-order to get topological order
4. Return None if cycle detected

**Complexity:** O(V + E)

---

### Problem 3: Course Schedule I (LeetCode 207)

Given `numCourses` and prerequisites `prerequisites[i] = [a, b]` (must take b before a), determine if you can finish all courses.

```python
def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool
```

**Approach:** Check if graph is DAG (has topological ordering).

**Complexity:** O(V + E)

---

### Problem 4: Course Schedule II (LeetCode 210)

Return a valid ordering to finish all courses, or empty array if impossible.

```python
def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]
```

**Approach:** Return topological ordering.

**Complexity:** O(V + E)

## 🧪 Testing

```bash
pytest tests/test_project_38.py -v
```

## 📊 Complexity Analysis

| Function | Time | Space | Approach |
|----------|------|-------|----------|
| `kahns_algorithm` | O(V+E) | O(V) | BFS with in-degree |
| `topological_sort_dfs` | O(V+E) | O(V) | DFS post-order |
| `can_finish` | O(V+E) | O(V) | Cycle detection |
| `find_order` | O(V+E) | O(V) | Topological sort |

## 💡 Hints

**Kahn's Algorithm:** Start with vertices having no dependencies (in-degree = 0).

**DFS Approach:** Add vertices to result after visiting all descendants (post-order).

**Cycle Detection:** If topological sort doesn't include all vertices → cycle exists.

---

**Estimated Time:** 3-4 hours
**Difficulty:** ⭐⭐⭐ Medium
**Prerequisites:** DFS, BFS, graphs
