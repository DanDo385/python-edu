# Project 27: Tree Traversals

## Overview

Master tree traversal algorithms - the foundation for working with hierarchical data structures. Learn to navigate binary trees using different traversal orders (inorder, preorder, postorder, level-order) through both recursive and iterative approaches.

## Learning Objectives

- Understand different tree traversal strategies and their applications
- Implement recursive and iterative traversal algorithms
- Master depth-first search (DFS) and breadth-first search (BFS) on trees
- Analyze time and space complexity of tree operations
- Build and manipulate binary tree structures

## Problems

Implement the following functions in `solution/solution.py`:

### Problem 1: TreeNode Class (Easy)
```python
class TreeNode:
    """
    A node in a binary tree.

    Attributes:
        val: The value stored in the node
        left: Reference to left child (TreeNode or None)
        right: Reference to right child (TreeNode or None)
    """
```

**Purpose:** Foundation for all tree operations

### Problem 2: Inorder Traversal - Recursive (Easy)
```python
def inorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    """
    Perform inorder traversal (Left -> Root -> Right) recursively.

    Args:
        root: Root node of binary tree

    Returns:
        List of node values in inorder sequence

    Time Complexity: O(?)
    Space Complexity: O(?)
    """
```

**Examples:**
```python
#       1
#      / \
#     2   3
#    / \
#   4   5
inorder_traversal_recursive(root) # Returns [4, 2, 5, 1, 3]
```

**Use Case:** BST traversal produces sorted order

### Problem 3: Preorder Traversal - Recursive (Easy)
```python
def preorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    """
    Perform preorder traversal (Root -> Left -> Right) recursively.

    Args:
        root: Root node of binary tree

    Returns:
        List of node values in preorder sequence

    Time Complexity: O(?)
    Space Complexity: O(?)
    """
```

**Examples:**
```python
#       1
#      / \
#     2   3
#    / \
#   4   5
preorder_traversal_recursive(root) # Returns [1, 2, 4, 5, 3]
```

**Use Case:** Tree copying, prefix expression evaluation

### Problem 4: Postorder Traversal - Recursive (Easy)
```python
def postorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    """
    Perform postorder traversal (Left -> Right -> Root) recursively.

    Args:
        root: Root node of binary tree

    Returns:
        List of node values in postorder sequence

    Time Complexity: O(?)
    Space Complexity: O(?)
    """
```

**Examples:**
```python
#       1
#      / \
#     2   3
#    / \
#   4   5
postorder_traversal_recursive(root) # Returns [4, 5, 2, 3, 1]
```

**Use Case:** Tree deletion, postfix expression evaluation

### Problem 5: Level-Order Traversal (Medium)
```python
def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform level-order traversal (breadth-first) using a queue.

    Args:
        root: Root node of binary tree

    Returns:
        List of lists, where each inner list contains values at that level

    Time Complexity: O(?)
    Space Complexity: O(?)
    """
```

**Examples:**
```python
#       1
#      / \
#     2   3
#    / \
#   4   5
level_order_traversal(root) # Returns [[1], [2, 3], [4, 5]]
```

**Use Case:** Finding shortest path, level-based processing

### Problem 6: Inorder Traversal - Iterative (Medium)
```python
def inorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Perform inorder traversal iteratively using a stack.

    Args:
        root: Root node of binary tree

    Returns:
        List of node values in inorder sequence

    Time Complexity: O(?)
    Space Complexity: O(?)
    """
```

**Examples:**
```python
#       1
#      / \
#     2   3
#    / \
#   4   5
inorder_traversal_iterative(root) # Returns [4, 2, 5, 1, 3]
```

**Challenge:** Same result as recursive, but uses explicit stack

### Problem 7: Preorder Traversal - Iterative (Medium)
```python
def preorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Perform preorder traversal iteratively using a stack.

    Args:
        root: Root node of binary tree

    Returns:
        List of node values in preorder sequence

    Time Complexity: O(?)
    Space Complexity: O(?)
    """
```

**Examples:**
```python
#       1
#      / \
#     2   3
#    / \
#   4   5
preorder_traversal_iterative(root) # Returns [1, 2, 4, 5, 3]
```

### Problem 8: Postorder Traversal - Iterative (Hard)
```python
def postorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Perform postorder traversal iteratively using a stack.

    Args:
        root: Root node of binary tree

    Returns:
        List of node values in postorder sequence

    Time Complexity: O(?)
    Space Complexity: O(?)
    """
```

**Examples:**
```python
#       1
#      / \
#     2   3
#    / \
#   4   5
postorder_traversal_iterative(root) # Returns [4, 5, 2, 3, 1]
```

**Challenge:** Most complex iterative traversal - requires tracking visited nodes

### Problem 9: Tree Height/Depth (Easy)
```python
def max_depth(root: Optional[TreeNode]) -> int:
    """
    Calculate the maximum depth (height) of a binary tree.

    Args:
        root: Root node of binary tree

    Returns:
        Maximum depth (number of nodes from root to deepest leaf)

    Time Complexity: O(?)
    Space Complexity: O(?)
    """
```

**Examples:**
```python
#       1
#      / \
#     2   3
#    / \
#   4   5
max_depth(root) # Returns 3
```

### Problem 10: Build Tree from List (Medium)
```python
def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from a level-order list representation.
    None represents missing nodes.

    Args:
        values: Level-order list of node values

    Returns:
        Root node of constructed tree

    Time Complexity: O(?)
    Space Complexity: O(?)
    """
```

**Examples:**
```python
build_tree_from_list([1, 2, 3, 4, 5])
#       1
#      / \
#     2   3
#    / \
#   4   5

build_tree_from_list([1, None, 2, 3])
#   1
#    \
#     2
#    /
#   3
```

**Use Case:** Testing, tree construction from serialized format

## Tree Traversal Summary

| Traversal | Order | Recursive | Iterative | Primary Use Case |
|-----------|-------|-----------|-----------|------------------|
| **Inorder** | L→Root→R | Easy | Medium | BST: sorted order |
| **Preorder** | Root→L→R | Easy | Medium | Tree copying |
| **Postorder** | L→R→Root | Easy | Hard | Tree deletion |
| **Level-order** | BFS | Medium | N/A | Shortest path, level processing |

## Complexity Reference

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| All traversals | O(n) | O(h) | h = height, worst case O(n) for skewed tree |
| Level-order | O(n) | O(w) | w = max width, worst case O(n) |
| Tree height | O(n) | O(h) | Recursive call stack |

## Constraints

- Number of nodes: 0 ≤ n ≤ 10,000
- Node values: -10,000 ≤ val ≤ 10,000
- Trees may be empty (root = None)
- Trees may be skewed (all left or all right children)

## Testing

```bash
pytest tests/ -v
```

## Tips

1. **Recursive approach**:
   - Base case: if root is None, return
   - Recursive case: process based on traversal order
   - Natural and intuitive for tree problems

2. **Iterative approach**:
   - Use stack for DFS (inorder, preorder, postorder)
   - Use queue for BFS (level-order)
   - More complex but avoids recursion overhead

3. **Pattern recognition**:
   - Inorder: Process left subtree, then root, then right
   - Preorder: Process root first, then subtrees
   - Postorder: Process root last, after subtrees
   - Level-order: Process level by level, left to right

4. **Common mistakes**:
   - Forgetting to handle None/empty tree
   - Wrong order in recursive calls
   - Not properly managing stack/queue in iterative versions

## Real-World Applications

- **File systems**: Directory traversal (preorder for listing)
- **Compilers**: Expression tree evaluation (inorder for infix, postorder for postfix)
- **DOM manipulation**: HTML tree traversal
- **Database indexing**: B-tree traversal
- **Game AI**: Decision tree traversal

## Next Steps

After completing this project, you'll be ready for:
- Project 28: Binary Search Tree
- Project 29: Tree Construction
- Project 30: Advanced Tree Problems
