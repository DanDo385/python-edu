"""
Project 28: Binary Search Tree

This module implements Binary Search Tree (BST) operations including insertion,
search, deletion, validation, finding kth smallest element, and BST iterator.

A Binary Search Tree is a binary tree where for every node:
- All values in the left subtree < node.val
- All values in the right subtree > node.val

This property enables efficient O(log n) operations on balanced trees.

Author: Python-Edu DSA Curriculum
Time Complexity: Most operations O(h) where h is height
Space Complexity: O(h) for recursion stack
"""

from typing import Optional, List


class TreeNode:
    """
    A node in a binary tree.

    Attributes:
        val (int): The value stored in the node
        left (TreeNode | None): Reference to left child node
        right (TreeNode | None): Reference to right child node
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


def insert_bst(root: Optional[TreeNode], val: int) -> TreeNode:
    """
    Insert a value into a Binary Search Tree.

    The BST property is maintained: for every node, all values in left subtree
    < node.val < all values in right subtree.

    Algorithm:
    1. If root is None, create new node with val
    2. If val < root.val, recursively insert into left subtree
    3. If val > root.val, recursively insert into right subtree
    4. If val == root.val, typically ignore (no duplicates in standard BST)
    5. Return root

    Args:
        root: Root of BST (or None for empty tree)
        val: Value to insert

    Returns:
        Root of BST after insertion

    Time Complexity: O(h) where h is height
                     Best case O(log n) for balanced tree
                     Worst case O(n) for skewed tree
    Space Complexity: O(h) for recursion stack

    Examples:
        >>> # Insert into empty tree
        >>> root = insert_bst(None, 5)
        >>> root.val
        5

        >>> # Insert smaller value (goes left)
        >>> root = insert_bst(root, 3)
        >>> root.left.val
        3

        >>> # Insert larger value (goes right)
        >>> root = insert_bst(root, 7)
        >>> root.right.val
        7

        >>> # Build complete BST
        >>> root = None
        >>> for val in [5, 3, 7, 1, 4, 6, 9]:
        ...     root = insert_bst(root, val)
        >>> root.val
        5
    """
    # Base case: empty tree, create new node
    if root is None:
        return TreeNode(val)

    # Recursive case: traverse to correct position
    if val < root.val:
        # Insert into left subtree
        root.left = insert_bst(root.left, val)
    elif val > root.val:
        # Insert into right subtree
        root.right = insert_bst(root.right, val)
    # If val == root.val, we don't insert duplicates (do nothing)

    return root


def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Search for a value in BST. Return the node if found, None otherwise.

    Uses BST property to efficiently navigate:
    - If val < node.val, search left
    - If val > node.val, search right
    - If val == node.val, found!

    Algorithm:
    1. If root is None, value not found, return None
    2. If val == root.val, found, return root
    3. If val < root.val, recursively search left subtree
    4. If val > root.val, recursively search right subtree

    Args:
        root: Root of BST
        val: Value to search for

    Returns:
        TreeNode containing val, or None if not found

    Time Complexity: O(h) where h is height
    Space Complexity: O(h) for recursive calls (O(1) for iterative version)

    Examples:
        >>> # Build BST: 5, 3, 7, 1, 4
        >>> root = TreeNode(5)
        >>> root.left = TreeNode(3, TreeNode(1), TreeNode(4))
        >>> root.right = TreeNode(7)

        >>> # Found
        >>> node = search_bst(root, 3)
        >>> node.val
        3

        >>> # Not found
        >>> node = search_bst(root, 10)
        >>> node is None
        True

        >>> # Search in empty tree
        >>> search_bst(None, 5) is None
        True
    """
    # Base case: empty tree or not found
    if root is None:
        return None

    # Found the value
    if val == root.val:
        return root

    # Search left or right based on BST property
    if val < root.val:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)


def delete_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Delete a value from BST while maintaining BST property.

    Three cases to handle:
    1. Node is a leaf (no children): simply remove
    2. Node has one child: replace node with its child
    3. Node has two children: replace with inorder successor (smallest in right subtree)
       - Find minimum value in right subtree
       - Copy that value to current node
       - Delete the minimum node from right subtree

    Algorithm:
    1. Find the node to delete (recursive search)
    2. Handle three cases:
       Case 1: Leaf node → return None
       Case 2: One child → return the child
       Case 3: Two children → replace with successor, delete successor
    3. Return the modified tree root

    Args:
        root: Root of BST
        val: Value to delete

    Returns:
        Root of BST after deletion (may be None if tree becomes empty)

    Time Complexity: O(h) where h is height
    Space Complexity: O(h) for recursion stack

    Examples:
        >>> # Build BST
        >>> root = TreeNode(5)
        >>> root.left = TreeNode(3)
        >>> root.right = TreeNode(7)

        >>> # Delete leaf
        >>> root = delete_bst(root, 7)
        >>> root.right is None
        True

        >>> # Delete node with one child
        >>> root.left.left = TreeNode(1)
        >>> root = delete_bst(root, 3)
        >>> root.left.val
        1

        >>> # Delete root (two children case tested in test suite)
        >>> root = delete_bst(root, 5)
    """
    # Base case: value not found
    if root is None:
        return None

    # Find the node to delete
    if val < root.val:
        # Delete from left subtree
        root.left = delete_bst(root.left, val)
    elif val > root.val:
        # Delete from right subtree
        root.right = delete_bst(root.right, val)
    else:
        # Found the node to delete
        # Case 1: Leaf node or node with one child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Case 2: Node with two children
        # Find inorder successor (minimum value in right subtree)
        successor = _find_min(root.right)

        # Copy successor value to current node
        root.val = successor.val

        # Delete the successor from right subtree
        root.right = delete_bst(root.right, successor.val)

    return root


def _find_min(node: TreeNode) -> TreeNode:
    """
    Find the minimum value node in a BST.

    The minimum is the leftmost node.

    Args:
        node: Root of subtree to search

    Returns:
        Node with minimum value

    Time Complexity: O(h) where h is height
    Space Complexity: O(1)
    """
    current = node
    while current.left is not None:
        current = current.left
    return current


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    Determine if a binary tree is a valid BST.

    IMPORTANT: The BST property must hold for ALL nodes, not just immediate children.
    For each node, ALL values in left subtree must be less than node.val,
    and ALL values in right subtree must be greater than node.val.

    Common mistake: Only comparing with immediate parent (wrong!)
    Correct approach: Track valid range (min, max) for each subtree

    Algorithm:
    1. Use helper function with min/max bounds
    2. For each node, check if value is within valid range
    3. Recursively validate left subtree with updated max bound
    4. Recursively validate right subtree with updated min bound

    Args:
        root: Root of binary tree to validate

    Returns:
        True if valid BST, False otherwise

    Time Complexity: O(n) - must visit each node once
    Space Complexity: O(h) for recursion stack

    Examples:
        >>> # Valid BST
        >>> root = TreeNode(5)
        >>> root.left = TreeNode(3, TreeNode(1), TreeNode(4))
        >>> root.right = TreeNode(7)
        >>> is_valid_bst(root)
        True

        >>> # Invalid: right child of 3 should be < 5
        >>> root = TreeNode(5)
        >>> root.left = TreeNode(3)
        >>> root.left.right = TreeNode(6)  # 6 > 5, but in left subtree!
        >>> is_valid_bst(root)
        False

        >>> # Empty tree is valid
        >>> is_valid_bst(None)
        True
    """
    def validate(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        """
        Helper function to validate BST with min/max bounds.

        Args:
            node: Current node to validate
            min_val: Minimum valid value for this node (exclusive)
            max_val: Maximum valid value for this node (exclusive)

        Returns:
            True if subtree rooted at node is valid BST
        """
        # Base case: empty tree is valid
        if node is None:
            return True

        # Check if current node value is within valid range
        if node.val <= min_val or node.val >= max_val:
            return False

        # Recursively validate left and right subtrees with updated bounds
        # Left subtree: all values must be < node.val (update max_val)
        # Right subtree: all values must be > node.val (update min_val)
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    # Start with infinite range
    return validate(root, float('-inf'), float('inf'))


def kth_smallest(root: TreeNode, k: int) -> int:
    """
    Find the kth smallest element in BST (1-indexed).

    Key insight: Inorder traversal of BST produces sorted sequence.
    - Visit left subtree (smaller values)
    - Visit current node
    - Visit right subtree (larger values)

    We can stop as soon as we've visited k nodes.

    Algorithm:
    1. Perform inorder traversal
    2. Count nodes visited
    3. When count reaches k, return that value

    Args:
        root: Root of BST (guaranteed non-empty)
        k: Position (1-indexed, 1 <= k <= number of nodes)

    Returns:
        The kth smallest value

    Time Complexity: O(h + k) where h is height
                     Best case: O(k) if k is small
                     Worst case: O(n) if k = n
    Space Complexity: O(h) for recursion stack

    Examples:
        >>> # Build BST
        >>> root = TreeNode(5)
        >>> root.left = TreeNode(3, TreeNode(1), TreeNode(4))
        >>> root.right = TreeNode(7)
        >>> # Inorder: [1, 3, 4, 5, 7]

        >>> kth_smallest(root, 1)  # Smallest
        1
        >>> kth_smallest(root, 2)
        3
        >>> kth_smallest(root, 3)
        4
        >>> kth_smallest(root, 5)  # Largest
        7
    """
    # Use list to store count and result (mutable in closure)
    count = [0]
    result = [None]

    def inorder(node: Optional[TreeNode]) -> None:
        """
        Inorder traversal that stops after finding kth element.

        Args:
            node: Current node
        """
        if node is None or result[0] is not None:
            return

        # Traverse left subtree (smaller values)
        inorder(node.left)

        # Visit current node
        count[0] += 1
        if count[0] == k:
            result[0] = node.val
            return

        # Traverse right subtree (larger values)
        inorder(node.right)

    inorder(root)
    return result[0]


class BSTIterator:
    """
    Implement an iterator for BST that traverses in-order (sorted order).

    The iterator should support:
    - next(): Returns the next smallest element
    - has_next(): Returns True if more elements exist

    Requirements:
    - next() and has_next() should run in O(1) average time
    - Use O(h) space where h is tree height
    - Do NOT use O(n) space to store all values

    Implementation strategy:
    - Use a stack to simulate inorder traversal
    - Initialize stack with leftmost path
    - On next(), pop from stack, push right child's leftmost path

    Time Complexity:
        __init__: O(h) to initialize stack with leftmost path
        next(): O(1) amortized (each node pushed/popped once)
        has_next(): O(1)
    Space Complexity: O(h) for stack

    Examples:
        >>> # Build BST
        >>> root = TreeNode(7)
        >>> root.left = TreeNode(3)
        >>> root.right = TreeNode(15, TreeNode(9), TreeNode(20))

        >>> iterator = BSTIterator(root)
        >>> iterator.next()     # 3
        3
        >>> iterator.next()     # 7
        7
        >>> iterator.has_next() # True
        True
        >>> iterator.next()     # 9
        9
        >>> iterator.next()     # 15
        15
        >>> iterator.next()     # 20
        20
        >>> iterator.has_next() # False
        False
    """

    def __init__(self, root: Optional[TreeNode]):
        """
        Initialize the iterator.

        Push all left nodes from root to stack to prepare for first next() call.

        Args:
            root: Root of BST
        """
        self.stack: List[TreeNode] = []
        self._push_left(root)

    def _push_left(self, node: Optional[TreeNode]) -> None:
        """
        Push all left nodes from node to stack.

        This prepares the stack to return the leftmost (smallest) unvisited node.

        Args:
            node: Starting node
        """
        while node is not None:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        Return the next smallest element.

        Pops from stack and pushes the right child's leftmost path.

        Returns:
            Next smallest value

        Time Complexity: O(1) amortized
        """
        # Pop the top node (next smallest)
        node = self.stack.pop()

        # If it has a right child, push all left nodes of right subtree
        if node.right:
            self._push_left(node.right)

        return node.val

    def has_next(self) -> bool:
        """
        Check if there are more elements.

        Returns:
            True if more elements exist, False otherwise

        Time Complexity: O(1)
        """
        return len(self.stack) > 0


def build_bst_from_list(values: List[int]) -> Optional[TreeNode]:
    """
    Build a BST by inserting values in the given order.

    Helper function for testing and demonstrations.

    Args:
        values: List of values to insert

    Returns:
        Root of constructed BST

    Time Complexity: O(n * h) where n is number of values, h is height
    Space Complexity: O(h) for recursion during inserts

    Examples:
        >>> root = build_bst_from_list([5, 3, 7, 1, 4, 6, 9])
        >>> root.val
        5
        >>> root.left.val
        3
        >>> root.right.val
        7
    """
    root = None
    for val in values:
        root = insert_bst(root, val)
    return root


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Perform inorder traversal of BST (returns sorted values).

    Helper function for testing and demonstrations.

    Args:
        root: Root of BST

    Returns:
        List of values in sorted order

    Time Complexity: O(n)
    Space Complexity: O(h) for recursion stack

    Examples:
        >>> root = build_bst_from_list([5, 3, 7, 1, 4])
        >>> inorder_traversal(root)
        [1, 3, 4, 5, 7]
    """
    if root is None:
        return []

    result = []
    result.extend(inorder_traversal(root.left))
    result.append(root.val)
    result.extend(inorder_traversal(root.right))
    return result


if __name__ == "__main__":
    # Demonstration of BST operations
    print("Binary Search Tree Demonstrations")
    print("=" * 70)

    # Demo 1: Build BST
    print("\n1. Building BST from values [5, 3, 7, 1, 4, 6, 9]:")
    root = build_bst_from_list([5, 3, 7, 1, 4, 6, 9])
    print("        5")
    print("       / \\")
    print("      3   7")
    print("     / \\ / \\")
    print("    1  4 6  9")
    print(f"   Inorder traversal (sorted): {inorder_traversal(root)}")

    # Demo 2: Search
    print("\n2. Searching in BST:")
    found = search_bst(root, 4)
    print(f"   Search for 4: {'Found' if found else 'Not found'}")
    found = search_bst(root, 10)
    print(f"   Search for 10: {'Found' if found else 'Not found'}")

    # Demo 3: Validate BST
    print("\n3. Validating BST:")
    print(f"   Is valid BST: {is_valid_bst(root)}")

    # Create invalid BST
    invalid_root = TreeNode(5)
    invalid_root.left = TreeNode(3)
    invalid_root.left.right = TreeNode(6)  # 6 > 5 but in left subtree!
    print(f"   Invalid tree is valid BST: {is_valid_bst(invalid_root)}")

    # Demo 4: Kth Smallest
    print("\n4. Finding Kth Smallest:")
    for k in [1, 3, 5, 7]:
        print(f"   {k}th smallest: {kth_smallest(root, k)}")

    # Demo 5: BST Iterator
    print("\n5. BST Iterator (inorder traversal):")
    iterator = BSTIterator(root)
    values = []
    while iterator.has_next():
        values.append(iterator.next())
    print(f"   Iterator sequence: {values}")

    # Demo 6: Deletion
    print("\n6. Deletion Operations:")
    test_root = build_bst_from_list([5, 3, 7, 1, 4, 6, 9])
    print(f"   Original: {inorder_traversal(test_root)}")

    # Delete leaf
    test_root = delete_bst(test_root, 1)
    print(f"   After deleting 1 (leaf): {inorder_traversal(test_root)}")

    # Delete node with one child
    test_root = delete_bst(test_root, 7)
    print(f"   After deleting 7 (one child): {inorder_traversal(test_root)}")

    # Delete node with two children
    test_root = delete_bst(test_root, 5)
    print(f"   After deleting 5 (two children): {inorder_traversal(test_root)}")

    # Demo 7: Edge Cases
    print("\n7. Edge Cases:")
    print(f"   Empty tree is valid BST: {is_valid_bst(None)}")
    print(f"   Single node: {inorder_traversal(TreeNode(42))}")

    # Skewed tree (worst case)
    skewed = build_bst_from_list([1, 2, 3, 4, 5])
    print(f"   Right-skewed tree [1,2,3,4,5]: {inorder_traversal(skewed)}")

    print("\n" + "=" * 70)
    print("All BST operations demonstrated!")
