# Project 09: Decorators and Metaprogramming - Solution Walkthrough

## Problem Definition

This module teaches how to wrap function behavior without changing function source code.

The exercise implements five decorators:
- `timer`
- `repeat(times)`
- `cache`
- `validate_args(*types)`
- `debug`

Why this matters:
- Cross-cutting concerns (logging, timing, validation, caching) should be reusable.
- Decorators are the standard Python mechanism for that reuse.

## Mental Model

A function in Python is an object. Variables store references to function objects.

```python
def add(a, b):
    return a + b

f = add
```

`f` and `add` reference the same function object.

Decorator syntax:

```python
@decorator
def work():
    ...
```

is equivalent to:

```python
def work():
    ...
work = decorator(work)
```

So decoration is a reassignment of a function reference.

## Step-by-Step Build-Up

### 1) Start with a plain wrapper

Goal: run extra code before/after original function.

```python
def wrapper(*args, **kwargs):
    # before
    result = func(*args, **kwargs)
    # after
    return result
```

This establishes the core pattern: receive callable, return callable.

### 2) Turn wrapper into reusable decorator

`timer(func)` and `debug(func)` both follow:
1. accept function reference
2. define inner wrapper closure
3. return wrapper reference

### 3) Add decorator factory for arguments

`repeat(times)` and `validate_args(*types)` need one extra layer:

1. factory captures config (`times`, `types`)
2. factory returns decorator
3. decorator returns wrapper

This 3-layer structure is required because `@repeat(3)` is a function call that must produce a decorator.

### 4) Add state via closure

`cache` creates `cached_results = {}` in outer scope.
Returned wrapper captures that dictionary reference.
Every call to the wrapper mutates the same dictionary.

## Design Decisions and Tradeoffs

Decision: use closures for state (`cache`) instead of global variables.
- Why chosen: state is local to decorated function instance.
- Alternative rejected: one module-global cache for everything.
- Tradeoff: simpler encapsulation, less global observability.

Decision: preserve metadata with `@wraps`.
- Why chosen: keeps `__name__`, docstring, and introspection behavior.
- Alternative rejected: raw wrappers with lost metadata.
- Tradeoff: minor extra import, better tooling compatibility.

Decision: cache by positional args tuple.
- Why chosen: simple and fast for hashable positional args.
- Alternative rejected: full arg normalization including kwargs.
- Tradeoff: simpler implementation, narrower input support.

## Indirection, References, and Memory

### Function references

Before decoration:

```text
add_name ------> function add
```

After `add = timer(add)`:

```text
add_name ------> wrapper function
wrapper closure ------> original add function
```

The name now points to wrapper, which holds a reference to original.

### Closure state reference (`cache`)

```text
cached_results ------> {}
wrapper closure ------> same dict
```

Each wrapper call mutates that same dict object. Aliasing principle is unchanged from module 01.

Identity checks can make this concrete:

```python
id(cached_results)  # stays constant across calls
```

### Mutation side effects

Because cache dict is shared across calls for one decorated function,
second call with same args returns previous value without recomputation.

## Complexity Notes

- `timer`: overhead `O(1)` plus wrapped call
- `repeat(times)`: `O(times)` wrapped invocations
- `cache`: average `O(1)` lookup/insert for hashable args
- `validate_args`: `O(m)` where `m` is validated argument count
- `debug`: formatting cost proportional to argument representation size

## Example Walkthrough: `cache`

Input:

```python
@cache
def expensive(n):
    return n * n
```

First call `expensive(5)`:
1. wrapper checks key `(5,)` not present
2. calls original function
3. stores result in dict
4. returns 25

Second call `expensive(5)`:
1. wrapper finds `(5,)` in dict
2. returns cached value directly
3. original function is not called

## Key Takeaways

1. Decorators are function reference transformations.
2. `@decorator` is syntactic sugar for reassignment.
3. Closures let wrappers retain state safely.
4. `@wraps` preserves function identity metadata for tooling.
5. Reference and mutation rules from module 01 fully apply to decorators.
