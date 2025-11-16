#!/usr/bin/env python3
"""
Scaffold generator for Python-50x-Minis
Creates directory structure for all 50 projects
"""

import os
from pathlib import Path

# Project definitions (num, name, description, phase)
PROJECTS = [
    # Phase I - Python & DSA (01-15)
    (1, "basic-python-syntax", "Variables, types, I/O, arithmetic", 1),
    (2, "control-flow-loops", "Conditionals, loops, FizzBuzz", 1),
    (3, "functions-modules", "Functions, scope, imports, docstrings", 1),
    (4, "lists-tuples", "Sequences, slicing, comprehensions", 1),
    (5, "dictionaries-sets", "Hash maps, sets, frequency counting", 1),
    (6, "oop-basics", "Classes, objects, methods, encapsulation", 1),
    (7, "oop-advanced", "Inheritance, polymorphism, exceptions", 1),
    (8, "recursion-divide-conquer", "Factorial, Fibonacci, GCD, binary search", 1),
    (9, "searching-algorithms", "Linear search, binary search, O(log n)", 1),
    (10, "sorting-algorithms", "Insertion sort, merge sort, quicksort", 1),
    (11, "stack-queue", "LIFO/FIFO, balanced parentheses, BFS", 1),
    (12, "linked-lists", "Nodes, insertion, deletion, reversal", 1),
    (13, "binary-trees", "Tree traversals, BST, height", 1),
    (14, "graphs-traversal", "DFS, BFS, adjacency lists, paths", 1),
    (15, "dynamic-programming", "Memoization, tabulation, optimization", 1),

    # Phase II - ML Math (16-30)
    (16, "numpy-101", "Arrays, vectorization, broadcasting", 2),
    (17, "numpy-advanced", "Matrix ops, performance, @ operator", 2),
    (18, "linear-algebra-essentials", "Dot products, solving Ax=b, projections", 2),
    (19, "gradient-descent-basics", "1D optimization, learning rate, convergence", 2),
    (20, "linear-regression-scratch", "MSE loss, gradient ∂L/∂w, fitting", 2),
    (21, "logistic-regression", "Sigmoid, cross-entropy, classification", 2),
    (22, "activation-functions", "ReLU, tanh, softmax, derivatives", 2),
    (23, "manual-backpropagation", "Chain rule, gradient flow, 2-layer net", 2),
    (24, "autodiff-engine", "Comp graphs, reverse-mode AD, .backward()", 2),
    (25, "mlp-from-scratch", "MLP, XOR, non-linear separation", 2),
    (26, "model-evaluation", "Train/val/test, metrics, confusion matrix", 2),
    (27, "regularization", "L1/L2, dropout, early stopping", 2),
    (28, "hyperparameter-tuning", "Grid search, LR schedules, validation", 2),
    (29, "batch-gradient-descent", "SGD vs batch vs mini-batch, momentum", 2),
    (30, "mnist-numpy-capstone", "MNIST classifier in pure NumPy", 2),

    # Phase III - PyTorch (31-40)
    (31, "pytorch-tensors-gpu", "torch.Tensor, GPU, device management", 3),
    (32, "pytorch-autograd", "requires_grad, .backward(), .grad", 3),
    (33, "pytorch-modules", "nn.Module, custom layers, forward()", 3),
    (34, "pytorch-mnist-training", "DataLoader, training loop, checkpoints", 3),
    (35, "cnn-cifar10", "Conv layers, pooling, CIFAR-10", 3),
    (36, "embeddings-text-classification", "nn.Embedding, LSTM, IMDB sentiment", 3),
    (37, "advanced-training", "Adam, LR schedulers, gradient clipping", 3),
    (38, "transfer-learning", "Pretrained ResNet, fine-tuning, freezing", 3),
    (39, "char-rnn-shakespeare", "Char-level LM, text generation", 3),
    (40, "seq2seq-attention", "Encoder-decoder, attention, translation", 3),

    # Phase IV - Transformers & LLMs (41-50)
    (41, "scaled-dot-product-attention", "Q/K/V, softmax, masking", 4),
    (42, "transformer-blocks", "Multi-head attention, FFN, LayerNorm", 4),
    (43, "gpt-decoder-model", "GPT architecture, causal masking", 4),
    (44, "tokenization-bpe", "BPE, SentencePiece, vocab building", 4),
    (45, "babygpt-training", "Train GPT on WikiText-2, perplexity", 4),
    (46, "llm-inference-decoding", "Greedy, beam search, top-k/top-p", 4),
    (47, "model-quantization", "INT8, compression, speed/memory", 4),
    (48, "llm-serving-api", "FastAPI, batching, deployment", 4),
    (49, "rag-system", "Vector DB, RAG, embeddings, Q&A", 4),
    (50, "llm-system-design", "Architecture, scaling, monitoring", 4),
]

def create_project_structure(num, name, desc, phase):
    """Create directory structure for a single project"""
    # Project directory name
    proj_dir = f"project-{num:02d}-{name}"
    proj_path = Path(proj_dir)

    # Create directories
    proj_path.mkdir(exist_ok=True)
    (proj_path / "solution").mkdir(exist_ok=True)
    (proj_path / "test").mkdir(exist_ok=True)

    # Create README.md
    readme_content = f"""# Project {num:02d}: {name.replace('-', ' ').title()}

> {desc}

---

## What You'll Learn

### Core Concepts
- TODO: List key concepts
- TODO: Technical skills
- TODO: Practical applications

### Prerequisites
- Completion of prior projects (01-{num-1:02d})
- TODO: Specific background knowledge

---

## Why This Matters

### Real-World Applications
TODO: Where is this used in production systems?

### Connections to Future Projects
TODO: How does this enable later projects?

---

## When to Use This

### Problem Indicators
TODO: Signs this technique applies

### Anti-Patterns
TODO: When NOT to use this approach

---

## Pitfalls & Gotchas

### Common Mistakes
1. TODO: Typical beginner errors
2. TODO: Edge cases to watch for
3. TODO: Performance traps

### Debugging Tips
TODO: How to troubleshoot issues

---

## Performance Considerations

### Time Complexity
TODO: Big-O analysis

### Space Complexity
TODO: Memory usage

### Optimization Strategies
TODO: Performance improvements

---

## Step-by-Step Walkthrough

### Approach 1: Naive Solution
TODO: Brute force approach with complexity

### Approach 2: Optimized Solution
TODO: Improved algorithm

### Implementation Details
TODO: Key implementation choices

---

## How to Run

### Setup
```bash
cd project-{num:02d}-{name}
```

### Running the Exercise
```bash
python exercise.py
```

### Running Tests
```bash
pytest test/test_project_{num:02d}.py -v
```

### Expected Output
```
TODO: Sample test output
```

---

## Cross-Language Comparison

### Python
```python
# TODO: Python implementation snippet
```

### Rust
```rust
// TODO: Equivalent Rust code
```

### C
```c
// TODO: Equivalent C code
```

### JavaScript
```javascript
// TODO: Equivalent JS code
```

---

## Advanced Challenges

1. **Challenge 1**: TODO
2. **Challenge 2**: TODO
3. **Challenge 3**: TODO

---

## References

- [DSA Primer](../../DSA_PRIMER.md)
- [Python Basics](../../PYTHON_BASICS.md)
- TODO: Specific resources

---

## Related Projects

- [Project {max(1,num-1):02d}](../project-{max(1,num-1):02d}-*/): Previous project
- [Project {min(50,num+1):02d}](../project-{min(50,num+1):02d}-*/): Next project

---

Last updated: 2025-11-16
"""
    (proj_path / "README.md").write_text(readme_content)

    # Create exercise.py
    exercise_content = f'''"""
Project {num:02d}: {name.replace('-', ' ').title()}

Exercise file with TODOs and partial implementation.

Learning objectives:
- TODO: List objectives

Author: Python-50x-Minis
"""

from typing import List, Optional, Any


# =============================================================================
# THINK BEFORE CODING
# =============================================================================
# 1. What is the problem asking?
# 2. What are the inputs and outputs?
# 3. What are the edge cases?
# 4. What is the brute force approach?
# 5. How can we optimize?


# =============================================================================
# EXERCISE FUNCTIONS
# =============================================================================

def main_function(arg1: Any, arg2: Optional[Any] = None) -> Any:
    """
    TODO: Main function description.

    Args:
        arg1: TODO description
        arg2: TODO description

    Returns:
        TODO: Return value description

    Raises:
        ValueError: TODO: When does this raise?

    Examples:
        >>> main_function(example_input)
        expected_output

    Time Complexity: TODO: O(?)
    Space Complexity: TODO: O(?)
    """
    # TODO: Implement this function
    pass


# =============================================================================
# HELPER FUNCTIONS (if needed)
# =============================================================================

def helper_function(arg: Any) -> Any:
    """
    TODO: Helper function description.
    """
    # TODO: Implement
    pass


# =============================================================================
# MAIN (for testing)
# =============================================================================

if __name__ == "__main__":
    # TODO: Add example usage
    print(f"Project {num:02d}: {name.replace('-', ' ').title()}")

    # Example test case
    # result = main_function(test_input)
    # print(f"Result: {{result}}")
'''
    (proj_path / "exercise.py").write_text(exercise_content)

    # Create solution/solution.py
    solution_content = f'''"""
Project {num:02d}: {name.replace('-', ' ').title()} - SOLUTION

Full implementation with detailed inline comments.

This solution demonstrates:
- TODO: Key techniques
- TODO: Optimization strategies
- TODO: Best practices

Author: Python-50x-Minis
Date: 2025-11-16
"""

from typing import List, Optional, Any


# =============================================================================
# SOLUTION IMPLEMENTATION
# =============================================================================

def main_function(arg1: Any, arg2: Optional[Any] = None) -> Any:
    """
    TODO: Complete function description with mathematical notation if needed.

    Algorithm:
    ----------
    1. TODO: Step 1
    2. TODO: Step 2
    3. TODO: Step 3

    Args:
        arg1: TODO detailed description with types and constraints
        arg2: TODO optional parameter explanation

    Returns:
        TODO: Precise description of return value

    Raises:
        ValueError: TODO specific error conditions
        TypeError: TODO type-related errors

    Examples:
        >>> main_function([1, 2, 3])
        6

        >>> main_function([], default=0)
        0

    Time Complexity:
        TODO: O(?) - detailed breakdown

    Space Complexity:
        TODO: O(?) - memory usage analysis

    Notes:
        TODO: Implementation notes, numerical stability, edge cases
    """
    # TODO: Full implementation with line-by-line comments

    # Input validation
    if not arg1:
        raise ValueError("arg1 cannot be empty")

    # Main algorithm
    result = None  # TODO: implement

    return result


# =============================================================================
# ALTERNATIVE IMPLEMENTATIONS
# =============================================================================

def alternative_approach(arg: Any) -> Any:
    """
    Alternative solution demonstrating different trade-offs.

    This version prioritizes:
    - TODO: What this optimizes for (readability, speed, memory)

    Trade-offs:
    - TODO: What we gain
    - TODO: What we sacrifice
    """
    # TODO: Alternative implementation
    pass


# =============================================================================
# USAGE EXAMPLES
# =============================================================================

if __name__ == "__main__":
    # Example 1: Basic usage
    print("Example 1:")
    # TODO: demonstrate usage

    # Example 2: Edge case
    print("Example 2:")
    # TODO: demonstrate edge case

    # Example 3: Complex scenario
    print("Example 3:")
    # TODO: demonstrate complex usage
'''
    (proj_path / "solution" / "solution.py").write_text(solution_content)

    # Create test/test_project_NN.py
    test_content = f'''"""
Tests for Project {num:02d}: {name.replace('-', ' ').title()}

Test categories:
- Positive tests: Happy path, expected behavior
- Edge cases: Boundary conditions, empty inputs, None handling
- Error cases: Invalid inputs, type errors
- Performance: Basic benchmarks (where relevant)

Author: Python-50x-Minis
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import from both exercise and solution for comparison
try:
    from exercise import main_function as exercise_fn
except ImportError:
    exercise_fn = None

try:
    from solution.solution import main_function as solution_fn
except ImportError:
    solution_fn = None


# =============================================================================
# POSITIVE TESTS
# =============================================================================

class TestPositiveCases:
    """Test normal, expected behavior."""

    def test_basic_functionality(self):
        """Test basic happy path."""
        # TODO: implement test
        assert True  # placeholder

    def test_typical_input(self):
        """Test with typical inputs."""
        # TODO: implement test
        assert True  # placeholder


# =============================================================================
# EDGE CASES
# =============================================================================

class TestEdgeCases:
    """Test boundary conditions and edge cases."""

    def test_empty_input(self):
        """Test with empty input."""
        # TODO: implement test
        assert True  # placeholder

    def test_single_element(self):
        """Test with single element."""
        # TODO: implement test
        assert True  # placeholder

    def test_large_input(self):
        """Test with large input."""
        # TODO: implement test
        assert True  # placeholder


# =============================================================================
# ERROR CASES
# =============================================================================

class TestErrorHandling:
    """Test error conditions and exception handling."""

    def test_invalid_input_type(self):
        """Test with wrong input type."""
        # TODO: implement test (should raise TypeError)
        assert True  # placeholder

    def test_invalid_input_value(self):
        """Test with invalid value."""
        # TODO: implement test (should raise ValueError)
        assert True  # placeholder


# =============================================================================
# PROPERTY-BASED TESTS (optional, using Hypothesis)
# =============================================================================

try:
    from hypothesis import given, strategies as st

    class TestProperties:
        """Property-based tests for invariants."""

        @given(st.integers())
        def test_property_example(self, value):
            """Test that certain property always holds."""
            # TODO: implement property test
            assert True  # placeholder

except ImportError:
    # Hypothesis not installed, skip property tests
    pass


# =============================================================================
# PERFORMANCE TESTS (optional)
# =============================================================================

class TestPerformance:
    """Basic performance benchmarks."""

    @pytest.mark.slow
    def test_performance_small_input(self, benchmark):
        """Benchmark with small input."""
        # TODO: implement benchmark
        # Usage: benchmark(function, arg1, arg2)
        pass

    @pytest.mark.slow
    def test_performance_large_input(self, benchmark):
        """Benchmark with large input."""
        # TODO: implement benchmark
        pass


# =============================================================================
# COMPARISON TESTS (exercise vs solution)
# =============================================================================

class TestExerciseSolutionEquivalence:
    """Compare exercise and solution implementations."""

    @pytest.mark.skipif(exercise_fn is None or solution_fn is None,
                        reason="Exercise or solution not implemented")
    def test_same_output(self):
        """Test that exercise and solution produce same output."""
        # TODO: implement comparison test
        test_input = None  # TODO: define test input
        # assert exercise_fn(test_input) == solution_fn(test_input)
        assert True  # placeholder


# =============================================================================
# FIXTURES (if needed)
# =============================================================================

@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {{
        # TODO: define sample data
    }}


@pytest.fixture
def large_data():
    """Provide large dataset for performance tests."""
    # TODO: generate large test data
    return None


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def assert_close(a, b, tol=1e-9):
    """Assert two numbers are close (for floating-point comparisons)."""
    assert abs(a - b) < tol, f"{{a}} and {{b}} differ by more than {{tol}}"
'''
    (proj_path / "test" / f"test_project_{num:02d}.py").write_text(test_content)

    # Create solution_in_words.md
    solution_in_words = f"""# Project {num:02d}: {name.replace('-', ' ').title()} - Solution Walkthrough

> A human-readable explanation of the solution approach

---

## Problem Statement

TODO: Restate the problem in plain English

---

## Intuition

TODO: The "aha!" moment - what's the key insight?

---

## Approach

### Visual Representation
```
TODO: ASCII diagram showing the algorithm

Example:
┌─────┐    ┌─────┐    ┌─────┐
│  1  │ -> │  2  │ -> │  3  │
└─────┘    └─────┘    └─────┘
```

### Step-by-Step

1. **Step 1**: TODO
   - Why: TODO
   - Pseudocode: TODO

2. **Step 2**: TODO
   - Why: TODO
   - Pseudocode: TODO

3. **Step 3**: TODO
   - Why: TODO
   - Pseudocode: TODO

---

## Complexity Analysis

### Time Complexity: O(?)
**Breakdown**:
- Step 1: O(?)
- Step 2: O(?)
- Total: O(?)

**Why**:
TODO: Explain the dominant term

### Space Complexity: O(?)
**Breakdown**:
- Data structure 1: O(?)
- Data structure 2: O(?)
- Total: O(?)

---

## Example Walkthrough

### Input
```
TODO: Specific example input
```

### Execution Trace
```
TODO: Step-by-step execution with values

Iteration 1:
  - State: TODO
  - Action: TODO
  - Result: TODO

Iteration 2:
  - State: TODO
  - Action: TODO
  - Result: TODO
```

### Output
```
TODO: Final output for the example
```

---

## Edge Cases Handled

1. **Empty input**: TODO how we handle it
2. **Single element**: TODO how we handle it
3. **All same elements**: TODO how we handle it
4. **Negative values**: TODO how we handle it

---

## Alternative Approaches

### Approach 2: [Name]
**Idea**: TODO
**Complexity**: Time O(?), Space O(?)
**Trade-off**: TODO (why not this one?)

### Approach 3: [Name]
**Idea**: TODO
**Complexity**: Time O(?), Space O(?)
**Trade-off**: TODO

---

## Key Takeaways

1. TODO: Main lesson learned
2. TODO: Pattern that reappears
3. TODO: Common pitfall avoided

---

## Further Reading

- TODO: Related algorithms or concepts
- TODO: Papers or articles

---

Last updated: 2025-11-16
"""
    (proj_path / "solution_in_words.md").write_text(solution_in_words)

    # Create notebook.ipynb (for Phase II+)
    if phase >= 2:
        notebook_content = '''{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Project ''' + f'{num:02d}' + ''': ''' + name.replace('-', ' ').title() + '''\\n",
    "\\n",
    "> ''' + desc + '''\\n",
    "\\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Setup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Imports\\n",
    "import numpy as np\\n",
    "import matplotlib.pyplot as plt\\n",
    "\\n",
    "# Visualization settings\\n",
    "plt.style.use('seaborn-v0_8')\\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## TODO: Section 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# TODO: Add code"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Visualization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# TODO: Add visualization code"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercises\\n",
    "\\n",
    "1. TODO\\n",
    "2. TODO"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
'''
        (proj_path / "notebook.ipynb").write_text(notebook_content)

    print(f"Created: {proj_dir}")

def main():
    """Generate all project scaffolds"""
    print("=" * 80)
    print("Python-50x-Minis Scaffold Generator")
    print("=" * 80)
    print()

    for num, name, desc, phase in PROJECTS:
        create_project_structure(num, name, desc, phase)

    print()
    print("=" * 80)
    print(f"Successfully created {len(PROJECTS)} project scaffolds!")
    print("=" * 80)

if __name__ == "__main__":
    main()
