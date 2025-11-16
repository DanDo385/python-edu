# Project 35: Depth-First Search - Solution Explained

## Concept Overview

**Depth-First Search (DFS)** is a fundamental graph traversal algorithm that explores as far as possible along each branch before backtracking. Think of it like exploring a maze: you follow one path all the way until you hit a dead end, then backtrack to try a different path.

### Core Principle

The key insight of DFS is: **Go deep first, then wide**. This is in contrast to Breadth-First Search (BFS), which explores level by level.

DFS uses a **stack** data structure (either explicitly or implicitly through recursion) to keep track of which vertices to visit next. This LIFO (Last-In-First-Out) nature causes DFS to explore deeply before exploring neighbors.

### Why DFS Matters

DFS is one of the most versatile graph algorithms:
- **Simple to implement** - Especially the recursive version
- **Memory efficient** - O(h) space where h is the height/depth
- **Powerful applications** - Cycle detection, topological sorting, finding connected components
- **Foundation for advanced algorithms** - Strongly connected components, articulation points

## Graph Representations

Before diving into DFS, we need to understand how to represent graphs in code.

### Adjacency List

**Structure:** Dictionary mapping each vertex to a list of its neighbors.

```
Graph: 0 -- 1 -- 2
       |
       3

Adjacency List:
{
  0: [1, 3],
  1: [0, 2],
  2: [1],
  3: [0]
}
```

**Pros:**
- Space efficient for sparse graphs: O(V + E)
- Fast to iterate over neighbors: O(degree)
- Easy to add edges: O(1)

**Cons:**
- Checking if edge exists: O(degree) - must scan the list

**When to use:** Most graphs in practice (social networks, road maps, etc.)

### Adjacency Matrix

**Structure:** 2D array where matrix[i][j] = 1 if edge exists from i to j.

```
Graph: 0 -> 1 -> 2

Adjacency Matrix:
  0 1 2
0 [0 1 0]
1 [0 0 1]
2 [0 0 0]
```

**Pros:**
- Check if edge exists: O(1) - direct array access
- Good for dense graphs: When E ≈ V²

**Cons:**
- Space: O(V²) - even for sparse graphs
- Iterating neighbors: O(V) - must scan entire row

**When to use:** Dense graphs, when you need fast edge lookups

## DFS Algorithms Explained

### Algorithm 1: DFS Recursive

**Problem:** Traverse a graph starting from a given vertex, visiting all reachable vertices.

**Approach:**

The recursive approach is the most natural way to implement DFS:

```
Algorithm:
1. Mark current vertex as visited
2. Process current vertex (add to result)
3. For each unvisited neighbor:
   - Recursively call DFS on neighbor
```

**Why This Works:**

The call stack acts as the implicit stack for DFS. When we recursively visit a neighbor, we're going "deep" into that path. When the recursive call returns (no more unvisited neighbors), we naturally backtrack.

**Key Details:**

1. **Visited Set:** Essential to avoid infinite loops in graphs with cycles
2. **Processing Order:** We process a vertex when we first visit it (pre-order)
3. **Backtracking:** Happens automatically when function returns

**Complexity:**
- **Time:** O(V + E) - Visit each vertex once, explore each edge once
- **Space:** O(V) - Visited set + recursion stack (up to V deep)

**Example Walkthrough:**

```
Graph: 0 -- 1 -- 3
       |
       2

DFS from 0:

Step 1: Visit 0
  visited = {0}
  result = [0]
  neighbors = [1, 2]

Step 2: Visit 1 (first neighbor)
  visited = {0, 1}
  result = [0, 1]
  neighbors = [0, 3]  (0 is visited, skip)

Step 3: Visit 3 (neighbor of 1)
  visited = {0, 1, 3}
  result = [0, 1, 3]
  neighbors = [1]  (1 is visited, skip)

Step 4: Backtrack to 1 (no more neighbors)
Step 5: Backtrack to 0
Step 6: Visit 2 (second neighbor of 0)
  visited = {0, 1, 3, 2}
  result = [0, 1, 3, 2]

Final result: [0, 1, 3, 2]
```

---

### Algorithm 2: DFS Iterative

**Problem:** Same as recursive DFS, but without using recursion.

**Approach:**

```
Algorithm:
1. Create explicit stack, push start vertex
2. While stack is not empty:
   a. Pop vertex from stack
   b. If not visited:
      - Mark as visited
      - Process vertex
      - Push all unvisited neighbors to stack
```

**Why This Works:**

We're explicitly simulating what the recursive version does with the call stack. The stack stores vertices to visit next, and we pop them one by one.

**Key Differences from Recursive:**

1. **Explicit Stack:** We manage our own stack
2. **Visit Order:** May differ slightly from recursive due to stack ordering
3. **No Stack Overflow:** Can handle very deep graphs

**Complexity:**
- **Time:** O(V + E) - Same as recursive
- **Space:** O(V) - Explicit stack instead of call stack

**Example:**

```
Graph: 0 -> 1 -> 2 -> 3

Iteration 1:
  stack = [0]
  pop 0, visit it
  result = [0]
  push neighbors: stack = [1]

Iteration 2:
  stack = [1]
  pop 1, visit it
  result = [0, 1]
  push neighbors: stack = [2]

Iteration 3:
  stack = [2]
  pop 2, visit it
  result = [0, 1, 2]
  push neighbors: stack = [3]

Iteration 4:
  stack = [3]
  pop 3, visit it
  result = [0, 1, 2, 3]
  no neighbors

Final result: [0, 1, 2, 3]
```

---

### Algorithm 3: Path Finding with DFS

**Problem:** Find ANY path from start to end (not necessarily the shortest).

**Key Insight:**

We need to track the **current path** as we explore. When we backtrack, we remove vertices from the path.

**Approach:**

```
Algorithm:
1. Maintain current path list
2. DFS with modifications:
   - Add vertex to path when visiting
   - If destination reached: return path
   - Explore neighbors recursively
   - Remove vertex from path when backtracking (important!)
```

**Why Backtracking Matters:**

If we don't remove vertices when backtracking, the path will contain all explored vertices, not just the path to the destination.

**Example:**

```
Graph: 0 -- 1 -- 3
       |    |
       2 ---+

Find path from 0 to 3:

Path 1: Try 0 -> 1 -> 3
  Visit 0: path = [0]
  Visit 1: path = [0, 1]
  Visit 3: path = [0, 1, 3] ✓ Found!

Alternative path (if we tried 2 first):
  Visit 0: path = [0]
  Visit 2: path = [0, 2]
  Visit 1: path = [0, 2, 1]
  Visit 3: path = [0, 2, 1, 3] ✓ Found!

Both are valid paths!
```

**Complexity:**
- **Time:** O(V + E) - In the worst case
- **Space:** O(V) - Path storage + recursion stack

---

### Algorithm 4: Finding All Paths

**Problem:** Find ALL paths from start to end.

**Key Difference from Single Path:**

Don't stop at the first path! Continue exploring all possibilities.

**Approach:**

```
Algorithm:
1. Maintain current path and list of all paths
2. DFS with modifications:
   - Add vertex to path and visited
   - If destination: save COPY of path (important!)
   - Explore all neighbors
   - Remove vertex from BOTH path and visited (backtracking)
```

**Why Remove from Visited?**

Unlike simple DFS, we need to allow vertices to be visited multiple times in different paths. For example, in a diamond graph, the middle vertices might be part of multiple paths.

**Example:**

```
Graph: 0 -> 1 -> 3
       |         ^
       +----2----+

Find all paths from 0 to 3:

Exploration 1: 0 -> 1 -> 3
  path = [0]
  path = [0, 1]
  path = [0, 1, 3] ✓ Save [0, 1, 3]
  Backtrack: path = [0, 1], visited removes 3
  Backtrack: path = [0], visited removes 1

Exploration 2: 0 -> 2 -> 3
  path = [0, 2]
  path = [0, 2, 3] ✓ Save [0, 2, 3]

Result: [[0, 1, 3], [0, 2, 3]]
```

**Complexity:**
- **Time:** O(V! · V) in worst case (complete graph with many paths)
- **Space:** O(V) for recursion depth

---

### Algorithm 5: Connected Components

**Problem:** Find all connected components in an undirected graph.

**Key Insight:**

A connected component is a maximal set of vertices where there's a path between any two vertices.

**Approach:**

```
Algorithm:
1. Initialize global visited set
2. For each vertex 0 to V-1:
   - If not visited:
     - Start DFS to find all vertices in this component
     - Add component to results
```

**Why This Works:**

Each DFS finds one complete component. By trying all vertices as starting points, we ensure we find all components (even in disconnected graphs).

**Example:**

```
Graph: 0 -- 1    2 -- 3    4

Components:
- DFS from 0: finds {0, 1}
- DFS from 2: finds {2, 3}
- DFS from 4: finds {4}

Result: [[0, 1], [2, 3], [4]]
```

**Complexity:**
- **Time:** O(V + E) - Visit each vertex and edge once
- **Space:** O(V) - Visited set

---

### Algorithm 6: Cycle Detection (Undirected Graph)

**Problem:** Detect if an undirected graph contains a cycle.

**Key Insight:**

In an undirected graph, if we visit a vertex that's already visited AND it's not our parent (where we came from), we've found a cycle!

**Why Parent Matters:**

In undirected graphs, edges go both ways. If we're at vertex 1 (came from vertex 0), vertex 0 is in our neighbors. But visiting 0 from 1 doesn't mean there's a cycle - it's just the edge we came from!

**Approach:**

```
Algorithm:
1. DFS with parent parameter
2. For each neighbor:
   - If not visited: recursively check
   - If visited AND not parent: CYCLE!
```

**Example:**

```
Tree (No Cycle):
0 -- 1 -- 2
     |
     3

DFS from 0:
  At 0: parent = -1, visit 1
  At 1: parent = 0, visit 2 and 3
  At 2: parent = 1, neighbor 1 is parent (skip)
  At 3: parent = 1, neighbor 1 is parent (skip)
  No cycle found ✓

Cycle Graph:
0 -- 1
|    |
2 ---+

DFS from 0:
  At 0: parent = -1, visit 1
  At 1: parent = 0, visit 2
  At 2: parent = 1, neighbor 0 is visited AND not parent
  CYCLE DETECTED! ✗
```

**Complexity:**
- **Time:** O(V + E)
- **Space:** O(V)

---

### Algorithm 7: Cycle Detection (Directed Graph)

**Problem:** Detect if a directed graph contains a cycle.

**Key Insight:**

Directed graphs are trickier! We need three states:
- **White (0):** Unvisited
- **Gray (1):** Being processed (in recursion stack)
- **Black (2):** Completely done

If we encounter a **Gray** vertex, we've found a **back edge** → cycle!

**Why Three Colors?**

Consider: 0 → 1 → 2, 0 → 3

When we finish processing 1 and 2, then visit 3, we might see that 1 is visited. But this doesn't mean cycle! 1 is completely done (Black), not in our current path.

If 1 were Gray, it means it's in our current recursion stack (current path) → back edge → cycle!

**Approach:**

```
Algorithm:
1. Initialize all vertices as White
2. DFS:
   - Mark current as Gray
   - For each neighbor:
     - If Gray: CYCLE (back edge!)
     - If White: recursively check
   - Mark current as Black
```

**Example:**

```
DAG (No Cycle):
0 -> 1 -> 2
     |
     v
     3

DFS from 0:
  0: Gray
  1: Gray
  2: Gray -> Black (done)
  3: Gray -> Black (done)
  1: Black (done)
  0: Black (done)
  No Gray vertex encountered ✓

Cycle Graph:
0 -> 1 -> 2
     ^    |
     +----+

DFS from 0:
  0: Gray
  1: Gray
  2: Gray
  Check neighbor 1: It's Gray!
  CYCLE DETECTED! ✗
```

**Complexity:**
- **Time:** O(V + E)
- **Space:** O(V)

---

### Algorithm 8: Topological Sort

**Problem:** Order vertices in a DAG such that for every edge u → v, u comes before v.

**Key Insight:**

Add vertices to result in **post-order** (after processing all descendants), then **reverse** the result.

**Why Post-Order?**

Think of dependencies: A vertex should be processed only after all its dependencies (descendants in DFS tree) are processed. By adding in post-order and reversing, we ensure this.

**Approach:**

```
Algorithm:
1. Check if graph has cycle (topological sort only works on DAGs)
2. DFS that adds vertices in post-order
3. Reverse the result
```

**Example:**

```
Course Prerequisites:
0 (Intro) -> 1 (DS) -> 2 (Algo)
              |
              v
             3 (Systems)

DFS with post-order:
  Visit 0:
    Visit 1:
      Visit 2:
        No neighbors, add 2: result = [2]
      Visit 3:
        No neighbors, add 3: result = [2, 3]
      Add 1: result = [2, 3, 1]
    Add 0: result = [2, 3, 1, 0]

  Reverse: [0, 1, 3, 2] or [0, 1, 2, 3]

Both are valid topological orders!
- Must take Intro (0) before DS (1) ✓
- Must take DS (1) before Algo (2) and Systems (3) ✓
```

**Complexity:**
- **Time:** O(V + E)
- **Space:** O(V)

---

### Algorithm 9: Bipartite Check

**Problem:** Determine if a graph can be 2-colored such that no adjacent vertices have the same color.

**Key Insight:**

A graph is bipartite ⟺ It has no odd-length cycles.

Use DFS to try 2-coloring:
- Color start with 0
- Color neighbors with 1
- Color their neighbors with 0
- If conflict → not bipartite

**Approach:**

```
Algorithm:
1. Initialize all vertices as uncolored (-1)
2. DFS with coloring:
   - Color current vertex with given color
   - For each neighbor:
     - If uncolored: color with opposite color
     - If same color: NOT BIPARTITE!
```

**Example:**

```
Bipartite (Even Cycle):
0 -- 1
|    |
3 -- 2

Coloring:
  0: Color 0 (Red)
  1: Color 1 (Blue) - neighbor of 0
  2: Color 0 (Red) - neighbor of 1
  3: Color 1 (Blue) - neighbor of 0 and 2
  Check 3's neighbors: 0 is Red, 2 is Red (opposite) ✓
  BIPARTITE!

Not Bipartite (Odd Cycle):
0 -- 1
|    |
2 ---+

Coloring:
  0: Color 0 (Red)
  1: Color 1 (Blue) - neighbor of 0
  2: Color 0 (Red) - neighbor of 0 and 1
  Check 2's neighbors: 1 is Blue (opposite) ✓
  Continue to neighbor 2 of 1: It's Red!
  But 2 is also neighbor of 0 which is Red!
  Conflict at 1-2 edge: both endpoints Red!
  NOT BIPARTITE!
```

**Complexity:**
- **Time:** O(V + E)
- **Space:** O(V)

---

## DFS vs BFS: When to Use Which?

### Use DFS When:

1. **Finding ANY path** (not necessarily shortest)
   - DFS naturally finds a path, though it may not be shortest

2. **Detecting cycles**
   - DFS with parent tracking (undirected) or 3-coloring (directed)

3. **Topological sorting**
   - Post-order DFS naturally gives topological order

4. **Exploring all possibilities** (backtracking)
   - Finding all paths, solving puzzles, generating permutations

5. **Memory is limited**
   - DFS uses O(h) space where h is height
   - BFS uses O(w) space where w is width
   - For wide graphs, DFS is more memory-efficient

6. **Tree traversals**
   - Pre-order, in-order, post-order are all DFS-based

### Use BFS When:

1. **Finding shortest path** (in unweighted graphs)
   - BFS naturally finds shortest path (minimum edges)

2. **Level-order traversal**
   - BFS explores level by level

3. **Finding all nodes at distance k**
   - BFS naturally groups vertices by distance

4. **Testing connectivity**
   - Both work, but BFS is often simpler

5. **Wide, shallow graphs**
   - BFS is more natural for wide graphs

### Example Comparison:

```
Graph:     0
          /|\
         1 2 3
        /|
       4 5

DFS from 0: [0, 1, 4, 5, 2, 3]
            (goes deep first)

BFS from 0: [0, 1, 2, 3, 4, 5]
            (level by level)

Find shortest path 0 to 4:
- DFS might find: 0 → 1 → 4 (length 2) ✓ or other path
- BFS always finds: 0 → 1 → 4 (length 2) ✓ shortest!
```

---

## Common Patterns and Variations

### Pattern 1: DFS with Path Tracking

**When:** Finding paths, solving mazes

**Key Idea:** Maintain current path, backtrack by removing from path

```python
def dfs_with_path(vertex, path):
    path.append(vertex)
    if is_goal(vertex):
        return path.copy()

    for neighbor in neighbors(vertex):
        if neighbor not in visited:
            result = dfs_with_path(neighbor, path)
            if result:
                return result

    path.pop()  # Backtrack!
    return None
```

### Pattern 2: DFS with State

**When:** Tracking multiple properties (color, distance, etc.)

**Key Idea:** Pass state through DFS

```python
def dfs_with_state(vertex, state):
    state[vertex] = PROCESSING

    for neighbor in neighbors(vertex):
        if state[neighbor] == UNVISITED:
            dfs_with_state(neighbor, state)
        elif state[neighbor] == PROCESSING:
            # Found back edge!

    state[vertex] = DONE
```

### Pattern 3: DFS with Backtracking

**When:** Finding all solutions, generating combinations

**Key Idea:** Remove from visited set when backtracking

```python
def dfs_backtracking(vertex, visited):
    visited.add(vertex)
    process(vertex)

    for neighbor in neighbors(vertex):
        if neighbor not in visited:
            dfs_backtracking(neighbor, visited)

    visited.remove(vertex)  # Allow revisiting in other paths!
```

---

## Key Insights and Tips

### 1. Always Use Visited Set

Without it, you'll have infinite loops in graphs with cycles!

```python
# BAD: No visited set
def dfs_bad(vertex):
    for neighbor in neighbors(vertex):
        dfs_bad(neighbor)  # Infinite loop!

# GOOD: With visited set
def dfs_good(vertex, visited):
    visited.add(vertex)
    for neighbor in neighbors(vertex):
        if neighbor not in visited:
            dfs_good(neighbor, visited)
```

### 2. Handle Disconnected Graphs

Not all graphs are connected! To visit all vertices:

```python
def dfs_all_vertices(graph):
    visited = set()
    for vertex in range(graph.num_vertices):
        if vertex not in visited:
            dfs(vertex, visited)
```

### 3. Be Careful with Undirected vs Directed

Undirected cycle detection needs parent tracking!
Directed cycle detection needs 3-color marking!

### 4. Copy Paths When Storing

Don't store references to mutable lists!

```python
# BAD: All paths end up the same!
all_paths.append(current_path)

# GOOD: Store a copy
all_paths.append(current_path.copy())
```

### 5. Understand the Recursion Stack

DFS recursion depth can reach V in the worst case (linear graph).
For very large graphs, consider iterative DFS.

---

## Complexity Analysis Summary

| Algorithm | Time | Space | Notes |
|-----------|------|-------|-------|
| DFS Recursive | O(V + E) | O(V) | Recursion stack + visited set |
| DFS Iterative | O(V + E) | O(V) | Explicit stack + visited set |
| Path Finding | O(V + E) | O(V) | May terminate early |
| All Paths | O(V! · V) | O(V) | Exponential for dense graphs |
| Connected Components | O(V + E) | O(V) | Visit all vertices and edges |
| Cycle Detection (Undirected) | O(V + E) | O(V) | With parent tracking |
| Cycle Detection (Directed) | O(V + E) | O(V) | With 3-color marking |
| Topological Sort | O(V + E) | O(V) | DFS + reverse |
| Bipartite Check | O(V + E) | O(V) | DFS with 2-coloring |

**Note:** V = vertices, E = edges

---

## Interview Tips

### 1. Clarify the Graph Properties

- **Directed or undirected?**
- **Weighted or unweighted?**
- **Connected or disconnected?**
- **Any cycles?**

### 2. Choose the Right Approach

- Need shortest path? → BFS (or Dijkstra if weighted)
- Cycle detection? → DFS with appropriate technique
- Topological sort? → DFS post-order
- Finding paths? → DFS with path tracking

### 3. Handle Edge Cases

- **Empty graph** (no vertices)
- **Single vertex**
- **Disconnected graph**
- **Self-loops**
- **Parallel edges**

### 4. Optimize Space

- For large graphs, iterative DFS avoids stack overflow
- Consider in-place marking if allowed (instead of visited set)

### 5. Draw Diagrams

Always draw the graph and trace through your algorithm!

```
Example: Is this graph bipartite?

    0 --- 1
    |     |
    2 --- 3

Draw it, color it:
Red: 0, 3
Blue: 1, 2

Check edges:
0-1: Red-Blue ✓
1-3: Blue-Red ✓
2-0: Blue-Red ✓
2-3: Blue-Red ✓

Yes, bipartite!
```

---

## Key Takeaways

1. **DFS is powerful and versatile** - Master it for many graph problems

2. **Recursion is natural for DFS** - The call stack does the work

3. **Visited set is essential** - Prevents infinite loops

4. **Different problems need different DFS variations**:
   - Basic DFS: Simple traversal
   - With parent: Undirected cycle detection
   - With 3-colors: Directed cycle detection
   - With path: Path finding
   - With backtracking: All paths
   - Post-order: Topological sort
   - With coloring: Bipartite check

5. **DFS vs BFS depends on the problem**:
   - DFS: Paths, cycles, topology, backtracking
   - BFS: Shortest paths, level-order

6. **Time complexity is usually O(V + E)**:
   - Visit each vertex once
   - Explore each edge once

7. **Space complexity is O(V)**:
   - Visited set + recursion stack (or explicit stack)
   - In worst case, stack depth reaches V

8. **Practice makes perfect**:
   - Implement DFS from scratch
   - Solve various DFS problems
   - Understand when to use each variation

---

## Practice Strategy

1. **Master basic DFS first** - Recursive and iterative
2. **Understand the visited set pattern** - Why it's needed
3. **Practice cycle detection** - Both undirected and directed
4. **Learn topological sort** - Post-order DFS technique
5. **Solve path problems** - Path finding and all paths
6. **Apply to real scenarios** - Maze solving, dependency resolution
7. **Compare with BFS** - Understand when to use which

## Related Concepts

- **Breadth-First Search (BFS)** - Level-order traversal
- **Backtracking** - DFS with state exploration
- **Recursion** - Core technique for DFS
- **Stacks** - Data structure for iterative DFS
- **Tree Traversals** - Pre-order, in-order, post-order
- **Strongly Connected Components** - Advanced DFS application
- **Articulation Points and Bridges** - Graph structure analysis

---

**Next Steps:**
- Project 36: Breadth-First Search (BFS)
- Practice DFS problems on LeetCode/HackerRank
- Implement advanced DFS applications (Tarjan's algorithm, etc.)
