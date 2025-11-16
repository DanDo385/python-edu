# Project 30: Advanced Tree Problems

## Overview

Tackle advanced tree problems that require deep understanding of tree structure, path analysis, and complex traversals. These problems are commonly asked in technical interviews and build upon fundamental tree concepts.

## Learning Objectives

- Find Lowest Common Ancestor (LCA) in binary trees
- Calculate maximum path sums in trees
- Compute tree diameter
- Perform vertical order traversal
- Flatten trees to linked list structure
- Master advanced tree recursion patterns

## Problems

Implement the following in `solution/solution.py`:

### Problem 1: Lowest Common Ancestor (Medium)
```python
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find the lowest common ancestor of two nodes in a binary tree.

    LCA is the lowest node that has both p and q as descendants.

    Time Complexity: O(n)
    Space Complexity: O(h) for recursion stack
    """
```

### Problem 2: Binary Tree Maximum Path Sum (Hard)
```python
def max_path_sum(root: TreeNode) -> int:
    """
    Find the maximum path sum in a binary tree.
    Path can start and end at any nodes.

    Time Complexity: O(n)
    Space Complexity: O(h)
    """
```

### Problem 3: Diameter of Binary Tree (Easy)
```python
def diameter_of_binary_tree(root: TreeNode) -> int:
    """
    Calculate the diameter (longest path between any two nodes).

    Time Complexity: O(n)
    Space Complexity: O(h)
    """
```

### Problem 4: Vertical Order Traversal (Hard)
```python
def vertical_order_traversal(root: TreeNode) -> List[List[int]]:
    """
    Return vertical order traversal (nodes grouped by vertical column).

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
```

### Problem 5: Flatten Binary Tree to Linked List (Medium)
```python
def flatten(root: TreeNode) -> None:
    """
    Flatten tree to linked list in-place (preorder traversal).

    Time Complexity: O(n)
    Space Complexity: O(h)
    """
```

## Testing

```bash
pytest tests/test_project_30.py -v
```
