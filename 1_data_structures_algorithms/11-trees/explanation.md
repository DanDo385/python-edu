# Solution in Words: Trees

## How to Think About This Problem

### Understanding Trees

Think of a tree like a family tree or organizational chart - it has a root at the top and branches downward.

**Mental Model:**
```
Root (top)
  ├── Left subtree
  └── Right subtree
```

### Tree Terminology

- **Root**: Top node (no parent)
- **Node**: Element with data and children
- **Leaf**: Node with no children
- **Height**: Longest path from root to leaf
- **Depth**: Distance from root to node

### Traversal Thinking

1. **Preorder**: Process root, then left, then right
2. **Inorder**: Process left, then root, then right (gives sorted order for BST)
3. **Postorder**: Process left, then right, then root

### Recursive Thinking

Trees are naturally recursive:
- A tree = root + left subtree + right subtree
- Each subtree is itself a tree
- Base case: empty tree (None)

### Problem-Solving Strategy

1. **Handle base case**: If node is None, return appropriate value
2. **Process current node**: Based on traversal order
3. **Recurse on subtrees**: Call function on left and right children
4. **Combine results**: Based on what you're calculating

