# Project 26: Binary Tree Basics - Solution Explained

## Core Pattern: Recursion on Trees

**Key Insight**: Trees are naturally recursive - process node, recurse on children.

### TreeNode Class

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Problem 1: Create Tree from List

**Pattern**: Level-order construction with queue
- Use queue to track nodes
- Assign left/right children from list
- **Time**: O(n), **Space**: O(n)

### Problem 2: Tree Height

**Pattern**: Recursive max depth
```python
def height(root):
    if not root: return 0
    return 1 + max(height(root.left), height(root.right))
```
- **Time**: O(n) - visit each node once
- **Space**: O(h) - recursion stack depth

### Problem 3: Tree Size

**Pattern**: Recursive counting
```python
def size(root):
    if not root: return 0
    return 1 + size(root.left) + size(root.right)
```

### Problem 4: Count Leaves

**Pattern**: Base case is leaf
```python
if not root.left and not root.right:
    return 1  # Found leaf
```

### Problem 5: Is Same Tree

**Pattern**: Synchronized recursion
- Check both null: equal
- Check one null: not equal
- Check values and recurse on both children

## Key Takeaways

1. **Tree recursion pattern**:
   - Base case: null node
   - Recursive case: process node + recurse on children
   
2. **Height vs Size**:
   - Height: max depth (longest path)
   - Size: total nodes (sum all)
   
3. **Tree traversal patterns**:
   - Pre-order: process, left, right
   - In-order: left, process, right
   - Post-order: left, right, process
   
4. **Space complexity**: O(h) for recursion where h = height
