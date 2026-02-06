# Project 08 (DSA Track): Linked List - Solution Walkthrough

## Problem Definition

This module teaches a singly linked list from first principles.

Operations implemented:
- append
- prepend
- find
- remove
- reverse
- to_list

Why it matters:
- Linked lists force you to reason about references/pointers explicitly.
- They are a foundation for stacks, queues, hash buckets, and graph adjacency chains.
- They make memory-model mistakes visible (lost nodes, broken links, cycles).

## Mental Model

A node has two fields:
- `data`
- `next` (reference to another node or `None`)

List shape:

```text
head -> [A|next] -> [B|next] -> [C|None]
```

Unlike arrays, nodes are not contiguous. Traversal follows references.

This directly matches Python's reference model from module 01:
- names hold references to objects,
- reassignment changes which object a name references,
- mutation changes object state seen by all aliases.

## Step-by-Step Reasoning

### 1) `append(data)`

Goal: add at tail.

- Create `new_node`.
- If list empty (`head is None`), set `head = new_node`.
- Else walk until `current.next is None`, then set `current.next = new_node`.

Invariant after append:
- existing chain unchanged,
- exactly one new tail node with `next = None`.

### 2) `prepend(data)`

Goal: add at head in `O(1)`.

- Create `new_node`.
- Point `new_node.next` to current head.
- Move head to `new_node`.

### 3) `find(data)`

- Start from `head`.
- Compare `current.data` each step.
- Return first matching node, else `None`.

### 4) `remove(data)`

Two cases:

- Removing head:
  - if `head.data == data`, set `head = head.next`.

- Removing non-head:
  - track current node,
  - if `current.next.data == data`, bypass target with:
    `current.next = current.next.next`.

This bypass operation is the central pointer update.

### 5) `reverse()`

Use three references:
- `previous`
- `current`
- `next_node`

Loop:
1. save `next_node = current.next`
2. flip `current.next = previous`
3. move forward (`previous = current`, `current = next_node`)

After loop: `head = previous`.

## Indirection, References, and Memory

### Assignment vs mutation

```python
a = Node(1)
b = a
b.data = 99
# a.data is now 99 (same object)
```

`a` and `b` are aliases to one node object.

### Link mutation changes graph structure

Before removal of `B`:

```text
head -> A -> B -> C -> None
```

Operation:

```python
current = A
current.next = current.next.next
```

After:

```text
head -> A -> C -> None
```

Node `B` is now detached from chain (unless another reference still points to it).

### Identity checks

`id(node)` helps verify you still reference same object during traversal and reversal.

## Design Decisions and Tradeoffs

Decision: singly linked list (not doubly linked).
- Why chosen: simpler pointer model for first exposure.
- Alternative rejected: prev pointers on each node.
- Tradeoff: simpler node structure, slower backward operations.

Decision: linear traversal for append.
- Why chosen: minimal state in list object.
- Alternative rejected: maintain tail pointer.
- Tradeoff: append is `O(n)` instead of `O(1)`.

Decision: in-place reverse.
- Why chosen: demonstrates pointer inversion clearly.
- Alternative rejected: allocate new list and copy data.
- Tradeoff: mutation complexity vs memory efficiency.

## Complexity

Let `n` = number of nodes.

- `append`: `O(n)` time, `O(1)` extra space
- `prepend`: `O(1)` time, `O(1)` extra space
- `find`: `O(n)` time
- `remove`: `O(n)` time
- `reverse`: `O(n)` time, `O(1)` extra space
- `to_list`: `O(n)` time, `O(n)` output space

## Example Walkthrough: Reverse

Start:

```text
head -> 1 -> 2 -> 3 -> None
previous=None, current=1
```

Iteration 1:
- save next=2
- set `1.next = None`
- move previous=1, current=2

Iteration 2:
- save next=3
- set `2.next = 1`
- move previous=2, current=3

Iteration 3:
- save next=None
- set `3.next = 2`
- move previous=3, current=None

Finish: `head = previous` => `3 -> 2 -> 1 -> None`.

## Key Takeaways

1. Linked lists are reference graphs, not contiguous arrays.
2. Most operations are controlled pointer rewiring.
3. Aliasing and mutation semantics are central to correctness.
4. Explicit invariants prevent common pointer bugs.
