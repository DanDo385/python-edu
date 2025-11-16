"""
Tests for Project 11: Numerical Computing with NumPy

Comprehensive test suite covering:
- Array creation and properties
- Vectorization performance
- Array indexing and slicing
- Broadcasting operations
- Matrix operations for ML
- Statistical analysis
- Data preprocessing
- Linear regression implementation
- Performance verification
"""

import pytest
import numpy as np
from solution.solution import (
    create_arrays,
    compare_vectorization,
    array_operations,
    demonstrate_broadcasting,
    matrix_operations_ml,
    statistical_analysis,
    preprocess_data,
    linear_regression_numpy
)


class TestCreateArrays:
    """Tests for array creation functionality."""

    def test_from_list(self):
        """Test array creation from Python list."""
        arrays = create_arrays()
        assert 'from_list' in arrays
        assert np.array_equal(arrays['from_list'], np.array([1, 2, 3, 4, 5]))
        assert arrays['from_list'].dtype in [np.int32, np.int64]

    def test_zeros_array(self):
        """Test zeros array creation."""
        arrays = create_arrays()
        assert 'zeros' in arrays
        assert arrays['zeros'].shape == (3, 4)
        assert np.all(arrays['zeros'] == 0)

    def test_ones_array(self):
        """Test ones array creation."""
        arrays = create_arrays()
        assert 'ones' in arrays
        assert arrays['ones'].shape == (2, 3)
        assert np.all(arrays['ones'] == 1)

    def test_range_array(self):
        """Test range array creation."""
        arrays = create_arrays()
        assert 'range' in arrays
        assert np.array_equal(arrays['range'], np.arange(10))

    def test_linspace_array(self):
        """Test linspace array creation."""
        arrays = create_arrays()
        assert 'linspace' in arrays
        expected = np.linspace(0, 1, 5)
        np.testing.assert_array_almost_equal(arrays['linspace'], expected)

    def test_random_array(self):
        """Test random array creation."""
        arrays = create_arrays()
        assert 'random' in arrays
        assert arrays['random'].shape == (3, 3)
        assert np.all(arrays['random'] >= 0)
        assert np.all(arrays['random'] < 1)

    def test_identity_matrix(self):
        """Test identity matrix creation."""
        arrays = create_arrays()
        assert 'identity' in arrays
        assert arrays['identity'].shape == (4, 4)
        assert np.array_equal(arrays['identity'], np.eye(4))


class TestCompareVectorization:
    """Tests for vectorization performance comparison."""

    def test_small_array(self):
        """Test with small array."""
        results = compare_vectorization(n=1000)
        assert 'python_time' in results
        assert 'numpy_time' in results
        assert 'speedup' in results
        assert 'result' in results

    def test_speedup_factor(self):
        """Test that NumPy is significantly faster."""
        results = compare_vectorization(n=100000)
        # NumPy should be at least 10x faster
        assert results['speedup'] > 10

    def test_correctness(self):
        """Test that both methods give same result."""
        results = compare_vectorization(n=100)
        # Result should be sum of squares: 0^2 + 1^2 + ... + 99^2
        expected = sum(i**2 for i in range(100))
        assert results['result'] == expected

    def test_numpy_faster(self):
        """Test that NumPy time is less than Python time."""
        results = compare_vectorization(n=10000)
        assert results['numpy_time'] < results['python_time']


class TestArrayOperations:
    """Tests for array indexing and slicing."""

    def test_first_row(self):
        """Test extracting first row."""
        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        ops = array_operations(arr)
        assert np.array_equal(ops['first_row'], np.array([1, 2, 3]))

    def test_last_column(self):
        """Test extracting last column."""
        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        ops = array_operations(arr)
        assert np.array_equal(ops['last_column'], np.array([3, 6, 9]))

    def test_subarray(self):
        """Test extracting center subarray."""
        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        ops = array_operations(arr)
        expected = np.array([[5, 6], [8, 9]])
        assert np.array_equal(ops['subarray'], expected)

    def test_diagonal(self):
        """Test extracting diagonal."""
        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        ops = array_operations(arr)
        assert np.array_equal(ops['diagonal'], np.array([1, 5, 9]))

    def test_boolean_mask(self):
        """Test boolean masking."""
        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        ops = array_operations(arr)
        mean_val = np.mean(arr)  # 5.0
        expected = arr[arr > mean_val]
        assert np.array_equal(ops['boolean_mask'], expected)

    def test_fancy_index(self):
        """Test fancy indexing."""
        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        ops = array_operations(arr)
        assert np.array_equal(ops['fancy_index'], np.array([1, 5, 9]))

    def test_small_array(self):
        """Test with small array (< 3x3)."""
        arr = np.array([[1, 2], [3, 4]])
        ops = array_operations(arr)
        assert ops['subarray'].shape == (2, 2)


class TestDemonstrateBroadcasting:
    """Tests for broadcasting demonstrations."""

    def test_add_row_vector(self):
        """Test broadcasting row vector addition."""
        results = demonstrate_broadcasting()
        expected = np.array([[2, 3, 4], [2, 3, 4], [2, 3, 4]])
        np.testing.assert_array_almost_equal(
            results['add_row_vector'], expected
        )

    def test_multiply_column(self):
        """Test broadcasting column multiplication."""
        results = demonstrate_broadcasting()
        expected = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
        np.testing.assert_array_almost_equal(
            results['multiply_column'], expected
        )

    def test_normalize_columns(self):
        """Test column normalization (zero mean)."""
        results = demonstrate_broadcasting()
        normalized = results['normalize_columns']
        # Check that column means are approximately 0
        column_means = np.mean(normalized, axis=0)
        np.testing.assert_array_almost_equal(
            column_means, np.zeros(3), decimal=10
        )

    def test_distance_matrix(self):
        """Test pairwise distance matrix."""
        results = demonstrate_broadcasting()
        dist_matrix = results['distance_matrix']
        # Distance matrix should be symmetric
        np.testing.assert_array_almost_equal(
            dist_matrix, dist_matrix.T
        )
        # Diagonal should be zero (distance from point to itself)
        np.testing.assert_array_almost_equal(
            np.diag(dist_matrix), np.zeros(3)
        )
        # Distance from [0,0] to [1,1] should be sqrt(2)
        assert abs(dist_matrix[0, 1] - np.sqrt(2)) < 1e-10

    def test_matrix_shape(self):
        """Test that matrix has correct shape."""
        results = demonstrate_broadcasting()
        assert results['matrix'].shape == (3, 3)


class TestMatrixOperationsML:
    """Tests for ML matrix operations."""

    def test_gram_matrix_shape(self):
        """Test Gram matrix has correct shape."""
        X = np.array([[1, 2], [3, 4], [5, 6]])
        y = np.array([1, 0, 1])
        ops = matrix_operations_ml(X, y)
        assert ops['gram_matrix'].shape == (3, 3)

    def test_gram_matrix_symmetric(self):
        """Test that Gram matrix is symmetric."""
        X = np.array([[1, 2], [3, 4], [5, 6]])
        y = np.array([1, 0, 1])
        ops = matrix_operations_ml(X, y)
        gram = ops['gram_matrix']
        np.testing.assert_array_almost_equal(gram, gram.T)

    def test_feature_means(self):
        """Test feature means calculation."""
        X = np.array([[1, 2], [3, 4], [5, 6]])
        y = np.array([1, 0, 1])
        ops = matrix_operations_ml(X, y)
        expected = np.array([3, 4])
        np.testing.assert_array_almost_equal(
            ops['feature_means'], expected
        )

    def test_normalized_X_zero_mean(self):
        """Test that normalized X has zero mean."""
        X = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)
        y = np.array([1, 0, 1])
        ops = matrix_operations_ml(X, y)
        column_means = np.mean(ops['normalized_X'], axis=0)
        np.testing.assert_array_almost_equal(
            column_means, np.zeros(2), decimal=10
        )

    def test_covariance_shape(self):
        """Test covariance matrix shape."""
        X = np.array([[1, 2], [3, 4], [5, 6]])
        y = np.array([1, 0, 1])
        ops = matrix_operations_ml(X, y)
        assert ops['covariance'].shape == (2, 2)

    def test_correlation_shape(self):
        """Test correlation matrix shape."""
        X = np.array([[1, 2], [3, 4], [5, 6]])
        y = np.array([1, 0, 1])
        ops = matrix_operations_ml(X, y)
        assert ops['correlation'].shape == (2, 2)

    def test_correlation_diagonal_ones(self):
        """Test that correlation matrix diagonal is all ones."""
        X = np.array([[1, 2], [3, 4], [5, 6]])
        y = np.array([1, 0, 1])
        ops = matrix_operations_ml(X, y)
        diagonal = np.diag(ops['correlation'])
        np.testing.assert_array_almost_equal(diagonal, np.ones(2))


class TestStatisticalAnalysis:
    """Tests for statistical analysis functions."""

    def test_mean_calculation(self):
        """Test mean calculation."""
        data = np.array([1, 2, 3, 4, 5])
        stats = statistical_analysis(data)
        assert stats['mean'] == 3.0

    def test_median_calculation(self):
        """Test median calculation."""
        data = np.array([1, 2, 3, 4, 5])
        stats = statistical_analysis(data)
        assert stats['median'] == 3.0

    def test_median_robust_to_outliers(self):
        """Test that median is robust to outliers."""
        data = np.array([1, 2, 3, 4, 5, 100])
        stats = statistical_analysis(data)
        # Median should be 3.5, not affected by 100
        assert stats['median'] == 3.5
        # Mean should be much higher due to outlier
        assert stats['mean'] > 10

    def test_std_and_var(self):
        """Test standard deviation and variance."""
        data = np.array([1, 2, 3, 4, 5])
        stats = statistical_analysis(data)
        expected_std = np.std(data)
        expected_var = np.var(data)
        assert abs(stats['std'] - expected_std) < 1e-10
        assert abs(stats['var'] - expected_var) < 1e-10

    def test_min_max(self):
        """Test min and max values."""
        data = np.array([1, 2, 3, 4, 5, 100])
        stats = statistical_analysis(data)
        assert stats['min'] == 1.0
        assert stats['max'] == 100.0

    def test_percentiles(self):
        """Test percentile calculation."""
        data = np.array([1, 2, 3, 4, 5])
        stats = statistical_analysis(data)
        assert len(stats['percentiles']) == 3
        # 50th percentile should be median
        assert stats['percentiles'][1] == stats['median']

    def test_range(self):
        """Test range calculation."""
        data = np.array([1, 2, 3, 4, 5])
        stats = statistical_analysis(data)
        assert stats['range'] == 4.0  # 5 - 1

    def test_iqr(self):
        """Test interquartile range."""
        data = np.array([1, 2, 3, 4, 5])
        stats = statistical_analysis(data)
        # IQR = Q3 - Q1
        assert stats['iqr'] == stats['percentiles'][2] - stats['percentiles'][0]

    def test_2d_array(self):
        """Test with 2D array."""
        data = np.array([[1, 2], [3, 4]])
        stats = statistical_analysis(data)
        # Should flatten and compute stats on all elements
        assert stats['mean'] == 2.5


class TestPreprocessData:
    """Tests for data preprocessing functions."""

    def test_normalized_range(self):
        """Test that normalized data is in [0, 1]."""
        X = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
        processed = preprocess_data(X)
        normalized = processed['normalized']
        assert normalized.min() >= 0
        assert normalized.max() <= 1
        # Should actually reach 0 and 1
        assert normalized.min() == 0
        assert normalized.max() == 1

    def test_standardized_mean_std(self):
        """Test that standardized data has zero mean and unit variance."""
        X = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
        processed = preprocess_data(X)
        standardized = processed['standardized']
        # Mean should be approximately 0
        assert abs(standardized.mean()) < 1e-10
        # Std should be approximately 1
        assert abs(standardized.std() - 1.0) < 1e-10

    def test_robust_scaling(self):
        """Test robust scaling with outliers."""
        X = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 100.0]])
        processed = preprocess_data(X)
        # Robust scaling should be less affected by outlier than standard scaling
        robust = processed['robust_scaled']
        assert robust.shape == X.shape

    def test_clipping_outliers(self):
        """Test that outliers are clipped."""
        X = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 100.0]])
        processed = preprocess_data(X)
        clipped = processed['clipped']
        original = processed['original']
        # Clipped version should have smaller max value
        assert clipped.max() < original.max()

    def test_original_preserved(self):
        """Test that original data is included."""
        X = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
        processed = preprocess_data(X)
        assert 'original' in processed
        np.testing.assert_array_almost_equal(
            processed['original'], X
        )

    def test_constant_feature(self):
        """Test handling of constant feature (avoid division by zero)."""
        X = np.array([[1.0, 5.0], [1.0, 5.0], [1.0, 5.0]])
        processed = preprocess_data(X)
        # Should not raise error or produce NaN
        assert not np.any(np.isnan(processed['normalized']))
        assert not np.any(np.isnan(processed['standardized']))


class TestLinearRegression:
    """Tests for linear regression implementation."""

    def test_simple_linear_fit(self):
        """Test simple linear relationship: y = 2x."""
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([2, 4, 6, 8, 10], dtype=float)
        model = linear_regression_numpy(X, y)
        # Weights: [intercept, slope]
        # Should be close to [0, 2]
        assert abs(model['weights'][1] - 2.0) < 1e-10
        assert abs(model['weights'][0]) < 1e-10

    def test_with_intercept(self):
        """Test linear relationship with intercept: y = 2x + 3."""
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([5, 7, 9, 11, 13], dtype=float)
        model = linear_regression_numpy(X, y)
        # Weights: [intercept, slope]
        # Should be close to [3, 2]
        assert abs(model['weights'][1] - 2.0) < 1e-10
        assert abs(model['weights'][0] - 3.0) < 1e-10

    def test_perfect_fit_r2(self):
        """Test R² score for perfect fit."""
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([2, 4, 6, 8, 10], dtype=float)
        model = linear_regression_numpy(X, y)
        # Perfect fit should have R² = 1.0
        assert abs(model['r2_score'] - 1.0) < 1e-10

    def test_perfect_fit_mse(self):
        """Test MSE for perfect fit."""
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([2, 4, 6, 8, 10], dtype=float)
        model = linear_regression_numpy(X, y)
        # Perfect fit should have MSE ≈ 0
        assert model['mse'] < 1e-10

    def test_predictions_shape(self):
        """Test that predictions have correct shape."""
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([2, 4, 6, 8, 10], dtype=float)
        model = linear_regression_numpy(X, y)
        assert model['predictions'].shape == y.shape

    def test_residuals(self):
        """Test residuals calculation."""
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([2, 4, 6, 8, 10], dtype=float)
        model = linear_regression_numpy(X, y)
        # Residuals = y - predictions
        expected_residuals = y - model['predictions']
        np.testing.assert_array_almost_equal(
            model['residuals'], expected_residuals
        )

    def test_rmse(self):
        """Test RMSE calculation."""
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([2, 4, 6, 8, 10], dtype=float)
        model = linear_regression_numpy(X, y)
        # RMSE should be sqrt(MSE)
        assert abs(model['rmse'] - np.sqrt(model['mse'])) < 1e-10

    def test_multiple_features(self):
        """Test with multiple features."""
        X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
        y = np.array([5, 8, 11, 14], dtype=float)  # y = 1 + 2*x1 + 1*x2
        model = linear_regression_numpy(X, y)
        # Should fit with 3 weights (intercept + 2 features)
        assert len(model['weights']) == 3
        assert model['r2_score'] > 0.9  # Should have good fit

    def test_imperfect_fit(self):
        """Test with noisy data."""
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([2.1, 3.9, 6.2, 7.8, 10.1], dtype=float)
        model = linear_regression_numpy(X, y)
        # R² should be high but not perfect
        assert 0.95 < model['r2_score'] < 1.0
        # MSE should be small but non-zero
        assert model['mse'] > 0


class TestPerformance:
    """Performance verification tests."""

    def test_large_array_creation(self):
        """Test creating large arrays efficiently."""
        # Should handle 1M elements quickly
        large_arr = np.arange(1000000)
        assert len(large_arr) == 1000000

    def test_vectorization_speedup(self):
        """Test that vectorization provides significant speedup."""
        results = compare_vectorization(n=100000)
        # NumPy should be at least 20x faster
        assert results['speedup'] > 20

    def test_matrix_multiplication_performance(self):
        """Test that matrix multiplication is efficient."""
        # Create moderately sized matrices
        A = np.random.random((500, 500))
        B = np.random.random((500, 500))

        import time
        start = time.time()
        C = A @ B
        duration = time.time() - start

        # Should complete in reasonable time (< 1 second)
        assert duration < 1.0
        assert C.shape == (500, 500)

    def test_statistical_operations_performance(self):
        """Test that statistical operations are efficient."""
        large_data = np.random.random(1000000)

        import time
        start = time.time()
        stats = statistical_analysis(large_data)
        duration = time.time() - start

        # Should complete quickly (< 0.1 seconds)
        assert duration < 0.1
        assert 'mean' in stats


class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_empty_array_operations(self):
        """Test operations with empty dimensions."""
        arr = np.array([[]])
        # Should handle gracefully without crashing
        try:
            ops = array_operations(arr)
            # If it succeeds, results should be valid
            assert isinstance(ops, dict)
        except (ValueError, IndexError):
            # Or raise appropriate error
            pass

    def test_single_element(self):
        """Test with single-element array."""
        data = np.array([42])
        stats = statistical_analysis(data)
        assert stats['mean'] == 42
        assert stats['median'] == 42
        assert stats['std'] == 0
        assert stats['min'] == 42
        assert stats['max'] == 42

    def test_negative_values(self):
        """Test with negative values."""
        X = np.array([[-5.0, -3.0], [-1.0, 1.0], [3.0, 5.0]])
        processed = preprocess_data(X)
        # Should handle negative values correctly
        assert not np.any(np.isnan(processed['normalized']))
        assert not np.any(np.isnan(processed['standardized']))

    def test_all_zeros(self):
        """Test with array of zeros."""
        data = np.zeros(10)
        stats = statistical_analysis(data)
        assert stats['mean'] == 0
        assert stats['std'] == 0
        assert stats['var'] == 0


# Integration tests
class TestIntegration:
    """Integration tests combining multiple functions."""

    def test_ml_pipeline(self):
        """Test complete ML preprocessing and modeling pipeline."""
        # Generate synthetic data
        np.random.seed(42)
        X = np.random.random((100, 3))
        # True relationship: y = 2*x1 + 3*x2 - x3 + 5 + noise
        y = (2*X[:, 0] + 3*X[:, 1] - X[:, 2] + 5 +
             np.random.normal(0, 0.1, 100))

        # Preprocess
        processed = preprocess_data(X)
        X_normalized = processed['normalized']

        # Train model
        model = linear_regression_numpy(X_normalized, y)

        # Verify results
        assert model['r2_score'] > 0.9  # Should fit well
        assert model['mse'] < 1.0  # Low error

    def test_statistical_analysis_pipeline(self):
        """Test statistical analysis on real-world-like data."""
        # Generate data with outliers
        np.random.seed(42)
        data = np.concatenate([
            np.random.normal(50, 10, 95),  # Normal data
            np.array([150, 200, 0, -50, 250])  # Outliers
        ])

        # Analyze
        stats = statistical_analysis(data)

        # Median should be more robust than mean
        assert abs(stats['median'] - 50) < abs(stats['mean'] - 50)

        # IQR should be reasonable
        assert 10 < stats['iqr'] < 30

    def test_broadcasting_with_real_data(self):
        """Test broadcasting on realistic dataset normalization."""
        # Simulate feature matrix
        np.random.seed(42)
        X = np.random.random((100, 5)) * 100

        # Normalize using broadcasting
        mean = np.mean(X, axis=0)
        std = np.std(X, axis=0)
        X_normalized = (X - mean) / std

        # Verify zero mean, unit variance
        np.testing.assert_array_almost_equal(
            np.mean(X_normalized, axis=0), np.zeros(5), decimal=10
        )
        np.testing.assert_array_almost_equal(
            np.std(X_normalized, axis=0), np.ones(5), decimal=10
        )


def test_all_functions_importable():
    """Test that all required functions are importable."""
    # This test ensures all functions are properly exported
    assert callable(create_arrays)
    assert callable(compare_vectorization)
    assert callable(array_operations)
    assert callable(demonstrate_broadcasting)
    assert callable(matrix_operations_ml)
    assert callable(statistical_analysis)
    assert callable(preprocess_data)
    assert callable(linear_regression_numpy)
