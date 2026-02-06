# Solution in Words: Graphs and Graph Traversal

## How to Think About This Problem

### Understanding Graphs

Think of a graph like a map of cities connected by roads - nodes are cities, edges are roads.

**Mental Model:**
```
    0
   / \
  1---2
  |
  3
```

### Graph Representation

**Adjacency List**: Each node stores list of neighbors
- Efficient for sparse graphs
- Easy to iterate neighbors

### DFS Thinking

**Depth-First**: Go as deep as possible before backtracking
- Like exploring a maze - go down one path until dead end
- Uses stack (recursion naturally)
- Mark visited nodes to avoid cycles

### BFS Thinking

**Breadth-First**: Explore all neighbors before going deeper
- Like ripples in water - expand outward level by level
- Uses queue
- Guarantees shortest path in unweighted graphs

### Problem-Solving Strategy

1. **Represent graph**: Adjacency list using dict
2. **Choose traversal**: DFS for paths, BFS for shortest path
3. **Track visited**: Avoid revisiting nodes
4. **Process nodes**: Based on problem requirements

