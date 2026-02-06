"""
Project 31: PyTorch Tensors - SOLUTION

Complete solution demonstrating PyTorch tensor fundamentals.
"""

import torch
import numpy as np
import time


def create_tensor_from_list(python_list):
    """Create a PyTorch tensor from a Python list."""
    return torch.tensor(python_list)


def create_zeros_tensor(shape):
    """Create a tensor filled with zeros."""
    return torch.zeros(shape)


def create_random_tensor(shape):
    """Create a tensor with random values."""
    return torch.randn(shape)


def tensor_operations(tensor1, tensor2):
    """Perform basic operations on tensors."""
    return {
        'add': tensor1 + tensor2,
        'multiply': tensor1 * tensor2,
        'dot_product': torch.matmul(tensor1, tensor2) if tensor1.dim() > 1 else torch.dot(tensor1, tensor2)
    }


def reshape_tensor(tensor, new_shape):
    """Reshape a tensor to new dimensions."""
    return tensor.reshape(new_shape)


def get_tensor_shape(tensor):
    """Get the shape of a tensor."""
    return tensor.shape


def move_to_gpu(tensor):
    """Move tensor to GPU if available."""
    if torch.cuda.is_available():
        device = 'cuda'
        tensor_gpu = tensor.to(device)
    else:
        device = 'cpu'
        tensor_gpu = tensor
    
    return tensor_gpu, device


def tensor_to_numpy(tensor):
    """Convert PyTorch tensor to NumPy array."""
    # Make sure tensor is on CPU
    if tensor.is_cuda:
        tensor = tensor.cpu()
    return tensor.numpy()


def numpy_to_tensor(numpy_array):
    """Convert NumPy array to PyTorch tensor."""
    return torch.from_numpy(numpy_array)


def compare_cpu_gpu_performance(size=(1000, 1000)):
    """Compare performance of matrix multiplication on CPU vs GPU."""
    # Create random matrices
    a_cpu = torch.randn(size[0], size[1])
    b_cpu = torch.randn(size[1], size[0])
    
    # CPU timing
    start = time.perf_counter()
    result_cpu = torch.matmul(a_cpu, b_cpu)
    cpu_time = time.perf_counter() - start
    
    gpu_time = None
    speedup = None
    
    # GPU timing (if available)
    if torch.cuda.is_available():
        a_gpu = a_cpu.cuda()
        b_gpu = b_cpu.cuda()
        
        # Synchronize before timing
        torch.cuda.synchronize()
        start = time.perf_counter()
        result_gpu = torch.matmul(a_gpu, b_gpu)
        torch.cuda.synchronize()  # Wait for GPU to finish
        gpu_time = time.perf_counter() - start
        
        speedup = cpu_time / gpu_time if gpu_time > 0 else None
    
    return {
        'cpu_time': cpu_time,
        'gpu_time': gpu_time,
        'speedup': speedup
    }


def set_random_seed(seed=42):
    """Set random seed for reproducibility."""
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


# Example usage
if __name__ == "__main__":
    print("PyTorch Tensors Demo")
    print("=" * 50)
    
    # Create tensors
    tensor = create_tensor_from_list([1, 2, 3, 4, 5])
    print(f"Tensor from list: {tensor}")
    
    zeros = create_zeros_tensor((3, 4))
    print(f"\nZeros tensor shape: {zeros.shape}")
    
    # GPU operations
    tensor_gpu, device = move_to_gpu(torch.randn(5))
    print(f"\nTensor on device: {device}")
    
    # Performance comparison
    if torch.cuda.is_available():
        perf = compare_cpu_gpu_performance(size=(500, 500))
        print(f"\nCPU time: {perf['cpu_time']:.4f}s")
        print(f"GPU time: {perf['gpu_time']:.4f}s")
        print(f"Speedup: {perf['speedup']:.2f}x")
    else:
        print("\nGPU not available for performance comparison")
