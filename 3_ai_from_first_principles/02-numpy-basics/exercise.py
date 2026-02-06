"""
Project 16: NumPy 101 – Arrays and Vectorized Operations

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.

Note: You'll need to install numpy: pip install numpy
"""

import numpy as np


def create_array_from_list(python_list):
    """
    Create a NumPy array from a Python list.
    
    Args:
        python_list (list): Python list of numbers
    
    Returns:
        np.ndarray: NumPy array
    """
    # TODO: Convert Python list to NumPy array
    return None


def create_zeros_array(size):
    """
    Create an array filled with zeros.
    
    Args:
        size (int): Size of array
    
    Returns:
        np.ndarray: Array of zeros
    """
    # TODO: Create array of zeros using np.zeros()
    return None


def create_range_array(start, stop, step=1):
    """
    Create an array with values from start to stop (exclusive) with given step.
    
    Args:
        start (int): Start value
        stop (int): Stop value (exclusive)
        step (int): Step size (default 1)
    
    Returns:
        np.ndarray: Array of values
    """
    # TODO: Use np.arange() to create array
    return None


def vectorized_add(arr, value):
    """
    Add a value to every element in the array using vectorization.
    
    Args:
        arr (np.ndarray): Input array
        value (int or float): Value to add
    
    Returns:
        np.ndarray: Array with value added to each element
    """
    # TODO: Add value to entire array (no loop!)
    return None


def vectorized_multiply(arr, value):
    """
    Multiply every element by a value using vectorization.
    
    Args:
        arr (np.ndarray): Input array
        value (int or float): Value to multiply by
    
    Returns:
        np.ndarray: Array with each element multiplied
    """
    # TODO: Multiply entire array by value (no loop!)
    return None


def vectorized_square(arr):
    """
    Square every element in the array using vectorization.
    
    Args:
        arr (np.ndarray): Input array
    
    Returns:
        np.ndarray: Array with each element squared
    """
    # TODO: Square each element (use ** operator)
    return None


def get_array_shape(arr):
    """
    Get the shape (dimensions) of an array.
    
    Args:
        arr (np.ndarray): Input array
    
    Returns:
        tuple: Shape of array
    """
    # TODO: Return array shape
    return None


def reshape_array(arr, new_shape):
    """
    Reshape an array to new dimensions.
    
    Args:
        arr (np.ndarray): Input array
        new_shape (tuple): Desired shape (e.g., (2, 3))
    
    Returns:
        np.ndarray: Reshaped array
    """
    # TODO: Reshape array to new_shape
    return None


def calculate_mean(arr):
    """
    Calculate the mean (average) of array elements.
    
    Args:
        arr (np.ndarray): Input array
    
    Returns:
        float: Mean value
    """
    # TODO: Use np.mean() to calculate mean
    return None


def calculate_sum(arr):
    """
    Calculate the sum of all array elements.
    
    Args:
        arr (np.ndarray): Input array
    
    Returns:
        int or float: Sum of elements
    """
    # TODO: Use np.sum() to calculate sum
    return None


def normalize_array(arr):
    """
    Normalize array to have mean 0 and standard deviation 1.
    
    Formula: (arr - mean) / std
    
    Args:
        arr (np.ndarray): Input array
    
    Returns:
        np.ndarray: Normalized array
    """
    # TODO: Calculate mean and std, then normalize
    # Hint: Use np.mean() and np.std()
    return None


def elementwise_operation(arr1, arr2, operation='add'):
    """
    Perform element-wise operation between two arrays.
    
    Args:
        arr1 (np.ndarray): First array
        arr2 (np.ndarray): Second array (same shape as arr1)
        operation (str): 'add', 'multiply', or 'subtract'
    
    Returns:
        np.ndarray: Result of element-wise operation
    """
    # TODO: Perform element-wise operation
    # Hint: Use if/elif to check operation type
    return None

