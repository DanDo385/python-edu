"""
Test suite for Project 16: NumPy 101

Run with: pytest test.py -v
"""

import pytest
import numpy as np
from exercise import (
    create_array_from_list,
    create_zeros_array,
    create_range_array,
    vectorized_add,
    vectorized_multiply,
    vectorized_square,
    get_array_shape,
    reshape_array,
    calculate_mean,
    calculate_sum,
    normalize_array,
    elementwise_operation,
)


class TestArrayCreation:
    """Test array creation functions."""
    
    def test_create_from_list(self):
        result = create_array_from_list([1, 2, 3, 4, 5])
        assert isinstance(result, np.ndarray)
        assert np.array_equal(result, [1, 2, 3, 4, 5])
    
    def test_create_zeros(self):
        result = create_zeros_array(5)
        assert isinstance(result, np.ndarray)
        assert np.array_equal(result, [0, 0, 0, 0, 0])
        assert result.shape == (5,)
    
    def test_create_range(self):
        result = create_range_array(0, 5)
        assert np.array_equal(result, [0, 1, 2, 3, 4])
        
        result = create_range_array(2, 10, 2)
        assert np.array_equal(result, [2, 4, 6, 8])


class TestVectorizedOperations:
    """Test vectorized operations."""
    
    def test_vectorized_add(self):
        arr = np.array([1, 2, 3, 4, 5])
        result = vectorized_add(arr, 10)
        assert np.array_equal(result, [11, 12, 13, 14, 15])
    
    def test_vectorized_multiply(self):
        arr = np.array([1, 2, 3, 4, 5])
        result = vectorized_multiply(arr, 3)
        assert np.array_equal(result, [3, 6, 9, 12, 15])
    
    def test_vectorized_square(self):
        arr = np.array([1, 2, 3, 4, 5])
        result = vectorized_square(arr)
        assert np.array_equal(result, [1, 4, 9, 16, 25])


class TestArrayProperties:
    """Test array shape and reshaping."""
    
    def test_get_shape(self):
        arr = np.array([[1, 2, 3], [4, 5, 6]])
        shape = get_array_shape(arr)
        assert shape == (2, 3)
    
    def test_reshape_array(self):
        arr = np.array([1, 2, 3, 4, 5, 6])
        result = reshape_array(arr, (2, 3))
        assert result.shape == (2, 3)
        assert np.array_equal(result, [[1, 2, 3], [4, 5, 6]])


class TestStatistics:
    """Test statistical operations."""
    
    def test_calculate_mean(self):
        arr = np.array([1, 2, 3, 4, 5])
        mean = calculate_mean(arr)
        assert abs(mean - 3.0) < 0.001
    
    def test_calculate_sum(self):
        arr = np.array([1, 2, 3, 4, 5])
        total = calculate_sum(arr)
        assert total == 15


class TestNormalization:
    """Test array normalization."""
    
    def test_normalize_array(self):
        arr = np.array([1, 2, 3, 4, 5])
        normalized = normalize_array(arr)
        # Check mean is approximately 0
        assert abs(np.mean(normalized)) < 0.001
        # Check std is approximately 1
        assert abs(np.std(normalized) - 1.0) < 0.001


class TestElementwiseOperations:
    """Test element-wise operations."""
    
    def test_elementwise_add(self):
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        result = elementwise_operation(arr1, arr2, 'add')
        assert np.array_equal(result, [5, 7, 9])
    
    def test_elementwise_multiply(self):
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        result = elementwise_operation(arr1, arr2, 'multiply')
        assert np.array_equal(result, [4, 10, 18])
    
    def test_elementwise_subtract(self):
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        result = elementwise_operation(arr1, arr2, 'subtract')
        assert np.array_equal(result, [-3, -3, -3])

