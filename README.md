# Python-EDU-1: CS50-Style Learning Tracks

This repository is a teaching-first curriculum. You are expected to read, implement, test, and then compare against reference solutions.

## Tracks

1. `1_data_structures_algorithms`
- Focus: recursion, searching, sorting, linked structures, trees, graphs, dynamic programming.
- Goal: reason about correctness, runtime, memory, and data layout.

2. `2_python_as_systems_tool`
- Focus: Python as an engineering language, not only syntax.
- Goal: understand execution, references, mutation, modularity, OOP, decorators, and production-style tooling patterns.

3. `3_ai_from_first_principles`
- Focus: NumPy and ML systems from fundamentals through modern LLM topics.
- Goal: build model intuition from math and execution, not black-box API usage.

## Prerequisites

- Comfortable with basic arithmetic and high-school algebra.
- Able to run Python and `pytest` from terminal.
- Recommended: Python 3.11+ and a virtual environment.

## Dependencies & Phased Learning

This curriculum is designed in phases to introduce dependencies gradually.

*   **Phase 1: Pure Python**
    *   **Tracks:** `1_data_structures_algorithms` and the beginning of `2_python_as_systems_tool`.
    *   **Dependencies:** None. These projects use only the Python standard library, allowing you to focus on core computer science and language fundamentals without external tools.

*   **Phase 2: External Libraries**
    *   **Tracks:** Later projects in `2_python_as_systems_tool` and all of `3_ai_from_first_principles`.
    *   **Dependencies:** These tracks introduce powerful libraries for data analysis, web development, and machine learning (e.g., `pandas`, `flask`, `numpy`, `torch`).

To install all required packages for all tracks, run:
```bash
pip install -r requirements.txt
```

## Suggested Order

1. Start with `2_python_as_systems_tool/01-basic-python-syntax`.
2. Alternate between Python systems work and DSA:
- Example: Python 01-03, then DSA 01-03, then continue.
3. Start `3_ai_from_first_principles` after you are comfortable with:
- Functions and loops
- Lists/dictionaries
- Basic recursion

A practical sequence is:
1. `2_python_as_systems_tool/01` to `09`
2. `1_data_structures_algorithms/01` to `08`
3. Continue deeper modules in both tracks
4. Begin `3_ai_from_first_principles`

## How To Use One Module End-to-End

Each module typically contains:

- `exercise.py`
- Your working file. Implement the TODOs.

- `solution.py`
- Reference implementation. Read only after attempting the exercise.

- `explanation.md`
- Teaching walkthrough: problem, mental model, step-by-step reasoning, design choices, tradeoffs.

- `test_solution.py` (or `test/` folder in some modules)
- Validation layer. Confirms behavior, edge cases, and invariants.

Recommended workflow:
1. Read `explanation.md` first (understand model and execution flow).
2. Implement `exercise.py` without peeking at `solution.py`.
3. Run tests.
4. Compare your code to `solution.py`.
5. Re-read `explanation.md` and explain back the memory/execution model in your own words.

## Running Tests

From repository root:

```bash
pytest -v
```

For a single module:

```bash
pytest -v 2_python_as_systems_tool/05-lists-tuples/test_solution.py
```

## Teaching Standard

Material in this repository should explain:
- what problem is being solved,
- how data moves through memory,
- why each design decision was chosen,
- and how tests enforce invariants.

If a module skips those, treat it as incomplete and remediate before moving on.
