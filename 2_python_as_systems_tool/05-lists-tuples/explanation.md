# Project 05: Lists and Tuples - Solution Walkthrough

## Problem Definition

This module teaches two sequence types with different semantics:
- `list`: mutable, good for in-place updates
- `tuple`: immutable, good for stable snapshots/contracts

The exercise builds a scoreboard pipeline:
1. Normalize scores with bonus and clamping.
2. Rank scores.
3. Return leaders as an immutable tuple.

Why this matters:
- Sequence choice affects bugs, especially around accidental mutation.
- Production code fails often on aliasing, not algorithm novelty.

## Mental Model

Think of names as labels pointing to objects in memory (from module 01).

```text
scores -----> [72, 94, 51, 88]   # one list object
alias  -----> [72, 94, 51, 88]   # same object, different label
```

If you mutate through one label, both see the change.

```python
scores = [1, 2, 3]
alias = scores
alias[0] = 99
# scores is now [99, 2, 3]
```

So `normalize_scores` explicitly copies with `list(scores)` before mutation.

Tuple mental model:
- A tuple is a fixed ordered container.
- Returning top-k as tuple prevents later in-place edits to the leaderboard.

## Step-by-Step Reasoning

1. Normalize safely.
- Validate input list and numeric values.
- Copy list to avoid mutating caller-owned state.
- Apply bonus and clamp each value into `[0, 100]`.

2. Rank deterministically.
- Use `sorted(..., reverse=True)` to create a ranked copy.

3. Snapshot leaders.
- Slice top-k and convert to tuple.
- Expose immutable API output for downstream stability.

4. Orchestrate without duplication.
- `build_scoreboard` composes `normalize_scores` and `top_k`.

## Design Decisions and Tradeoffs

Decision: copy list before update.
- Why chosen: removes aliasing side effects.
- Alternative rejected: mutate in place for speed.
- Tradeoff: `O(n)` extra memory for correctness and API safety.

Decision: return tuple for leaders.
- Why chosen: immutable result communicates intent.
- Alternative rejected: return list and rely on convention.
- Tradeoff: callers must create new tuple/list to modify.

Decision: strict type validation.
- Why chosen: clearer failure boundary in teaching code.
- Alternative rejected: permissive coercion.
- Tradeoff: slightly more boilerplate, fewer silent bugs.

## Reference and Identity Deep Dive

Use `id()` to inspect object identity:

```python
scores = [10, 20]
alias = scores
id(scores) == id(alias)  # True

copied = list(scores)
id(copied) == id(scores)  # False
```

This is the core memory transition in this module:
- Before copy: one list object shared by multiple labels.
- After copy: two independent list objects.

Mutation after copy affects only the copied list.

## Complexity

Let `n = len(scores)`.

- `normalize_scores`: Time `O(n)`, Space `O(n)`
- `top_k`: Time `O(n log n)` from sorting, Space `O(n)`
- `build_scoreboard`: dominated by sorting, Time `O(n log n)`, Space `O(n)`

## Example Walkthrough

Input:

```text
scores=[72, 94, 51, 88], bonus=3, k=2
```

Execution:
1. Copy scores: `[72, 94, 51, 88]` (new object)
2. Normalize+clamp: `[75, 97, 54, 91]`
3. Rank desc: `[97, 91, 75, 54]`
4. Top-2 tuple: `(97, 91)`

Output:

```text
([97.0, 91.0, 75.0, 54.0], (97.0, 91.0))
```

## Key Takeaways

1. List mutation is powerful but dangerous under aliasing.
2. Copying is a correctness tool, not just a convenience.
3. Tuples are useful when you want to promise immutability.
4. Identity (`id`) and mutation semantics are central Python skills.
