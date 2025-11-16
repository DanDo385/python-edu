# Project 16: Singly Linked List

> Master linked list fundamentals through hands-on implementation of core operations and classic algorithms

**Difficulty**: ⭐⭐ Intermediate
**Phase**: II (Data Structures & Algorithms)
**Prerequisites**: Project 01-15 (Basic Python, OOP, Recursion)
**Time**: 4-6 hours

---

## What You'll Learn

### Core Concepts
- **Node Structure**: Understanding the building block of linked lists
- **List Operations**: Insertion, deletion, traversal, search
- **Pointer Manipulation**: Working with references and maintaining list integrity
- **Two-Pointer Technique**: Fast/slow pointers for cycle detection and middle finding
- **List Reversal**: Iterative and recursive approaches
- **List Merging**: Combining sorted lists efficiently

### Technical Skills
- Implementing data structures from scratch
- Managing memory through object references
- Handling edge cases (empty lists, single nodes)
- Understanding time/space complexity trade-offs
- Writing robust code with proper error handling

### Practical Applications
- Implementing undo/redo functionality
- Building music/video playlists
- Managing browser history
- Task scheduling systems
- Memory-efficient data storage

### Prerequisites
- **Project 06**: OOP basics (classes, methods)
- **Project 08**: Recursion fundamentals
- **Project 15**: Dynamic programming (optional but helpful)
- Understanding of Python references vs values

---

## Why This Matters

### Linked Lists vs Arrays

Unlike arrays (Python lists), linked lists provide:

```python
# ARRAY (Python list)
arr = [1, 2, 3, 4, 5]
# Memory: [1][2][3][4][5]  (contiguous)
# Insert at front: O(n) - must shift all elements
# Access by index: O(1) - direct memory access

# LINKED LIST
# Memory: [1]→[2]→[3]→[4]→[5]  (scattered)
# Insert at front: O(1) - just update pointers
# Access by index: O(n) - must traverse from head
```

**Trade-offs**:
- ✅ **Linked Lists**: O(1) insertions/deletions at known positions
- ✅ **Arrays**: O(1) random access, better cache locality
- ❌ **Linked Lists**: O(n) access by index, more memory overhead
- ❌ **Arrays**: O(n) insertions/deletions (due to shifting)

### Real-World Applications

1. **Operating Systems**: Process scheduling, memory management
   ```python
   # Task queue in OS scheduler
   tasks = LinkedList()
   tasks.append(Task("process_1"))
   tasks.append(Task("process_2"))
   current_task = tasks.pop_front()  # O(1) - efficient!
   ```

2. **LRU Cache**: Least Recently Used cache eviction
   ```python
   # Combination of hash map + doubly linked list
   # LeetCode 146: LRU Cache uses linked list for O(1) evictions
   ```

3. **Blockchain**: Each block points to previous block
   ```python
   class Block:
       def __init__(self, data, prev_hash):
           self.data = data
           self.prev_hash = prev_hash  # Like a linked list!
   ```

4. **Music Playlists**: Navigate next/previous songs
   ```python
   playlist = LinkedList()
   playlist.append("Song A")
   playlist.append("Song B")
   current = playlist.head
   next_song = current.next  # O(1) navigation
   ```

### Connections to Future Projects
- **Project 17**: Doubly Linked List (two-way pointers)
- **Project 18**: Stack & Queue (can be implemented with linked lists)
- **Project 21**: Binary Trees (extension to tree structures)
- **Project 25**: Graph Algorithms (adjacency lists are linked lists)

---

## When to Use This

### Problem Indicators
You need a linked list when:
- Frequent insertions/deletions at the beginning
- Unknown or dynamic size
- No need for random access
- Building more complex structures (trees, graphs)

### Anti-Patterns (When NOT to use linked lists)

1. **Don't use for random access patterns**
   - ❌ `linked_list[100]`  # O(n) traversal
   - ✅ `array[100]`  # O(1) direct access

2. **Don't use when memory is tight**
   - Each node has overhead (data + pointer)
   - Arrays have better cache locality

3. **Don't use in Python for general purposes**
   - Python's `list` (dynamic array) is highly optimized
   - Use `collections.deque` for queue operations instead
   - Linked lists are educational but rarely used in production Python

---

## Problems

Complete the following problems in `solution/solution.py`:

### Problem 1: Implement LinkedList Class
Implement a complete singly linked list with the following operations:

```python
class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """A singly linked list implementation."""

    def __init__(self):
        """Initialize an empty linked list."""

    def append(self, data):
        """Add a node at the end. O(n) time."""

    def prepend(self, data):
        """Add a node at the beginning. O(1) time."""

    def delete(self, data):
        """Delete the first occurrence of data. O(n) time."""

    def search(self, data):
        """Search for data, return True if found. O(n) time."""

    def get(self, index):
        """Get data at index. O(n) time."""

    def size(self):
        """Return the number of nodes. O(n) time."""

    def is_empty(self):
        """Check if list is empty. O(1) time."""
```

**Example**:
```python
ll = LinkedList()
ll.append(1)      # 1
ll.append(2)      # 1 → 2
ll.prepend(0)     # 0 → 1 → 2
ll.delete(1)      # 0 → 2
print(ll.search(2))  # True
print(ll.get(1))     # 2
print(ll.size())     # 2
```

---

### Problem 2: Reverse Linked List
Reverse a singly linked list.

**Signature**:
```python
def reverse_list(head: Optional[Node]) -> Optional[Node]:
    """
    Reverse a linked list.

    Args:
        head: Head node of the list

    Returns:
        New head of reversed list

    Time: O(n), Space: O(1) iterative, O(n) recursive
    """
```

**Examples**:
```python
# Input:  1 → 2 → 3 → 4 → 5
# Output: 5 → 4 → 3 → 2 → 1

# Input:  1 → 2
# Output: 2 → 1

# Input:  1
# Output: 1

# Input:  None
# Output: None
```

**Approach**: Three-pointer technique (prev, curr, next)

---

### Problem 3: Detect Cycle
Determine if a linked list has a cycle.

**Signature**:
```python
def has_cycle(head: Optional[Node]) -> bool:
    """
    Detect if linked list has a cycle using Floyd's algorithm.

    Args:
        head: Head node of the list

    Returns:
        True if cycle exists, False otherwise

    Time: O(n), Space: O(1)
    """
```

**Examples**:
```python
# Input:  1 → 2 → 3 → 4 → 2 (cycle back to 2)
# Output: True

# Input:  1 → 2 → 3 → None
# Output: False

# Input:  1 → 1 (self-loop)
# Output: True
```

**Approach**: Floyd's Tortoise and Hare (slow/fast pointers)

---

### Problem 4: Find Middle Node
Find the middle node of a linked list. If two middle nodes exist, return the second one.

**Signature**:
```python
def find_middle(head: Optional[Node]) -> Optional[Node]:
    """
    Find the middle node of a linked list.

    Args:
        head: Head node of the list

    Returns:
        Middle node (second middle if even length)

    Time: O(n), Space: O(1)
    """
```

**Examples**:
```python
# Input:  1 → 2 → 3 → 4 → 5
# Output: 3 (node with data 3)

# Input:  1 → 2 → 3 → 4 → 5 → 6
# Output: 4 (second middle)

# Input:  1
# Output: 1

# Input:  None
# Output: None
```

**Approach**: Fast/slow pointer (fast moves 2x, slow moves 1x)

---

### Problem 5: Merge Two Sorted Lists
Merge two sorted linked lists into one sorted list.

**Signature**:
```python
def merge_sorted_lists(l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
    """
    Merge two sorted linked lists.

    Args:
        l1: Head of first sorted list
        l2: Head of second sorted list

    Returns:
        Head of merged sorted list

    Time: O(n + m), Space: O(1) iterative, O(n + m) recursive
    """
```

**Examples**:
```python
# Input:  l1 = 1 → 2 → 4
#         l2 = 1 → 3 → 4
# Output: 1 → 1 → 2 → 3 → 4 → 4

# Input:  l1 = None
#         l2 = 0
# Output: 0

# Input:  l1 = None
#         l2 = None
# Output: None
```

**Approach**: Two-pointer merge (similar to merge sort)

---

### Problem 6: Remove Nth Node From End
Remove the nth node from the end of the list.

**Signature**:
```python
def remove_nth_from_end(head: Optional[Node], n: int) -> Optional[Node]:
    """
    Remove nth node from the end of the list.

    Args:
        head: Head node of the list
        n: Position from end (1-indexed)

    Returns:
        New head of modified list

    Time: O(n), Space: O(1)
    """
```

**Examples**:
```python
# Input:  1 → 2 → 3 → 4 → 5, n = 2
# Output: 1 → 2 → 3 → 5 (removed 4)

# Input:  1, n = 1
# Output: None (removed only node)

# Input:  1 → 2, n = 2
# Output: 2 (removed head)
```

**Approach**: Two-pointer technique with n-gap

---

## Pitfalls & Gotchas

### Common Mistakes

1. **Forgetting to Update Head**
   ```python
   # WRONG: Deleting head without updating it
   def delete(self, data):
       current = self.head
       if current.data == data:
           current = current.next  # Doesn't update self.head!

   # RIGHT
   def delete(self, data):
       if self.head and self.head.data == data:
           self.head = self.head.next  # Update head reference
   ```

2. **Not Handling None/Empty Lists**
   ```python
   # WRONG: Crashes on empty list
   def reverse(head):
       current = head
       prev = None
       while current:  # What if head is None?
           ...

   # RIGHT
   def reverse(head):
       if not head:  # Handle empty list
           return None
       ...
   ```

3. **Losing References During Pointer Manipulation**
   ```python
   # WRONG: Lost reference to next node
   current.next = prev  # Lost reference to current.next!
   current = current.next  # Now current is prev, not original next!

   # RIGHT
   next_temp = current.next  # Save reference first
   current.next = prev
   current = next_temp  # Use saved reference
   ```

4. **Off-by-One Errors**
   ```python
   # Finding nth from end
   # Wrong: fast pointer starts too early/late
   # Right: Move fast pointer exactly n steps ahead
   ```

### Debugging Tips

1. **Draw Diagrams**: Visualize pointer movements on paper
   ```
   Before: 1 → 2 → 3
           ↑
         head

   After:  2 → 3
           ↑
         head
   ```

2. **Use Dummy Nodes**: Simplify edge cases
   ```python
   dummy = Node(0)  # Dummy head
   dummy.next = head
   # Now you can safely manipulate head without special cases
   ```

3. **Print-Debug Traversal**
   ```python
   def print_list(head):
       current = head
       while current:
           print(current.data, end=" → ")
           current = current.next
       print("None")
   ```

---

## Performance Considerations

### Time Complexity

| Operation | Singly Linked List | Python List (Array) |
|-----------|-------------------|---------------------|
| Access by index | O(n) | O(1) |
| Search | O(n) | O(n) |
| Insert at head | O(1) | O(n) |
| Insert at tail | O(n)* | O(1) amortized |
| Insert at middle | O(n) | O(n) |
| Delete at head | O(1) | O(n) |
| Delete at tail | O(n) | O(1) |
| Delete at middle | O(n) | O(n) |

*Can be O(1) if tail pointer is maintained

### Space Complexity

- **Storage**: O(n) - n nodes, each with data + pointer
- **Overhead**: Each node has pointer overhead (~8 bytes on 64-bit)
- **Python list**: More memory-efficient for dense data

### Optimization Strategies

1. **Maintain Tail Pointer**
   ```python
   class LinkedList:
       def __init__(self):
           self.head = None
           self.tail = None  # O(1) append!
   ```

2. **Maintain Size Counter**
   ```python
   class LinkedList:
       def __init__(self):
           self.head = None
           self.size_count = 0  # O(1) size()!
   ```

3. **Use Dummy Head**
   ```python
   class LinkedList:
       def __init__(self):
           self.dummy = Node(0)  # Sentinel node
           self.head = self.dummy.next
   ```

---

## Diagrams

### Node Structure

```
┌─────────────┐
│    Node     │
├─────────────┤
│ data: int   │ ◄── Stores the value
│ next: Node* │ ──┐ Pointer to next node
└─────────────┘   │
                  │
                  ▼
                Next Node or None
```

### Linked List Visualization

```
LinkedList
   │
   ▼
 head
   │
   ▼
┌───┬────┐   ┌───┬────┐   ┌───┬────┐   ┌───┬────┐
│ 1 │  ●─┼──▶│ 2 │  ●─┼──▶│ 3 │  ●─┼──▶│ 4 │None│
└───┴────┘   └───┴────┘   └───┴────┘   └───┴────┘
```

### List Reversal (Three-Pointer)

```
INITIAL:  None ← 1 → 2 → 3 → 4 → None
          ↑    ↑
        prev curr

STEP 1:   None ← 1   2 → 3 → 4 → None
          ↑    ↑   ↑
        prev curr next

STEP 2:   None ← 1 ← 2   3 → 4 → None
               ↑   ↑   ↑
             prev curr next

FINAL:    None ← 1 ← 2 ← 3 ← 4   None
                         ↑
                        head
```

### Cycle Detection (Floyd's Algorithm)

```
1 → 2 → 3 → 4 → 5
    ↑           ↓
    └───────────┘

slow: 1 → 2 → 3 → 4 → 5 → 2 (moves 1 step)
fast: 1 → 3 → 5 → 3 → 5 → 3 (moves 2 steps)
                 ↑
          They meet here! → Cycle detected
```

### Finding Middle (Fast/Slow Pointers)

```
1 → 2 → 3 → 4 → 5 → None

slow: 1 → 2 → 3 (moves 1 step per iteration)
fast: 1 → 3 → 5 → None (moves 2 steps per iteration)
          ↑
    When fast reaches end, slow is at middle
```

---

## How to Run

### Setup
```bash
cd /home/user/python-edu/dsa/projects/16-singly-linked-list
```

### Running Tests
```bash
# All tests
pytest tests/ -v

# Specific test class
pytest tests/test_project_16.py::TestLinkedListBasics -v

# With output
pytest tests/ -v -s

# With coverage
pytest tests/ --cov=solution --cov-report=html
```

### Expected Output
```
============================= test session starts ==============================
collected 45 items

tests/test_project_16.py::TestNode::test_node_creation PASSED            [  2%]
tests/test_project_16.py::TestLinkedListBasics::test_append PASSED       [  4%]
tests/test_project_16.py::TestLinkedListBasics::test_prepend PASSED      [  6%]
tests/test_project_16.py::TestReverseList::test_reverse_basic PASSED     [  8%]
tests/test_project_16.py::TestCycleDetection::test_no_cycle PASSED       [ 11%]
...

========================== 45 passed in 0.28s ===============================
```

---

## Cross-Language Comparison

### Python
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Automatic garbage collection
# No manual memory management needed
```

### C
```c
struct Node {
    int data;
    struct Node* next;
};

// Manual memory management
struct Node* node = malloc(sizeof(struct Node));
node->data = 42;
node->next = NULL;
free(node);  // Must free manually!
```

### Rust
```rust
struct Node {
    data: i32,
    next: Option<Box<Node>>,
}

// Ownership system prevents memory leaks
// No garbage collection, no manual free
```

### Java
```java
class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

// Garbage collected like Python
```

**Key insight**: Python's automatic memory management makes linked lists easier to implement but hides important concepts about pointers and memory.

---

## Advanced Challenges

1. **Challenge 1: Detect Cycle Start**
   - Find the node where the cycle begins
   - Use Floyd's algorithm + math proof
   - Time: O(n), Space: O(1)

2. **Challenge 2: Palindrome Check**
   - Check if linked list is a palindrome
   - Approach: Reverse second half, compare with first half
   - Time: O(n), Space: O(1)

3. **Challenge 3: Intersection Point**
   - Find the intersection of two linked lists
   - LeetCode 160: Intersection of Two Linked Lists
   - Time: O(n + m), Space: O(1)

4. **Challenge 4: Add Two Numbers**
   - Numbers represented as linked lists (reverse order)
   - LeetCode 2: Add Two Numbers
   - Time: O(max(n, m)), Space: O(max(n, m))

5. **Challenge 5: Flatten Nested List**
   - Flatten a multilevel linked list
   - LeetCode 430: Flatten a Multilevel Doubly Linked List
   - Use recursion or stack

---

## References

### Official Documentation
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque) - Python's optimized alternative

### Books
- *Introduction to Algorithms* (CLRS) — Chapter 10: Elementary Data Structures
- *Cracking the Coding Interview* (McDowell) — Chapter 2: Linked Lists

### Internal Resources
- [DSA_PRIMER.md](../../DSA_PRIMER.md) — Big-O complexity basics
- [Project 17: Doubly Linked List](../17-doubly-linked-list/) — Extension with backward pointers

### External Resources
- [LeetCode Linked List Problems](https://leetcode.com/tag/linked-list/)
- [Visualgo: Linked List Visualization](https://visualgo.net/en/list)
- [Floyd's Cycle Detection Algorithm](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare)

---

## Related Projects

- **Next**: [Project 17: Doubly Linked List](../17-doubly-linked-list/) — Bidirectional traversal
- **Related**: [Project 18: Stack & Queue](../18-stack-queue/) — Can be implemented with linked lists
- **Advanced**: [Project 21: Binary Trees](../21-binary-trees/) — Extension to tree structures

---

## Notes for Instructors

### Common Student Struggles
1. **"Why use linked lists when Python lists are better?"**
   - Answer: Educational value, understanding pointers, interview prep, building blocks for trees/graphs

2. **"How do I visualize pointer changes?"**
   - Answer: Draw diagrams, use debugger, print statements after each step

3. **"Why does reversing work with three pointers?"**
   - Answer: Need to track prev (new next), curr (node to reverse), next (prevent losing rest of list)

### Teaching Tips
- Start with visualizations (draw on board)
- Emphasize edge cases: empty list, single node, two nodes
- Use dummy nodes to simplify code
- Compare to real-world examples (train cars, paper chain)
- Practice on paper before coding

---

Last updated: 2025-11-16
