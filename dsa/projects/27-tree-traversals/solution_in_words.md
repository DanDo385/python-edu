# Project 27: Tree Traversals - Solution Explained

## Concept Overview

Tree traversal is the process of visiting every node in a tree data structure exactly once in a systematic way. Understanding tree traversals is fundamental to working with hierarchical data structures.

### What is a Binary Tree?

A binary tree is a hierarchical data structure where each node has at most two children: left and right. Trees are used to represent hierarchical relationships like:
- File systems (directories and files)
- Organization charts
- Expression evaluation
- Database indexing

### Types of Tree Traversals

There are two main categories:

1. **Depth-First Search (DFS)**: Explores as deep as possible before backtracking
   - Inorder (Left → Root → Right)
   - Preorder (Root → Left → Right)
   - Postorder (Left → Right → Root)

2. **Breadth-First Search (BFS)**: Explores level by level
   - Level-order traversal

## Detailed Explanation of Each Traversal

### 1. Inorder Traversal (Left → Root → Right)

**Order:** Visit left subtree first, then root, then right subtree.

**Visual Example:**
```
        4
       / \
      2   6
     / \ / \
    1  3 5  7

Inorder: [1, 2, 3, 4, 5, 6, 7]
```

**Why It Matters:**
- For Binary Search Trees (BST), inorder traversal produces values in **sorted order**
- This is the most common traversal for BSTs

**Recursive Approach:**
```
1. If node is None, return
2. Traverse left subtree (recursive call)
3. Visit current node (add to result)
4. Traverse right subtree (recursive call)
```

**Iterative Approach:**
```
1. Use a stack to simulate recursion
2. Go as far left as possible, pushing nodes
3. Pop from stack, visit node
4. Move to right child
5. Repeat until stack is empty
```

### 2. Preorder Traversal (Root → Left → Right)

**Order:** Visit root first, then left subtree, then right subtree.

**Visual Example:**
```
        4
       / \
      2   6
     / \ / \
    1  3 5  7

Preorder: [4, 2, 1, 3, 6, 5, 7]
```

**Why It Matters:**
- Used for **tree copying** (create root before children)
- Used for **prefix expression** evaluation
- Used for **serialization** (save tree structure)

**Recursive Approach:**
```
1. If node is None, return
2. Visit current node (add to result)
3. Traverse left subtree (recursive call)
4. Traverse right subtree (recursive call)
```

**Iterative Approach:**
```
1. Use a stack, push root
2. Pop node, visit it
3. Push right child (so it's processed later)
4. Push left child (so it's processed first)
5. Repeat until stack is empty
```

**Key Insight:** Push right before left because stacks are LIFO (Last In, First Out).

### 3. Postorder Traversal (Left → Right → Root)

**Order:** Visit left subtree first, then right subtree, then root.

**Visual Example:**
```
        4
       / \
      2   6
     / \ / \
    1  3 5  7

Postorder: [1, 3, 2, 5, 7, 6, 4]
```

**Why It Matters:**
- Used for **tree deletion** (delete children before parent)
- Used for **postfix expression** evaluation
- Used for **calculating tree properties** (height, size)

**Recursive Approach:**
```
1. If node is None, return
2. Traverse left subtree (recursive call)
3. Traverse right subtree (recursive call)
4. Visit current node (add to result)
```

**Iterative Approach:**
```
1. Use a stack and track last visited node
2. Go as far left as possible
3. Peek at stack top
4. If right child exists and not visited, go right
5. Otherwise, pop and visit node
6. Update last visited
```

**Key Insight:** This is the hardest iterative traversal because we must ensure both children are visited before the parent.

### 4. Level-Order Traversal (BFS)

**Order:** Visit nodes level by level, left to right.

**Visual Example:**
```
        4
       / \
      2   6
     / \ / \
    1  3 5  7

Level-order: [[4], [2, 6], [1, 3, 5, 7]]
```

**Why It Matters:**
- Used for **finding shortest path** in unweighted trees
- Used for **level-based processing** (e.g., "print each level")
- Used for **tree width** calculations

**Approach (Always Iterative with Queue):**
```
1. Use a queue (FIFO - First In, First Out)
2. Add root to queue
3. While queue not empty:
   a. Get count of nodes at current level
   b. Process all nodes at this level
   c. Add their children for next level
4. Return list of levels
```

**Key Insight:** Use queue for BFS (level-by-level), use stack for DFS (depth-first).

## Approach Comparison: Recursive vs Iterative

### Recursive Approach

**Advantages:**
- Clean, easy to understand
- Natural for tree structures
- Less code to write

**Disadvantages:**
- Uses call stack (risk of stack overflow for very deep trees)
- Harder to control/pause execution
- Hidden space complexity (call stack)

### Iterative Approach

**Advantages:**
- Explicit control over execution
- No stack overflow risk (can handle deeper trees)
- Can be paused/resumed
- Clear space complexity (explicit stack/queue)

**Disadvantages:**
- More complex code
- Requires manual stack/queue management
- Easier to make mistakes (especially postorder)

## Complexity Analysis

### Time Complexity: O(n) for ALL traversals

**Why?** We visit each node exactly once.
- n nodes → n visits → O(n)
- This applies to all traversal types (inorder, preorder, postorder, level-order)

### Space Complexity

**Recursive DFS (Inorder, Preorder, Postorder):**
- Best case (balanced tree): O(log n) - call stack depth
- Worst case (skewed tree): O(n) - call stack depth
- Average case: O(h) where h is tree height

**Iterative DFS:**
- Same as recursive: O(h) for explicit stack
- Best case: O(log n)
- Worst case: O(n)

**Level-Order (BFS):**
- Space: O(w) where w is maximum tree width
- Worst case: O(n) for complete binary tree (last level has ~n/2 nodes)
- Best case: O(1) for skewed tree (width = 1)

## Implementation Patterns

### Recursive Pattern Template

```python
def traversal_recursive(root):
    if root is None:
        return []

    result = []

    # PREORDER: Visit here (before recursion)
    # result.append(root.val)

    # INORDER: Visit here (between left and right)
    result.extend(traversal_recursive(root.left))
    # result.append(root.val)
    result.extend(traversal_recursive(root.right))

    # POSTORDER: Visit here (after recursion)
    # result.append(root.val)

    return result
```

### Iterative Stack Pattern (DFS)

```python
def traversal_iterative(root):
    if root is None:
        return []

    result = []
    stack = []  # or initialize with [root] for preorder
    current = root

    while current or stack:
        # Pattern varies by traversal type
        # Inorder: go left, pop, visit, go right
        # Preorder: pop, visit, push right, push left
        # Postorder: go left, peek, check right, pop

    return result
```

### Iterative Queue Pattern (BFS)

```python
def level_order_traversal(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)  # Key: snapshot current level size
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result
```

## Common Pitfalls and How to Avoid Them

### 1. Forgetting to Handle Empty Trees
**Problem:** Accessing `root.val` when root is None
**Solution:** Always check `if root is None: return []` at the start

### 2. Wrong Order in Recursive Calls
**Problem:** Mixing up when to visit root vs traverse subtrees
**Solution:** Remember the names:
- **Pre**order = **Pre**fix = Root **before** children
- **In**order = Root **in** the middle
- **Post**order = Root **after** children (like **post**script)

### 3. Stack vs Queue Confusion
**Problem:** Using stack for BFS or queue for DFS
**Solution:**
- **Stack** (LIFO) → **DFS** (go deep)
- **Queue** (FIFO) → **BFS** (go wide)

### 4. Not Tracking Last Visited in Postorder Iterative
**Problem:** Visiting nodes multiple times
**Solution:** Track `last_visited` to know when right subtree is done

### 5. Not Snapshotting Level Size in BFS
**Problem:** Processing children as part of current level
**Solution:** `level_size = len(queue)` before inner loop

## Real-World Applications

### Inorder Traversal
- **Database indexing**: B-tree traversal in sorted order
- **Expression evaluation**: Convert binary tree to infix notation
- **Validation**: Check if BST is valid (should be sorted)

### Preorder Traversal
- **File systems**: Directory listing (list directory before contents)
- **Tree serialization**: Save tree structure to file/network
- **Tree copying**: Create copy by creating root first

### Postorder Traversal
- **File systems**: Calculate directory sizes (children before parent)
- **Tree deletion**: Delete children before parent to avoid dangling pointers
- **Expression evaluation**: Postfix (RPN) calculator
- **Dependency resolution**: Build systems, package managers

### Level-Order Traversal
- **Shortest path**: Find minimum distance in unweighted tree
- **Level-based processing**: "Print all nodes at distance k"
- **Tree width**: Find maximum width of tree
- **Serialization**: Human-readable tree representation

## Key Takeaways

1. **All traversals visit every node once**: Time complexity is always O(n)

2. **Choose traversal based on problem requirements:**
   - Need sorted order (BST)? → Inorder
   - Building/copying tree? → Preorder
   - Deleting tree? → Postorder
   - Level-by-level processing? → Level-order

3. **Recursive is easier, iterative is more flexible:**
   - Start with recursive for clarity
   - Use iterative for very deep trees or when you need fine control

4. **Understand the pattern:**
   - DFS (inorder, preorder, postorder) → Use stack or recursion
   - BFS (level-order) → Use queue

5. **Space matters:**
   - Recursive: Hidden cost in call stack
   - Iterative: Explicit stack/queue
   - Both are O(h) for DFS, O(w) for BFS

6. **Master the fundamentals:**
   - These patterns appear in countless interview questions
   - Tree traversals are building blocks for advanced algorithms
   - Practice until you can write them without thinking

## Practice Progression

1. **Start with recursive implementations** (easier to understand)
2. **Verify with iterative implementations** (deeper understanding)
3. **Compare results** (recursive should match iterative)
4. **Solve variations:**
   - Right-to-left traversals
   - Zigzag level order
   - Vertical order traversal
   - Boundary traversal
5. **Apply to real problems:**
   - Path sum calculations
   - Tree construction from traversals
   - Lowest common ancestor
   - Tree diameter

## Visual Mental Model

Think of traversals as different ways to read a book:

- **Preorder**: Read chapter titles first, then content (table of contents)
- **Inorder**: Read left to right, line by line (normal reading)
- **Postorder**: Read footnotes first, then main text (academic reading)
- **Level-order**: Read headlines, then articles, layer by layer (newspaper scanning)

Each has its purpose. Master all four, and you'll have complete control over any tree-based algorithm.
