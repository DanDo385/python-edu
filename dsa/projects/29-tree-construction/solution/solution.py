"""
Project 29: Tree Construction

This module implements algorithms to construct binary trees from different
traversal sequences and to serialize/deserialize trees.

Key concepts:
- Building trees from preorder + inorder traversals
- Building trees from postorder + inorder traversals
- Serializing and deserializing binary trees

Author: Python-Edu DSA Curriculum
"""

from typing import Optional, List
from collections import deque


class TreeNode:
    """Binary tree node."""

    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_preorder_inorder(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """
    Construct binary tree from preorder and inorder traversal sequences.

    Preorder: Root → Left → Right (first element is root)
    Inorder: Left → Root → Right (root splits left/right subtrees)

    Algorithm:
    1. Create hash map of inorder indices for O(1) lookup
    2. Use recursion with index pointers
    3. Pick root from preorder, find it in inorder
    4. Split inorder into left and right subtrees
    5. Recursively build left and right subtrees

    Args:
        preorder: Preorder traversal sequence
        inorder: Inorder traversal sequence

    Returns:
        Root of constructed tree

    Time Complexity: O(n) where n is number of nodes
    Space Complexity: O(n) for hash map and recursion stack

    Examples:
        >>> preorder = [3, 9, 20, 15, 7]
        >>> inorder = [9, 3, 15, 20, 7]
        >>> root = build_tree_preorder_inorder(preorder, inorder)
        >>> root.val
        3
        >>> root.left.val
        9
        >>> root.right.val
        20
    """
    if not preorder or not inorder:
        return None

    # Build hash map for O(1) inorder index lookup
    inorder_map = {val: idx for idx, val in enumerate(inorder)}

    pre_idx = [0]  # Use list to make it mutable in nested function

    def build(in_left: int, in_right: int) -> Optional[TreeNode]:
        """
        Recursively build tree from current ranges.

        Args:
            in_left: Left boundary of inorder range
            in_right: Right boundary of inorder range

        Returns:
            Root of current subtree
        """
        if in_left > in_right:
            return None

        # Pick current root from preorder
        root_val = preorder[pre_idx[0]]
        root = TreeNode(root_val)
        pre_idx[0] += 1

        # Find root position in inorder
        in_idx = inorder_map[root_val]

        # Build left subtree (elements before root in inorder)
        root.left = build(in_left, in_idx - 1)

        # Build right subtree (elements after root in inorder)
        root.right = build(in_idx + 1, in_right)

        return root

    return build(0, len(inorder) - 1)


def build_tree_postorder_inorder(postorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """
    Construct binary tree from postorder and inorder traversal sequences.

    Postorder: Left → Right → Root (last element is root)
    Inorder: Left → Root → Right (root splits left/right subtrees)

    Algorithm:
    1. Create hash map of inorder indices for O(1) lookup
    2. Process postorder from right to left (reverse of postorder)
    3. Build RIGHT subtree first, then LEFT (important!)

    Args:
        postorder: Postorder traversal sequence
        inorder: Inorder traversal sequence

    Returns:
        Root of constructed tree

    Time Complexity: O(n)
    Space Complexity: O(n)

    Examples:
        >>> postorder = [9, 15, 7, 20, 3]
        >>> inorder = [9, 3, 15, 20, 7]
        >>> root = build_tree_postorder_inorder(postorder, inorder)
        >>> root.val
        3
    """
    if not postorder or not inorder:
        return None

    # Build hash map for O(1) inorder index lookup
    inorder_map = {val: idx for idx, val in enumerate(inorder)}

    post_idx = [len(postorder) - 1]  # Start from end

    def build(in_left: int, in_right: int) -> Optional[TreeNode]:
        """Recursively build tree from current ranges."""
        if in_left > in_right:
            return None

        # Pick current root from end of postorder
        root_val = postorder[post_idx[0]]
        root = TreeNode(root_val)
        post_idx[0] -= 1

        # Find root position in inorder
        in_idx = inorder_map[root_val]

        # Build RIGHT subtree first (postorder is LRN, so we process RNL)
        root.right = build(in_idx + 1, in_right)

        # Build LEFT subtree
        root.left = build(in_left, in_idx - 1)

        return root

    return build(0, len(inorder) - 1)


def serialize(root: Optional[TreeNode]) -> str:
    """
    Serialize a binary tree to a string representation.

    Uses level-order (BFS) traversal. Null nodes represented as "null".
    Format: "val1,val2,null,val3,..." 

    Args:
        root: Root of binary tree

    Returns:
        String representation

    Time Complexity: O(n)
    Space Complexity: O(n)

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        >>> serialize(root)
        '1,2,3,null,null,4,5'

        >>> serialize(None)
        ''
    """
    if not root:
        return ""

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    # Remove trailing nulls
    while result and result[-1] == "null":
        result.pop()

    return ",".join(result)


def deserialize(data: str) -> Optional[TreeNode]:
    """
    Deserialize string back to binary tree.

    Args:
        data: String representation from serialize()

    Returns:
        Root of reconstructed tree

    Time Complexity: O(n)
    Space Complexity: O(n)

    Examples:
        >>> root = deserialize("1,2,3,null,null,4,5")
        >>> root.val
        1
        >>> root.left.val
        2
        >>> root.right.val
        3
    """
    if not data:
        return None

    values = data.split(",")
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Process left child
        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1

        # Process right child
        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1

    return root


# Helper functions for testing and demonstrations
def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Helper: Get inorder traversal."""
    if not root:
        return []
    return (inorder_traversal(root.left) + 
            [root.val] + 
            inorder_traversal(root.right))


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Helper: Get preorder traversal."""
    if not root:
        return []
    return ([root.val] + 
            preorder_traversal(root.left) + 
            preorder_traversal(root.right))


def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Helper: Get postorder traversal."""
    if not root:
        return []
    return (postorder_traversal(root.left) + 
            postorder_traversal(root.right) + 
            [root.val])


if __name__ == "__main__":
    print("Tree Construction Demonstrations")
    print("=" * 70)

    # Demo 1: Build from preorder and inorder
    print("\n1. Build from Preorder and Inorder:")
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(f"   Preorder: {preorder}")
    print(f"   Inorder:  {inorder}")
    root1 = build_tree_preorder_inorder(preorder, inorder)
    print(f"   Result tree (preorder): {preorder_traversal(root1)}")
    print(f"   Result tree (inorder):  {inorder_traversal(root1)}")

    # Demo 2: Build from postorder and inorder
    print("\n2. Build from Postorder and Inorder:")
    postorder = [9, 15, 7, 20, 3]
    inorder = [9, 3, 15, 20, 7]
    print(f"   Postorder: {postorder}")
    print(f"   Inorder:   {inorder}")
    root2 = build_tree_postorder_inorder(postorder, inorder)
    print(f"   Result tree (postorder): {postorder_traversal(root2)}")
    print(f"   Result tree (inorder):   {inorder_traversal(root2)}")

    # Demo 3: Serialize and Deserialize
    print("\n3. Serialize and Deserialize:")
    root3 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    print(f"   Original tree (inorder): {inorder_traversal(root3)}")
    serialized = serialize(root3)
    print(f"   Serialized: {serialized}")
    root3_reconstructed = deserialize(serialized)
    print(f"   Reconstructed (inorder): {inorder_traversal(root3_reconstructed)}")

    # Demo 4: Edge cases
    print("\n4. Edge Cases:")
    print(f"   Empty tree serialize: '{serialize(None)}'")
    print(f"   Empty tree deserialize: {deserialize('')}")
    single = TreeNode(1)
    print(f"   Single node serialize: '{serialize(single)}'")

    print("\n" + "=" * 70)
    print("All tree construction operations demonstrated!")
