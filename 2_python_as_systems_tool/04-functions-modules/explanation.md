# Project 04: Functions and Modules - Solution Walkthrough

## Problem Definition

This module teaches how to decompose one task into small, testable functions.

The concrete task is to build a temperature report:
- Input: many readings in one unit (`C` or `F`)
- Output: `(count, min_c, max_c, avg_c)`

Why it matters:
- Real engineering work is mostly composition of small functions.
- Modular decomposition reduces bugs and makes tests precise.
- Unit conversion and aggregation are common in data pipelines.

## Mental Model

Think of the program as an assembly line:

1. `to_celsius` converts one value.
2. `stable_mean` computes one aggregate safely.
3. `build_temperature_report` orchestrates the whole pipeline.

Data flow:

```text
raw readings -> convert each reading -> converted list in C
                                     -> min/max/mean -> final tuple report
```

Execution model:
- Each function has one responsibility.
- The orchestrator calls helpers instead of inlining everything.
- Tests can target each layer independently.

## Step-by-Step Reasoning

1. Validate boundaries first.
- If unit is not `C` or `F`, fail early.
- If input values are non-numeric, fail early.
- If readings are empty, fail early.

2. Normalize representation.
- Convert every reading to Celsius once.
- Keep all downstream logic unit-independent.

3. Compute aggregates on normalized data.
- `count = len(converted)`
- `min`, `max` from converted values
- `average` from `stable_mean`

4. Return one stable contract.
- A fixed tuple shape makes callers predictable.

## Design Decisions and Tradeoffs

Decision: separate conversion and averaging into helpers.
- Why chosen: easier debugging and unit testing.
- Alternative rejected: one giant function with inline logic.
- Tradeoff: more functions to read, but better locality of responsibility.

Decision: use `math.fsum` in `stable_mean`.
- Why chosen: better floating-point summation behavior.
- Alternative rejected: plain `sum`.
- Tradeoff: tiny complexity increase for better numerical robustness.

Decision: reject string input for `readings`.
- Why chosen: strings are iterable but semantically incorrect here.
- Alternative rejected: implicit character-by-character conversion.
- Tradeoff: stricter API, fewer silent bugs.

## Complexity

Let `n` be number of readings.

- Time: `O(n)`
  - one pass to convert
  - one pass equivalent for aggregation operations
- Space: `O(n)`
  - converted Celsius list

## Example Walkthrough

Input:

```text
readings = [32, 68, 212], unit = "F"
```

Execution:

1. Convert each value:
- `32F -> 0C`
- `68F -> 20C`
- `212F -> 100C`

2. Converted list becomes `[0.0, 20.0, 100.0]`.

3. Aggregates:
- count = 3
- min = 0.0
- max = 100.0
- avg = 40.0

Output:

```text
(3, 0.0, 100.0, 40.0)
```

## Key Takeaways

1. Start with a clear contract for each function.
2. Normalize representations early so downstream logic stays simple.
3. Helper functions make both reasoning and testing easier.
4. Module-level design is mostly about boundaries and explicit contracts.
