# Project 28: Binary Search Tree

## Overview

Master Binary Search Trees (BST) - a fundamental data structure that combines the efficiency of binary search with the dynamic capabilities of a linked structure. BSTs maintain sorted data and enable fast search, insertion, and deletion operations.

## Learning Objectives

- Implement BST core operations (insert, search, delete)
- Understand BST properties and invariants
- Validate BST structure
- Navigate BST to find specific elements (kth smallest)
- Implement BST iterator for in-order traversal
- Analyze time complexity based on tree balance
- Handle edge cases (empty trees, duplicates, deletions)

## Problems

Implement the following in `solution/solution.py`:

### Problem 1: BST Insert (Medium)
```python
def insert_bst(root: Optional[TreeNode], val: int) -> TreeNode:
    """
    Insert a value into a Binary Search Tree.

    BST Property: For every node, all values in left subtree < node.val < all values in right subtree

    Args:
        root: Root of BST (or None for empty tree)
        val: Value to insert

    Returns:
        Root of BST after insertion

    Time Complexity: O(h) where h is height (O(log n) balanced, O(n) skewed)
    Space Complexity: O(h) for recursion stack
    """
```

**Examples:**
```python
# Insert into empty tree
root = insert_bst(None, 5)  # Returns TreeNode(5)

# Insert smaller value (goes left)
root = insert_bst(root, 3)
#     5
#    /
#   3

# Insert larger value (goes right)
root = insert_bst(root, 7)
#     5
#    / \
#   3   7

# Build BST: [5,3,7,1,4,6,9]
#       5
#      / \
#     3   7
#    / \ / \
#   1  4 6  9
```

**Use Case:** Dynamic sorted data storage

---

### Problem 2: BST Search (Easy)
```python
def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Search for a value in BST. Return the node if found, None otherwise.

    Args:
        root: Root of BST
        val: Value to search for

    Returns:
        TreeNode containing val, or None if not found

    Time Complexity: O(h) where h is height
    Space Complexity: O(h) for recursion (O(1) iterative)
    """
```

**Examples:**
```python
#       5
#      / \
#     3   7
#    / \
#   1   4

node = search_bst(root, 3)  # Returns TreeNode(3)
node = search_bst(root, 10) # Returns None
```

**Use Case:** Fast lookup in sorted data

---

### Problem 3: BST Delete (Hard)
```python
def delete_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Delete a value from BST while maintaining BST property.

    Three cases:
    1. Node is leaf: simply remove
    2. Node has one child: replace with child
    3. Node has two children: replace with inorder successor (or predecessor)

    Args:
        root: Root of BST
        val: Value to delete

    Returns:
        Root of BST after deletion

    Time Complexity: O(h) where h is height
    Space Complexity: O(h) for recursion stack
    """
```

**Examples:**
```python
# Delete leaf node
#       5            5
#      / \    =>    /
#     3   7        3
root = delete_bst(root, 7)

# Delete node with one child
#       5            5
#      /      =>      \
#     3                7
#    / \
#   1   7
root = delete_bst(root, 3)

# Delete node with two children (replace with successor)
#       5            6
#      / \    =>    / \
#     3   7        3   7
#        / \
#       6   9
root = delete_bst(root, 5)  # Replace 5 with inorder successor 6
```

**Challenge:** Correctly handle all three deletion cases

---

### Problem 4: Validate BST (Medium)
```python
def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    Determine if a binary tree is a valid BST.

    BST Property must hold for ALL nodes:
    - All left subtree values < node.val
    - All right subtree values > node.val

    Args:
        root: Root of binary tree

    Returns:
        True if valid BST, False otherwise

    Time Complexity: O(n) - visit each node once
    Space Complexity: O(h) for recursion stack
    """
```

**Examples:**
```python
# Valid BST
#     5
#    / \
#   3   7
#  / \
# 1   4
is_valid_bst(root)  # True

# Invalid BST (4 > 3 but 4 < 5, violates BST property)
#     5
#    / \
#   3   7
#    \
#     6  (6 > 3 but 6 > 5, INVALID!)
is_valid_bst(root)  # False

# Tricky case - need min/max bounds, not just parent comparison
#     10
#    /  \
#   5    15
#       /  \
#      6   20  (6 < 15 but 6 < 10, INVALID!)
is_valid_bst(root)  # False
```

**Key Insight:** Must track valid range (min, max) for each subtree, not just compare with parent

---

### Problem 5: Kth Smallest in BST (Medium)
```python
def kth_smallest(root: TreeNode, k: int) -> int:
    """
    Find the kth smallest element in BST.

    Uses in-order traversal which visits BST in sorted order.

    Args:
        root: Root of BST (non-empty)
        k: Position (1-indexed, 1 <= k <= n)

    Returns:
        The kth smallest value

    Time Complexity: O(h + k) - worst case O(n)
    Space Complexity: O(h) for recursion stack
    """
```

**Examples:**
```python
#       5
#      / \
#     3   7
#    / \
#   1   4
# Inorder: [1, 3, 4, 5, 7]

kth_smallest(root, 1)  # 1 (smallest)
kth_smallest(root, 2)  # 3
kth_smallest(root, 3)  # 4
kth_smallest(root, 5)  # 7 (largest)
```

**Use Case:** Finding median, percentiles in sorted data

---

### Problem 6: BST Iterator (Medium)
```python
class BSTIterator:
    """
    Implement an iterator for BST that traverses in-order (sorted order).

    next() returns the next smallest element
    has_next() returns True if more elements exist

    Requirements:
    - next() and has_next() should run in O(1) average time
    - Use O(h) space where h is tree height
    """

    def __init__(self, root: Optional[TreeNode]):
        """Initialize iterator with BST root."""
        pass

    def next(self) -> int:
        """Return next smallest element."""
        pass

    def has_next(self) -> bool:
        """Return True if more elements exist."""
        pass
```

**Examples:**
```python
#       7
#      / \
#     3   15
#        / \
#       9   20

iterator = BSTIterator(root)
iterator.next()      # 3
iterator.next()      # 7
iterator.has_next()  # True
iterator.next()      # 9
iterator.has_next()  # True
iterator.next()      # 15
iterator.next()      # 20
iterator.has_next()  # False
```

**Use Case:** Processing BST elements one at a time without loading all into memory

---

## BST Properties Summary

| Property | Description |
|----------|-------------|
| **BST Invariant** | For every node: left subtree < node < right subtree |
| **Inorder Traversal** | Produces sorted sequence |
| **Search** | O(h) - binary search on each level |
| **Insert** | O(h) - find position, add leaf |
| **Delete** | O(h) - find node, restructure |
| **Height** | Best: O(log n) balanced, Worst: O(n) skewed |

## Complexity Analysis

| Operation | Average | Worst Case | Notes |
|-----------|---------|------------|-------|
| Search | O(log n) | O(n) | Depends on balance |
| Insert | O(log n) | O(n) | Same as search |
| Delete | O(log n) | O(n) | Find + restructure |
| Validate | O(n) | O(n) | Must visit all nodes |
| Kth Smallest | O(h + k) | O(n) | Inorder traversal |
| Iterator next() | O(1) amortized | O(h) worst | Stack operations |

**Note:** n = number of nodes, h = height of tree

## Constraints

- Number of nodes: 0 ≤ n ≤ 10,000
- Node values: -10,000 ≤ val ≤ 10,000
- All values are unique (no duplicates)
- For kth smallest: 1 ≤ k ≤ n

## Testing

```bash
# Run all tests
pytest tests/test_project_28.py -v

# Run specific test
pytest tests/test_project_28.py::TestBSTInsert -v
```

## Tips

1. **BST Invariant:**
   - Always maintain: left < node < right
   - Use recursive structure to validate ranges
   - Track min/max bounds during validation

2. **Deletion is tricky:**
   - Three cases: leaf, one child, two children
   - For two children: replace with inorder successor (smallest in right subtree)
   - Or use inorder predecessor (largest in left subtree)

3. **Recursion is natural:**
   - BST operations are naturally recursive
   - Base case: None (empty tree)
   - Recursive case: go left or right based on comparison

4. **Iterative alternatives:**
   - Can implement search and insert iteratively
   - Often more efficient (no call stack overhead)
   - Harder to read but better for deep trees

## Common Mistakes

1. **Validation:** Comparing only with parent (wrong!) instead of tracking valid range
2. **Deletion:** Forgetting to handle all three cases
3. **Iterator:** Using O(n) space instead of O(h)
4. **Kth smallest:** Doing full inorder traversal instead of stopping at k

## Real-World Applications

- **Databases:** Index structures (though B-trees are more common)
- **File systems:** Directory structures
- **Autocomplete:** Sorted suggestions
- **Symbol tables:** Compiler variable lookup
- **Priority queues:** Alternative to heaps for sorted data

## Next Steps

After completing this project, you'll be ready for:
- Project 29: Tree Construction
- Project 30: Advanced Tree Problems
- Self-balancing trees (AVL, Red-Black) in advanced topics
