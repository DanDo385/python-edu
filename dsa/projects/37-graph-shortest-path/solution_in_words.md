# Project 37: Shortest Path Algorithms - Solution Explained

## Concept Overview

Shortest path algorithms find optimal paths in weighted graphs where edges have costs/weights. Unlike BFS (which works for unweighted graphs), these algorithms handle weights representing distances, times, or costs.

### Three Major Algorithms

1. **Dijkstra's Algorithm** - Fastest for non-negative weights
2. **Bellman-Ford Algorithm** - Handles negative weights, detects negative cycles
3. **Floyd-Warshall Algorithm** - All-pairs shortest paths

## Problem 1: Dijkstra's Algorithm

**Problem:** Find shortest paths from source to all vertices (non-negative weights only).

**Core Idea:** Greedy approach - always expand the closest unvisited vertex.

**Algorithm:**
```
1. Initialize: dist[start] = 0, all others = ∞
2. Use min-heap: (distance, vertex)
3. While heap not empty:
   - Pop vertex u with minimum distance
   - For each neighbor v:
     - If dist[u] + weight(u,v) < dist[v]:
       - Update dist[v]
       - Add (dist[v], v) to heap
```

**Why It Works:**
- Greedy choice is safe: shortest path to closest vertex is final
- Once a vertex is visited, its distance is optimal (proof by contradiction)
- **Only works with non-negative weights!** Negative weights invalidate the greedy assumption

**Complexity:** O((V + E) log V) with binary heap

**Key Insight:** Use priority queue to efficiently select minimum distance vertex.

---

## Problem 2: Bellman-Ford Algorithm

**Problem:** Find shortest paths handling negative weights and detect negative cycles.

**Core Idea:** Relax all edges V-1 times (dynamic programming).

**Algorithm:**
```
1. Initialize: dist[start] = 0, all others = ∞
2. Repeat V-1 times:
   - For each edge (u, v, weight):
     - Relax: dist[v] = min(dist[v], dist[u] + weight)
3. Check negative cycle:
   - Try relaxing edges one more time
   - If any distance improves → negative cycle
```

**Why V-1 Iterations?**
- Shortest simple path has at most V-1 edges
- After iteration k, all paths with ≤k edges are correct
- After V-1 iterations, all shortest paths found

**Negative Cycle Detection:**
- If Vth iteration still improves distances → cycle with negative total weight
- Such cycles make "shortest path" undefined (can loop infinitely reducing cost)

**Complexity:** O(V × E)

**When to Use:** When graph has negative weights or you need to detect negative cycles (e.g., currency arbitrage).

---

## Problem 3: Floyd-Warshall Algorithm

**Problem:** Find shortest paths between all pairs of vertices.

**Core Idea:** Dynamic programming considering intermediate vertices.

**Algorithm:**
```
1. Initialize dist[i][j]:
   - 0 if i == j
   - edge weight if edge exists
   - ∞ otherwise

2. For k = 0 to V-1:  (intermediate vertices)
   For i = 0 to V-1:
     For j = 0 to V-1:
       dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

**DP Recurrence:**
```
dist[i][j] using vertices {0..k} = min(
    dist[i][j] using {0..k-1},     # Don't use k
    dist[i][k] + dist[k][j]         # Use k as intermediate
)
```

**Why It Works:**
- Consider each vertex k as potential intermediate
- Build solution incrementally: paths using {0}, then {0,1}, then {0,1,2}, etc.
- Order matters: must complete iteration k before k+1

**Complexity:** O(V³) - Three nested loops

**When to Use:** Need all-pairs distances, dense graphs, or preprocessing for multiple queries.

---

## Problem 4: Network Delay Time

**Problem:** Time for signal to reach all nodes starting from node k.

**Approach:** Apply Dijkstra's algorithm
1. Build weighted graph from times array
2. Run Dijkstra from node k
3. Find maximum distance (bottleneck)
4. Return -1 if any node unreachable

**Why Dijkstra?**
- Single-source shortest paths problem
- All weights non-negative (time ≥ 0)
- Need distance to all nodes

**Key Insight:** Maximum distance = time for last node to receive signal (all others received earlier).

---

## Algorithm Comparison

| Feature | Dijkstra | Bellman-Ford | Floyd-Warshall |
|---------|----------|--------------|----------------|
| **Weights** | Non-negative only | Any weights | Any weights |
| **Problem** | Single-source | Single-source | All-pairs |
| **Time** | O((V+E) log V) | O(VE) | O(V³) |
| **Space** | O(V) | O(V) | O(V²) |
| **Negative Cycles** | Can't handle | Detects | Detects |
| **Best For** | GPS, routing | Currency, cycles | Dense graphs, preprocessing |

## Key Insights

### When to Use Each Algorithm

**Dijkstra:**
- All weights non-negative ✓
- Need single-source shortest paths ✓
- Performance critical ✓
- Examples: GPS navigation, network routing

**Bellman-Ford:**
- Has negative weights ✓
- Need negative cycle detection ✓
- Simpler to implement ✓
- Examples: Currency arbitrage, financial applications

**Floyd-Warshall:**
- Need all-pairs distances ✓
- Dense graph (E ≈ V²) ✓
- Multiple distance queries ✓
- Examples: Distance matrices, transitive closure

**BFS:**
- Unweighted (or all weights = 1) ✓
- Simplest option ✓
- Examples: Social networks, minimum moves

### Common Pitfalls

1. **Using Dijkstra with negative weights** → Incorrect results!
2. **Forgetting negative cycle check** → Infinite loops
3. **Off-by-one in Floyd-Warshall** → Wrong intermediate vertices
4. **Not initializing to ∞** → Incorrect comparisons
5. **Mixing up 0-indexed vs 1-indexed** → Array bounds errors

### Implementation Tips

**Dijkstra with Priority Queue:**
```python
import heapq
pq = [(0, start)]  # (distance, vertex)
while pq:
    dist, u = heapq.heappop(pq)
    for v, weight in neighbors(u):
        new_dist = dist + weight
        if new_dist < distances[v]:
            distances[v] = new_dist
            heapq.heappush(pq, (new_dist, v))
```

**Bellman-Ford Relaxation:**
```python
for _ in range(V - 1):
    for u, v, weight in edges:
        if dist[u] + weight < dist[v]:
            dist[v] = dist[u] + weight
```

**Floyd-Warshall Pattern:**
```python
for k in range(V):
    for i in range(V):
        for j in range(V):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

## Conclusion

Shortest path algorithms are fundamental to graph theory and have countless real-world applications. Understanding when to use each algorithm is crucial:
- **Dijkstra** for speed with non-negative weights
- **Bellman-Ford** for negative weights and cycle detection
- **Floyd-Warshall** for all-pairs in dense graphs

Master these algorithms and you can solve a wide range of optimization problems!
