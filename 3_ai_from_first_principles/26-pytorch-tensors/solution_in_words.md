# Solution Explanation: PyTorch Tensors

## Overview

This project introduces PyTorch tensors, the foundation of all PyTorch operations. Tensors are similar to NumPy arrays but can run on GPU and support automatic differentiation.

## Key Concepts Explained

### PyTorch Tensors vs NumPy Arrays

**Similarities:**
- Similar API (familiar if you know NumPy)
- Support multi-dimensional arrays
- Element-wise and matrix operations

**Differences:**
- **GPU support**: Can run on GPU (much faster!)
- **Automatic differentiation**: Can compute gradients automatically
- **Neural network integration**: Built for deep learning

### Tensor Creation

**From Python lists:**
```python
tensor = torch.tensor([1, 2, 3, 4, 5])
```

**Pre-filled tensors:**
```python
zeros = torch.zeros(5)
ones = torch.ones(5)
rand = torch.randn(5)  # Random from normal distribution
```

**From NumPy:**
```python
numpy_array = np.array([1, 2, 3])
tensor = torch.from_numpy(numpy_array)
```

### GPU Acceleration

**Check availability:**
```python
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
```

**Move to GPU:**
```python
tensor_gpu = tensor.to(device)
# or shorthand
tensor_gpu = tensor.cuda()
```

**Why GPU?**
- **Much faster** for large matrix operations
- **Parallel processing**: GPUs have thousands of cores
- **Essential** for training deep networks

### Tensor Operations

**Element-wise:**
```python
result = tensor1 + tensor2
result = tensor1 * 2
result = tensor1 ** 2
```

**Matrix multiplication:**
```python
result = tensor1 @ tensor2
# or
result = torch.matmul(tensor1, tensor2)
```

**Shape manipulation:**
```python
reshaped = tensor.reshape(2, 3)
transposed = tensor.T
```

### NumPy Interoperability

**PyTorch → NumPy:**
```python
numpy_array = tensor.numpy()  # Must be on CPU!
```

**NumPy → PyTorch:**
```python
tensor = torch.from_numpy(numpy_array)
```

**Important:** Tensors on GPU cannot be converted directly to NumPy. Move to CPU first!

### Reproducibility

**Set random seed:**
```python
torch.manual_seed(42)  # CPU operations
torch.cuda.manual_seed_all(42)  # GPU operations
```

**Why important:**
- Ensures experiments are reproducible
- Critical for debugging and comparing results

## Implementation Details

### GPU Operations

```python
def move_to_gpu(tensor):
    if torch.cuda.is_available():
        device = 'cuda'
        tensor_gpu = tensor.to(device)
    else:
        device = 'cpu'
        tensor_gpu = tensor
    return tensor_gpu, device
```

**Key Points:**
- Always check GPU availability
- Use `.to(device)` for flexibility
- Operations on GPU tensors are automatically on GPU

### Performance Comparison

```python
# CPU timing
start = time.perf_counter()
result_cpu = torch.matmul(a_cpu, b_cpu)
cpu_time = time.perf_counter() - start

# GPU timing
torch.cuda.synchronize()  # Wait for previous operations
start = time.perf_counter()
result_gpu = torch.matmul(a_gpu, b_gpu)
torch.cuda.synchronize()  # Wait for GPU to finish
gpu_time = time.perf_counter() - start
```

**Key Points:**
- GPU operations are asynchronous
- Need `torch.cuda.synchronize()` for accurate timing
- GPU speedup increases with larger operations

## Common Pitfalls

1. **GPU tensor to NumPy**: Must move to CPU first!
2. **Forgetting synchronize**: GPU timing inaccurate without it
3. **Device mismatch**: Operations require tensors on same device
4. **Not setting seed**: Results not reproducible

## Real-World Application

**In Practice:**
- Always check GPU availability
- Move models and data to GPU for training
- Use CPU for small operations (overhead not worth it)
- Set random seeds for reproducibility
- Convert to NumPy only when needed (stays on GPU otherwise)

**Next Steps:**
- Project 32: Automatic differentiation (autograd)
- Project 33: Neural network modules
- All use tensors as foundation!

## Why This Matters

PyTorch tensors are the foundation of all PyTorch operations:
- Every neural network uses tensors
- GPU acceleration is essential for deep learning
- Understanding tensors helps debug and optimize

This project establishes the foundation for all PyTorch work!
