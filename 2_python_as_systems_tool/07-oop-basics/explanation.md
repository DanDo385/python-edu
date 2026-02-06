# Project 07: OOP Basics - Solution Walkthrough

## Problem Definition

This module teaches object-oriented basics through a Todo domain:
- `Task`: one object with local state (`title`, `done`)
- `TodoList`: one object that manages many `Task` objects

Why it matters:
- OOP is mostly about modeling stateful objects and their interactions.
- Most bugs in OOP beginner code come from misunderstanding shared references.

## Mental Model

`Task` objects live in memory. Variables store references to those objects.

```text
task_ref -----> Task(title="Read", done=False)
alias    -----> same Task object
```

If `alias.mark_done()` runs, `task_ref.done` also becomes `True` because both names point to one object.

`TodoList` is composition:

```text
TodoList.tasks -----> [Task(...), Task(...), ...]
```

The list stores references to Task objects, not copies.

## Step-by-Step Reasoning

1. Define `Task` boundary.
- Validate title at construction.
- Store canonical title and initial state.
- Expose one mutator: `mark_done`.

2. Define `TodoList` boundary.
- Keep an internal list of `Task` references.
- `add_task` constructs and stores new Task.
- `complete_task` mutates first unfinished match.

3. Query behavior.
- `pending_titles` projects unfinished tasks.
- `completion_ratio` summarizes done fraction.

4. Handle edge conventions.
- Empty list ratio is `0.0` to avoid divide-by-zero and keep predictable API.

## Design Decisions and Tradeoffs

Decision: `TodoList` creates `Task` inside `add_task`.
- Why chosen: one place enforces title validation and object creation.
- Alternative rejected: accept arbitrary dicts or strings everywhere.
- Tradeoff: tighter coupling, simpler invariants.

Decision: mark only first unfinished title match.
- Why chosen: deterministic behavior when duplicate titles exist.
- Alternative rejected: mark all matches automatically.
- Tradeoff: callers may need repeated calls for duplicates.

Decision: expose tasks via methods, not direct external mutation APIs.
- Why chosen: keeps invariants local.
- Tradeoff: slightly more method code.

## Indirection, Identity, and Aliasing

Identity check:

```python
todo = TodoList()
a = todo.add_task("Read")
b = a
id(a) == id(b)  # True
```

After `b.mark_done()`, `a.done` is also `True`.

This is the same reference model taught in module 01, now applied to user-defined objects.

Before mutation:

```text
a ------> Task(done=False)
b ------> same Task(done=False)
```

After `b.mark_done()`:

```text
a ------> Task(done=True)
b ------> same Task(done=True)
```

No reassignment happened; the object itself changed.

## Complexity

Let `n` be task count.

- `add_task`: `O(1)`
- `complete_task`: `O(n)` worst case scan
- `pending_titles`: `O(n)`
- `completion_ratio`: `O(n)`
- Space: `O(n)` for stored tasks

## Example Walkthrough

Input actions:

```text
add("Read")
add("Write")
complete("Read")
```

Execution:
1. Two Task objects created and appended.
2. `complete("Read")` finds first unfinished `"Read"` and marks done.
3. `pending_titles()` returns `['Write']`.
4. `completion_ratio()` returns `1 / 2 = 0.5`.

## Key Takeaways

1. Class instances are mutable reference objects.
2. Multiple names can alias the same instance.
3. Composition (`TodoList` owns `Task`) is foundational OOP.
4. Object boundaries and invariants matter more than syntax.
