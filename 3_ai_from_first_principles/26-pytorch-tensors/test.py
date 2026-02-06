"""
Test suite for Project 31: PyTorch Tensors

Run with: pytest test.py -v
"""

import pytest
import torch
import numpy as np
from exercise import (
    create_tensor_from_list,
    create_zeros_tensor,
    create_random_tensor,
    tensor_operations,
    reshape_tensor,
    get_tensor_shape,
    move_to_gpu,
    tensor_to_numpy,
    numpy_to_tensor,
    compare_cpu_gpu_performance,
    set_random_seed,
)


class TestTensorCreation:
    """Test tensor creation functions."""
    
    def test_create_from_list(self):
        """Test creating tensor from Python list."""
        result = create_tensor_from_list([1, 2, 3, 4, 5])
        assert isinstance(result, torch.Tensor)
        assert torch.equal(result, torch.tensor([1, 2, 3, 4, 5]))
    
    def test_create_zeros(self):
        """Test creating zeros tensor."""
        result = create_zeros_tensor((3, 4))
        assert result.shape == (3, 4)
        assert torch.all(result == 0)
    
    def test_create_random(self):
        """Test creating random tensor."""
        result = create_random_tensor((5, 5))
        assert result.shape == (5, 5)
        # Random values should not all be the same
        assert not torch.all(result == result[0, 0])


class TestTensorOperations:
    """Test tensor operations."""
    
    def test_tensor_operations(self):
        """Test basic tensor operations."""
        t1 = torch.tensor([1.0, 2.0, 3.0])
        t2 = torch.tensor([4.0, 5.0, 6.0])
        
        result = tensor_operations(t1, t2)
        
        assert torch.equal(result['add'], t1 + t2)
        assert torch.equal(result['multiply'], t1 * t2)
        assert abs(result['dot_product'] - torch.dot(t1, t2).item()) < 0.001
    
    def test_matrix_multiplication(self):
        """Test matrix multiplication."""
        t1 = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
        t2 = torch.tensor([[5.0, 6.0], [7.0, 8.0]])
        
        result = tensor_operations(t1, t2)
        expected = torch.matmul(t1, t2)
        assert torch.allclose(result['dot_product'], expected)


class TestShapeManipulation:
    """Test shape manipulation."""
    
    def test_reshape_tensor(self):
        """Test reshaping tensor."""
        tensor = torch.arange(12)
        result = reshape_tensor(tensor, (3, 4))
        
        assert result.shape == (3, 4)
        assert torch.equal(result.flatten(), tensor)
    
    def test_get_shape(self):
        """Test getting tensor shape."""
        tensor = torch.randn(2, 3, 4)
        shape = get_tensor_shape(tensor)
        
        assert shape == torch.Size((2, 3, 4))
        assert tuple(shape) == (2, 3, 4)


class TestGPUOperations:
    """Test GPU operations."""
    
    def test_move_to_gpu(self):
        """Test moving tensor to GPU."""
        tensor = torch.tensor([1.0, 2.0, 3.0])
        tensor_gpu, device = move_to_gpu(tensor)
        
        assert isinstance(tensor_gpu, torch.Tensor)
        assert device in ['cuda', 'cpu']
        
        if torch.cuda.is_available():
            assert tensor_gpu.device.type == 'cuda'
        else:
            assert tensor_gpu.device.type == 'cpu'


class TestNumPyConversion:
    """Test NumPy conversion."""
    
    def test_tensor_to_numpy(self):
        """Test converting tensor to NumPy."""
        tensor = torch.tensor([1.0, 2.0, 3.0])
        numpy_array = tensor_to_numpy(tensor)
        
        assert isinstance(numpy_array, np.ndarray)
        assert np.array_equal(numpy_array, [1.0, 2.0, 3.0])
    
    def test_numpy_to_tensor(self):
        """Test converting NumPy to tensor."""
        numpy_array = np.array([1.0, 2.0, 3.0])
        tensor = numpy_to_tensor(numpy_array)
        
        assert isinstance(tensor, torch.Tensor)
        assert torch.equal(tensor, torch.tensor([1.0, 2.0, 3.0]))


class TestPerformance:
    """Test performance comparison."""
    
    def test_compare_cpu_gpu(self):
        """Test CPU vs GPU performance comparison."""
        result = compare_cpu_gpu_performance(size=(100, 100))
        
        assert 'cpu_time' in result
        assert result['cpu_time'] > 0
        
        if torch.cuda.is_available():
            assert 'gpu_time' in result
            assert result['gpu_time'] is not None
            assert result['speedup'] is not None
            # GPU should be faster (or at least not slower)
            assert result['speedup'] >= 0.5  # Allow some variance


class TestReproducibility:
    """Test random seed setting."""
    
    def test_set_random_seed(self):
        """Test that setting seed produces reproducible results."""
        set_random_seed(42)
        tensor1 = torch.randn(5)
        
        set_random_seed(42)
        tensor2 = torch.randn(5)
        
        # Should be identical with same seed
        assert torch.allclose(tensor1, tensor2)
