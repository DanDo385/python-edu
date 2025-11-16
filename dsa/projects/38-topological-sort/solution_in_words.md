# Project 38: Topological Sort - Solution Explained

## Concept Overview

**Topological Sort** produces a linear ordering of vertices in a DAG where for every edge u→v, u comes before v. Only possible for Directed Acyclic Graphs (no cycles).

## Two Approaches

### 1. Kahn's Algorithm (BFS-based)

**Idea:** Remove vertices with no incoming edges iteratively.

**Algorithm:**
1. Compute in-degree for each vertex
2. Add all 0 in-degree vertices to queue
3. Process queue: remove vertex, decrease neighbor in-degrees
4. If all vertices processed → valid topological order
5. If not all vertices processed → cycle exists

**Why It Works:** Vertices with no dependencies can be processed first. Removing them updates dependencies for remaining vertices.

**Time:** O(V + E), **Space:** O(V)

### 2. DFS-based Topological Sort

**Idea:** Use post-order DFS traversal, then reverse.

**Algorithm:**
1. Visit vertices using DFS
2. Add vertex to result AFTER visiting all descendants (post-order)
3. Reverse the result

**Why It Works:** Post-order ensures a vertex appears after all its descendants. Reversing puts it before its descendants in topological order.

**Time:** O(V + E), **Space:** O(V)

## Applications

**Course Schedule:** Prerequisites define dependencies. Topological sort gives valid course order.

**Build Systems:** Files depend on imports. Topological sort gives compilation order.

**Task Scheduling:** Tasks have dependencies. Topological sort gives execution order.

## Key Insights

- **DAG Required:** Cycles make topological ordering impossible
- **Multiple Valid Orders:** Most DAGs have multiple valid topological orderings
- **Cycle Detection:** If topological sort fails → cycle exists

Both algorithms have same complexity but different properties:
- Kahn's: More intuitive, explicitly tracks in-degrees
- DFS: More elegant, reuses DFS infrastructure
