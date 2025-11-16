"""
Project 30: Advanced Tree Problems

Advanced tree algorithms including LCA, path sums, diameter, 
vertical order traversal, and tree flattening.

Author: Python-Edu DSA Curriculum
"""

from typing import Optional, List, Dict
from collections import deque, defaultdict


class TreeNode:
    """Binary tree node."""
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find lowest common ancestor of two nodes.

    Time: O(n), Space: O(h)

    Examples:
        >>> root = TreeNode(3)
        >>> root.left = TreeNode(5)
        >>> root.right = TreeNode(1)
        >>> p, q = root.left, root.right
        >>> lca = lowest_common_ancestor(root, p, q)
        >>> lca.val
        3
    """
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    return left if left else right


def max_path_sum(root: TreeNode) -> int:
    """
    Find maximum path sum (path can start/end anywhere).

    Time: O(n), Space: O(h)

    Examples:
        >>> root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        >>> max_path_sum(root)
        42
    """
    max_sum = [float('-inf')]

    def max_gain(node):
        if not node:
            return 0

        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        price_newpath = node.val + left_gain + right_gain
        max_sum[0] = max(max_sum[0], price_newpath)

        return node.val + max(left_gain, right_gain)

    max_gain(root)
    return max_sum[0]


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """
    Calculate tree diameter (longest path between any two nodes).

    Time: O(n), Space: O(h)

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        >>> diameter_of_binary_tree(root)
        3
    """
    diameter = [0]

    def depth(node):
        if not node:
            return 0

        left_depth = depth(node.left)
        right_depth = depth(node.right)

        diameter[0] = max(diameter[0], left_depth + right_depth)
        return 1 + max(left_depth, right_depth)

    depth(root)
    return diameter[0]


def vertical_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Return vertical order traversal.

    Time: O(n log n), Space: O(n)

    Examples:
        >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        >>> vertical_order_traversal(root)
        [[9], [3, 15], [20], [7]]
    """
    if not root:
        return []

    column_table = defaultdict(list)
    queue = deque([(root, 0)])

    while queue:
        node, column = queue.popleft()
        column_table[column].append(node.val)

        if node.left:
            queue.append((node.left, column - 1))
        if node.right:
            queue.append((node.right, column + 1))

    return [column_table[x] for x in sorted(column_table.keys())]


def flatten(root: Optional[TreeNode]) -> None:
    """
    Flatten tree to linked list in-place (preorder).

    Time: O(n), Space: O(h)

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
        >>> flatten(root)
        >>> # Result: 1->2->3->4->5->6 (right pointers)
    """
    if not root:
        return

    def flatten_helper(node):
        if not node:
            return None

        if not node.left and not node.right:
            return node

        left_tail = flatten_helper(node.left)
        right_tail = flatten_helper(node.right)

        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None

        return right_tail if right_tail else left_tail

    flatten_helper(root)


if __name__ == "__main__":
    print("Advanced Tree Problems Demonstrations")
    print("=" * 60)

    # Demo 1: LCA
    print("\n1. Lowest Common Ancestor:")
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    lca = lowest_common_ancestor(root, root.left.left, root.left.right)
    print(f"   LCA of 6 and 2: {lca.val}")

    # Demo 2: Max Path Sum
    print("\n2. Maximum Path Sum:")
    root2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(f"   Max path sum: {max_path_sum(root2)}")

    # Demo 3: Diameter
    print("\n3. Diameter:")
    root3 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(f"   Diameter: {diameter_of_binary_tree(root3)}")

    print("\n" + "=" * 60)
