# Project 08: OOP Advanced - Solution Walkthrough

## Problem Definition

This module extends OOP basics into advanced patterns:
- abstract base class (`Shape`)
- inheritance (`Rectangle`, `Circle`)
- polymorphism (`scale_all` calling `shape.scale`)
- container composition (`ShapeCollection`)

Why it matters:
- Real codebases rely on interfaces/contracts and subtype behavior.
- You need predictable extension without rewriting existing callers.

## Mental Model

`Shape` defines behavior contract, not concrete data.
Concrete classes implement the contract with their own state.

```text
Shape (contract)
  ├─ Rectangle(width, height)
  └─ Circle(radius)
```

`ShapeCollection` stores references to `Shape` objects:

```text
ShapeCollection._shapes -> [Rectangle(...), Circle(...)]
```

When `scale_all(2)` runs, each referenced object mutates itself.
Any alias to those objects sees updated dimensions.

## Step-by-Step Reasoning

1. Define contract first.
- `Shape` requires `area`, `perimeter`, `scale`.
- This guarantees shared interface for collection logic.

2. Implement concrete types.
- `Rectangle` keeps `width/height`.
- `Circle` keeps `radius`.
- Each class validates positive numeric dimensions.

3. Build polymorphic container.
- `add` accepts only `Shape` instances.
- `total_area` sums `shape.area()` without branching by type.
- `scale_all` dispatches `shape.scale(factor)` dynamically.

4. Return stable query semantics.
- `largest_shape` returns `None` for empty collection, else max by area.

## Design Decisions and Tradeoffs

Decision: abstract base class vs duck-typing only.
- Why chosen: explicit teaching contract and earlier failure if methods missing.
- Alternative rejected: unconstrained objects with runtime attribute errors.
- Tradeoff: slightly more boilerplate, clearer guarantees.

Decision: in-place `scale`.
- Why chosen: demonstrates mutation and reference sharing.
- Alternative rejected: return new scaled copies.
- Tradeoff: mutable state requires careful alias reasoning.

Decision: shared numeric validator helper.
- Why chosen: consistency and reduced duplication.
- Alternative rejected: repeated ad-hoc checks.
- Tradeoff: one extra helper function.

## Indirection, Identity, and Aliasing

Key memory transition:

```python
rect = Rectangle(2, 3)
alias = rect
collection.add(rect)
collection.scale_all(2)
```

- `rect`, `alias`, and internal collection entry all reference one object.
- `scale_all` calls `Rectangle.scale`, mutating object fields.
- After mutation, all references observe new dimensions.

Check with identity:

```python
id(rect) == id(alias)  # True
```

This is the same reference model from module 01, now under inheritance/polymorphism.

## Complexity

Let `n` be shape count.

- `add`: `O(1)`
- `total_area`: `O(n)`
- `largest_shape`: `O(n)`
- `scale_all`: `O(n)`
- Space: `O(n)` for stored references

## Example Walkthrough

Input operations:

```text
add Rectangle(2, 3)
add Circle(1)
scale_all(2)
```

Execution:
1. Collection stores references to two shape objects.
2. `scale_all(2)` dispatches:
- Rectangle: width=4, height=6
- Circle: radius=2
3. `total_area` now uses scaled dimensions.

Output intuition:
- Rectangle area changed from 6 to 24.
- Circle area changed from pi to 4*pi.

## Key Takeaways

1. Abstract contracts let callers depend on behavior, not concrete classes.
2. Polymorphism removes type-branching from callers.
3. In-place mutation and shared references are powerful but require explicit reasoning.
4. OOP design quality depends on boundaries and invariants, not class count.
