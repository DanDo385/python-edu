# Project 18: Linear Regression from Scratch

> Implement linear regression with gradient descent—no sklearn, pure NumPy

**Difficulty**: ⭐⭐ Intermediate
**Phase**: II (Machine Learning Foundations)
**Prerequisites**: NumPy basics, calculus (derivatives), linear algebra
**Time**: 6-8 hours

---

## What You'll Learn

### Core Concepts
- **Linear Regression**: Fitting a line to data, predicting continuous values
- **Cost Function**: Mean Squared Error (MSE) as optimization objective
- **Gradient Descent**: Iterative optimization algorithm
- **Feature Normalization**: Scaling inputs for faster convergence
- **Vectorization**: Using NumPy for efficient matrix operations
- **Model Evaluation**: R² score, residuals, prediction error

### Technical Skills
- Implementing machine learning algorithms from scratch
- Deriving and implementing gradients
- Debugging numerical optimization (learning rate, convergence)
- Vectorizing computations with NumPy
- Visualizing loss landscapes and predictions
- Understanding bias-variance tradeoff

### Mathematical Foundations
- **Linear Algebra**: Matrix multiplication, dot products, transposes
- **Calculus**: Partial derivatives, chain rule, gradients
- **Statistics**: Mean, variance, correlation, R² coefficient
- **Optimization**: Convex optimization, local minima, convergence

### Prerequisites
- **Project 11**: NumPy fundamentals (arrays, broadcasting, operations)
- **Calculus**: Understanding derivatives (∂/∂x)
- **Linear Algebra**: Matrix operations, vector dot products
- **Recommended**: Familiarity with gradient descent concept

---

## Why This Matters

### The Foundation of Machine Learning

Linear regression is the **simplest supervised learning algorithm**, but it teaches fundamental concepts that apply to all of ML:

1. **Model**: Hypothesis function that maps inputs to outputs
2. **Loss**: Quantifying how wrong your predictions are
3. **Optimization**: Finding parameters that minimize loss
4. **Generalization**: Testing on unseen data

**Every deep learning model** (neural networks, transformers, LLMs) follows this pattern:
```
Model → Loss → Gradients → Update Parameters → Repeat
```

### From Linear Regression to Neural Networks

```
Linear Regression:  y = wx + b
Neural Network:     y = σ(W₃σ(W₂σ(W₁x + b₁) + b₂) + b₃)
                        └─────────────┬─────────────┘
                        Same gradient descent!
```

**Why start here**:
- ✅ **Interpretable**: You can visualize the line fit
- ✅ **Fast to train**: Converges in seconds
- ✅ **Mathematically simple**: Derivatives are straightforward
- ✅ **Debuggable**: Easy to verify gradients manually

### Real-World Applications

1. **Finance**: Stock price prediction, risk modeling
2. **Economics**: Demand forecasting, price elasticity
3. **Science**: Modeling physical relationships (Hooke's law, Ohm's law)
4. **Engineering**: Calibration, sensor fusion
5. **Healthcare**: Drug dosage optimization, disease progression

### Connections to Future Projects
- **Project 20**: Logistic regression (classification via sigmoid)
- **Project 22**: Neural networks (stacking linear layers + activations)
- **Project 27**: Regularization (L1/L2 penalty to prevent overfitting)
- **Project 34**: PyTorch autograd (automatic gradient computation)
- **Project 43**: GPT models (same gradient descent, bigger models)

---

## Mathematical Foundations

### The Linear Model

**Goal**: Find the best-fit line through data points.

**Hypothesis function** (for one feature):
```
ĥ(x) = wx + b

where:
  ĥ(x) = predicted output
  x    = input feature
  w    = weight (slope)
  b    = bias (y-intercept)
```

**Multiple features** (vectorized):
```
ĥ(X) = Xw + b

where:
  X ∈ ℝ^(m×n) = input matrix (m samples, n features)
  w ∈ ℝ^n     = weight vector
  b ∈ ℝ       = bias scalar
  ĥ ∈ ℝ^m     = predictions
```

**Matrix form** (with bias trick):
```
ĥ(X) = Xθ

where:
  X ∈ ℝ^(m×(n+1)) = [1, x₁, x₂, ..., xₙ]  (prepend column of 1s)
  θ ∈ ℝ^(n+1)      = [b, w₁, w₂, ..., wₙ]ᵀ
```

---

### The Cost Function (Mean Squared Error)

**Intuition**: Measure average squared distance between predictions and actual values.

**Formula**:
```
J(w, b) = (1/2m) Σᵢ₌₁ᵐ (ĥ(xⁱ) - yⁱ)²

where:
  m     = number of training examples
  ĥ(xⁱ) = prediction for example i
  yⁱ    = actual value for example i
  1/2   = convenience factor (cancels with derivative)
```

**Vectorized form**:
```
J(θ) = (1/2m) ||Xθ - y||²
     = (1/2m) (Xθ - y)ᵀ(Xθ - y)
```

**Why MSE?**
- ✅ **Differentiable**: Smooth, easy to optimize
- ✅ **Convex**: Single global minimum (no local minima!)
- ✅ **Penalizes outliers**: Squaring amplifies large errors
- ❌ **Sensitive to outliers**: Can dominate the loss

**Alternatives**:
- Mean Absolute Error (MAE): L1 loss, more robust to outliers
- Huber Loss: Combines MSE (small errors) + MAE (large errors)

---

### Gradient Descent Algorithm

**Intuition**: Walk downhill on the loss landscape until you reach the valley (minimum).

**Update rule**:
```
θ := θ - α ∇J(θ)

where:
  θ  = parameters [b, w₁, w₂, ..., wₙ]
  α  = learning rate (step size)
  ∇J = gradient (direction of steepest ascent)
```

**Gradients** (partial derivatives):
```
∂J/∂w = (1/m) Σᵢ₌₁ᵐ (ĥ(xⁱ) - yⁱ) · xⁱ
∂J/∂b = (1/m) Σᵢ₌₁ᵐ (ĥ(xⁱ) - yⁱ)
```

**Vectorized gradients**:
```
∇J(θ) = (1/m) Xᵀ(Xθ - y)

Breakdown:
  Xθ - y         = residuals (errors) ∈ ℝ^m
  Xᵀ             = feature matrix transpose ∈ ℝ^(n+1)×m
  Xᵀ(Xθ - y)     = gradient ∈ ℝ^(n+1)
```

**Algorithm** (batch gradient descent):
```
1. Initialize θ randomly (or zeros)
2. For iter = 1 to max_iterations:
     a. Compute predictions: ĥ = Xθ
     b. Compute loss: J = (1/2m)||ĥ - y||²
     c. Compute gradients: ∇J = (1/m)Xᵀ(ĥ - y)
     d. Update parameters: θ := θ - α∇J
     e. Check convergence: if ||∇J|| < ε, break
3. Return θ
```

**Convergence criteria**:
- Maximum iterations reached
- Gradient magnitude below threshold: ||∇J|| < ε
- Loss change below threshold: |J(θₜ) - J(θₜ₋₁)| < δ

---

### Feature Normalization (Standardization)

**Problem**: Features with different scales cause uneven gradients.

**Example**:
```
Feature 1: House size    (500 - 5000 sq ft)
Feature 2: # bedrooms    (1 - 5)

Gradient for w₁ will be ~1000x larger than w₂!
→ Slow convergence, requires tiny learning rate
```

**Solution**: Standardize features to mean=0, std=1.

**Z-score normalization**:
```
x_norm = (x - μ) / σ

where:
  μ = mean(x)
  σ = std(x)
```

**Benefits**:
- ✅ Faster convergence (symmetric loss landscape)
- ✅ Larger learning rates possible
- ✅ Numerical stability (prevents overflow/underflow)
- ✅ Interpretable weights (same scale)

**IMPORTANT**: Save μ and σ from training data, apply same transform to test data!

```python
# CORRECT
X_train_norm = (X_train - μ_train) / σ_train
X_test_norm = (X_test - μ_train) / σ_train  # Use training stats!

# WRONG
X_test_norm = (X_test - μ_test) / σ_test  # Data leakage!
```

---

## When to Use This

### Problem Indicators
Use linear regression when:
- **Continuous output**: Predicting numbers (prices, temperatures, counts)
- **Linear relationship**: Output roughly proportional to inputs
- **Interpretability needed**: Must explain predictions (healthcare, finance)
- **Baseline model**: Quick first attempt before complex models
- **Small datasets**: Works well with 100s-1000s of examples

### When NOT to Use Linear Regression

1. **Non-linear relationships**
   - ❌ Y = X² (use polynomial features or neural networks)
   - ❌ Y = sin(X) (use Fourier features or RNNs)

2. **Classification tasks**
   - ❌ Spam detection (binary: spam/not spam)
   - ✅ Use logistic regression instead

3. **Outlier-heavy data**
   - ❌ MSE heavily penalizes outliers
   - ✅ Use MAE or Huber loss

4. **High-dimensional data (n >> m)**
   - ❌ More features than samples → overfitting
   - ✅ Use regularization (Ridge/Lasso)

---

## Implementation Challenges

### Challenge 1: Choosing Learning Rate α

**Too small**: Slow convergence, many iterations
```
α = 0.001 → 100,000 iterations to converge
```

**Too large**: Overshoots minimum, diverges
```
α = 1.0 → Loss oscillates or explodes: J = NaN
```

**Just right**: Fast convergence, stable
```
α = 0.01 → Converges in 1,000 iterations
```

**Strategy**:
1. Start with α = 0.01
2. Plot loss vs. iteration
3. If oscillating: reduce α by 10x
4. If too slow: increase α by 2-3x
5. Use learning rate schedules (decay over time)

---

### Challenge 2: Debugging Gradient Descent

**Symptoms of bugs**:
- Loss increases instead of decreasing
- Loss = NaN or infinity
- Weights explode to huge values
- No convergence after many iterations

**Debugging checklist**:
1. **Verify gradient math**: Use numerical gradient checking
2. **Check feature scaling**: Are features normalized?
3. **Reduce learning rate**: Try α = 0.001
4. **Check for bugs**: Print shapes, check for NaN in data
5. **Visualize loss curve**: Should monotonically decrease

**Numerical gradient checking**:
```python
# Analytical gradient (your implementation)
grad_analytical = compute_gradient(X, y, theta)

# Numerical gradient (finite differences)
epsilon = 1e-7
grad_numerical = (J(theta + eps) - J(theta - eps)) / (2 * eps)

# Should be very close (< 1e-7 difference)
assert np.allclose(grad_analytical, grad_numerical, atol=1e-7)
```

---

### Challenge 3: Vectorization vs. Loops

**Slow (loops)**:
```python
# O(n²) time due to Python loops
for i in range(m):
    prediction = 0
    for j in range(n):
        prediction += X[i, j] * w[j]
    predictions[i] = prediction + b
```

**Fast (vectorized)**:
```python
# O(n²) time but ~100x faster due to NumPy C backend
predictions = X @ w + b  # Matrix multiplication
```

**Golden rule**: **Never loop over samples or features**. Use NumPy broadcasting.

---

## Diagrams

### Linear Regression Geometry

```
y
│        ● (actual)
│       /
│  ●   /
│     /   ●
│    /   /
│   /   / ↑ residual (error)
│  /   ●
│ / ← best-fit line: y = wx + b
│/
└────────────────── x

Goal: Minimize sum of squared residuals
```

---

### Gradient Descent Visualization

```
Loss J(w)
│
│   ╱╲
│  ╱  ╲
│ ╱    ╲
│╱  ●→  ╲
│   ↓    ╲
│    ●→   ╲
│     ↓    ╲
│      ●→   ╲  ← walk downhill
│       ↓    ╲
│        ●    ╲  minimum!
└──────────────── w

Each step: w := w - α(∂J/∂w)
```

---

### Feature Normalization Effect

```
Before normalization:
  w₁ (large scale)
  │   ╱╲
  │  ╱  ╲   ← elongated (slow)
  │ ╱    ╲
  └────────── w₂ (small scale)

After normalization:
  w₁
  │   ╱●╲
  │  │   │  ← circular (fast)
  │  ╲___╱
  └────────── w₂

Same scale → faster convergence
```

---

### Batch Gradient Descent Process

```
Iteration 0:
  θ = [0, 0, 0]    J = 250.5

Iteration 1:
  ∇J = [5.2, -3.1, 1.8]
  θ = [0, 0, 0] - 0.01 * [5.2, -3.1, 1.8] = [-0.052, 0.031, -0.018]
  J = 198.3  ✓ (decreased)

Iteration 2:
  ∇J = [4.1, -2.5, 1.4]
  θ = [-0.052, 0.031, -0.018] - 0.01 * [4.1, -2.5, 1.4] = [-0.093, 0.056, -0.032]
  J = 156.7  ✓ (decreased)

...

Iteration 1000:
  ∇J = [0.001, -0.0002, 0.0005]  ← small gradient
  θ = [2.45, -1.23, 0.87]
  J = 12.3  ✓ (converged!)
```

---

## Step-by-Step Implementation Guide

### Step 1: Initialize Parameters
```python
# Random initialization (small values)
w = np.random.randn(n_features) * 0.01
b = 0.0

# Or zeros (works for convex problems like linear regression)
w = np.zeros(n_features)
b = 0.0
```

**Why small random values?**
- Large values can cause overflow
- For linear regression, zeros work fine (convex)
- For neural networks, random is essential (break symmetry)

---

### Step 2: Forward Pass (Compute Predictions)
```python
# Predictions for all samples (vectorized)
y_pred = X @ w + b  # Shape: (m,)

# Equivalently (with bias trick):
# X_with_bias = np.column_stack([np.ones(m), X])  # Add column of 1s
# theta = np.concatenate([[b], w])
# y_pred = X_with_bias @ theta
```

**Shapes**:
- X: (m, n) - m samples, n features
- w: (n,) - n weights
- b: scalar
- y_pred: (m,) - m predictions

---

### Step 3: Compute Loss
```python
# Mean Squared Error
residuals = y_pred - y_true  # Shape: (m,)
loss = (1 / (2 * m)) * np.sum(residuals ** 2)

# Or using np.dot for efficiency:
loss = (1 / (2 * m)) * np.dot(residuals, residuals)
```

---

### Step 4: Compute Gradients
```python
# Gradient w.r.t. weights
dw = (1 / m) * X.T @ residuals  # Shape: (n,)

# Gradient w.r.t. bias
db = (1 / m) * np.sum(residuals)  # Scalar

# Shapes check:
# X.T: (n, m)
# residuals: (m,)
# X.T @ residuals: (n,) ✓
```

**Derivation**:
```
J = (1/2m) Σ(ŷⁱ - yⁱ)²
  = (1/2m) Σ(wᵀxⁱ + b - yⁱ)²

∂J/∂w = (1/m) Σ(ŷⁱ - yⁱ) · xⁱ   ← chain rule
      = (1/m) Xᵀ(ŷ - y)

∂J/∂b = (1/m) Σ(ŷⁱ - yⁱ)
```

---

### Step 5: Update Parameters
```python
# Gradient descent update
w = w - learning_rate * dw
b = b - learning_rate * db
```

**Convergence check**:
```python
gradient_norm = np.sqrt(np.sum(dw**2) + db**2)
if gradient_norm < 1e-6:
    print("Converged!")
    break
```

---

### Step 6: Repeat Until Convergence
```python
for iteration in range(max_iterations):
    # Forward pass
    y_pred = X @ w + b

    # Loss
    loss = (1 / (2 * m)) * np.sum((y_pred - y_true) ** 2)

    # Gradients
    residuals = y_pred - y_true
    dw = (1 / m) * X.T @ residuals
    db = (1 / m) * np.sum(residuals)

    # Update
    w = w - learning_rate * dw
    b = b - learning_rate * db

    # Logging
    if iteration % 100 == 0:
        print(f"Iteration {iteration}: Loss = {loss:.4f}")

    # Early stopping
    if np.linalg.norm(dw) < 1e-6:
        break
```

---

## How to Run

### Setup
```bash
cd /home/user/python-edu/ai/Projects/18-linear-regression-scratch
```

### Running the Solution
```bash
python solution/solution.py
```

### Running Tests
```bash
# All tests
pytest tests/test_project_18.py -v

# Specific test class
pytest tests/test_project_18.py::TestLinearRegression -v

# With output
pytest tests/test_project_18.py -v -s

# Coverage report
pytest tests/test_project_18.py --cov=solution --cov-report=html
```

### Expected Output
```
============================= test session starts ==============================
collected 25 items

tests/test_project_18.py::TestLinearRegression::test_fit_simple PASSED   [  4%]
tests/test_project_18.py::TestLinearRegression::test_predict PASSED      [  8%]
tests/test_project_18.py::TestLinearRegression::test_convergence PASSED  [ 12%]
tests/test_project_18.py::TestFeatureNormalization::test_normalize PASSED[ 16%]
...

========================== 25 passed in 2.34s ===============================
```

---

## Performance Considerations

### Time Complexity

| Operation | Complexity | Notes |
|-----------|-----------|--------|
| Forward pass | O(mn) | Matrix multiply X @ w |
| Loss computation | O(m) | Sum over m samples |
| Gradient computation | O(mn) | Matrix multiply Xᵀ @ residuals |
| Parameter update | O(n) | Update n weights + 1 bias |
| **Per iteration** | **O(mn)** | Dominated by matrix ops |
| **Total training** | **O(kmn)** | k = # iterations (~1000) |

**Optimizations**:
- Use BLAS-optimized NumPy (OpenBLAS, MKL)
- Batch/mini-batch gradient descent for large datasets
- Early stopping to reduce k
- Sparse matrices for sparse features

---

### Space Complexity

| Data Structure | Space | Notes |
|----------------|-------|--------|
| Training data X | O(mn) | m samples, n features |
| Labels y | O(m) | m samples |
| Parameters w, b | O(n) | n weights + 1 bias |
| Gradients dw, db | O(n) | Same as parameters |
| Predictions ŷ | O(m) | Temporary during training |
| **Total** | **O(mn)** | Dominated by training data |

**Memory-efficient variants**:
- Stochastic Gradient Descent (SGD): Process one sample at a time
- Mini-batch GD: Process small batches (e.g., 32 samples)
- Streaming/online learning: Update on each new sample

---

### Numerical Stability

**Common issues**:
1. **Overflow**: Features too large → ŷ = NaN
   - Solution: Normalize features
2. **Underflow**: Learning rate too small → no progress
   - Solution: Increase α
3. **Ill-conditioned matrices**: Highly correlated features
   - Solution: Remove correlated features or use regularization

---

## Advanced Challenges

### Challenge 1: Analytical Solution (Normal Equation)
Instead of gradient descent, solve directly:
```
θ = (XᵀX)⁻¹Xᵀy

Pros:
- No iterations, no learning rate
- Exact solution

Cons:
- O(n³) time (matrix inversion)
- O(n²) space (XᵀX matrix)
- Numerical instability if XᵀX singular
```

**Task**: Implement and compare with gradient descent.

---

### Challenge 2: Mini-Batch Gradient Descent
Use small batches instead of full dataset:
```python
for epoch in range(num_epochs):
    for batch_X, batch_y in get_batches(X, y, batch_size=32):
        # Compute gradients on mini-batch
        y_pred = batch_X @ w + b
        dw = (1 / batch_size) * batch_X.T @ (y_pred - batch_y)
        w = w - learning_rate * dw
```

**Benefits**: Faster per iteration, can handle large datasets.

---

### Challenge 3: Polynomial Features
Model non-linear relationships:
```python
# Original: X = [x]
# Polynomial: X_poly = [x, x², x³]

X_poly = np.column_stack([X, X**2, X**3])
model.fit(X_poly, y)
```

**Task**: Visualize underfitting (linear), good fit (quadratic), overfitting (degree 10).

---

### Challenge 4: Regularization (Ridge Regression)
Add L2 penalty to prevent overfitting:
```
J(θ) = (1/2m)||Xθ - y||² + (λ/2)||θ||²

∇J = (1/m)Xᵀ(Xθ - y) + λθ
```

**Task**: Implement and show how λ controls model complexity.

---

### Challenge 5: Learning Rate Schedules
Decay learning rate over time:
```python
# Time decay
alpha_t = alpha_0 / (1 + decay_rate * t)

# Step decay
alpha_t = alpha_0 * drop_rate^floor(t / epochs_drop)

# Exponential decay
alpha_t = alpha_0 * exp(-decay_rate * t)
```

**Task**: Compare convergence speed with different schedules.

---

## References

### Mathematical Foundations
- [Linear Algebra Review](../../MACHINE_LEARNING_MATH.md)
- [Matrix Cookbook](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf)
- [Convex Optimization (Boyd & Vandenberghe)](https://web.stanford.edu/~boyd/cvxbook/)

### Machine Learning Theory
- Andrew Ng's [CS229 Lecture Notes](http://cs229.stanford.edu/notes/)
- [Elements of Statistical Learning](https://hastie.su.domains/ElemStatLearn/) - Chapter 3
- [Pattern Recognition and Machine Learning (Bishop)](https://www.microsoft.com/en-us/research/people/cmbishop/)

### Implementation Resources
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [Numerical Recipes](http://numerical.recipes/) - Chapter on optimization

### Internal Resources
- [DSA Primer](../../DSA_PRIMER.md) - Complexity analysis
- [Autodiff from Scratch](../../AUTODIFF_FROM_SCRATCH.md) - Gradient computation

---

## Related Projects

- **Previous**: [Project 17: Exploratory Data Analysis](../17-exploratory-data-analysis/) - Data visualization
- **Next**: [Project 19: Data Preprocessing & Train-Test Split](../19-data-preprocessing-train-test-split/) - Model evaluation
- **Related**: [Project 20: Logistic Regression](../20-logistic-regression-binary-classification/) - Binary classification
- **Advanced**: [Project 22: Vectorized Neural Network](../22-vectorized-neural-network-numpy/) - Multi-layer networks

---

## Notes for Instructors

### Common Student Struggles

1. **"Why is my loss increasing?"**
   - Answer: Learning rate too large or gradient computation bug
   - Fix: Reduce α by 10x, verify gradient with numerical check

2. **"Training is very slow!"**
   - Answer: Features not normalized or learning rate too small
   - Fix: Standardize features, increase α

3. **"What learning rate should I use?"**
   - Answer: Start with 0.01, adjust based on loss curve
   - Rule: If oscillating, divide by 10; if too slow, multiply by 3

4. **"When do I stop training?"**
   - Answer: Multiple criteria: max iterations, gradient norm, loss change
   - Best practice: Early stopping on validation set

### Teaching Tips
- Visualize loss curve in real-time (matplotlib)
- Show gradient descent animation (3D surface plot)
- Compare with sklearn.LinearRegression for validation
- Emphasize vectorization (show speed difference with loops)
- Derive gradients on whiteboard (intuition building)

### Assessment Ideas
- Implement from scratch (no sklearn)
- Achieve R² > 0.95 on test data
- Explain why normalization helps (in words)
- Debug intentionally broken gradient code
- Extend to polynomial regression

---

Last updated: 2025-11-16
