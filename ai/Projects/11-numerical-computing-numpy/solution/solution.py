"""
Project 11: Numerical Computing with NumPy

This module demonstrates NumPy fundamentals for AI/ML:
- Array creation and operations
- Vectorization and performance optimization
- Broadcasting for efficient computations
- Matrix operations for machine learning
- Statistical analysis for data science

Author: Python-Edu AI Curriculum
Time Complexity: Varies by operation (detailed in each function)
Space Complexity: O(n) to O(n^2) depending on operation
"""

import numpy as np
import time
from typing import Dict, Tuple


def create_arrays() -> dict:
    """
    Demonstrate different ways to create NumPy arrays.

    NumPy provides multiple array creation methods:
    1. From Python lists/tuples
    2. Zeros, ones, empty arrays
    3. Range and linspace for sequences
    4. Random arrays for initialization
    5. Identity matrices for linear algebra

    Returns:
        Dictionary with various array creation examples:
        - 'from_list': Array created from Python list
        - 'zeros': Array filled with zeros
        - 'ones': Array filled with ones
        - 'range': Sequential array (like range())
        - 'linspace': Evenly spaced values
        - 'random': Random values in [0, 1)
        - 'identity': Identity matrix (I)

    Time Complexity: O(n) where n is total elements
    Space Complexity: O(n)

    Examples:
        >>> arrays = create_arrays()
        >>> arrays['from_list']
        array([1, 2, 3, 4, 5])
        >>> arrays['zeros'].shape
        (3, 4)
        >>> arrays['identity']
        array([[1., 0., 0., 0.],
               [0., 1., 0., 0.],
               [0., 0., 1., 0.],
               [0., 0., 0., 1.]])
    """
    # Create from Python list
    from_list = np.array([1, 2, 3, 4, 5])

    # Create zeros array: useful for initialization
    zeros = np.zeros((3, 4))  # 3x4 matrix of zeros

    # Create ones array: useful for bias vectors
    ones = np.ones((2, 3))  # 2x3 matrix of ones

    # Create range array: like Python's range()
    range_arr = np.arange(10)  # [0, 1, 2, ..., 9]

    # Create linspace: evenly spaced values
    linspace_arr = np.linspace(0, 1, 5)  # 5 points from 0 to 1

    # Create random array: useful for weight initialization in ML
    np.random.seed(42)  # For reproducibility
    random_arr = np.random.random((3, 3))  # 3x3 random values [0, 1)

    # Create identity matrix: I in linear algebra
    identity = np.eye(4)  # 4x4 identity matrix

    return {
        'from_list': from_list,
        'zeros': zeros,
        'ones': ones,
        'range': range_arr,
        'linspace': linspace_arr,
        'random': random_arr,
        'identity': identity
    }


def compare_vectorization(n: int = 1000000) -> dict:
    """
    Compare performance: vectorized operations vs Python loops.

    This demonstrates why NumPy is essential for AI/ML:
    - Python loops: Interpreted, slow, ~100ms for 1M operations
    - NumPy vectorized: Compiled C code, fast, ~1ms for same operations

    The key insight: **Avoid Python loops, use NumPy operations**

    Algorithm:
    1. Python approach: Loop through list, square each, sum
    2. NumPy approach: arr**2 (vectorized), then sum
    3. Measure timing for both
    4. Calculate speedup factor

    Args:
        n: Number of elements (default 1M for clear demonstration)

    Returns:
        Dict with timing results and speedup:
        - 'python_time': Time for Python loop (seconds)
        - 'numpy_time': Time for NumPy vectorized (seconds)
        - 'speedup': How many times faster NumPy is
        - 'result': Computed sum of squares (for verification)

    Time Complexity:
        - Python loop: O(n) in Python interpreter (SLOW)
        - NumPy vectorized: O(n) in compiled C (FAST)
    Space Complexity: O(n) for array storage

    Examples:
        >>> results = compare_vectorization(1000000)
        >>> results['speedup'] > 50  # NumPy is 50-100x faster
        True
        >>> results['python_time'] > results['numpy_time']
        True
    """
    # Python loop approach (SLOW)
    python_list = list(range(n))
    start_time = time.time()
    python_result = sum([x**2 for x in python_list])
    python_time = time.time() - start_time

    # NumPy vectorized approach (FAST)
    numpy_array = np.arange(n)
    start_time = time.time()
    numpy_result = np.sum(numpy_array**2)  # Vectorized: no loop!
    numpy_time = time.time() - start_time

    # Calculate speedup
    speedup = python_time / numpy_time if numpy_time > 0 else float('inf')

    # Verify both methods give same result
    assert python_result == numpy_result, "Results don't match!"

    return {
        'python_time': round(python_time, 6),
        'numpy_time': round(numpy_time, 6),
        'speedup': round(speedup, 2),
        'result': int(numpy_result)
    }


def array_operations(arr: np.ndarray) -> dict:
    """
    Demonstrate array indexing, slicing, and fancy indexing.

    NumPy provides powerful indexing mechanisms:
    1. Basic indexing: arr[i, j]
    2. Slicing: arr[start:end, :]
    3. Boolean masking: arr[arr > 5]
    4. Fancy indexing: arr[[0, 2, 4]]

    These are essential for:
    - Extracting features from datasets
    - Filtering data based on conditions
    - Selecting specific samples/features

    Args:
        arr: 2D NumPy array

    Returns:
        Dictionary with slicing examples:
        - 'first_row': First row of array
        - 'last_column': Last column of array
        - 'subarray': Center 2x2 subarray (if array >= 3x3)
        - 'diagonal': Diagonal elements
        - 'boolean_mask': Elements > mean value
        - 'fancy_index': Diagonal elements via fancy indexing

    Time Complexity: O(k) where k is elements selected
    Space Complexity: O(k) for new arrays (views are O(1))

    Examples:
        >>> arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> ops = array_operations(arr)
        >>> ops['first_row']
        array([1, 2, 3])
        >>> ops['diagonal']
        array([1, 5, 9])
    """
    # Basic indexing: get first row
    first_row = arr[0, :].copy()  # Copy to avoid view issues

    # Basic indexing: get last column
    last_column = arr[:, -1].copy()

    # Slicing: get center 2x2 subarray (for arrays >= 3x3)
    if arr.shape[0] >= 3 and arr.shape[1] >= 3:
        # Calculate center indices
        row_start = arr.shape[0] // 2 - 1
        col_start = arr.shape[1] // 2 - 1
        subarray = arr[row_start:row_start+2, col_start:col_start+2].copy()
    else:
        subarray = arr.copy()

    # Diagonal elements
    diagonal = np.diag(arr).copy()

    # Boolean masking: elements greater than mean
    mean_val = np.mean(arr)
    boolean_mask = arr[arr > mean_val].copy()

    # Fancy indexing: diagonal elements via indices
    n = min(arr.shape)
    indices = np.arange(n)
    fancy_index = arr[indices, indices].copy()

    return {
        'first_row': first_row,
        'last_column': last_column,
        'subarray': subarray,
        'diagonal': diagonal,
        'boolean_mask': boolean_mask,
        'fancy_index': fancy_index
    }


def demonstrate_broadcasting() -> dict:
    """
    Demonstrate NumPy broadcasting with practical ML examples.

    Broadcasting rules (simplified):
    1. If arrays have different dimensions, pad with 1s on the left
    2. Arrays are compatible if dimensions are equal or one is 1
    3. Result shape is element-wise maximum of input shapes

    Examples:
    - (3, 3) + (3,) → (3, 3) + (1, 3) → (3, 3)
    - (4, 1) * (3,) → (4, 1) * (1, 3) → (4, 3)

    Broadcasting is crucial for:
    - Adding bias vectors to matrices
    - Normalizing features (subtract mean, divide by std)
    - Computing pairwise distances

    Returns:
        Dictionary with broadcasting examples:
        - 'matrix': Original 3x3 matrix
        - 'add_row_vector': Add [1,2,3] to each row
        - 'multiply_column': Multiply columns by [1,2,3]
        - 'normalize_columns': Subtract mean from each column
        - 'distance_matrix': Pairwise Euclidean distances

    Time Complexity: O(n*m) for (n,m) result
    Space Complexity: O(n*m)

    Examples:
        >>> results = demonstrate_broadcasting()
        >>> results['add_row_vector']
        array([[2, 3, 4],
               [2, 3, 4],
               [2, 3, 4]])
    """
    # Create base matrix (3x3)
    matrix = np.ones((3, 3))

    # Example 1: Add row vector to each row
    # (3, 3) + (3,) broadcasts to (3, 3)
    row_vector = np.array([1, 2, 3])
    add_row_vector = matrix + row_vector

    # Example 2: Multiply each column by different value
    # (3, 3) * (3, 1) broadcasts to (3, 3)
    col_vector = np.array([[1], [2], [3]])  # Shape: (3, 1)
    multiply_column = matrix * col_vector

    # Example 3: Normalize columns (subtract column mean)
    # This is common in ML preprocessing
    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]], dtype=float)
    column_means = np.mean(data, axis=0)  # Shape: (3,)
    normalize_columns = data - column_means  # Broadcasting!

    # Example 4: Pairwise distance matrix
    # Compute ||x_i - x_j|| for all pairs of points
    points = np.array([[0, 0], [1, 1], [2, 2]])  # 3 points in 2D
    # Expand dimensions for broadcasting: (3, 1, 2) - (1, 3, 2)
    diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
    distance_matrix = np.sqrt(np.sum(diff**2, axis=2))

    return {
        'matrix': matrix,
        'add_row_vector': add_row_vector,
        'multiply_column': multiply_column,
        'normalize_columns': normalize_columns,
        'distance_matrix': distance_matrix
    }


def matrix_operations_ml(X: np.ndarray, y: np.ndarray) -> dict:
    """
    Perform common matrix operations used in machine learning.

    These operations appear everywhere in ML:
    1. Gram matrix (X @ X.T): Similarity between samples
    2. Covariance matrix: Feature correlations
    3. Feature normalization: Zero mean, unit variance
    4. Dot products: Cosine similarity, neural network activations

    Args:
        X: Feature matrix, shape (n_samples, n_features)
        y: Target vector, shape (n_samples,)

    Returns:
        Dictionary with ML-relevant operations:
        - 'gram_matrix': X @ X.T (sample similarity)
        - 'feature_means': Mean of each feature
        - 'normalized_X': X centered (zero mean)
        - 'covariance': Feature covariance matrix
        - 'correlation': Feature correlation matrix

    Time Complexity:
        - Matrix multiply: O(n^2 * m) for (n,m) @ (m,n)
        - Element-wise ops: O(n*m)
        - Covariance: O(n*m^2)
    Space Complexity: O(max(n^2, m^2)) for result matrices

    Examples:
        >>> X = np.array([[1, 2], [3, 4], [5, 6]])
        >>> y = np.array([1, 0, 1])
        >>> ops = matrix_operations_ml(X, y)
        >>> ops['gram_matrix'].shape
        (3, 3)
        >>> ops['covariance'].shape
        (2, 2)
    """
    n_samples, n_features = X.shape

    # 1. Gram matrix: X @ X.T (n x n)
    # Measures similarity between samples
    gram_matrix = X @ X.T

    # 2. Feature means: average of each column
    feature_means = np.mean(X, axis=0)  # Shape: (n_features,)

    # 3. Normalized X: center the data (zero mean)
    normalized_X = X - feature_means  # Broadcasting!

    # 4. Covariance matrix: measures how features vary together
    # Cov(X) = (X - mean)^T @ (X - mean) / (n - 1)
    covariance = np.cov(X.T)  # Shape: (n_features, n_features)

    # 5. Correlation matrix: normalized covariance
    # Corr = Cov / (std_i * std_j)
    correlation = np.corrcoef(X.T)  # Shape: (n_features, n_features)

    return {
        'gram_matrix': gram_matrix,
        'feature_means': feature_means,
        'normalized_X': normalized_X,
        'covariance': covariance,
        'correlation': correlation
    }


def statistical_analysis(data: np.ndarray) -> dict:
    """
    Compute statistical measures essential for data analysis and ML.

    Statistical analysis is fundamental for:
    - Exploratory Data Analysis (EDA)
    - Feature engineering
    - Outlier detection
    - Model evaluation

    Key statistics:
    - Mean: Average value (sensitive to outliers)
    - Median: Middle value (robust to outliers)
    - Std/Var: Spread of data
    - Percentiles: Distribution quantiles

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
        - 'percentiles': [25th, 50th, 75th] percentiles
        - 'range': Max - Min
        - 'iqr': Interquartile range (Q3 - Q1)

    Time Complexity:
        - Mean, std, var, min, max: O(n)
        - Median, percentiles: O(n log n) due to sorting
    Space Complexity: O(1) for scalars, O(k) for k-dimensional stats

    Examples:
        >>> data = np.array([1, 2, 3, 4, 5, 100])
        >>> stats = statistical_analysis(data)
        >>> stats['median']  # Robust to outlier (100)
        3.5
        >>> stats['mean']  # Affected by outlier
        19.166666666666668
    """
    # Flatten to 1D if needed for overall statistics
    flat_data = data.flatten()

    # Basic statistics
    mean = np.mean(flat_data)
    median = np.median(flat_data)
    std = np.std(flat_data)
    var = np.var(flat_data)
    min_val = np.min(flat_data)
    max_val = np.max(flat_data)

    # Percentiles: [25th, 50th, 75th]
    percentiles = np.percentile(flat_data, [25, 50, 75])

    # Additional useful statistics
    data_range = max_val - min_val
    iqr = percentiles[2] - percentiles[0]  # Interquartile range

    return {
        'mean': float(mean),
        'median': float(median),
        'std': float(std),
        'var': float(var),
        'min': float(min_val),
        'max': float(max_val),
        'percentiles': percentiles,
        'range': float(data_range),
        'iqr': float(iqr)
    }


def preprocess_data(X: np.ndarray) -> dict:
    """
    Vectorized data preprocessing for machine learning.

    Preprocessing is crucial for ML model performance:
    1. Normalization: Scale features to [0, 1]
    2. Standardization: Transform to zero mean, unit variance
    3. Missing values: Fill with mean/median/mode
    4. Outlier clipping: Cap extreme values

    Why preprocess?
    - Many ML algorithms assume normalized features
    - Gradient descent converges faster with standardized data
    - Outliers can dominate model training

    Args:
        X: Raw data array, shape (n_samples, n_features)

    Returns:
        Dictionary with preprocessed versions:
        - 'original': Original data (for comparison)
        - 'normalized': Min-max scaled to [0, 1]
        - 'standardized': Z-score normalized (μ=0, σ=1)
        - 'robust_scaled': Scaled using median and IQR
        - 'clipped': Outliers clipped (3σ from mean)

    Time Complexity: O(n*m) for (n,m) array
    Space Complexity: O(n*m) for each preprocessed array

    Examples:
        >>> X = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 100.0]])
        >>> processed = preprocess_data(X)
        >>> processed['normalized'].max()
        1.0
        >>> processed['normalized'].min()
        0.0
    """
    # Create copy to avoid modifying original
    X = X.astype(float)

    # 1. Min-Max Normalization: scale to [0, 1]
    # Formula: (x - min) / (max - min)
    X_min = np.min(X, axis=0)
    X_max = np.max(X, axis=0)
    # Avoid division by zero
    range_vals = X_max - X_min
    range_vals[range_vals == 0] = 1
    normalized = (X - X_min) / range_vals

    # 2. Standardization: Z-score normalization
    # Formula: (x - mean) / std
    X_mean = np.mean(X, axis=0)
    X_std = np.std(X, axis=0)
    # Avoid division by zero
    X_std[X_std == 0] = 1
    standardized = (X - X_mean) / X_std

    # 3. Robust Scaling: use median and IQR (robust to outliers)
    # Formula: (x - median) / IQR
    X_median = np.median(X, axis=0)
    Q1 = np.percentile(X, 25, axis=0)
    Q3 = np.percentile(X, 75, axis=0)
    IQR = Q3 - Q1
    IQR[IQR == 0] = 1
    robust_scaled = (X - X_median) / IQR

    # 4. Clip outliers: values beyond 3 standard deviations
    lower_bound = X_mean - 3 * X_std
    upper_bound = X_mean + 3 * X_std
    clipped = np.clip(X, lower_bound, upper_bound)

    return {
        'original': X,
        'normalized': normalized,
        'standardized': standardized,
        'robust_scaled': robust_scaled,
        'clipped': clipped
    }


def linear_regression_numpy(X: np.ndarray, y: np.ndarray) -> dict:
    """
    Implement linear regression using NumPy (closed-form solution).

    Linear Regression finds weights θ that minimize:
        Loss = ||y - Xθ||²

    Closed-form solution (Normal Equation):
        θ = (X^T X)^(-1) X^T y

    This demonstrates:
    - Matrix multiplication (X^T X)
    - Matrix inversion
    - Predictions (X @ θ)
    - Evaluation metrics (MSE, R²)

    Args:
        X: Feature matrix, shape (n_samples, n_features)
        y: Target vector, shape (n_samples,)

    Returns:
        Dictionary with:
        - 'weights': Learned weights θ, shape (n_features,)
        - 'predictions': y_pred = X @ θ
        - 'mse': Mean squared error
        - 'rmse': Root mean squared error
        - 'r2_score': R² coefficient (1 = perfect fit)
        - 'residuals': y - y_pred

    Time Complexity: O(n*m^2 + m^3) where n=samples, m=features
        - X^T @ X: O(n*m^2)
        - Matrix inverse: O(m^3)
        - X @ θ: O(n*m)
    Space Complexity: O(n*m + m^2)

    Examples:
        >>> X = np.array([[1], [2], [3], [4], [5]])
        >>> y = np.array([2, 4, 6, 8, 10])  # y = 2x
        >>> model = linear_regression_numpy(X, y)
        >>> model['weights'][0]  # Should be close to 2
        2.0
        >>> model['r2_score']  # Should be close to 1
        1.0

    Notes:
        - Assumes X^T X is invertible (full rank)
        - For large datasets, use gradient descent instead
        - Add regularization (Ridge/Lasso) for better generalization
    """
    # Add bias column (intercept term): X_new = [1, X]
    n_samples = X.shape[0]
    X_with_bias = np.c_[np.ones(n_samples), X]  # Add column of 1s

    # Normal Equation: θ = (X^T X)^(-1) X^T y
    # Step 1: Compute X^T @ X
    XTX = X_with_bias.T @ X_with_bias  # Shape: (m+1, m+1)

    # Step 2: Compute X^T @ y
    XTy = X_with_bias.T @ y  # Shape: (m+1,)

    # Step 3: Solve XTX @ θ = XTy
    # Use np.linalg.solve (more stable than inverse)
    try:
        weights = np.linalg.solve(XTX, XTy)
    except np.linalg.LinAlgError:
        # Fallback to pseudo-inverse if matrix is singular
        weights = np.linalg.pinv(XTX) @ XTy

    # Make predictions
    predictions = X_with_bias @ weights

    # Compute evaluation metrics
    residuals = y - predictions
    mse = np.mean(residuals**2)
    rmse = np.sqrt(mse)

    # R² score: R² = 1 - (SS_res / SS_tot)
    # SS_res = sum of squared residuals
    # SS_tot = total sum of squares
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r2_score = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0.0

    return {
        'weights': weights,
        'predictions': predictions,
        'mse': float(mse),
        'rmse': float(rmse),
        'r2_score': float(r2_score),
        'residuals': residuals
    }


# Additional utility functions for demonstration

def demonstrate_numpy_vs_python():
    """
    Comprehensive performance comparison: NumPy vs Pure Python.

    Demonstrates the speed advantage of NumPy across different operations:
    1. Element-wise operations
    2. Aggregations (sum, mean)
    3. Matrix multiplication
    4. Statistical computations
    """
    n = 100000

    print("=" * 60)
    print("NumPy vs Pure Python Performance Comparison")
    print("=" * 60)

    # Test 1: Element-wise addition
    print("\n1. Element-wise Addition (100k elements)")
    python_list_a = list(range(n))
    python_list_b = list(range(n, 2*n))

    start = time.time()
    python_result = [a + b for a, b in zip(python_list_a, python_list_b)]
    python_time = time.time() - start

    numpy_array_a = np.arange(n)
    numpy_array_b = np.arange(n, 2*n)

    start = time.time()
    numpy_result = numpy_array_a + numpy_array_b
    numpy_time = time.time() - start

    print(f"   Python: {python_time:.6f}s")
    print(f"   NumPy:  {numpy_time:.6f}s")
    print(f"   Speedup: {python_time/numpy_time:.1f}x")

    # Test 2: Sum
    print("\n2. Sum (100k elements)")
    start = time.time()
    python_sum = sum(python_list_a)
    python_time = time.time() - start

    start = time.time()
    numpy_sum = np.sum(numpy_array_a)
    numpy_time = time.time() - start

    print(f"   Python: {python_time:.6f}s")
    print(f"   NumPy:  {numpy_time:.6f}s")
    print(f"   Speedup: {python_time/numpy_time:.1f}x")

    # Test 3: Matrix multiplication
    print("\n3. Matrix Multiplication (100x100)")
    size = 100
    python_matrix_a = [[i+j for j in range(size)] for i in range(size)]
    python_matrix_b = [[i*j for j in range(size)] for i in range(size)]

    start = time.time()
    python_result = [[sum(a*b for a,b in zip(row,col))
                      for col in zip(*python_matrix_b)]
                     for row in python_matrix_a]
    python_time = time.time() - start

    numpy_matrix_a = np.array(python_matrix_a)
    numpy_matrix_b = np.array(python_matrix_b)

    start = time.time()
    numpy_result = numpy_matrix_a @ numpy_matrix_b
    numpy_time = time.time() - start

    print(f"   Python: {python_time:.6f}s")
    print(f"   NumPy:  {numpy_time:.6f}s")
    print(f"   Speedup: {python_time/numpy_time:.1f}x")

    print("\n" + "=" * 60)
    print("Conclusion: NumPy is 50-100x faster than pure Python!")
    print("=" * 60)


if __name__ == "__main__":
    print("Project 11: Numerical Computing with NumPy")
    print("=" * 60)

    # Test 1: Array creation
    print("\n1. Array Creation Methods:")
    arrays = create_arrays()
    print(f"   From list: {arrays['from_list']}")
    print(f"   Zeros shape: {arrays['zeros'].shape}")
    print(f"   Identity matrix shape: {arrays['identity'].shape}")

    # Test 2: Vectorization comparison
    print("\n2. Vectorization Performance:")
    perf = compare_vectorization(100000)
    print(f"   Python time: {perf['python_time']:.6f}s")
    print(f"   NumPy time: {perf['numpy_time']:.6f}s")
    print(f"   Speedup: {perf['speedup']:.1f}x")

    # Test 3: Array operations
    print("\n3. Array Operations:")
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ops = array_operations(arr)
    print(f"   First row: {ops['first_row']}")
    print(f"   Diagonal: {ops['diagonal']}")
    print(f"   Values > mean: {ops['boolean_mask']}")

    # Test 4: Broadcasting
    print("\n4. Broadcasting:")
    broadcast = demonstrate_broadcasting()
    print(f"   Distance matrix:\n{broadcast['distance_matrix']}")

    # Test 5: Matrix operations for ML
    print("\n5. Matrix Operations for ML:")
    X = np.array([[1, 2], [3, 4], [5, 6]])
    y = np.array([1, 0, 1])
    ml_ops = matrix_operations_ml(X, y)
    print(f"   Feature means: {ml_ops['feature_means']}")
    print(f"   Correlation matrix:\n{ml_ops['correlation']}")

    # Test 6: Statistical analysis
    print("\n6. Statistical Analysis:")
    data = np.array([1, 2, 3, 4, 5, 100])
    stats = statistical_analysis(data)
    print(f"   Mean: {stats['mean']:.2f}")
    print(f"   Median: {stats['median']:.2f}")
    print(f"   Std: {stats['std']:.2f}")

    # Test 7: Data preprocessing
    print("\n7. Data Preprocessing:")
    X_raw = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 100.0]])
    processed = preprocess_data(X_raw)
    print(f"   Normalized min: {processed['normalized'].min():.2f}")
    print(f"   Normalized max: {processed['normalized'].max():.2f}")
    print(f"   Standardized mean: {processed['standardized'].mean():.6f}")

    # Test 8: Linear regression
    print("\n8. Linear Regression:")
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])  # y = 2x
    model = linear_regression_numpy(X, y)
    print(f"   Weights (slope, intercept): {model['weights']}")
    print(f"   R² score: {model['r2_score']:.6f}")
    print(f"   RMSE: {model['rmse']:.6f}")

    print("\n" + "=" * 60)

    # Comprehensive performance demo
    print("\n")
    demonstrate_numpy_vs_python()
