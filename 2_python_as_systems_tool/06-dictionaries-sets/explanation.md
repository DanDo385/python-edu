# Project 06: Dictionaries and Sets - Solution Walkthrough

## Problem Definition

This module teaches when to use:
- `dict` for key -> value association (frequency counting)
- `set` for uniqueness and fast membership checks

The exercise analyzes words and returns:
- frequency map (`counts`)
- unique terms (`unique_words`)
- repeated terms (`repeated_words`)

Why it matters:
- Most backend/data tasks are map-and-filter pipelines.
- Correct normalization and membership logic prevents subtle data bugs.

## Mental Model

Dictionary mental model:

```text
counts = {
  "data": 2,
  "python": 1,
}
```

Set mental model:

```text
unique_words   = {"data", "python"}
repeated_words = {"data"}
```

Both dict and set are mutable reference objects in Python.
If two names point to the same dict/set, mutation through one name is visible through the other.

```python
a = {"x": 1}
b = a
b["y"] = 2
# a is now {"x": 1, "y": 2}
```

This connects directly to module 01: variables hold references, not copies.

## Step-by-Step Reasoning

1. Normalize vocabulary first.
- Remove punctuation and lowercase each token.
- Normalize `stop_words` with the same rule.
- Reason: without shared normalization, filtering and counting disagree.

2. Filter invalid or ignorable tokens.
- Skip empty normalized tokens.
- Skip words in stop-word set.

3. Count with dict updates.
- `counts[word] = counts.get(word, 0) + 1`

4. Derive set views from dict.
- `unique_words = set(counts.keys())`
- `repeated_words = {w for w, c in counts.items() if c > 1}`

## Design Decisions and Tradeoffs

Decision: explicit normalization function.
- Why chosen: single source of truth for token cleaning.
- Alternative rejected: inline normalization in multiple places.
- Tradeoff: one extra function, much less duplication.

Decision: use set for stop words.
- Why chosen: average `O(1)` membership checks.
- Alternative rejected: list-based membership (`O(n)`).
- Tradeoff: set has no ordering, which is fine for filtering.

Decision: strict type checks.
- Why chosen: fail fast at module boundary for teaching clarity.
- Alternative rejected: permissive coercion.
- Tradeoff: slightly stricter API, easier debugging.

## Indirection and Memory Model

Before counting:

```text
counts ------> {}
```

During counting of "data":

```text
counts ------> {"data": 1}
```

After second "data":

```text
counts ------> {"data": 2}
```

No new `counts` dict is created each update; the same dict object is mutated.
That is why aliases see changes:

```python
counts = {}
alias = counts
counts["a"] = 1
# alias also sees {"a": 1}
```

Using `id(counts)` before and after updates shows identity stays constant.

## Complexity

Let `n` = number of input words, `u` = number of unique normalized words.

- Time: `O(n)` average
  - normalization and filtering per token
  - dict/set updates are average `O(1)`
- Space: `O(u)`
  - dictionary keys and derived sets

## Example Walkthrough

Input:

```text
words = ["Data", "science", "data", "Python!"]
stop_words = ["science"]
```

Execution:
1. Normalize stop words -> `{ "science" }`
2. Normalize/scan words:
- `"Data" -> "data"` count becomes 1
- `"science" -> "science"` skipped (stop word)
- `"data" -> "data"` count becomes 2
- `"Python!" -> "python"` count becomes 1

Output:

```text
counts: {"data": 2, "python": 1}
unique_words: {"data", "python"}
repeated_words: {"data"}
```

## Key Takeaways

1. Dicts answer "how many" and "what value" questions.
2. Sets answer "is this present" and "what is unique" questions.
3. Normalization must be consistent across all branches.
4. Dict/set mutation follows shared-reference semantics from module 01.
