# Project 11: Numerical Computing with NumPy

## Overview

This project introduces NumPy—the fundamental package for scientific computing in Python and the foundation of AI/ML libraries like TensorFlow, PyTorch, and scikit-learn. You'll learn efficient array operations, vectorization, broadcasting, and why NumPy is 10-100x faster than pure Python for numerical computations.

## Learning Objectives

- Understand NumPy arrays and their advantages over Python lists
- Master vectorization and eliminate slow Python loops
- Learn broadcasting for efficient array operations
- Perform matrix operations essential for ML algorithms
- Compute statistical operations for data analysis
- Recognize when and why to use NumPy in AI/ML

## Why NumPy for AI/ML?

**Speed**: NumPy operations are implemented in C and executed at near-native speed
- Pure Python loops: **~100ms** for 1M operations
- NumPy vectorized: **~1ms** for the same operations (100x faster!)

**Memory**: NumPy arrays use contiguous memory blocks
- Python list of 1M integers: **~28MB**
- NumPy array of 1M integers: **~4MB** (7x less memory!)

**Foundation**: All major AI/ML libraries build on NumPy
- TensorFlow/PyTorch tensors are based on NumPy arrays
- scikit-learn expects NumPy arrays as input
- Pandas DataFrames are built on NumPy

## Problems

Implement the following functions in `solution/solution.py`:

### Problem 1: Array Creation and Properties (Easy)
```python
def create_arrays() -> dict:
    """
    Demonstrate different ways to create NumPy arrays.

    Returns:
        Dictionary with various array creation examples

    Examples of what to create:
    - Array from list: [1, 2, 3, 4, 5]
    - Zeros array: shape (3, 4)
    - Ones array: shape (2, 3)
    - Range array: 0 to 9
    - Linspace: 0 to 1 with 5 points
    - Random array: shape (3, 3) with values [0, 1)
    - Identity matrix: 4x4

    Time Complexity: O(n) where n is total elements
    Space Complexity: O(n)
    """
```

### Problem 2: Vectorization vs Loops (Medium)
```python
def compare_vectorization(n: int = 1000000) -> dict:
    """
    Compare performance: vectorized operations vs Python loops.

    Demonstrate the speed difference between:
    1. Python loop: sum of squares
    2. NumPy vectorized: sum of squares

    Args:
        n: Number of elements (default 1M)

    Returns:
        Dict with timing results and speedup factor

    Time Complexity:
        - Python loop: O(n)
        - NumPy vectorized: O(n) but 50-100x faster
    Space Complexity: O(n)
    """
```

**Examples:**
```python
results = compare_vectorization(1000000)
# Returns:
# {
#     'python_time': 0.15,      # seconds
#     'numpy_time': 0.002,      # seconds
#     'speedup': 75.0,          # NumPy is 75x faster
#     'result': 333333833333    # sum of squares
# }
```

### Problem 3: Array Indexing and Slicing (Easy)
```python
def array_operations(arr: np.ndarray) -> dict:
    """
    Demonstrate array indexing, slicing, and fancy indexing.

    Args:
        arr: 2D NumPy array

    Returns:
        Dictionary with slicing examples:
        - 'first_row': First row
        - 'last_column': Last column
        - 'subarray': Center 2x2 subarray (for arrays >= 3x3)
        - 'diagonal': Diagonal elements
        - 'boolean_mask': Elements > mean value
        - 'fancy_index': Elements at specific indices

    Time Complexity: O(k) where k is elements selected
    Space Complexity: O(k)
    """
```

**Examples:**
```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = array_operations(arr)
# Returns:
# {
#     'first_row': array([1, 2, 3]),
#     'last_column': array([3, 6, 9]),
#     'subarray': array([[5, 6], [8, 9]]),
#     'diagonal': array([1, 5, 9]),
#     'boolean_mask': array([6, 7, 8, 9]),  # > mean (5)
#     'fancy_index': array([1, 5, 9])
# }
```

### Problem 4: Broadcasting (Medium)
```python
def demonstrate_broadcasting() -> dict:
    """
    Demonstrate NumPy broadcasting with practical examples.

    Broadcasting allows operations on arrays of different shapes:
    - (3, 3) + (3,) broadcasts (3,) to (3, 3)
    - (4, 1) * (3,) broadcasts to (4, 3)

    Returns:
        Dictionary with broadcasting examples:
        - 'add_row_vector': Add 1D array to each row
        - 'multiply_column': Multiply each column by scalar array
        - 'normalize_columns': Subtract mean from each column
        - 'distance_matrix': Pairwise distances between points

    Time Complexity: O(n*m) for (n,m) result
    Space Complexity: O(n*m)
    """
```

**Examples:**
```python
results = demonstrate_broadcasting()
# Example: Add [1, 2, 3] to each row of 3x3 matrix
# [[1, 1, 1],     [1, 2, 3]     [[2, 3, 4],
#  [1, 1, 1]  +   [1, 2, 3]  =   [2, 3, 4],
#  [1, 1, 1]]     [1, 2, 3]      [2, 3, 4]]
```

### Problem 5: Matrix Operations for ML (Medium)
```python
def matrix_operations_ml(X: np.ndarray, y: np.ndarray) -> dict:
    """
    Perform common matrix operations used in machine learning.

    Operations:
    1. Matrix multiplication (X @ X.T)
    2. Element-wise operations (sigmoid activation)
    3. Dot products (similarity between vectors)
    4. Transpose operations
    5. Matrix inverse (if square and invertible)

    Args:
        X: Feature matrix, shape (n_samples, n_features)
        y: Target vector, shape (n_samples,)

    Returns:
        Dictionary with ML-relevant operations

    Time Complexity:
        - Matrix multiply: O(n^3) for (n,n) @ (n,n)
        - Element-wise: O(n*m)
    Space Complexity: O(n*m) for result matrices
    """
```

**Examples:**
```python
X = np.array([[1, 2], [3, 4], [5, 6]])  # 3 samples, 2 features
y = np.array([1, 0, 1])
results = matrix_operations_ml(X, y)
# Returns:
# {
#     'gram_matrix': X @ X.T,           # (3, 3) similarity matrix
#     'feature_means': mean per feature, # (2,)
#     'normalized_X': X - mean,         # (3, 2) centered data
#     'correlation': correlation matrix  # (2, 2)
# }
```

### Problem 6: Statistical Operations (Easy)
```python
def statistical_analysis(data: np.ndarray) -> dict:
    """
    Compute statistical measures essential for data analysis and ML.

    Args:
        data: NumPy array (1D or 2D)

    Returns:
        Dictionary with statistical measures:
        - 'mean': Mean value(s)
        - 'median': Median value(s)
        - 'std': Standard deviation
        - 'var': Variance
        - 'min': Minimum value
        - 'max': Maximum value
        - 'percentiles': 25th, 50th, 75th percentiles
        - 'correlation': Correlation matrix (if 2D)

    Time Complexity: O(n) for most operations, O(n log n) for median
    Space Complexity: O(1) for single values, O(k) for k-dimensional stats
    """
```

**Examples:**
```python
data = np.array([1, 2, 3, 4, 5, 100])  # Note outlier
stats = statistical_analysis(data)
# Returns:
# {
#     'mean': 19.17,
#     'median': 3.5,      # Robust to outlier
#     'std': 38.95,
#     'percentiles': array([2.25, 3.5, 5.75])
# }
```

### Problem 7: Vectorized Data Preprocessing (Medium)
```python
def preprocess_data(X: np.ndarray) -> dict:
    """
    Vectorized data preprocessing for machine learning.

    Implement common preprocessing steps:
    1. Min-Max normalization: scale to [0, 1]
    2. Standardization: (X - mean) / std (zero mean, unit variance)
    3. Handle missing values (represented as np.nan)
    4. Clip outliers (values beyond 3 standard deviations)

    Args:
        X: Raw data array, shape (n_samples, n_features)

    Returns:
        Dictionary with preprocessed versions:
        - 'normalized': Min-max scaled
        - 'standardized': Z-score normalized
        - 'clipped': Outliers clipped
        - 'filled': NaN values filled with column mean

    Time Complexity: O(n*m) for (n,m) array
    Space Complexity: O(n*m) for new arrays
    """
```

**Examples:**
```python
X = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 100.0]])  # Last value is outlier
processed = preprocess_data(X)
# Returns:
# {
#     'normalized': [[0.0, 0.0], [0.5, 0.02], [1.0, 1.0]],
#     'standardized': [[-1.22, -0.67], [0.0, -0.64], [1.22, 1.31]],
#     'clipped': [[1.0, 2.0], [3.0, 4.0], [5.0, 4.0]]  # Outlier clipped
# }
```

### Problem 8: Linear Algebra for ML (Hard)
```python
def linear_regression_numpy(X: np.ndarray, y: np.ndarray) -> dict:
    """
    Implement linear regression using NumPy (closed-form solution).

    Formula: θ = (X^T X)^(-1) X^T y
    This is the Normal Equation for linear regression.

    Args:
        X: Feature matrix, shape (n_samples, n_features)
        y: Target vector, shape (n_samples,)

    Returns:
        Dictionary with:
        - 'weights': Learned weights θ
        - 'predictions': y_pred = X @ θ
        - 'mse': Mean squared error
        - 'r2_score': R² coefficient of determination

    Time Complexity: O(n*m^2 + m^3) where n=samples, m=features
        - X^T X: O(n*m^2)
        - Matrix inverse: O(m^3)
    Space Complexity: O(n*m)
    """
```

**Examples:**
```python
# Simple 1D linear regression: y = 2x + 1
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 5, 7, 9, 11])
results = linear_regression_numpy(X, y)
# Returns:
# {
#     'weights': array([2.0, 1.0]),  # slope=2, intercept=1
#     'mse': 0.0,                     # Perfect fit
#     'r2_score': 1.0                 # Perfect correlation
# }
```

## Performance Comparison: NumPy vs Pure Python

```python
# Example: Sum of 1 million numbers
import numpy as np
import time

# Pure Python
start = time.time()
python_list = list(range(1_000_000))
result = sum([x**2 for x in python_list])
python_time = time.time() - start
# Time: ~0.15 seconds

# NumPy
start = time.time()
numpy_array = np.arange(1_000_000)
result = np.sum(numpy_array**2)
numpy_time = time.time() - start
# Time: ~0.002 seconds

# Speedup: 75x faster! 🚀
```

## Key NumPy Concepts

### 1. Vectorization
**Bad (Python loop):**
```python
result = []
for i in range(len(a)):
    result.append(a[i] + b[i])
```

**Good (NumPy vectorized):**
```python
result = a + b  # 100x faster!
```

### 2. Broadcasting
```python
# Add scalar to array
arr + 5  # Broadcasts 5 to all elements

# Add 1D array to 2D array
matrix + row_vector  # Broadcasts row_vector to each row
```

### 3. Memory Efficiency
```python
# Python list: Each element is a Python object (28 bytes)
python_list = [1, 2, 3, 4, 5]  # ~140 bytes

# NumPy array: Contiguous block of same-type values
numpy_array = np.array([1, 2, 3, 4, 5])  # ~20 bytes + overhead
```

## Constraints

- Array sizes: 0 ≤ n ≤ 10,000,000 (10 million elements)
- Data types: Focus on `float64` and `int64`
- For matrix operations: Assume well-conditioned matrices

## Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=solution --cov-report=term-missing

# Run performance tests
pytest tests/ -v -k performance
```

## Tips

1. **Think in Arrays**: Replace loops with array operations
2. **Broadcasting**: Learn the broadcasting rules to avoid explicit loops
3. **Memory Views**: Use views (slicing) instead of copies when possible
4. **Profiling**: Use `%timeit` in Jupyter to measure performance
5. **Documentation**: NumPy docs are excellent—use them!

## Real-World Applications

### Machine Learning
- **Feature matrices**: Store datasets as NumPy arrays
- **Matrix multiplication**: Core operation in neural networks
- **Gradient descent**: Vectorized weight updates

### Data Science
- **Statistical analysis**: Fast computation of means, stds, correlations
- **Data cleaning**: Vectorized preprocessing pipelines
- **Feature engineering**: Create new features from existing ones

### Scientific Computing
- **Simulations**: Physics, chemistry, biology simulations
- **Signal processing**: Audio/image processing
- **Numerical methods**: Solving differential equations

## Common Pitfalls

1. **Copying vs Views**: Understand when NumPy returns a view vs a copy
2. **Data Types**: Be aware of integer overflow and float precision
3. **Memory**: Large arrays can consume lots of RAM
4. **Loop Habits**: Resist the urge to use Python loops—vectorize!

## Next Steps

After completing this project, you'll be ready for:
- **Project 12**: Data Manipulation with Pandas
- **Project 13**: Data Visualization with Matplotlib
- **Project 20**: Neural Networks from Scratch

## Resources

- [NumPy Official Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy for MATLAB Users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)
- [From Python to NumPy](https://www.labri.fr/perso/nrougier/from-python-to-numpy/)
