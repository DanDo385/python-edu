# Project 36: Breadth-First Search - Solution Explained

## Concept Overview

**Breadth-First Search (BFS)** is a graph traversal algorithm that explores vertices level by level, starting from a source vertex. Unlike DFS which goes deep first, BFS explores all immediate neighbors before moving to the next level.

### Core Principle

The key insight of BFS is: **Explore level by level**. All vertices at distance k from the source are visited before any vertex at distance k+1.

BFS uses a **queue** data structure (FIFO - First In First Out) to maintain the frontier of vertices to explore. This FIFO nature ensures level-by-level exploration.

### Why BFS Matters

BFS is essential for:
- **Shortest paths** - Guarantees shortest path in unweighted graphs
- **Level-order traversal** - Natural fit for tree/graph level processing
- **Minimum steps problems** - Finding minimum moves in puzzles/games
- **Network analysis** - Finding distances and connectivity

## Problem 1: BFS Traversal

**Problem:** Traverse a graph starting from a given vertex, visiting all reachable vertices level by level.

**Approach:**

The BFS algorithm uses a queue to maintain the frontier:

```
Algorithm:
1. Initialize queue with start vertex
2. Mark start as visited
3. While queue is not empty:
   - Dequeue vertex from front
   - Process vertex (add to result)
   - Enqueue all unvisited neighbors
   - Mark neighbors as visited when adding to queue
4. Return visit order
```

**Why This Works:**

The queue ensures FIFO processing:
- Vertices added first are processed first
- All vertices at distance 1 are enqueued before distance 2
- This guarantees level-by-level exploration

**Key Implementation Details:**

1. **Mark visited when adding to queue** - Not when popping! This prevents duplicate entries.
2. **Use deque for O(1) operations** - `collections.deque` provides O(1) popleft()
3. **Track visited set** - Essential to avoid infinite loops

**Example Walkthrough:**

```
Graph: 0 -- 1 -- 3
       |
       2

BFS from 0:

Initial: queue = [0], visited = {0}

Step 1: Dequeue 0
  - Add 0 to result: [0]
  - Enqueue neighbors 1, 2
  - queue = [1, 2], visited = {0, 1, 2}

Step 2: Dequeue 1
  - Add 1 to result: [0, 1]
  - Enqueue neighbor 3
  - queue = [2, 3], visited = {0, 1, 2, 3}

Step 3: Dequeue 2
  - Add 2 to result: [0, 1, 2]
  - No new neighbors
  - queue = [3]

Step 4: Dequeue 3
  - Add 3 to result: [0, 1, 2, 3]
  - No new neighbors
  - queue = []

Final result: [0, 1, 2, 3]
```

**Complexity:**
- **Time:** O(V + E) - Visit each vertex once, explore each edge once
- **Space:** O(V) - Queue and visited set can hold up to V vertices

---

## Problem 2: Shortest Path (Unweighted Graph)

**Problem:** Find the shortest path from start to end in an unweighted graph.

**Approach:**

BFS guarantees the shortest path because it explores level by level. The first time we reach a vertex, it's via the shortest path!

```
Algorithm:
1. Use BFS with parent tracking
2. Keep a parent dictionary: parent[child] = parent_vertex
3. When destination is reached:
   - Reconstruct path by following parent pointers
   - Reverse to get path from start to end
4. Return path
```

**Why BFS Finds Shortest Path:**

**Key Insight:** BFS explores by distance:
- Level 0: Start vertex (distance 0)
- Level 1: All vertices at distance 1
- Level 2: All vertices at distance 2
- etc.

The first time BFS reaches a vertex, we've found the shortest path because:
- All shorter paths would have been explored first
- We explore distance k before distance k+1

**Path Reconstruction:**

```python
# When we reach destination, reconstruct path:
path = []
current = end
while current is not None:
    path.append(current)
    current = parent[current]
path.reverse()  # Reverse to get start → end
```

**Example:**

```
Graph: 0 -- 1 -- 3
       |    |
       2 ---+

Finding shortest path from 0 to 3:

BFS exploration:
- Distance 0: vertex 0
- Distance 1: vertices 1, 2 (neighbors of 0)
- Distance 2: vertex 3 (neighbor of 1 and 2)

Parent tracking:
- parent[0] = None
- parent[1] = 0
- parent[2] = 0
- parent[3] = 1  (3 is reached from 1 first)

Reconstructed path: 3 → 1 → 0 → None
Reversed: [0, 1, 3] ✓ (shortest path!)
```

**Complexity:**
- **Time:** O(V + E)
- **Space:** O(V) for queue and parent dictionary

---

## Problem 3: Level-Order Traversal

**Problem:** Return vertices grouped by their distance from the start vertex.

**Approach:**

Process the queue level by level using a clever technique:

```
Algorithm:
1. Initialize queue with start vertex
2. While queue is not empty:
   - Record current queue size (this is the level size)
   - Process exactly that many vertices
   - All neighbors added form the next level
3. Return list of levels
```

**Why This Works:**

At any point, the queue contains vertices from at most 2 consecutive levels. By processing `queue.size()` vertices at a time, we process exactly one level.

**Example:**

```
Tree:     0
        /   \
       1     2
      / \
     3   4

Level-by-level processing:

Initial: queue = [0]

Level 0:
  - level_size = 1
  - Process 0, add neighbors 1, 2
  - current_level = [0]
  - queue = [1, 2]

Level 1:
  - level_size = 2
  - Process 1, add neighbors 3, 4
  - Process 2, no neighbors
  - current_level = [1, 2]
  - queue = [3, 4]

Level 2:
  - level_size = 2
  - Process 3, 4
  - current_level = [3, 4]
  - queue = []

Result: [[0], [1, 2], [3, 4]]
```

**Alternative Approach:**

Using None as level marker:
```python
queue = deque([start, None])
while queue:
    vertex = queue.popleft()
    if vertex is None:
        if queue:  # More levels exist
            queue.append(None)  # Mark end of next level
        continue
    # Process vertex...
```

**Complexity:**
- **Time:** O(V + E)
- **Space:** O(V)

---

## Problem 4: Word Ladder

**Problem:** Find shortest transformation sequence from start word to end word, changing one letter at a time.

**Approach:**

This is a shortest path problem! Each word is a vertex, and edges connect words differing by one letter.

**Naive Approach (Inefficient):**
```
For each word, compare with every other word: O(N² × M)
```

**Optimized Approach - Pattern Matching:**

```
Key Optimization:
Instead of comparing all pairs, use pattern matching:
- For "hit": create patterns "*it", "h*t", "hi*"
- Group words by patterns
- Words sharing a pattern are neighbors!
```

**Algorithm:**
```
1. Build pattern dictionary:
   - For each word, create all patterns
   - Group words by patterns

2. BFS:
   - Start from start word
   - For current word, check all patterns
   - Each pattern gives list of neighbors
   - Track parents for path reconstruction
   - When end word is reached, reconstruct path
```

**Example:**

```
Words: ["hit", "hot", "dot", "dog", "cog"]

Pattern dictionary:
  "*it": ["hit"]
  "h*t": ["hit", "hot"]
  "hi*": ["hit"]
  "*ot": ["hot", "dot"]
  "ho*": ["hot"]
  "d*t": ["dot"]
  "do*": ["dot", "dog"]
  "*og": ["dog", "cog"]
  "d*g": ["dog"]
  "co*": ["cog"]
  "c*g": ["cog"]

BFS from "hit" to "cog":

Step 1: current = "hit"
  - Pattern "h*t": neighbors ["hot"]
  - Enqueue "hot"

Step 2: current = "hot"
  - Pattern "*ot": neighbors ["dot"]
  - Pattern "do*": neighbors ["dot"]
  - Enqueue "dot"

Step 3: current = "dot"
  - Pattern "do*": neighbors ["dog"]
  - Enqueue "dog"

Step 4: current = "dog"
  - Pattern "*og": neighbors ["cog"]
  - Found end! Reconstruct path

Path: hit → hot → dot → dog → cog
```

**Why Pattern Matching is Faster:**

- **Without patterns:** O(N² × M) - compare every word pair
- **With patterns:** O(M² × N) - create M patterns per word, compare patterns

For typical word ladder problems, M (word length) << N (number of words), so this is much faster!

**Complexity:**
- **Time:** O(M² × N) where M = word length, N = number of words
- **Space:** O(M × N) for pattern dictionary

---

## Key Insights

### BFS vs DFS

| Aspect | BFS | DFS |
|--------|-----|-----|
| Data Structure | Queue (FIFO) | Stack/Recursion (LIFO) |
| Exploration | Level by level | Deep first |
| Shortest Path | Yes (unweighted) | No |
| Memory | O(width) | O(height) |
| Best For | Shortest path, level-order | Cycles, topological sort |

### When to Use BFS

**Use BFS when:**
- Finding shortest path in unweighted graphs
- Need level-order traversal
- Finding minimum number of steps/moves
- Testing if target is within k steps
- Finding all nodes at distance k

**Don't use BFS when:**
- Graph is weighted (use Dijkstra instead)
- Need to explore all paths (use DFS with backtracking)
- Graph is very wide (BFS uses more memory)

### Common Pitfalls

1. **Using list instead of deque**
   - `list.pop(0)` is O(n), not O(1)!
   - Always use `collections.deque`

2. **Marking visited when popping**
   - Mark when adding to queue
   - Otherwise, duplicates in queue

3. **Forgetting parent tracking**
   - Need parent dictionary for path reconstruction
   - Can't reconstruct shortest path without it

4. **Not handling edge cases**
   - What if start == end?
   - What if graph is disconnected?
   - What if end word not in list?

### BFS Template (Master This!)

```python
from collections import deque

def bfs_template(graph, start):
    queue = deque([start])
    visited = {start}

    while queue:
        vertex = queue.popleft()

        # Process vertex
        process(vertex)

        # Explore neighbors
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

**For shortest path, add:**
```python
parent = {start: None}

# In loop:
parent[neighbor] = vertex

# Reconstruct path:
path = []
current = end
while current is not None:
    path.append(current)
    current = parent[current]
path.reverse()
```

**For level-order, add:**
```python
while queue:
    level_size = len(queue)
    current_level = []

    for _ in range(level_size):
        vertex = queue.popleft()
        current_level.append(vertex)
        # ... add neighbors

    levels.append(current_level)
```

## Conclusion

BFS is a fundamental algorithm every programmer must master. Its level-by-level exploration makes it perfect for shortest path problems and level-order traversals. The key is understanding the queue-based approach and how to adapt it for different problems (path tracking, level grouping, pattern matching).

Remember: **BFS guarantees shortest path in unweighted graphs!** This is its superpower.
