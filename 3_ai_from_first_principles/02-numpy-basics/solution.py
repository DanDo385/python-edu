"""
Project 16: NumPy 101 – Arrays and Vectorized Operations - SOLUTION

Complete solution with detailed comments explaining NumPy arrays, vectorization,
and why they're essential for machine learning.
"""

import numpy as np


def create_array_from_list(python_list):
    """
    Create a NumPy array from a Python list.
    
    This is the most basic way to create a NumPy array. The key difference
    from a Python list is that NumPy arrays:
    1. Store homogeneous data (all same type)
    2. Are stored in contiguous memory (faster access)
    3. Support vectorized operations (no loops needed)
    
    Args:
        python_list (list): Python list of numbers
    
    Returns:
        np.ndarray: NumPy array
    
    Example:
        create_array_from_list([1, 2, 3])  # Returns array([1, 2, 3])
    """
    # np.array() converts a Python list (or any sequence) into a NumPy array
    # This is the fundamental conversion that enables all NumPy operations
    # The array will have the same elements but be stored more efficiently
    return np.array(python_list)


def create_zeros_array(size):
    """
    Create an array filled with zeros.
    
    This is useful for initializing arrays before filling them with data.
    Common in machine learning for initializing weight matrices, bias vectors, etc.
    
    Args:
        size (int): Size of array
    
    Returns:
        np.ndarray: Array of zeros
    
    Example:
        create_zeros_array(5)  # Returns array([0., 0., 0., 0., 0.])
    """
    # np.zeros() creates an array filled with zeros
    # The dtype (data type) defaults to float64
    # This is faster than creating a list and converting because NumPy
    # can allocate the memory directly without Python overhead
    return np.zeros(size)


def create_range_array(start, stop, step=1):
    """
    Create an array with values from start to stop (exclusive) with given step.
    
    Similar to Python's range(), but returns a NumPy array instead of a range object.
    This is useful for creating sequences of numbers for indexing, plotting, etc.
    
    Args:
        start (int): Start value
        stop (int): Stop value (exclusive, like range())
        step (int): Step size (default 1)
    
    Returns:
        np.ndarray: Array of values
    
    Example:
        create_range_array(0, 5)      # Returns array([0, 1, 2, 3, 4])
        create_range_array(2, 10, 2)   # Returns array([2, 4, 6, 8])
    """
    # np.arange() is NumPy's version of range(), but returns an array
    # It's similar to range() but creates the array immediately
    # This is useful when you need the actual array values, not just iteration
    return np.arange(start, stop, step)


def vectorized_add(arr, value):
    """
    Add a value to every element in the array using vectorization.
    
    This demonstrates the power of vectorization: instead of looping through
    each element, NumPy applies the operation to the entire array at once.
    This is implemented in C, making it much faster than Python loops.
    
    Time complexity: O(n) but with constant factor ~100x smaller than Python loop
    Space complexity: O(n) for the result array
    
    Args:
        arr (np.ndarray): Input array
        value (int or float): Value to add
    
    Returns:
        np.ndarray: Array with value added to each element
    
    Example:
        vectorized_add(np.array([1, 2, 3]), 10)  # Returns array([11, 12, 13])
    """
    # This is vectorization in action!
    # Instead of: [x + value for x in arr]  (Python loop, slow)
    # We do: arr + value  (NumPy vectorized, fast)
    # NumPy automatically broadcasts the scalar value to match the array shape
    # and performs the addition element-wise in optimized C code
    return arr + value


def vectorized_multiply(arr, value):
    """
    Multiply every element by a value using vectorization.
    
    Similar to vectorized_add, but demonstrates multiplication.
    This pattern (scalar * array) is fundamental in linear algebra and ML.
    
    Args:
        arr (np.ndarray): Input array
        value (int or float): Value to multiply by
    
    Returns:
        np.ndarray: Array with each element multiplied
    
    Example:
        vectorized_multiply(np.array([1, 2, 3]), 3)  # Returns array([3, 6, 9])
    """
    # Vectorized multiplication: each element multiplied by value
    # This is how we scale vectors in linear algebra
    # In ML, this is how we apply learning rates, scale features, etc.
    return arr * value


def vectorized_square(arr):
    """
    Square every element in the array using vectorization.
    
    Demonstrates element-wise exponentiation. The ** operator works
    element-wise on NumPy arrays, which is much faster than looping.
    
    Args:
        arr (np.ndarray): Input array
    
    Returns:
        np.ndarray: Array with each element squared
    
    Example:
        vectorized_square(np.array([1, 2, 3, 4]))  # Returns array([1, 4, 9, 16])
    """
    # Element-wise exponentiation using ** operator
    # arr ** 2 squares each element
    # This is equivalent to: [x**2 for x in arr] but much faster
    # In ML, we use this for squared errors, squared distances, etc.
    return arr ** 2


def get_array_shape(arr):
    """
    Get the shape (dimensions) of an array.
    
    Shape describes how data is organized. Understanding shape is crucial
    for machine learning, where we work with multi-dimensional data:
    - 1D: vectors (features)
    - 2D: matrices (samples × features)
    - 3D+: tensors (batches, sequences, etc.)
    
    Args:
        arr (np.ndarray): Input array
    
    Returns:
        tuple: Shape of array
    
    Example:
        get_array_shape(np.array([[1, 2], [3, 4]]))  # Returns (2, 2)
    """
    # arr.shape returns a tuple describing the dimensions
    # For 1D array [1, 2, 3]: shape is (3,) - one dimension of size 3
    # For 2D array [[1,2], [3,4]]: shape is (2, 2) - two dimensions, each size 2
    # Shape is fundamental in ML - you must understand it to work with data correctly
    return arr.shape


def reshape_array(arr, new_shape):
    """
    Reshape an array to new dimensions.
    
    Reshaping changes how data is organized without changing the data itself.
    The total number of elements must remain the same.
    This is essential in ML for preparing data (flattening images, batching, etc.)
    
    Args:
        arr (np.ndarray): Input array
        new_shape (tuple): Desired shape (e.g., (2, 3))
    
    Returns:
        np.ndarray: Reshaped array
    
    Example:
        arr = np.array([1, 2, 3, 4, 5, 6])
        reshape_array(arr, (2, 3))  # Returns [[1, 2, 3], [4, 5, 6]]
    """
    # arr.reshape() reorganizes data into new dimensions
    # The product of new_shape dimensions must equal total elements
    # Example: 6 elements can be reshaped to (2, 3) or (3, 2) or (6, 1), etc.
    # This doesn't copy data (usually), just changes the view
    # In ML: we reshape images (28×28) to vectors (784) for neural networks
    return arr.reshape(new_shape)


def calculate_mean(arr):
    """
    Calculate the mean (average) of array elements.
    
    Mean is a fundamental statistical measure. In ML, we use it for:
    - Feature normalization (subtract mean)
    - Loss functions (mean squared error)
    - Batch statistics
    
    Args:
        arr (np.ndarray): Input array
    
    Returns:
        float: Mean value
    
    Example:
        calculate_mean(np.array([1, 2, 3, 4, 5]))  # Returns 3.0
    """
    # np.mean() calculates the arithmetic mean: sum of elements / count
    # This is vectorized - works on entire array at once
    # Much faster than: sum(arr) / len(arr) for large arrays
    # In ML: we compute mean loss, mean accuracy, mean features, etc.
    return np.mean(arr)


def calculate_sum(arr):
    """
    Calculate the sum of all array elements.
    
    Summation is fundamental in mathematics and ML. Used in:
    - Loss functions (sum of errors)
    - Aggregations (sum of weights, gradients)
    - Counting operations
    
    Args:
        arr (np.ndarray): Input array
    
    Returns:
        int or float: Sum of elements
    
    Example:
        calculate_sum(np.array([1, 2, 3, 4, 5]))  # Returns 15
    """
    # np.sum() sums all elements in the array
    # This is highly optimized - can use SIMD instructions on CPU
    # Much faster than Python's built-in sum() for NumPy arrays
    # In ML: we sum losses, sum gradients, sum weights, etc.
    return np.sum(arr)


def normalize_array(arr):
    """
    Normalize array to have mean 0 and standard deviation 1.
    
    Normalization (also called standardization or z-score normalization) is
    crucial in machine learning. It ensures features are on the same scale,
    which helps algorithms converge faster and perform better.
    
    Formula: normalized = (arr - mean) / std
    
    This is a common preprocessing step in ML pipelines.
    
    Args:
        arr (np.ndarray): Input array
    
    Returns:
        np.ndarray: Normalized array (mean ≈ 0, std ≈ 1)
    
    Example:
        arr = np.array([1, 2, 3, 4, 5])
        normalize_array(arr)  # Returns array with mean ~0, std ~1
    """
    # Calculate mean of the array
    # Mean is the average value
    mean = np.mean(arr)
    
    # Calculate standard deviation
    # Std measures how spread out the values are
    # np.std() computes: sqrt(mean((arr - mean)**2))
    std = np.std(arr)
    
    # Normalize: subtract mean (centers data at 0), divide by std (scales to unit variance)
    # This is the z-score formula from statistics
    # After normalization:
    # - Mean becomes approximately 0
    # - Standard deviation becomes approximately 1
    # - Data is "standardized" to a common scale
    normalized = (arr - mean) / std
    
    return normalized
    
    # Why normalize in ML?
    # 1. Features on different scales (e.g., age 0-100, income 0-100000)
    #    can cause algorithms to favor larger-scale features
    # 2. Gradient descent converges faster when features are normalized
    # 3. Some algorithms (like k-means, neural networks) work better with normalized data


def elementwise_operation(arr1, arr2, operation='add'):
    """
    Perform element-wise operation between two arrays.
    
    Element-wise operations apply an operation to corresponding elements
    of two arrays. Both arrays must have the same shape (or be broadcastable).
    This is fundamental in linear algebra and ML.
    
    Args:
        arr1 (np.ndarray): First array
        arr2 (np.ndarray): Second array (same shape as arr1)
        operation (str): 'add', 'multiply', or 'subtract'
    
    Returns:
        np.ndarray: Result of element-wise operation
    
    Example:
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        elementwise_operation(arr1, arr2, 'add')  # Returns [5, 7, 9]
    """
    # Check which operation to perform
    if operation == 'add':
        # Element-wise addition: [a1, a2] + [b1, b2] = [a1+b1, a2+b2]
        # This is vector addition in linear algebra
        return arr1 + arr2
    
    elif operation == 'multiply':
        # Element-wise multiplication (Hadamard product): [a1, a2] * [b1, b2] = [a1*b1, a2*b2]
        # Note: This is NOT matrix multiplication (that's np.dot() or @)
        # Element-wise multiplication is used in many ML operations
        return arr1 * arr2
    
    elif operation == 'subtract':
        # Element-wise subtraction: [a1, a2] - [b1, b2] = [a1-b1, a2-b2]
        # Used for computing differences, errors, gradients, etc.
        return arr1 - arr2
    
    else:
        raise ValueError(f"Unknown operation: {operation}")
    
    # Key insight: All these operations are vectorized
    # They happen in parallel (conceptually) across all elements
    # This is why NumPy is fast - operations are implemented in C
    # and can use CPU vectorization instructions (SIMD)

