"""
Project 31: PyTorch Tensors and GPU Fundamentals

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.

Note: You'll need to install PyTorch: pip install torch
"""

import torch
import numpy as np


def create_tensor_from_list(python_list):
    """
    Create a PyTorch tensor from a Python list.
    
    Args:
        python_list (list): Python list of numbers
    
    Returns:
        torch.Tensor: PyTorch tensor
    """
    # TODO: Convert Python list to PyTorch tensor
    # Use torch.tensor()
    return None


def create_zeros_tensor(shape):
    """
    Create a tensor filled with zeros.
    
    Args:
        shape (tuple): Shape of tensor, e.g., (3, 4)
    
    Returns:
        torch.Tensor: Tensor of zeros
    """
    # TODO: Create tensor of zeros using torch.zeros()
    return None


def create_random_tensor(shape):
    """
    Create a tensor with random values from standard normal distribution.
    
    Args:
        shape (tuple): Shape of tensor
    
    Returns:
        torch.Tensor: Random tensor
    """
    # TODO: Create random tensor using torch.randn()
    return None


def tensor_operations(tensor1, tensor2):
    """
    Perform basic operations on tensors.
    
    Args:
        tensor1 (torch.Tensor): First tensor
        tensor2 (torch.Tensor): Second tensor (same shape as tensor1)
    
    Returns:
        dict: Dictionary with keys 'add', 'multiply', 'dot_product'
            - 'add': Element-wise addition
            - 'multiply': Element-wise multiplication
            - 'dot_product': Dot product (if 1D) or matrix multiplication (if 2D)
    """
    # TODO: Perform operations
    return {
        'add': None,
        'multiply': None,
        'dot_product': None
    }


def reshape_tensor(tensor, new_shape):
    """
    Reshape a tensor to new dimensions.
    
    Args:
        tensor (torch.Tensor): Input tensor
        new_shape (tuple): Desired shape
    
    Returns:
        torch.Tensor: Reshaped tensor
    """
    # TODO: Reshape tensor using .reshape() or .view()
    return None


def get_tensor_shape(tensor):
    """
    Get the shape of a tensor.
    
    Args:
        tensor (torch.Tensor): Input tensor
    
    Returns:
        torch.Size: Shape of tensor (can be converted to tuple)
    """
    # TODO: Get tensor shape
    return None


def move_to_gpu(tensor):
    """
    Move tensor to GPU if available, otherwise return on CPU.
    
    Args:
        tensor (torch.Tensor): Input tensor
    
    Returns:
        torch.Tensor: Tensor on GPU (if available) or CPU
        str: Device name ('cuda' or 'cpu')
    """
    # TODO: Check if CUDA is available
    # Move tensor to GPU if available, otherwise keep on CPU
    # Return tensor and device name
    device = None
    tensor_gpu = None
    return tensor_gpu, device


def tensor_to_numpy(tensor):
    """
    Convert PyTorch tensor to NumPy array.
    
    Args:
        tensor (torch.Tensor): Input tensor
    
    Returns:
        np.ndarray: NumPy array
    
    Note:
        - Tensor must be on CPU (not GPU)
        - Use .cpu() if needed, then .numpy()
    """
    # TODO: Convert tensor to NumPy array
    # Make sure tensor is on CPU first!
    return None


def numpy_to_tensor(numpy_array):
    """
    Convert NumPy array to PyTorch tensor.
    
    Args:
        numpy_array (np.ndarray): Input NumPy array
    
    Returns:
        torch.Tensor: PyTorch tensor
    """
    # TODO: Convert NumPy array to tensor using torch.from_numpy()
    return None


def compare_cpu_gpu_performance(size=(1000, 1000)):
    """
    Compare performance of matrix multiplication on CPU vs GPU.
    
    Args:
        size (tuple): Size of matrices to multiply
    
    Returns:
        dict: Dictionary with 'cpu_time', 'gpu_time', 'speedup'
            - 'cpu_time': Time on CPU (seconds)
            - 'gpu_time': Time on GPU (seconds, None if GPU unavailable)
            - 'speedup': GPU speedup factor (None if GPU unavailable)
    
    Note:
        Use time.time() or time.perf_counter() for timing
        GPU operations are asynchronous, may need torch.cuda.synchronize()
    """
    import time
    
    # TODO: Create random matrices
    # Time matrix multiplication on CPU
    # Time matrix multiplication on GPU (if available)
    # Compute speedup
    return {
        'cpu_time': None,
        'gpu_time': None,
        'speedup': None
    }


def set_random_seed(seed=42):
    """
    Set random seed for reproducibility.
    
    Args:
        seed (int): Random seed value
    
    Note:
        Use torch.manual_seed() for CPU operations
        Use torch.cuda.manual_seed_all() for GPU operations (if available)
    """
    # TODO: Set random seeds for reproducibility
    pass
