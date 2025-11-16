"""
Project 27: Tree Traversals

This module implements various tree traversal algorithms for binary trees,
including both recursive and iterative approaches for depth-first traversals
(inorder, preorder, postorder) and breadth-first traversal (level-order).

Author: Python-Edu DSA Curriculum
Time Complexity: O(n) for all traversals where n is number of nodes
Space Complexity: O(h) for DFS, O(w) for BFS where h=height, w=max width
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    """
    A node in a binary tree.

    This is the fundamental building block for binary tree structures.
    Each node contains a value and references to left and right children.

    Attributes:
        val (int): The value stored in the node
        left (TreeNode | None): Reference to left child node
        right (TreeNode | None): Reference to right child node

    Examples:
        >>> node = TreeNode(5)
        >>> node.val
        5
        >>> node.left is None
        True
        >>> node.right is None
        True

        >>> # Build small tree: 1 -> left: 2, right: 3
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(3)
    """

    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None):
        """
        Initialize a tree node.

        Args:
            val: Value to store in node (default: 0)
            left: Left child node (default: None)
            right: Right child node (default: None)
        """
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"TreeNode({self.val})"


def inorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    """
    Perform inorder traversal (Left -> Root -> Right) recursively.

    Inorder traversal visits nodes in the following order:
    1. Traverse left subtree
    2. Visit root node
    3. Traverse right subtree

    For Binary Search Trees, inorder traversal produces values in sorted order.

    Algorithm:
    1. Base case: if root is None, return empty list
    2. Recursively traverse left subtree
    3. Add current node's value
    4. Recursively traverse right subtree
    5. Combine results

    Args:
        root: Root node of binary tree

    Returns:
        List of node values in inorder sequence

    Time Complexity: O(n) where n is number of nodes (visit each node once)
    Space Complexity: O(h) where h is height (recursive call stack)
                     Worst case O(n) for skewed tree, O(log n) for balanced

    Examples:
        >>> #       1
        >>> #      / \\
        >>> #     2   3
        >>> #    / \\
        >>> #   4   5
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        >>> root.right = TreeNode(3)
        >>> inorder_traversal_recursive(root)
        [4, 2, 5, 1, 3]

        >>> # Empty tree
        >>> inorder_traversal_recursive(None)
        []

        >>> # Single node
        >>> inorder_traversal_recursive(TreeNode(42))
        [42]
    """
    if root is None:
        return []

    result = []

    # Traverse left subtree
    result.extend(inorder_traversal_recursive(root.left))

    # Visit root
    result.append(root.val)

    # Traverse right subtree
    result.extend(inorder_traversal_recursive(root.right))

    return result


def preorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    """
    Perform preorder traversal (Root -> Left -> Right) recursively.

    Preorder traversal visits nodes in the following order:
    1. Visit root node
    2. Traverse left subtree
    3. Traverse right subtree

    Useful for: tree copying, creating prefix expressions, serialization.

    Algorithm:
    1. Base case: if root is None, return empty list
    2. Add current node's value (visit root first)
    3. Recursively traverse left subtree
    4. Recursively traverse right subtree
    5. Combine results

    Args:
        root: Root node of binary tree

    Returns:
        List of node values in preorder sequence

    Time Complexity: O(n) where n is number of nodes
    Space Complexity: O(h) where h is height (recursive call stack)

    Examples:
        >>> #       1
        >>> #      / \\
        >>> #     2   3
        >>> #    / \\
        >>> #   4   5
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        >>> root.right = TreeNode(3)
        >>> preorder_traversal_recursive(root)
        [1, 2, 4, 5, 3]

        >>> preorder_traversal_recursive(None)
        []
    """
    if root is None:
        return []

    result = []

    # Visit root first
    result.append(root.val)

    # Traverse left subtree
    result.extend(preorder_traversal_recursive(root.left))

    # Traverse right subtree
    result.extend(preorder_traversal_recursive(root.right))

    return result


def postorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    """
    Perform postorder traversal (Left -> Right -> Root) recursively.

    Postorder traversal visits nodes in the following order:
    1. Traverse left subtree
    2. Traverse right subtree
    3. Visit root node

    Useful for: tree deletion, postfix expressions, calculating tree properties.

    Algorithm:
    1. Base case: if root is None, return empty list
    2. Recursively traverse left subtree
    3. Recursively traverse right subtree
    4. Add current node's value (visit root last)
    5. Combine results

    Args:
        root: Root node of binary tree

    Returns:
        List of node values in postorder sequence

    Time Complexity: O(n) where n is number of nodes
    Space Complexity: O(h) where h is height (recursive call stack)

    Examples:
        >>> #       1
        >>> #      / \\
        >>> #     2   3
        >>> #    / \\
        >>> #   4   5
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        >>> root.right = TreeNode(3)
        >>> postorder_traversal_recursive(root)
        [4, 5, 2, 3, 1]

        >>> postorder_traversal_recursive(None)
        []
    """
    if root is None:
        return []

    result = []

    # Traverse left subtree
    result.extend(postorder_traversal_recursive(root.left))

    # Traverse right subtree
    result.extend(postorder_traversal_recursive(root.right))

    # Visit root last
    result.append(root.val)

    return result


def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform level-order traversal (breadth-first) using a queue.

    Level-order traversal visits nodes level by level, from left to right.
    This is a breadth-first search (BFS) approach.

    Useful for: finding shortest path, level-based processing, tree width.

    Algorithm:
    1. Handle empty tree case
    2. Initialize queue with root node
    3. While queue not empty:
       a. Get number of nodes at current level
       b. Process all nodes at this level
       c. Add their children to queue for next level
    4. Return list of levels

    Args:
        root: Root node of binary tree

    Returns:
        List of lists, where each inner list contains values at that level

    Time Complexity: O(n) where n is number of nodes (visit each once)
    Space Complexity: O(w) where w is maximum width of tree
                     Worst case O(n) for complete binary tree (last level has n/2 nodes)

    Examples:
        >>> #       1
        >>> #      / \\
        >>> #     2   3
        >>> #    / \\
        >>> #   4   5
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        >>> root.right = TreeNode(3)
        >>> level_order_traversal(root)
        [[1], [2, 3], [4, 5]]

        >>> level_order_traversal(None)
        []

        >>> # Single node
        >>> level_order_traversal(TreeNode(1))
        [[1]]

        >>> # Skewed tree (all right)
        >>> root = TreeNode(1)
        >>> root.right = TreeNode(2)
        >>> root.right.right = TreeNode(3)
        >>> level_order_traversal(root)
        [[1], [2], [3]]
    """
    if root is None:
        return []

    result = []
    queue = deque([root])  # Initialize queue with root

    while queue:
        level_size = len(queue)  # Number of nodes at current level
        current_level = []

        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            # Add children to queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


def inorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Perform inorder traversal iteratively using a stack.

    This achieves the same result as recursive inorder traversal but uses
    an explicit stack instead of the call stack. This can be more efficient
    and avoids stack overflow for very deep trees.

    Algorithm:
    1. Initialize empty stack and result list
    2. Start with current = root
    3. While current exists or stack not empty:
       a. Go as far left as possible, pushing nodes to stack
       b. When can't go left, pop from stack
       c. Visit popped node (add to result)
       d. Move to right child

    Args:
        root: Root node of binary tree

    Returns:
        List of node values in inorder sequence

    Time Complexity: O(n) where n is number of nodes
    Space Complexity: O(h) where h is height (explicit stack)

    Examples:
        >>> #       1
        >>> #      / \\
        >>> #     2   3
        >>> #    / \\
        >>> #   4   5
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        >>> root.right = TreeNode(3)
        >>> inorder_traversal_iterative(root)
        [4, 2, 5, 1, 3]
    """
    result = []
    stack = []
    current = root

    while current or stack:
        # Go as far left as possible
        while current:
            stack.append(current)
            current = current.left

        # Current is None, so we've reached leftmost node
        # Pop from stack and visit
        current = stack.pop()
        result.append(current.val)

        # Move to right child
        current = current.right

    return result


def preorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Perform preorder traversal iteratively using a stack.

    This uses a stack to simulate the recursive call stack. The key insight
    is to push right child first (so it's processed later) and left child
    second (so it's processed first).

    Algorithm:
    1. Handle empty tree
    2. Initialize stack with root
    3. While stack not empty:
       a. Pop node from stack
       b. Visit node (add to result)
       c. Push right child (if exists)
       d. Push left child (if exists)

    Args:
        root: Root node of binary tree

    Returns:
        List of node values in preorder sequence

    Time Complexity: O(n) where n is number of nodes
    Space Complexity: O(h) where h is height (explicit stack)

    Examples:
        >>> #       1
        >>> #      / \\
        >>> #     2   3
        >>> #    / \\
        >>> #   4   5
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        >>> root.right = TreeNode(3)
        >>> preorder_traversal_iterative(root)
        [1, 2, 4, 5, 3]
    """
    if root is None:
        return []

    result = []
    stack = [root]

    while stack:
        # Pop and visit node
        node = stack.pop()
        result.append(node.val)

        # Push right first (so left is processed first - stack is LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def postorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Perform postorder traversal iteratively using a stack.

    This is the most complex iterative traversal because we need to visit
    the root AFTER both children. We use a two-stack approach or track
    the last visited node.

    Approach: Use one stack and track last visited node
    - We can only visit root after visiting both children
    - Track last visited to know if we're coming from right child

    Algorithm:
    1. Handle empty tree
    2. Initialize stack and last_visited tracker
    3. While current exists or stack not empty:
       a. Go as far left as possible
       b. Peek at top of stack
       c. If right child exists and not yet visited, process right
       d. Otherwise, pop and visit node

    Args:
        root: Root node of binary tree

    Returns:
        List of node values in postorder sequence

    Time Complexity: O(n) where n is number of nodes
    Space Complexity: O(h) where h is height (explicit stack)

    Examples:
        >>> #       1
        >>> #      / \\
        >>> #     2   3
        >>> #    / \\
        >>> #   4   5
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        >>> root.right = TreeNode(3)
        >>> postorder_traversal_iterative(root)
        [4, 5, 2, 3, 1]
    """
    if root is None:
        return []

    result = []
    stack = []
    current = root
    last_visited = None

    while current or stack:
        # Go as far left as possible
        while current:
            stack.append(current)
            current = current.left

        # Peek at top of stack
        peek_node = stack[-1]

        # If right child exists and hasn't been visited, process right subtree
        if peek_node.right and peek_node.right != last_visited:
            current = peek_node.right
        else:
            # No right child or right child already processed
            # Now we can visit this node
            stack.pop()
            result.append(peek_node.val)
            last_visited = peek_node

    return result


def max_depth(root: Optional[TreeNode]) -> int:
    """
    Calculate the maximum depth (height) of a binary tree.

    The depth is the number of nodes along the longest path from root
    to a leaf node. An empty tree has depth 0, a single node has depth 1.

    This uses a simple recursive approach: depth = 1 + max(left_depth, right_depth)

    Algorithm:
    1. Base case: if root is None, depth is 0
    2. Recursively calculate left subtree depth
    3. Recursively calculate right subtree depth
    4. Return 1 + max(left_depth, right_depth)

    Args:
        root: Root node of binary tree

    Returns:
        Maximum depth (number of nodes from root to deepest leaf)

    Time Complexity: O(n) where n is number of nodes (visit each once)
    Space Complexity: O(h) where h is height (recursive call stack)

    Examples:
        >>> #       1
        >>> #      / \\
        >>> #     2   3
        >>> #    / \\
        >>> #   4   5
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        >>> root.right = TreeNode(3)
        >>> max_depth(root)
        3

        >>> max_depth(None)
        0

        >>> max_depth(TreeNode(1))
        1

        >>> # Skewed tree
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> root.left.left = TreeNode(3)
        >>> max_depth(root)
        3
    """
    if root is None:
        return 0

    # Calculate depth of left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # Depth is 1 (current node) + max of subtree depths
    return 1 + max(left_depth, right_depth)


def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from a level-order list representation.

    The list uses level-order (BFS) indexing where:
    - Index 0 is root
    - For node at index i: left child at 2*i+1, right child at 2*i+2
    - None represents a missing node

    This is the standard format used by LeetCode and other platforms.

    Algorithm:
    1. Handle empty list
    2. Create root from first value
    3. Use queue to track nodes to process
    4. For each node, assign left and right children from list
    5. Add non-null children to queue

    Args:
        values: Level-order list of node values (None for missing nodes)

    Returns:
        Root node of constructed tree

    Time Complexity: O(n) where n is number of values
    Space Complexity: O(n) for queue and tree nodes

    Examples:
        >>> # Build tree [1,2,3,4,5]
        >>> #       1
        >>> #      / \\
        >>> #     2   3
        >>> #    / \\
        >>> #   4   5
        >>> root = build_tree_from_list([1, 2, 3, 4, 5])
        >>> level_order_traversal(root)
        [[1], [2, 3], [4, 5]]

        >>> # Build tree [1,None,2,3]
        >>> #   1
        >>> #    \\
        >>> #     2
        >>> #    /
        >>> #   3
        >>> root = build_tree_from_list([1, None, 2, 3])
        >>> preorder_traversal_recursive(root)
        [1, 2, 3]

        >>> build_tree_from_list([])

        >>> build_tree_from_list([42])
        TreeNode(42)
    """
    if not values:
        return None

    # Create root
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1  # Index in values list

    while queue and i < len(values):
        node = queue.popleft()

        # Assign left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Assign right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


# Helper function for visualization (bonus)
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Convert a binary tree to level-order list representation.

    This is the inverse of build_tree_from_list. Useful for testing
    and visualization.

    Args:
        root: Root node of binary tree

    Returns:
        Level-order list representation of tree

    Time Complexity: O(n)
    Space Complexity: O(n)

    Examples:
        >>> #       1
        >>> #      / \\
        >>> #     2   3
        >>> #    / \\
        >>> #   4   5
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        >>> root.right = TreeNode(3)
        >>> tree_to_list(root)
        [1, 2, 3, 4, 5]
    """
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


if __name__ == "__main__":
    # Demonstration of all traversal methods
    print("Tree Traversals Demonstration")
    print("=" * 60)

    # Build example tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    print("\nBuilding tree from list [1, 2, 3, 4, 5]:")
    root = build_tree_from_list([1, 2, 3, 4, 5])
    print("        1")
    print("       / \\")
    print("      2   3")
    print("     / \\")
    print("    4   5")

    print("\nRecursive Traversals:")
    print("-" * 60)
    print(f"Inorder (L→Root→R):    {inorder_traversal_recursive(root)}")
    print(f"Preorder (Root→L→R):   {preorder_traversal_recursive(root)}")
    print(f"Postorder (L→R→Root):  {postorder_traversal_recursive(root)}")

    print("\nIterative Traversals:")
    print("-" * 60)
    print(f"Inorder (iterative):   {inorder_traversal_iterative(root)}")
    print(f"Preorder (iterative):  {preorder_traversal_iterative(root)}")
    print(f"Postorder (iterative): {postorder_traversal_iterative(root)}")

    print("\nLevel-Order Traversal (BFS):")
    print("-" * 60)
    print(f"Level-order: {level_order_traversal(root)}")

    print("\nTree Properties:")
    print("-" * 60)
    print(f"Max depth: {max_depth(root)}")

    print("\n" + "=" * 60)
    print("Edge Cases:")
    print("-" * 60)

    # Empty tree
    print(f"Empty tree inorder: {inorder_traversal_recursive(None)}")

    # Single node
    single = TreeNode(42)
    print(f"Single node depth: {max_depth(single)}")

    # Skewed tree
    skewed = build_tree_from_list([1, None, 2, None, None, None, 3])
    print(f"Skewed tree [1,None,2,None,None,None,3] preorder: "
          f"{preorder_traversal_recursive(skewed)}")
