# Project 37: Shortest Path Algorithms

[![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red.svg)](../../README.md)
[![Concepts](https://img.shields.io/badge/Concepts-Graphs%2C%20Shortest%20Path%2C%20Weighted%20Graphs-blue.svg)](../../README.md)

## 🎯 Overview

**Shortest Path Algorithms** are fundamental techniques for finding optimal paths in weighted graphs. While BFS finds shortest paths in unweighted graphs, these algorithms handle weighted edges representing distances, costs, or times:
- Dijkstra's algorithm for non-negative weights
- Bellman-Ford for graphs with negative weights
- Floyd-Warshall for all-pairs shortest paths
- Applications in navigation, network routing, and optimization

## 🎓 Learning Objectives

By completing this project, you will:
- Master Dijkstra's algorithm using priority queues
- Understand Bellman-Ford for negative edge weights
- Implement Floyd-Warshall for all-pairs shortest paths
- Apply shortest path algorithms to real problems
- Understand when to use each algorithm
- Analyze time and space complexity trade-offs

## 📚 Background

### Weighted Graphs

In a **weighted graph**, each edge has a numerical weight (cost, distance, time).

**Examples:**
- Road networks: edges = roads, weights = distances/times
- Computer networks: edges = connections, weights = latency
- Flight routes: edges = flights, weights = costs

### Shortest Path Problem Variants

**1. Single-Source Shortest Path (SSSP)**
- Find shortest paths from one vertex to all others
- Algorithms: Dijkstra, Bellman-Ford

**2. All-Pairs Shortest Path (APSP)**
- Find shortest paths between all vertex pairs
- Algorithm: Floyd-Warshall

**3. Single-Pair Shortest Path**
- Find shortest path between two specific vertices
- Use SSSP algorithms, stop when target reached

### Algorithm Comparison

| Algorithm | Graph Type | Time | Space | Use Case |
|-----------|-----------|------|-------|----------|
| BFS | Unweighted | O(V+E) | O(V) | Unweighted shortest path |
| Dijkstra | Non-negative weights | O((V+E) log V) | O(V) | GPS, routing |
| Bellman-Ford | Any weights | O(VE) | O(V) | Currency exchange, detect negative cycles |
| Floyd-Warshall | Any weights | O(V³) | O(V²) | All-pairs, dense graphs |

## 💻 Problems

Implement the following in `solution/solution.py`:

### Problem 1: Dijkstra's Algorithm

Implement Dijkstra's algorithm to find shortest paths from a source vertex to all other vertices in a graph with non-negative edge weights.

```python
def dijkstra(graph: WeightedGraph, start: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]
```

**Algorithm:**
1. Initialize distances: dist[start] = 0, all others = ∞
2. Use min-heap priority queue with (distance, vertex)
3. While queue not empty:
   - Pop vertex with minimum distance
   - For each neighbor:
     - Calculate new distance via current vertex
     - If new distance < current distance:
       - Update distance
       - Update parent
       - Add to queue
4. Return distances and parents

**Examples:**
```python
# Graph with weighted edges
g = WeightedGraph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(2, 1, 2)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 5)
g.add_edge(3, 4, 3)

distances, parents = dijkstra(g, 0)
# distances = {0: 0, 1: 3, 2: 1, 3: 4, 4: 7}
# Shortest path 0→4: 0→2→1→3→4 (distance = 7)
```

**Complexity:**
- Time: O((V + E) log V) with binary heap
- Space: O(V) for distances and priority queue

---

### Problem 2: Bellman-Ford Algorithm

Implement Bellman-Ford algorithm that handles negative edge weights and detects negative cycles.

```python
def bellman_ford(graph: WeightedGraph, start: int) -> Optional[Tuple[Dict[int, float], Dict[int, Optional[int]]]]
```

**Algorithm:**
1. Initialize distances: dist[start] = 0, all others = ∞
2. Relax all edges V-1 times:
   - For each edge (u, v, weight):
     - If dist[u] + weight < dist[v]:
       - Update dist[v] and parent[v]
3. Check for negative cycles:
   - Run relaxation one more time
   - If any distance updates → negative cycle exists
4. Return distances and parents (or None if negative cycle)

**Examples:**
```python
# Graph with negative weights
g = WeightedGraph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)

distances, parents = bellman_ford(g, 0)
# distances = {0: 0, 1: -1, 2: 2, 3: 1, 4: ∞}

# Graph with negative cycle
g2 = WeightedGraph(3)
g2.add_edge(0, 1, 1)
g2.add_edge(1, 2, -3)
g2.add_edge(2, 1, 2)  # Cycle 1→2→1 has weight -1
result = bellman_ford(g2, 0)
# result = None (negative cycle detected)
```

**Complexity:**
- Time: O(V × E)
- Space: O(V)

---

### Problem 3: Floyd-Warshall Algorithm

Implement Floyd-Warshall to find shortest paths between all pairs of vertices.

```python
def floyd_warshall(graph: WeightedGraph) -> Optional[List[List[float]]]
```

**Algorithm:**
1. Initialize distance matrix:
   - dist[i][i] = 0
   - dist[i][j] = edge weight if edge exists
   - dist[i][j] = ∞ otherwise
2. For each intermediate vertex k:
   - For each pair (i, j):
     - dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
3. Check for negative cycles:
   - If any dist[i][i] < 0 → negative cycle
4. Return distance matrix

**Examples:**
```python
g = WeightedGraph(4)
g.add_edge(0, 1, 3)
g.add_edge(0, 3, 7)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 1)

distances = floyd_warshall(g)
# distances[0][3] = 5  (path: 0→1→3)
# distances[0][2] = 4  (path: 0→1→2)
```

**Complexity:**
- Time: O(V³)
- Space: O(V²)

---

### Problem 4: Network Delay Time (LeetCode 743)

Given a network of `n` nodes, times `times[i] = (u, v, w)` indicating a signal takes `w` time to travel from node `u` to node `v`, and a starting node `k`, return the time it takes for all nodes to receive the signal. Return -1 if impossible.

```python
def network_delay_time(times: List[List[int]], n: int, k: int) -> int
```

**Approach:** Use Dijkstra's algorithm
1. Build weighted graph from times
2. Run Dijkstra from node k
3. Find maximum distance among all reachable nodes
4. If any node unreachable, return -1

**Examples:**
```python
times = [[2,1,1], [2,3,1], [3,4,1]]
n = 4
k = 2
network_delay_time(times, n, k)  # Returns 2
# Signal path: 2→1 (1), 2→3 (1), 3→4 (2)
# Maximum time is 2

times = [[1,2,1]]
n = 2
k = 1
network_delay_time(times, n, k)  # Returns 1

times = [[1,2,1]]
n = 2
k = 2
network_delay_time(times, n, k)  # Returns -1 (node 1 unreachable from 2)
```

**Complexity:**
- Time: O((V + E) log V)
- Space: O(V + E)

---

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest tests/test_project_37.py -v

# Run specific test class
pytest tests/test_project_37.py::TestDijkstra -v
pytest tests/test_project_37.py::TestBellmanFord -v

# Run with coverage
pytest tests/test_project_37.py --cov=solution --cov-report=html
```

## 📊 Complexity Analysis

| Function | Time Complexity | Space Complexity | Key Feature |
|----------|----------------|------------------|-------------|
| `dijkstra` | O((V+E) log V) | O(V) | Non-negative weights only |
| `bellman_ford` | O(V × E) | O(V) | Handles negative weights |
| `floyd_warshall` | O(V³) | O(V²) | All-pairs shortest paths |
| `network_delay_time` | O((V+E) log V) | O(V+E) | Dijkstra application |

## 💡 Hints

<details>
<summary>Hint 1: Dijkstra's Algorithm</summary>

**Key Points:**
- Use min-heap (priority queue) to always process closest vertex
- Mark vertices as visited to avoid reprocessing
- Only works with non-negative weights

**Python Priority Queue:**
```python
import heapq
heap = []
heapq.heappush(heap, (distance, vertex))
dist, vertex = heapq.heappop(heap)
```

**Why non-negative weights only?**
- Dijkstra assumes once a vertex is processed, its distance is final
- Negative edges could create shorter paths through already-processed vertices
</details>

<details>
<summary>Hint 2: Bellman-Ford Relaxation</summary>

**Edge Relaxation:**
```python
if dist[u] + weight < dist[v]:
    dist[v] = dist[u] + weight
    parent[v] = u
```

**Why V-1 iterations?**
- Shortest path has at most V-1 edges (simple path)
- After k iterations, all paths with ≤k edges are correct
- After V-1 iterations, all shortest paths are found

**Negative Cycle Detection:**
- If relaxation succeeds in iteration V → cycle exists
- Distances decrease indefinitely in negative cycles
</details>

<details>
<summary>Hint 3: Floyd-Warshall Dynamic Programming</summary>

**DP Insight:**
```
dist[i][j] via k = min(
    dist[i][j],           # Direct path
    dist[i][k] + dist[k][j]  # Path through k
)
```

**Why this works:**
- Consider all possible intermediate vertices
- Build solutions bottom-up
- Order matters: must process k=0, then k=1, etc.

**3D to 2D optimization:**
- Can use same array for updates (space optimization)
- dist[i][j] represents "using vertices 0..k as intermediates"
</details>

<details>
<summary>Hint 4: Network Delay Time</summary>

**Steps:**
1. Build adjacency list from times array
2. Run Dijkstra from source node k
3. Find max distance (bottleneck)
4. Check if all nodes reachable

**Edge Cases:**
- Some nodes unreachable → return -1
- Single node → return 0
- Disconnected graph → return -1
</details>

## 🔗 Related Concepts

- **BFS** (Project 36) - Shortest path in unweighted graphs
- **Priority Queues/Heaps** (Projects 31-33) - Used in Dijkstra
- **Dynamic Programming** (Projects 41-47) - Floyd-Warshall uses DP
- **Graph Representation** (Project 34) - Weighted graphs
- **Topological Sort** (Project 38) - DAG shortest paths

## 📖 References

- [Dijkstra's Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [Bellman-Ford - Wikipedia](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)
- [Floyd-Warshall - Wikipedia](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)
- [Introduction to Algorithms (CLRS)](https://en.wikipedia.org/wiki/Introduction_to_Algorithms) - Chapter 24

## 🎓 Key Insights

### Algorithm Selection Guide

**Use Dijkstra when:**
- All edge weights are non-negative
- Need single-source shortest paths
- Performance is critical
- Examples: GPS navigation, network routing

**Use Bellman-Ford when:**
- Graph has negative edge weights
- Need to detect negative cycles
- Simpler implementation preferred
- Examples: Currency arbitrage, some games

**Use Floyd-Warshall when:**
- Need all-pairs shortest paths
- Graph is dense
- Preprocessing time acceptable
- Examples: Distance matrices, transitive closure

**Use BFS when:**
- Graph is unweighted (or all weights equal)
- Simplest and fastest option
- Examples: Social networks, unweighted mazes

### Common Pitfalls

1. **Using Dijkstra with negative weights** → Incorrect results
2. **Forgetting negative cycle check in Bellman-Ford** → Infinite loops
3. **Off-by-one errors in Floyd-Warshall** → Wrong intermediate vertices
4. **Not initializing distances to infinity** → Incorrect comparisons
5. **Forgetting to handle unreachable vertices** → Crashes or wrong answers

---

**Estimated Time:** 5-6 hours
**Difficulty:** ⭐⭐⭐⭐ Hard
**Prerequisites:** Graphs, priority queues, dynamic programming basics
