# Automatic Differentiation from Scratch

> Building backpropagation intuition by implementing reverse-mode autodiff

---

## What is Automatic Differentiation?

**Automatic differentiation (AD)** computes derivatives automatically and efficiently—neither symbolic (like Mathematica) nor numerical (finite differences), but exact and fast.

### Three Ways to Compute Derivatives

| Method | How It Works | Pros | Cons |
|--------|--------------|------|------|
| **Symbolic** | Algebraic manipulation (∂/∂x rules) | Exact, mathematical | Slow, expression swell |
| **Numerical** | Finite differences: (f(x+h)-f(x))/h | Easy to implement | Slow, numerical error |
| **Automatic** | Chain rule on computation graph | Exact + fast | Requires framework |

**Autodiff is what PyTorch, TensorFlow, and JAX use** for backpropagation.

---

## The Core Idea: Computation Graphs

Every calculation can be represented as a **directed acyclic graph (DAG)**:

```
Example: f(x,y) = (x + y) * (x - 2)

Computation graph:
     x       y
      \     /
       \   /
        add   x    2
          \   |   /
           \  |  /
            \ | /
             sub
              |
             mul  →  output
```

Each node:
- Stores a **value** (forward pass)
- Stores a **gradient** (backward pass)
- Knows its **parents** (for backprop)
- Has a **local derivative function**

---

## Forward Pass: Build the Graph

```python
# Pseudo-code
z = x + y      # Create node: z = Add(x, y)
w = x - 2      # Create node: w = Sub(x, 2)
out = z * w    # Create node: out = Mul(z, w)
```

Each operation creates a new node and stores:
1. The computed value
2. References to parent nodes
3. The operation type (for backward pass)

---

## Backward Pass: Propagate Gradients

Starting from the output, apply the **chain rule** backwards:

```
If y = f(u) and u = g(x):
dy/dx = (dy/du) * (du/dx)
```

### Algorithm (Reverse Topological Order)
1. Set grad of output node to 1.0 (∂L/∂L = 1)
2. For each node in reverse order:
   - Compute local gradients
   - Accumulate to parent nodes

### Example: out = (x + y) * (x - 2)

**Forward**:
```
x = 3, y = 4
z = x + y = 7
w = x - 2 = 1
out = z * w = 7
```

**Backward** (compute ∂out/∂x and ∂out/∂y):
```
∂out/∂out = 1.0                    # Base case

∂out/∂z = w = 1                    # ∂(z*w)/∂z = w
∂out/∂w = z = 7                    # ∂(z*w)/∂w = z

∂out/∂x (via z) = ∂out/∂z * ∂z/∂x = 1 * 1 = 1
∂out/∂x (via w) = ∂out/∂w * ∂w/∂x = 7 * 1 = 7
∂out/∂x (total) = 1 + 7 = 8        # Sum from all paths!

∂out/∂y = ∂out/∂z * ∂z/∂y = 1 * 1 = 1
```

**Key insight**: Gradients **accumulate** when a variable has multiple paths.

---

## Implementation: MicroGrad-Style

### Step 1: The Tensor Class

```python
class Tensor:
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None  # Function to compute grads
        self._prev = set(_children)    # Parent nodes
        self._op = _op                 # Operation name (for debugging)

    def __repr__(self):
        return f"Tensor(data={self.data}, grad={self.grad})"
```

### Step 2: Define Operations

```python
def __add__(self, other):
    other = other if isinstance(other, Tensor) else Tensor(other)
    out = Tensor(self.data + other.data, (self, other), '+')

    def _backward():
        self.grad += out.grad          # ∂(a+b)/∂a = 1
        other.grad += out.grad         # ∂(a+b)/∂b = 1
    out._backward = _backward

    return out

def __mul__(self, other):
    other = other if isinstance(other, Tensor) else Tensor(other)
    out = Tensor(self.data * other.data, (self, other), '*')

    def _backward():
        self.grad += other.data * out.grad   # ∂(a*b)/∂a = b
        other.grad += self.data * out.grad   # ∂(a*b)/∂b = a
    out._backward = _backward

    return out
```

**Pattern**: Each operation stores a closure that knows how to backpropagate gradients.

### Step 3: The Backward Pass

```python
def backward(self):
    # Topological sort
    topo = []
    visited = set()
    def build_topo(v):
        if v not in visited:
            visited.add(v)
            for child in v._prev:
                build_topo(child)
            topo.append(v)
    build_topo(self)

    # Backward pass
    self.grad = 1.0
    for node in reversed(topo):
        node._backward()
```

**Topological sort** ensures we process nodes in the right order (children before parents).

### Usage Example

```python
x = Tensor(3.0)
y = Tensor(4.0)

z = x + y          # z = 7
w = x - 2          # w = 1
out = z * w        # out = 7

out.backward()

print(x.grad)      # 8.0
print(y.grad)      # 1.0
```

---

## More Operations

### Subtraction
```python
def __sub__(self, other):
    return self + (-other)

def __neg__(self):
    return self * -1
```

### Power
```python
def __pow__(self, power):
    out = Tensor(self.data ** power, (self,), f'**{power}')

    def _backward():
        self.grad += power * (self.data ** (power-1)) * out.grad
    out._backward = _backward

    return out
```

### ReLU (Non-linear Activation)
```python
def relu(self):
    out = Tensor(max(0, self.data), (self,), 'ReLU')

    def _backward():
        self.grad += (out.data > 0) * out.grad  # Derivative: 1 if x>0, else 0
    out._backward = _backward

    return out
```

### Exponential
```python
import math

def exp(self):
    out = Tensor(math.exp(self.data), (self,), 'exp')

    def _backward():
        self.grad += out.data * out.grad  # ∂e^x/∂x = e^x
    out._backward = _backward

    return out
```

---

## Extending to Vectors (Mini-NumPy)

For neural networks, we need **tensor operations**:

```python
import numpy as np

class Tensor:
    def __init__(self, data, requires_grad=False):
        self.data = np.array(data, dtype=np.float32)
        self.grad = None if not requires_grad else np.zeros_like(self.data)
        self.requires_grad = requires_grad
        self._backward = lambda: None
        self._prev = []

    def backward(self, gradient=None):
        if gradient is None:
            gradient = np.ones_like(self.data)  # For scalar output
        self.grad += gradient
        # ... topological sort and backward pass
```

**Broadcasting** (like NumPy) is crucial:
```python
A = Tensor([[1, 2], [3, 4]])   # (2, 2)
B = Tensor([10, 20])           # (2,)
C = A + B                       # (2, 2) - broadcast B to each row
```

---

## Neural Network with Autodiff

### Layer: y = Wx + b

```python
class Layer:
    def __init__(self, n_in, n_out):
        self.W = Tensor(np.random.randn(n_in, n_out) * 0.01, requires_grad=True)
        self.b = Tensor(np.zeros(n_out), requires_grad=True)

    def __call__(self, x):
        return x @ self.W + self.b  # @ is matrix multiply
```

### Training Loop

```python
# Model
layer1 = Layer(2, 4)   # 2 inputs -> 4 hidden
layer2 = Layer(4, 1)   # 4 hidden -> 1 output

# Training
for epoch in range(1000):
    # Forward
    h = layer1(x_train).relu()
    y_pred = layer2(h)

    # Loss
    loss = ((y_pred - y_train) ** 2).mean()

    # Backward
    loss.backward()

    # Update (simple SGD)
    for param in [layer1.W, layer1.b, layer2.W, layer2.b]:
        param.data -= learning_rate * param.grad
        param.grad.zero_()  # Reset gradients!
```

---

## Key Challenges & Solutions

### 1. Gradient Accumulation
**Problem**: A node used multiple times must sum gradients.

**Solution**: Use `+=` not `=` when backpropagating.

### 2. Scalar vs Vector Grads
**Problem**: Broadcasting changes gradient shapes.

**Solution**: Sum gradients along broadcasted dimensions.

```python
# If forward broadcast (2,) -> (3,2), backward must sum to (2,)
grad_input = grad_output.sum(axis=0)
```

### 3. In-Place Operations
**Problem**: Modifying tensors in-place breaks the graph.

**Solution**: Always create new tensors for operations.

### 4. Memory Leaks
**Problem**: Holding references to entire graph.

**Solution**: Detach intermediate values not needed for backprop.

---

## Numerical Gradient Checking

**Always verify your autodiff with finite differences**:

```python
def numerical_grad(f, x, h=1e-5):
    """Compute f'(x) numerically."""
    return (f(x + h) - f(x - h)) / (2 * h)

# Check
x = Tensor(3.0)
f = lambda x: x ** 2 + 2 * x

# Autodiff
y = f(x)
y.backward()
print(x.grad)  # Should be 2x + 2 = 8

# Numerical
print(numerical_grad(lambda val: (val ** 2 + 2 * val).data, x.data))  # ~8.0
```

---

## From MicroGrad to PyTorch

| Feature | MicroGrad | PyTorch |
|---------|-----------|---------|
| Graph | Explicit nodes | Implicit (dynamic) |
| Backward | Manual topo sort | `loss.backward()` |
| GPU | CPU only | `.to('cuda')` |
| Ops | 10-20 ops | 1000+ optimized ops |
| Performance | Educational | Production-ready |

**PyTorch uses the same core ideas**, just with:
- C++ backend for speed
- CUDA kernels for GPU
- Advanced optimizations (operator fusion, etc.)

---

## Related Projects

- [Project 23: Manual Backpropagation](./project-23-manual-backpropagation/)
- [Project 24: Autodiff Engine](./project-24-autodiff-engine/)
- [Project 25: MLP from Scratch](./project-25-mlp-from-scratch/)
- [Project 32: PyTorch Autograd](./project-32-pytorch-autograd/)

---

## Further Reading

- [micrograd](https://github.com/karpathy/micrograd) by Andrej Karpathy
- *Automatic Differentiation in Machine Learning: A Survey* (Baydin et al., 2018)
- PyTorch autograd internals

---

*"Backpropagation is just the chain rule applied systematically."*

Last updated: 2025-11-16
