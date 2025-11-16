# Project 36: Breadth-First Search (BFS)

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow.svg)](../../README.md)
[![Concepts](https://img.shields.io/badge/Concepts-Graphs%2C%20BFS%2C%20Shortest%20Path-blue.svg)](../../README.md)

## 🎯 Overview

**Breadth-First Search (BFS)** is a fundamental graph traversal algorithm that explores vertices level by level, starting from a source vertex. Unlike DFS which goes deep first, BFS explores all neighbors at the current depth before moving to the next level. BFS is essential for:
- Finding shortest paths in unweighted graphs
- Level-order traversal of trees
- Finding connected components
- Testing bipartiteness
- Solving puzzles and games (shortest moves)
- Network analysis and social networks

## 🎓 Learning Objectives

By completing this project, you will:
- Master BFS algorithm using queues
- Understand level-by-level graph exploration
- Find shortest paths in unweighted graphs
- Implement level-order traversal
- Solve word ladder and transformation problems
- Compare BFS vs DFS tradeoffs
- Analyze time and space complexity of BFS

## 📚 Background

### What is Breadth-First Search?

BFS is a graph traversal algorithm that explores vertices level by level, visiting all neighbors before moving deeper.

**Core Idea:**
1. Start at a source vertex
2. Visit all immediate neighbors (level 1)
3. Then visit all their neighbors (level 2)
4. Continue level by level until all reachable vertices are visited

**Key Characteristics:**
- **Exploration Strategy:** Level by level (breadth first)
- **Data Structure:** Queue (FIFO - First In First Out)
- **Memory:** O(w) where w is the maximum width
- **Applications:** Shortest path, level-order traversal, minimum moves

**BFS vs DFS:**

| Aspect | BFS | DFS |
|--------|-----|-----|
| Data Structure | Queue | Stack (recursion) |
| Exploration | Level by level | Deep first |
| Memory | O(w) - width | O(h) - height |
| Path Found | Shortest (unweighted) | Not shortest |
| Applications | Shortest path, level-order | Cycle detection, topological sort |

### Why Queue for BFS?

The queue ensures FIFO (First In First Out) processing:
- Vertices added first are processed first
- This guarantees level-by-level exploration
- All vertices at distance k are processed before distance k+1

### Shortest Path Property

**Key Insight:** In an unweighted graph, BFS finds the shortest path!

**Why?** Because BFS explores by levels:
- Level 0: Starting vertex (distance 0)
- Level 1: All vertices at distance 1
- Level 2: All vertices at distance 2
- etc.

The first time BFS reaches a vertex, it's via the shortest path.

## 💻 Problems

Implement the following in `solution/solution.py`:

### Problem 1: BFS Traversal (Queue-based)

Implement BFS to traverse a graph starting from a given vertex. Return vertices in the order they were visited.

```python
def bfs_traversal(graph: Graph, start: int) -> List[int]
```

**Algorithm:**
1. Create a queue and enqueue start vertex
2. Create visited set and result list
3. While queue is not empty:
   - Dequeue vertex
   - If not visited:
     - Mark as visited
     - Add to result
     - Enqueue all unvisited neighbors
4. Return visit order

**Examples:**
```python
# Linear graph: 0 -> 1 -> 2 -> 3
graph = Graph(4)
graph.add_edge(0, 1, directed=True)
graph.add_edge(1, 2, directed=True)
graph.add_edge(2, 3, directed=True)
bfs_traversal(graph, 0)  # Returns [0, 1, 2, 3]

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
bfs_traversal(graph, 0)  # Returns [0, 1, 2, 3]
```

**Complexity:**
- Time: O(V + E) - Visit each vertex once, explore each edge once
- Space: O(V) - Queue + visited set

---

### Problem 2: Shortest Path (Unweighted Graph)

Find the shortest path from start to end in an unweighted graph using BFS. Return the path as a list of vertices.

```python
def shortest_path_bfs(graph: Graph, start: int, end: int) -> Optional[List[int]]
```

**Algorithm:**
1. Use BFS with parent tracking
2. Keep a parent dictionary to reconstruct path
3. When destination is reached, reconstruct path using parent pointers
4. Return path from start to end

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

shortest_path_bfs(graph, 0, 3)  # Returns [0, 1, 3] (shortest path)
shortest_path_bfs(graph, 0, 2)  # Returns [0, 2] or [0, 1, 2]
shortest_path_bfs(graph, 0, 5)  # Returns None (vertex doesn't exist)
```

**Note:** BFS guarantees the shortest path in unweighted graphs!

**Complexity:**
- Time: O(V + E)
- Space: O(V) - Queue + parent dictionary

---

### Problem 3: Level-Order Traversal

Perform level-order traversal of a graph, returning vertices grouped by levels.

```python
def level_order_traversal(graph: Graph, start: int) -> List[List[int]]
```

**Algorithm:**
1. Use BFS with level tracking
2. Process vertices level by level
3. Use a marker (None) or count to separate levels
4. Return list of levels, where each level is a list of vertices

**Examples:**
```python
# Tree:
#     0
#    / \
#   1   2
#  / \
# 3   4
graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)

level_order_traversal(graph, 0)
# Returns [[0], [1, 2], [3, 4]]

# Diamond graph:
#   0
#  / \
# 1   2
#  \ /
#   3
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)

level_order_traversal(graph, 0)
# Returns [[0], [1, 2], [3]]
```

**Complexity:**
- Time: O(V + E)
- Space: O(V) - Queue + result storage

---

### Problem 4: Word Ladder

Given a start word, end word, and a word list, find the shortest transformation sequence from start to end, changing one letter at a time. Each intermediate word must exist in the word list.

```python
def word_ladder(start: str, end: str, word_list: List[str]) -> List[str]
```

**Algorithm:**
1. Build a graph where edges connect words differing by one letter
2. Use BFS to find shortest path from start to end
3. Track parent pointers to reconstruct path
4. Return transformation sequence

**Optimization:** Use pattern matching:
- For each word, create patterns (e.g., "hit" → "*it", "h*t", "hi*")
- Group words by patterns for efficient neighbor finding

**Examples:**
```python
word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
# Returns ["hit", "hot", "dot", "dog", "cog"]
# Transformation: hit → hot → dot → dog → cog

word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
# Returns [] (no path - "cog" not in word list)

word_ladder("a", "c", ["a", "b", "c"])
# Returns ["a", "c"] (assuming single letter change is allowed)
```

**Constraints:**
- All words have the same length
- All words contain only lowercase letters
- Start word doesn't need to be in word list
- End word must be in word list

**Complexity:**
- Time: O(M² × N) where M is word length, N is number of words
- Space: O(M × N) - Pattern dictionary + queue

---

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest tests/test_project_36.py -v

# Run specific test class
pytest tests/test_project_36.py::TestBFS -v
pytest tests/test_project_36.py::TestWordLadder -v

# Run with coverage
pytest tests/test_project_36.py --cov=solution --cov-report=html

# Test specific function
pytest tests/test_project_36.py::TestBFS::test_bfs_traversal -v
```

## 📊 Complexity Analysis

| Function | Time Complexity | Space Complexity | Key Technique |
|----------|----------------|------------------|---------------|
| `bfs_traversal` | O(V + E) | O(V) | Queue-based BFS |
| `shortest_path_bfs` | O(V + E) | O(V) | BFS with parent tracking |
| `level_order_traversal` | O(V + E) | O(V) | BFS with level markers |
| `word_ladder` | O(M² × N) | O(M × N) | BFS on word graph |

**Note:** V = number of vertices, E = number of edges, M = word length, N = number of words

## 💡 Hints

<details>
<summary>Hint 1: BFS Template</summary>

**Basic BFS Template:**
```python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result
```

Key points:
- Use `deque` for O(1) popleft()
- Mark as visited when adding to queue (not when popping)
- Process all vertices in queue
</details>

<details>
<summary>Hint 2: Shortest Path with BFS</summary>

To find the shortest path:
1. Keep a parent dictionary: `parent[child] = parent_vertex`
2. When destination is reached, reconstruct path backwards
3. Reverse the path to get start → end

```python
# Reconstruct path
path = []
current = end
while current is not None:
    path.append(current)
    current = parent.get(current)
path.reverse()
```
</details>

<details>
<summary>Hint 3: Level-Order Traversal</summary>

Two approaches:

**Approach 1: Use None as level marker**
```python
queue = deque([start, None])
# When you see None, you've finished a level
```

**Approach 2: Process level by level**
```python
while queue:
    level_size = len(queue)
    current_level = []
    for _ in range(level_size):
        vertex = queue.popleft()
        current_level.append(vertex)
        # Add neighbors
    levels.append(current_level)
```

Approach 2 is more robust!
</details>

<details>
<summary>Hint 4: Word Ladder</summary>

**Key Optimization: Pattern Matching**

Instead of comparing each word with every other word (O(N²)):
- Create patterns for each word
- Group words by patterns
- Find neighbors by looking up patterns

Example:
```
"hit" → patterns: "*it", "h*t", "hi*"
"hot" → patterns: "*ot", "h*t", "ho*"

Both share pattern "h*t", so they're neighbors!
```

This reduces neighbor finding from O(N × M) to O(M²).
</details>

## 🔗 Related Concepts

- **Depth-First Search (DFS)** (Project 35) - Alternative graph traversal
- **Queues** (Project 12) - Used in BFS
- **Shortest Path Algorithms** (Project 37) - Weighted graphs
- **Graph Representation** (Project 34) - Graph data structures
- **Trees** (Projects 26-30) - Special case where BFS gives level-order

## 📖 References

- [Breadth-First Search - GeeksforGeeks](https://www.geeksforgeeks.org/breadth-first-search-or-dfs-for-a-graph/)
- [BFS Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Introduction to Algorithms (CLRS)](https://en.wikipedia.org/wiki/Introduction_to_Algorithms) - Chapter 22

## 🎓 Key Insights

### When to Use BFS

**Use BFS when:**
- Finding shortest path in unweighted graphs
- Level-order traversal needed
- Finding minimum number of moves/steps
- Finding all nodes at distance k
- Testing if graph is bipartite
- Finding shortest transformation sequence

**Don't use BFS when:**
- Graph is weighted (use Dijkstra instead)
- You need to explore all paths (use DFS with backtracking)
- Memory is limited and graph is very wide (BFS uses more memory than DFS for wide graphs)

### BFS Properties

1. **Shortest Path:** First time a vertex is visited = shortest path
2. **Level-by-Level:** All vertices at distance k are visited before distance k+1
3. **Queue is Essential:** FIFO ensures correct level ordering
4. **Visited Set:** Mark as visited when adding to queue (not when processing)

### Common Pitfalls

1. **Using list instead of deque** → O(n) popleft() instead of O(1)
2. **Marking visited when popping** → Duplicate vertices in queue
3. **Forgetting to check if end is in word list** → Infinite loop in word ladder
4. **Not handling disconnected graphs** → Some vertices never visited

### BFS vs DFS Comparison

| Scenario | Better Choice | Why |
|----------|--------------|-----|
| Shortest path (unweighted) | BFS | Guarantees shortest |
| Path exists check | Either | Both work, DFS uses less memory |
| Level-order traversal | BFS | Natural fit |
| Topological sort | DFS | Post-order processing |
| Detecting cycles | DFS | Easier to track recursion stack |
| Wide shallow graph | DFS | Less memory |
| Narrow deep graph | BFS | Less memory |

---

**Estimated Time:** 3-4 hours
**Difficulty:** ⭐⭐⭐ Medium
**Prerequisites:** Queues, graph theory basics, DFS
