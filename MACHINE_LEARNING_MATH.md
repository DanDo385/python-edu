# Machine Learning Mathematics

> Essential linear algebra, calculus, and probability for deep learning

---

## Table of Contents
1. [Linear Algebra Foundations](#linear-algebra-foundations)
2. [Calculus for ML](#calculus-for-ml)
3. [Probability & Statistics](#probability-statistics)
4. [Numerical Stability](#numerical-stability)

---

## Linear Algebra Foundations

### Vectors
**Definition**: Ordered list of numbers (1D tensor)

```python
import numpy as np
v = np.array([1, 2, 3])  # Column vector (3,)
```

**Operations**:
```python
# Addition (element-wise)
v1 + v2  # [a₁+b₁, a₂+b₂, ...]

# Scalar multiplication
2 * v  # [2a₁, 2a₂, ...]

# Dot product (inner product)
np.dot(v1, v2)  # Σ(aᵢ * bᵢ) → scalar
# Geometric: v1·v2 = ||v1|| ||v2|| cos(θ)

# Norm (magnitude)
np.linalg.norm(v)  # √(Σvᵢ²)  - L2 norm (Euclidean)
np.linalg.norm(v, 1)  # Σ|vᵢ|  - L1 norm (Manhattan)
```

**ML Context**: Feature vectors, embeddings, weight vectors

### Matrices
**Definition**: 2D array of numbers (2D tensor)

```python
A = np.array([[1, 2], [3, 4]])  # Shape: (2, 2)
```

**Operations**:
```python
# Element-wise (Hadamard product)
A * B  # [aᵢⱼ * bᵢⱼ]

# Matrix multiplication
A @ B  # Valid if A is (m,n) and B is (n,p) → (m,p)
C[i,j] = Σₖ A[i,k] * B[k,j]

# Transpose
A.T  # Swap rows and columns: Aᵀ[i,j] = A[j,i]

# Inverse (A⁻¹)
np.linalg.inv(A)  # A @ A⁻¹ = I (identity)
# Only exists if det(A) ≠ 0 (non-singular)

# Solving linear systems: Ax = b
x = np.linalg.solve(A, b)  # More stable than inv(A) @ b
```

**Matrix Properties**:
- **Symmetric**: A = Aᵀ (e.g., covariance matrices)
- **Orthogonal**: AᵀA = I (columns are orthonormal)
- **Positive Definite**: xᵀAx > 0 for all x ≠ 0 (common in optimization)

**ML Context**:
- Weight matrices in neural networks
- Input: X is (batch_size, features)
- Weights: W is (features, hidden_units)
- Output: X @ W is (batch_size, hidden_units)

### Eigenvalues & Eigenvectors
**Definition**: Av = λv, where λ is eigenvalue, v is eigenvector

```python
eigenvalues, eigenvectors = np.linalg.eig(A)
```

**Intuition**: Eigenvectors are directions where linear transform A only scales

**ML Context**:
- PCA (Principal Component Analysis): Eigenvectors of covariance matrix
- Understanding model behavior (stability, convergence)

### Matrix Factorization
**Singular Value Decomposition (SVD)**:
```
A = UΣVᵀ
U: Left singular vectors (m×m, orthogonal)
Σ: Singular values (m×n, diagonal)
V: Right singular vectors (n×n, orthogonal)
```

```python
U, S, Vt = np.linalg.svd(A)
```

**Applications**:
- Dimensionality reduction
- Recommender systems (matrix completion)
- Low-rank approximations

---

## Calculus for ML

### Derivatives (Univariate)
**Definition**: Rate of change, slope of tangent

```
f'(x) = df/dx = lim[h→0] (f(x+h) - f(x)) / h
```

**Rules**:
```
Power rule: d/dx(xⁿ) = nxⁿ⁻¹
Sum: d/dx(f+g) = f' + g'
Product: d/dx(fg) = f'g + fg'
Chain: d/dx(f(g(x))) = f'(g(x)) · g'(x)
```

**Common Derivatives**:
```python
# f(x)          # f'(x)
x**n           # n * x**(n-1)
np.exp(x)      # np.exp(x)
np.log(x)      # 1 / x
np.sin(x)      # np.cos(x)
1 / x          # -1 / x**2
```

### Partial Derivatives (Multivariate)
**Definition**: Derivative with respect to one variable, holding others constant

```
∂f/∂x: Partial derivative of f w.r.t x
```

**Example**:
```python
f(x, y) = x² + 3xy + y²
∂f/∂x = 2x + 3y
∂f/∂y = 3x + 2y
```

### Gradient (∇)
**Definition**: Vector of all partial derivatives

```
∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]
```

**Intuition**: Points in direction of steepest ascent

**Gradient Descent** (optimization):
```python
# Minimize f(θ) by iteratively updating:
θ = θ - α * ∇f(θ)
# α: learning rate (step size)
```

**Example**:
```python
# f(x,y) = x² + y²
# ∇f = [2x, 2y]

x, y = 10, 10
alpha = 0.1
for _ in range(100):
    grad_x = 2 * x
    grad_y = 2 * y
    x -= alpha * grad_x
    y -= alpha * grad_y
# Converges to (0, 0), the minimum
```

### Chain Rule (Crucial for Backpropagation)
**Univariate**:
```
If y = f(u) and u = g(x), then:
dy/dx = (dy/du) * (du/dx)
```

**Multivariate** (Total Derivative):
```
If z = f(x, y), x = g(t), y = h(t):
dz/dt = (∂z/∂x)*(dx/dt) + (∂z/∂y)*(dy/dt)
```

**Neural Network Example**:
```
Forward: x → (Wx+b) → σ(·) → y → L(y, target)
Backward (chain rule):
∂L/∂W = (∂L/∂y) * (∂y/∂z) * (∂z/∂W)
         ↑         ↑         ↑
      loss'   activation'  input
```

### Jacobian Matrix
**Definition**: Matrix of all first-order partial derivatives

```
For f: ℝⁿ → ℝᵐ
J = [∂fᵢ/∂xⱼ]  (m × n matrix)
```

**Example**:
```python
f₁(x,y) = x² + y
f₂(x,y) = xy
# Jacobian:
# [∂f₁/∂x  ∂f₁/∂y]   [2x  1]
# [∂f₂/∂x  ∂f₂/∂y] = [y   x]
```

**ML Context**: Gradient of vector-valued functions (batch gradients)

### Hessian Matrix
**Definition**: Matrix of second-order partial derivatives

```
H = [∂²f/∂xᵢ∂xⱼ]
```

**ML Context**:
- Second-order optimization (Newton's method)
- Analyzing loss surface curvature

---

## Probability & Statistics

### Probability Basics
**Random Variable**: Variable whose value is random
- **Discrete**: P(X=x) (e.g., coin flip)
- **Continuous**: p(x) is probability density

**Expectation** (mean):
```
E[X] = Σ x·P(X=x)  (discrete)
E[X] = ∫ x·p(x)dx  (continuous)
```

**Variance**:
```
Var(X) = E[(X - E[X])²] = E[X²] - (E[X])²
```

### Common Distributions
**Bernoulli** (single coin flip):
```
P(X=1) = p
P(X=0) = 1-p
```

**Gaussian (Normal)**:
```
p(x) = (1/√(2πσ²)) * exp(-(x-μ)²/(2σ²))
μ: mean, σ²: variance
```

**ML Context**:
- Initialization: W ~ N(0, σ²)
- Noise modeling
- Bayesian inference

### Maximum Likelihood Estimation (MLE)
**Goal**: Find parameters θ that maximize P(data | θ)

```python
# Example: Estimate μ for Gaussian
# MLE for μ: mean of data
mu_mle = np.mean(data)
```

**Connection to Loss Functions**:
- **MSE** ≡ MLE with Gaussian noise
- **Cross-Entropy** ≡ MLE for classification (Bernoulli/Categorical)

---

## Numerical Stability

### Common Issues

**1. Overflow/Underflow**:
```python
# BAD: exp(1000) → inf
# GOOD: Use log-space
log_prob = 1000
prob = np.exp(np.clip(log_prob, -500, 500))
```

**2. Softmax Stability**:
```python
# BAD: exp can overflow
def softmax_unstable(x):
    return np.exp(x) / np.sum(np.exp(x))

# GOOD: Subtract max before exp
def softmax(x):
    x_max = np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x - x_max)
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)
```

**3. Log-Sum-Exp Trick**:
```python
# Compute log(Σ exp(xᵢ)) stably
def logsumexp(x):
    x_max = np.max(x)
    return x_max + np.log(np.sum(np.exp(x - x_max)))
```

**4. Vanishing Gradients**:
- **Problem**: Gradients → 0 in deep networks (sigmoid saturation)
- **Solutions**: ReLU, batch norm, residual connections, gradient clipping

**5. Exploding Gradients**:
- **Problem**: Gradients → ∞ (long sequences in RNNs)
- **Solutions**: Gradient clipping, LSTM/GRU, smaller learning rates

### Numerical Precision
```python
# Float32 (typical for DL):
# Range: ~1e-38 to 1e38
# Precision: ~7 decimal digits

# Float64 (double):
# Better precision but 2x memory

# Check equality with tolerance
np.allclose(a, b, rtol=1e-5, atol=1e-8)
```

---

## Essential Formulas for Neural Networks

### Activation Functions & Derivatives
```python
# Sigmoid
σ(x) = 1 / (1 + exp(-x))
σ'(x) = σ(x) * (1 - σ(x))

# Tanh
tanh(x) = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
tanh'(x) = 1 - tanh²(x)

# ReLU
ReLU(x) = max(0, x)
ReLU'(x) = 1 if x > 0 else 0

# Softmax (for class i)
softmax(xᵢ) = exp(xᵢ) / Σⱼ exp(xⱼ)
∂softmax(xᵢ)/∂xⱼ = softmax(xᵢ) * (δᵢⱼ - softmax(xⱼ))
```

### Loss Functions & Derivatives
```python
# Mean Squared Error (regression)
MSE = (1/n) * Σ(yᵢ - ŷᵢ)²
∂MSE/∂ŷᵢ = (2/n) * (ŷᵢ - yᵢ)

# Binary Cross-Entropy (binary classification)
BCE = -Σ [y*log(ŷ) + (1-y)*log(1-ŷ)]
∂BCE/∂ŷ = -y/ŷ + (1-y)/(1-ŷ)

# Categorical Cross-Entropy (multi-class)
CCE = -Σᵢ yᵢ * log(ŷᵢ)  (y is one-hot)
∂CCE/∂ŷᵢ = -yᵢ/ŷᵢ

# Combined Softmax + CCE (simpler derivative!)
∂(CCE∘Softmax)/∂zᵢ = ŷᵢ - yᵢ
```

### Matrix Calculus Rules
```python
# Linear layer: z = Wx + b
∂z/∂W = x (input)
∂z/∂x = W
∂z/∂b = 1

# For scalar loss L:
∂L/∂W = ∂L/∂z * ∂z/∂W = (∂L/∂z) ⊗ x
# (⊗ is outer product)
```

---

## Practical NumPy Operations

```python
import numpy as np

# Broadcasting
A = np.array([[1, 2, 3]])      # (1, 3)
B = np.array([[1], [2], [3]])  # (3, 1)
C = A + B                       # (3, 3) - broadcast

# Reduction operations
np.sum(A, axis=0)    # Sum over rows (column sums)
np.mean(A, axis=1)   # Mean over columns (row means)

# Matrix operations
np.dot(A, B)   # Matrix multiply (or A @ B)
A * B          # Element-wise (Hadamard)

# Numerical stability
np.exp(np.clip(x, -500, 500))  # Clip before exp
np.log(np.maximum(x, 1e-10))   # Avoid log(0)
```

---

## Related Projects
- [Project 16: NumPy 101](./project-16-numpy-101/)
- [Project 18: Linear Algebra Essentials](./project-18-linear-algebra-essentials/)
- [Project 19: Gradient Descent](./project-19-gradient-descent-basics/)
- [Project 23: Manual Backpropagation](./project-23-manual-backpropagation/)
- [Project 24: Autodiff Engine](./project-24-autodiff-engine/)

---

*"Mathematics is the language in which God has written the universe."* — Galileo

*"In machine learning, it's the language in which gradients flow."* — Everyone doing backprop

Last updated: 2025-11-16
