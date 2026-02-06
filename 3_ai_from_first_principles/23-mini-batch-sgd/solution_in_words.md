# Solution Explanation: Mini-Batch vs Stochastic Gradient Descent

## Overview

This project teaches the different ways to perform gradient descent based on how much data we use for each update. Understanding these variants is crucial for efficient training.

## Key Concepts Explained

### Three Variants of Gradient Descent

**1. Batch Gradient Descent:**
- Use entire dataset for each gradient update
- One update per epoch
- Stable gradients (low variance)
- Slow (especially for large datasets)
- Memory-intensive

**2. Stochastic Gradient Descent (SGD):**
- Use one example at a time
- Many updates per epoch (one per example)
- Noisy gradients (high variance)
- Fast updates
- Can escape local minima due to noise

**3. Mini-Batch Gradient Descent:**
- Use small batches (typically 32-256 examples)
- Multiple updates per epoch
- Balanced: stable enough, fast enough
- **Standard in practice**
- Works well with GPU parallelism

### Why Mini-Batch is Preferred

**Advantages:**
- **Balance**: Not too noisy (like SGD), not too slow (like Batch GD)
- **GPU efficiency**: GPUs excel at parallel batch processing
- **Stability**: Smoother convergence than SGD
- **Speed**: Faster than Batch GD

**Typical Batch Sizes:**
- Small datasets: 16-32
- Medium datasets: 32-128
- Large datasets: 128-512
- Limited memory: 8-16

### Batch Size Trade-offs

**Small Batch (SGD-like):**
- More updates per epoch → potentially faster convergence
- Noisier gradients → less stable
- Faster per update → better for large datasets
- Can escape local minima

**Large Batch:**
- Fewer updates per epoch → slower convergence
- Smoother gradients → more stable
- Slower per update → requires more memory
- More stable convergence

**Mini-Batch (32-256):**
- Good balance of all factors
- Standard choice in practice
- Works well with modern hardware

### Momentum

**Concept:**
- Accumulate velocity in direction of persistent gradients
- Helps overcome local minima
- Speeds convergence

**Mathematical Formulation:**
```
velocity = momentum * velocity + learning_rate * gradient
weights = weights - velocity
```

**Effect:**
- If gradients are consistent → velocity accumulates → larger steps
- If gradients change direction → velocity dampens → smaller steps
- Helps navigate loss landscape more efficiently

## Implementation Details

### Creating Batches

```python
def create_batches(X, y, batch_size, shuffle=True):
    n_samples = len(X)
    indices = np.arange(n_samples)
    
    if shuffle:
        np.random.shuffle(indices)
    
    batches = []
    for i in range(0, n_samples, batch_size):
        batch_indices = indices[i:i+batch_size]
        batches.append((X[batch_indices], y[batch_indices]))
    
    return batches
```

**Key Points:**
- Shuffle data to avoid order bias
- Handle remainder batch (last batch may be smaller)
- Return list of (batch_X, batch_y) tuples

### Mini-Batch Training Loop

```python
for epoch in range(epochs):
    batches = create_batches(X, y, batch_size)
    
    for batch_X, batch_y in batches:
        # Forward pass
        output = model.forward(batch_X)
        
        # Compute loss
        loss = compute_loss(output, batch_y)
        
        # Backward pass
        gradients = model.backward(batch_X, batch_y, output)
        
        # Update weights
        model.update(gradients, learning_rate)
```

**Key Points:**
- Process batches sequentially
- Update weights after each batch (not after full epoch)
- Shuffle batches each epoch

### Momentum Update

```python
def momentum_update(weights, gradients, velocity, learning_rate, momentum=0.9):
    # Update velocity: accumulate gradient direction
    velocity = momentum * velocity + learning_rate * gradients
    
    # Update weights: move in direction of velocity
    weights = weights - velocity
    
    return weights, velocity
```

**Key Points:**
- Velocity accumulates over time
- Momentum coefficient (typically 0.9) controls accumulation
- Larger momentum → more accumulation → faster convergence

## Common Pitfalls

1. **Not shuffling**: Order bias can hurt performance
2. **Batch size too large**: Slow convergence, memory issues
3. **Batch size too small**: Noisy gradients, slow convergence
4. **Forgetting remainder batch**: Losing data
5. **Not resetting velocity**: Momentum accumulates incorrectly

## Real-World Application

**In Practice:**
- Use mini-batch size 32-256 (standard)
- Shuffle data before each epoch
- Adjust batch size based on:
  - Dataset size
  - Available memory
  - GPU capacity
- Use momentum (0.9 is common)
- In PyTorch: `DataLoader` handles batching automatically

**In PyTorch (upcoming projects):**
- `DataLoader` creates batches automatically
- `batch_size` parameter controls size
- `shuffle=True` shuffles each epoch
- Momentum in optimizers: `torch.optim.SGD(..., momentum=0.9)`

## Why This Matters

Mini-batch gradient descent is **the standard** in deep learning:
- Used by default in all frameworks (PyTorch, TensorFlow)
- Understanding it helps choose appropriate batch sizes
- Essential for efficient training on large datasets
- Works well with GPU parallelism

This project bridges pure NumPy implementations to PyTorch's DataLoader, which uses mini-batch processing by default.
