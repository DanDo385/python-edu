# Project 29: Tree Construction

## Overview

Master tree construction algorithms that build binary trees from different traversal sequences and implement serialization/deserialization. These problems are crucial for understanding tree structure and traversal relationships.

## Learning Objectives

- Build trees from traversal sequences (preorder/inorder, postorder/inorder)
- Understand the relationship between different traversals
- Implement tree serialization and deserialization
- Handle tree reconstruction edge cases
- Analyze time and space complexity of construction algorithms

## Problems

Implement the following in `solution/solution.py`:

### Problem 1: Build Tree from Preorder and Inorder (Medium)
```python
def build_tree_preorder_inorder(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """
    Construct binary tree from preorder and inorder traversal sequences.

    Key insights:
    - First element of preorder is always the root
    - Find root in inorder to split left and right subtrees
    - Recursively construct left and right subtrees

    Args:
        preorder: Preorder traversal sequence
        inorder: Inorder traversal sequence

    Returns:
        Root of constructed tree

    Time Complexity: O(n) with hash map optimization
    Space Complexity: O(n) for recursion and hash map
    """
```

**Examples:**
```python
# Simple tree
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
#     3
#    / \
#   9   20
#      /  \
#     15   7

# Single node
preorder = [1]
inorder = [1]
# Result: TreeNode(1)
```

---

### Problem 2: Build Tree from Postorder and Inorder (Medium)
```python
def build_tree_postorder_inorder(postorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """
    Construct binary tree from postorder and inorder traversal sequences.

    Key insights:
    - Last element of postorder is always the root
    - Find root in inorder to split left and right subtrees
    - Recursively construct right then left subtrees (order matters!)

    Args:
        postorder: Postorder traversal sequence
        inorder: Inorder traversal sequence

    Returns:
        Root of constructed tree

    Time Complexity: O(n) with hash map optimization
    Space Complexity: O(n)
    """
```

**Examples:**
```python
postorder = [9, 15, 7, 20, 3]
inorder = [9, 3, 15, 20, 7]
#     3
#    / \
#   9   20
#      /  \
#     15   7
```

---

### Problem 3: Serialize and Deserialize Binary Tree (Hard)
```python
def serialize(root: Optional[TreeNode]) -> str:
    """
    Serialize a binary tree to a string representation.

    Use level-order (BFS) traversal with 'null' for missing nodes.

    Args:
        root: Root of binary tree

    Returns:
        String representation (e.g., "1,2,3,null,null,4,5")

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

def deserialize(data: str) -> Optional[TreeNode]:
    """
    Deserialize string back to binary tree.

    Args:
        data: String representation from serialize()

    Returns:
        Root of reconstructed tree

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
```

**Examples:**
```python
#     1
#    / \
#   2   3
#      / \
#     4   5

root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
serialized = serialize(root)  # "1,2,3,null,null,4,5"
reconstructed = deserialize(serialized)  # Same tree structure
```

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Preorder** | Root → Left → Right |
| **Inorder** | Left → Root → Right |
| **Postorder** | Left → Right → Root |
| **Uniqueness** | Need 2 traversals to uniquely construct tree (one must be inorder) |
| **Root Finding** | Preorder: first element, Postorder: last element |
| **Serialization** | Convert tree to string for storage/transmission |

## Complexity Analysis

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Build from traversals | O(n) | O(n) | With hash map for index lookup |
| Serialize | O(n) | O(n) | Visit each node once |
| Deserialize | O(n) | O(n) | Process each value once |

## Constraints

- Number of nodes: 0 ≤ n ≤ 10,000
- Node values: -10,000 ≤ val ≤ 10,000
- All values are unique (for construction problems)
- Traversal arrays are valid

## Testing

```bash
# Run all tests
pytest tests/test_project_29.py -v

# Run specific test
pytest tests/test_project_29.py::TestBuildFromTraversals -v
```

## Tips

1. **Building from traversals:**
   - Use hash map to quickly find root index in inorder
   - Carefully calculate left and right subtree sizes
   - Watch out for index boundaries

2. **Serialization:**
   - Use level-order (BFS) for natural representation
   - Include null markers for completeness
   - Handle empty tree case

3. **Common mistakes:**
   - Wrong index calculations when splitting arrays
   - Not handling empty subtrees
   - Forgetting to process right subtree before left in postorder

## Real-World Applications

- **Data persistence:** Save/load tree structures
- **Network transmission:** Send tree data between systems
- **Tree reconstruction:** Recover trees from partial information
- **Compiler design:** Parse trees from syntax analysis

## Next Steps

After completing this project, you'll be ready for:
- Project 30: Advanced Tree Problems
- Understanding tree structure deeply
