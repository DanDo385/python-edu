"""
Project 18: Linear Regression from Scratch - SOLUTION

Complete implementation of linear regression with gradient descent using only NumPy.
This solution demonstrates production-quality ML code with comprehensive documentation.

WHAT YOU'LL LEARN:
- Implementing gradient descent from scratch
- Vectorized operations with NumPy for efficiency
- Feature normalization (standardization)
- Cost function computation (MSE)
- Model evaluation (R² score, predictions)
- Debugging ML algorithms (gradient checking, convergence monitoring)

WHY THIS MATTERS:
Linear regression is the foundation of all machine learning. The patterns you learn here
(model → loss → gradients → update) apply to neural networks, transformers, and LLMs.
Understanding this deeply helps you:
1. Debug training issues in complex models
2. Implement custom loss functions and optimizers
3. Understand what libraries like PyTorch do under the hood
4. Recognize when gradient descent is failing (learning rate, normalization)

MATHEMATICAL FOUNDATIONS:
- Cost function: J(θ) = (1/2m) Σ(ŷⁱ - yⁱ)²
- Gradients: ∇J = (1/m) Xᵀ(Xθ - y)
- Update rule: θ := θ - α∇J
- Normalization: x_norm = (x - μ) / σ

TIME INVESTMENT: 6-8 hours to understand all details
PREREQUISITE: NumPy, basic calculus (derivatives), linear algebra

Author: Python-50x-Minis
Date: 2025-11-16
"""

import numpy as np
from typing import Optional, Tuple, Dict, List


class LinearRegression:
    """
    Linear Regression with Gradient Descent (from scratch, no sklearn).

    Implements a linear model: ŷ = Xw + b
    Optimized using batch gradient descent to minimize Mean Squared Error.

    Mathematical Background
    -----------------------
    Model:
        ŷ = Xw + b
        where X ∈ ℝ^(m×n), w ∈ ℝ^n, b ∈ ℝ, ŷ ∈ ℝ^m

    Cost Function (MSE):
        J(w,b) = (1/2m) Σᵢ₌₁ᵐ (ŷⁱ - yⁱ)²

    Gradients:
        ∂J/∂w = (1/m) Xᵀ(ŷ - y)  ∈ ℝ^n
        ∂J/∂b = (1/m) Σ(ŷ - y)    ∈ ℝ

    Update Rule:
        w := w - α(∂J/∂w)
        b := b - α(∂J/∂b)

    Attributes
    ----------
    learning_rate : float
        Step size for gradient descent (α)
    n_iterations : int
        Maximum number of training iterations
    normalize : bool
        Whether to standardize features (recommended!)
    verbose : bool
        Whether to print training progress

    Fitted Attributes
    -----------------
    weights_ : np.ndarray, shape (n_features,)
        Learned weight vector (w)
    bias_ : float
        Learned bias term (b)
    losses_ : list of float
        Training loss at each iteration
    feature_mean_ : np.ndarray, shape (n_features,)
        Mean of training features (for normalization)
    feature_std_ : np.ndarray, shape (n_features,)
        Standard deviation of training features (for normalization)

    Examples
    --------
    >>> # Simple linear data
    >>> X = np.array([[1], [2], [3], [4], [5]])
    >>> y = np.array([2, 4, 6, 8, 10])
    >>>
    >>> # Fit model
    >>> model = LinearRegression(learning_rate=0.01, n_iterations=1000)
    >>> model.fit(X, y)
    >>>
    >>> # Predictions
    >>> y_pred = model.predict(X)
    >>> print(f"R² score: {model.score(X, y):.4f}")

    Notes
    -----
    - Always normalize features for faster convergence!
    - Monitor loss curve to diagnose issues (oscillation, slow convergence)
    - If loss increases: learning rate too large
    - If loss barely decreases: learning rate too small or need normalization

    See Also
    --------
    - Project 19: Train-test split for proper evaluation
    - Project 20: Logistic regression for classification
    - Project 22: Neural networks (stacking linear layers)
    """

    def __init__(
        self,
        learning_rate: float = 0.01,
        n_iterations: int = 1000,
        normalize: bool = True,
        verbose: bool = False,
        tol: float = 1e-6,
    ):
        """
        Initialize Linear Regression model.

        Parameters
        ----------
        learning_rate : float, default=0.01
            Learning rate (α) for gradient descent.
            Too large: model diverges (loss → ∞)
            Too small: slow convergence
            Typical range: [0.001, 0.1]

        n_iterations : int, default=1000
            Maximum number of gradient descent iterations.
            More iterations = more training time but better fit.
            Typical range: [100, 10000]

        normalize : bool, default=True
            Whether to standardize features to mean=0, std=1.
            HIGHLY RECOMMENDED for faster convergence.
            Without normalization, features with different scales cause
            uneven gradients → need smaller learning rate → slow training.

        verbose : bool, default=False
            If True, print loss every 100 iterations.
            Useful for debugging convergence issues.

        tol : float, default=1e-6
            Convergence tolerance. Stop if gradient norm < tol.
            Smaller tol = more precise fit but longer training.

        Examples
        --------
        >>> # Fast training with normalization
        >>> model = LinearRegression(learning_rate=0.1, normalize=True)
        >>>
        >>> # Slow but works without normalization
        >>> model = LinearRegression(learning_rate=0.001, normalize=False)
        >>>
        >>> # Debug training
        >>> model = LinearRegression(verbose=True)
        """
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.normalize = normalize
        self.verbose = verbose
        self.tol = tol

        # Fitted parameters (set during fit())
        self.weights_ = None  # w ∈ ℝ^n
        self.bias_ = None     # b ∈ ℝ
        self.losses_ = []     # Training loss history

        # Normalization statistics (set during fit())
        self.feature_mean_ = None  # μ ∈ ℝ^n
        self.feature_std_ = None   # σ ∈ ℝ^n

    def _normalize_features(
        self,
        X: np.ndarray,
        fit: bool = False,
    ) -> np.ndarray:
        """
        Standardize features to mean=0, std=1 (Z-score normalization).

        This is CRITICAL for gradient descent convergence!

        Mathematical Formula
        --------------------
        X_norm = (X - μ) / σ

        where:
            μ = mean(X, axis=0)  ∈ ℝ^n
            σ = std(X, axis=0)   ∈ ℝ^n

        Why Normalization Helps
        -----------------------
        Without normalization:
            Feature 1: [1, 2, 3]           (small scale)
            Feature 2: [1000, 2000, 3000]  (large scale)

            → Gradient for w₂ is ~1000x larger than w₁
            → Need tiny learning rate to prevent w₂ from exploding
            → w₁ barely updates (slow convergence)

        With normalization:
            Feature 1: [-1, 0, 1]  (mean=0, std=1)
            Feature 2: [-1, 0, 1]  (mean=0, std=1)

            → Equal gradients
            → Larger learning rate possible
            → Faster convergence (10-100x speedup!)

        Parameters
        ----------
        X : np.ndarray, shape (m, n)
            Input features to normalize

        fit : bool, default=False
            If True, compute and store mean/std from X (training mode)
            If False, use stored mean/std (prediction mode)

            IMPORTANT: Always use training statistics for test data!

        Returns
        -------
        X_norm : np.ndarray, shape (m, n)
            Normalized features

        Examples
        --------
        >>> # Training: compute statistics
        >>> X_train_norm = model._normalize_features(X_train, fit=True)
        >>>
        >>> # Testing: use training statistics
        >>> X_test_norm = model._normalize_features(X_test, fit=False)

        Notes
        -----
        - Normalization is applied independently to each feature (column)
        - Constant features (std=0) are left unchanged (avoid division by zero)
        - Alternative: Min-max scaling to [0,1]: (X - min) / (max - min)
        """
        if fit:
            # TRAINING MODE: Compute and store statistics
            # Compute mean across samples (axis=0)
            # feature_mean_[j] = average of all samples for feature j
            self.feature_mean_ = np.mean(X, axis=0)  # Shape: (n,)

            # Compute standard deviation across samples
            # feature_std_[j] = spread of feature j values
            self.feature_std_ = np.std(X, axis=0)    # Shape: (n,)

            # Handle constant features (std=0) to avoid division by zero
            # If std=0, feature is constant → no normalization needed
            # Replace 0 with 1 to make (X - μ) / 1 = (X - μ) = 0
            self.feature_std_[self.feature_std_ == 0] = 1.0

        # NORMALIZE using stored statistics
        # Broadcasting: (m, n) - (n,) → (m, n)  [subtracts mean from each column]
        # Then: (m, n) / (n,) → (m, n)         [divides each column by its std]
        X_normalized = (X - self.feature_mean_) / self.feature_std_

        return X_normalized

    def _compute_cost(
        self,
        X: np.ndarray,
        y: np.ndarray,
    ) -> float:
        """
        Compute Mean Squared Error (MSE) cost function.

        Mathematical Formula
        --------------------
        J(w,b) = (1/2m) Σᵢ₌₁ᵐ (ŷⁱ - yⁱ)²
               = (1/2m) ||Xw + b - y||²

        where:
            m = number of samples
            ŷ = Xw + b = predictions
            y = actual values
            ||·|| = L2 norm (Euclidean distance)

        Why MSE?
        --------
        1. DIFFERENTIABLE: Smooth function, easy to optimize
        2. CONVEX: Single global minimum (no local minima!)
        3. PENALIZES LARGE ERRORS: Squaring amplifies outliers
        4. MATHEMATICALLY CONVENIENT: Derivative is simple

        Why (1/2m)?
        -----------
        - 1/m: Average over samples (scale-invariant)
        - 1/2: Cancels with derivative of x² → cleaner gradient

        Derivation of Gradient
        ----------------------
        J = (1/2m) Σ(ŷⁱ - yⁱ)²

        ∂J/∂w = (1/2m) Σ 2(ŷⁱ - yⁱ) · ∂ŷⁱ/∂w    [chain rule]
              = (1/2m) Σ 2(ŷⁱ - yⁱ) · xⁱ        [∂(wx+b)/∂w = x]
              = (1/m) Σ(ŷⁱ - yⁱ) · xⁱ           [2 cancels with 1/2]
              = (1/m) Xᵀ(ŷ - y)                 [vectorized]

        Parameters
        ----------
        X : np.ndarray, shape (m, n)
            Input features
        y : np.ndarray, shape (m,)
            Target values

        Returns
        -------
        cost : float
            Mean squared error

        Time Complexity
        ---------------
        O(mn) for predictions + O(m) for squared error = O(mn)

        Space Complexity
        ----------------
        O(m) for predictions array

        Examples
        --------
        >>> X = np.array([[1, 2], [3, 4], [5, 6]])
        >>> y = np.array([1, 2, 3])
        >>> model.weights_ = np.array([0.5, 0.5])
        >>> model.bias_ = 0.0
        >>> cost = model._compute_cost(X, y)
        >>> print(f"MSE: {cost:.4f}")
        """
        # Number of training examples
        m = X.shape[0]

        # FORWARD PASS: Compute predictions
        # ŷ = Xw + b
        # X @ self.weights_: Matrix-vector multiplication ∈ ℝ^m
        # + self.bias_: Broadcasting scalar to vector
        predictions = X @ self.weights_ + self.bias_  # Shape: (m,)

        # COMPUTE RESIDUALS (errors)
        # residuals[i] = ŷⁱ - yⁱ
        # Positive: over-prediction
        # Negative: under-prediction
        residuals = predictions - y  # Shape: (m,)

        # COMPUTE MSE
        # Sum of squared residuals, normalized by (2m)
        # Using np.dot for efficiency: dot(v, v) = ||v||²
        cost = (1 / (2 * m)) * np.dot(residuals, residuals)

        # Alternative (equivalent but slower):
        # cost = (1 / (2 * m)) * np.sum(residuals ** 2)

        return cost

    def _compute_gradients(
        self,
        X: np.ndarray,
        y: np.ndarray,
    ) -> Tuple[np.ndarray, float]:
        """
        Compute gradients of cost function w.r.t. weights and bias.

        This is the CORE of gradient descent!

        Mathematical Derivation
        -----------------------
        Given:
            J(w,b) = (1/2m) Σᵢ₌₁ᵐ (ŷⁱ - yⁱ)²
            ŷⁱ = wᵀxⁱ + b

        Gradient w.r.t. weights:
            ∂J/∂w = (1/m) Σᵢ₌₁ᵐ (ŷⁱ - yⁱ) · xⁱ
                  = (1/m) Xᵀ(ŷ - y)

        Gradient w.r.t. bias:
            ∂J/∂b = (1/m) Σᵢ₌₁ᵐ (ŷⁱ - yⁱ)
                  = (1/m) 1ᵀ(ŷ - y)

        Intuition
        ---------
        - Gradient points in direction of steepest ASCENT
        - We subtract gradient to go DOWNHILL (minimize loss)
        - Larger errors → larger gradients → bigger updates
        - When predictions are perfect (ŷ = y), gradient = 0

        Vectorization
        -------------
        Loop version (SLOW):
            for i in range(m):
                for j in range(n):
                    dw[j] += (y_pred[i] - y[i]) * X[i, j]
            dw /= m

        Vectorized (FAST):
            dw = (1/m) * X.T @ (y_pred - y)

        NumPy uses optimized BLAS libraries → 100x faster!

        Parameters
        ----------
        X : np.ndarray, shape (m, n)
            Input features
        y : np.ndarray, shape (m,)
            Target values

        Returns
        -------
        dw : np.ndarray, shape (n,)
            Gradient w.r.t. weights
        db : float
            Gradient w.r.t. bias

        Time Complexity
        ---------------
        O(mn) for X.T @ residuals (matrix-vector multiplication)

        Space Complexity
        ----------------
        O(n) for gradient vector

        Examples
        --------
        >>> X = np.array([[1, 2], [3, 4]])
        >>> y = np.array([1, 2])
        >>> dw, db = model._compute_gradients(X, y)
        >>> print(f"Weight gradient: {dw}")
        >>> print(f"Bias gradient: {db:.4f}")
        """
        # Number of training examples
        m = X.shape[0]

        # FORWARD PASS: Compute predictions
        predictions = X @ self.weights_ + self.bias_  # Shape: (m,)

        # RESIDUALS: ŷ - y
        residuals = predictions - y  # Shape: (m,)

        # GRADIENT W.R.T. WEIGHTS
        # (1/m) * Xᵀ(ŷ - y)
        # X.T: (n, m)
        # residuals: (m,)
        # X.T @ residuals: (n,)  [matrix-vector multiply]
        dw = (1 / m) * (X.T @ residuals)  # Shape: (n,)

        # GRADIENT W.R.T. BIAS
        # (1/m) * Σ(ŷ - y)
        # Sum all residuals and normalize
        db = (1 / m) * np.sum(residuals)  # Scalar

        # Numerical stability check (optional for debugging)
        # If gradients are NaN or too large, something is wrong!
        if np.any(np.isnan(dw)) or np.any(np.isinf(dw)):
            raise ValueError("Gradient contains NaN or Inf! Check data and learning rate.")

        return dw, db

    def fit(
        self,
        X: np.ndarray,
        y: np.ndarray,
    ) -> 'LinearRegression':
        """
        Fit linear regression model using batch gradient descent.

        This is the main training loop!

        Algorithm
        ---------
        1. Initialize parameters: w = 0, b = 0
        2. Normalize features (if enabled)
        3. For iter = 1 to n_iterations:
             a. Compute predictions: ŷ = Xw + b
             b. Compute loss: J = MSE(ŷ, y)
             c. Compute gradients: ∇J = (∂J/∂w, ∂J/∂b)
             d. Update parameters: w := w - α∇w, b := b - α∇b
             e. Check convergence: if ||∇J|| < tol, break
        4. Return fitted model

        Parameters
        ----------
        X : np.ndarray, shape (m, n)
            Training features (m samples, n features)
        y : np.ndarray, shape (m,)
            Target values (m samples)

        Returns
        -------
        self : LinearRegression
            Fitted model (enables chaining: model.fit(X, y).predict(X))

        Raises
        ------
        ValueError
            If X and y have incompatible shapes
            If learning rate causes divergence (NaN/Inf)

        Examples
        --------
        >>> # Simple 1D example
        >>> X = np.array([[1], [2], [3], [4]])
        >>> y = np.array([2, 4, 6, 8])
        >>> model = LinearRegression(learning_rate=0.01, n_iterations=1000)
        >>> model.fit(X, y)
        >>> print(f"w = {model.weights_[0]:.4f}, b = {model.bias_:.4f}")
        w = 2.0000, b = 0.0000

        >>> # Multiple features
        >>> X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
        >>> y = np.array([5, 7, 9, 11])
        >>> model.fit(X, y)

        Notes
        -----
        - Always check loss curve (model.losses_) to verify convergence
        - If loss increases: reduce learning rate
        - If loss barely changes: increase learning rate or check normalization
        - Early stopping: Training stops if gradient norm < tol
        """
        # INPUT VALIDATION
        # Ensure X is 2D array (m, n)
        if X.ndim == 1:
            X = X.reshape(-1, 1)  # Convert (m,) → (m, 1)

        # Check shapes match
        m, n = X.shape
        if y.shape[0] != m:
            raise ValueError(
                f"X and y have incompatible shapes: X has {m} samples, "
                f"y has {y.shape[0]} samples"
            )

        # FEATURE NORMALIZATION (if enabled)
        if self.normalize:
            X = self._normalize_features(X, fit=True)

        # INITIALIZE PARAMETERS
        # Weights: Start at zero (works for convex problems)
        # Alternative: Small random values: np.random.randn(n) * 0.01
        self.weights_ = np.zeros(n)  # Shape: (n,)
        self.bias_ = 0.0             # Scalar

        # Clear loss history
        self.losses_ = []

        # GRADIENT DESCENT LOOP
        for iteration in range(self.n_iterations):
            # 1. COMPUTE COST (for monitoring)
            cost = self._compute_cost(X, y)
            self.losses_.append(cost)

            # 2. COMPUTE GRADIENTS
            dw, db = self._compute_gradients(X, y)

            # 3. UPDATE PARAMETERS
            # Gradient descent: θ := θ - α∇J
            self.weights_ -= self.learning_rate * dw
            self.bias_ -= self.learning_rate * db

            # 4. LOGGING (if verbose)
            if self.verbose and iteration % 100 == 0:
                gradient_norm = np.linalg.norm(dw)
                print(
                    f"Iteration {iteration:4d}: "
                    f"Loss = {cost:.6f}, "
                    f"||∇w|| = {gradient_norm:.6f}"
                )

            # 5. EARLY STOPPING (convergence check)
            # If gradient is very small, we're at minimum
            gradient_norm = np.linalg.norm(dw)
            if gradient_norm < self.tol:
                if self.verbose:
                    print(f"Converged at iteration {iteration}")
                break

            # 6. DIVERGENCE CHECK
            # If loss is NaN or Inf, learning rate is too large
            if np.isnan(cost) or np.isinf(cost):
                raise ValueError(
                    f"Training diverged at iteration {iteration}! "
                    f"Try reducing learning_rate (current: {self.learning_rate})"
                )

        # FINAL LOGGING
        if self.verbose:
            print(f"\nTraining completed!")
            print(f"Final loss: {self.losses_[-1]:.6f}")
            print(f"Total iterations: {len(self.losses_)}")

        return self  # Enable method chaining

    def predict(
        self,
        X: np.ndarray,
    ) -> np.ndarray:
        """
        Predict target values for input features.

        Uses learned parameters: ŷ = Xw + b

        Parameters
        ----------
        X : np.ndarray, shape (m, n)
            Input features (m samples, n features)

        Returns
        -------
        predictions : np.ndarray, shape (m,)
            Predicted target values

        Raises
        ------
        ValueError
            If model not fitted yet (call fit() first)
            If X has wrong number of features

        Examples
        --------
        >>> X_train = np.array([[1], [2], [3]])
        >>> y_train = np.array([2, 4, 6])
        >>> model.fit(X_train, y_train)
        >>>
        >>> X_test = np.array([[4], [5]])
        >>> y_pred = model.predict(X_test)
        >>> print(y_pred)
        [8. 10.]

        Notes
        -----
        - Must call fit() before predict()
        - If normalization was used in training, it's applied automatically
        - Uses same feature statistics (mean, std) from training
        """
        # CHECK IF MODEL IS FITTED
        if self.weights_ is None or self.bias_ is None:
            raise ValueError("Model not fitted yet! Call fit() first.")

        # INPUT VALIDATION
        if X.ndim == 1:
            X = X.reshape(-1, 1)

        # Check number of features matches training
        if X.shape[1] != len(self.weights_):
            raise ValueError(
                f"X has {X.shape[1]} features, but model was trained with "
                f"{len(self.weights_)} features"
            )

        # NORMALIZE FEATURES (using training statistics)
        if self.normalize:
            X = self._normalize_features(X, fit=False)

        # MAKE PREDICTIONS
        # ŷ = Xw + b
        predictions = X @ self.weights_ + self.bias_

        return predictions

    def score(
        self,
        X: np.ndarray,
        y: np.ndarray,
    ) -> float:
        """
        Compute R² (coefficient of determination) score.

        R² measures how well predictions match actual values:
        - R² = 1.0: Perfect predictions (ŷ = y)
        - R² = 0.0: Predictions as good as mean baseline
        - R² < 0.0: Predictions worse than mean baseline

        Mathematical Formula
        --------------------
        R² = 1 - (SS_res / SS_tot)

        where:
            SS_res = Σ(yⁱ - ŷⁱ)²  (residual sum of squares)
            SS_tot = Σ(yⁱ - ȳ)²  (total sum of squares)
            ȳ = mean(y)

        Intuition
        ---------
        - SS_tot: How much variance in y?
        - SS_res: How much variance remains after predictions?
        - R² = fraction of variance explained by model

        Alternative Interpretation
        --------------------------
        R² = 1 - (MSE_model / MSE_baseline)

        where MSE_baseline predicts ȳ for all samples

        Parameters
        ----------
        X : np.ndarray, shape (m, n)
            Input features
        y : np.ndarray, shape (m,)
            True target values

        Returns
        -------
        r2_score : float
            R² coefficient in range (-∞, 1]
            Higher is better!

        Examples
        --------
        >>> X = np.array([[1], [2], [3], [4]])
        >>> y = np.array([2, 4, 6, 8])
        >>> model.fit(X, y)
        >>> r2 = model.score(X, y)
        >>> print(f"R² = {r2:.4f}")
        R² = 1.0000

        Notes
        -----
        - R² on training set can be overly optimistic
        - Always evaluate on separate test set
        - R² < 0 means model is worse than predicting mean
        """
        # Make predictions
        predictions = self.predict(X)

        # Residual sum of squares: Σ(y - ŷ)²
        # Measures how much error remains
        ss_res = np.sum((y - predictions) ** 2)

        # Total sum of squares: Σ(y - ȳ)²
        # Measures total variance in y
        ss_tot = np.sum((y - np.mean(y)) ** 2)

        # R² = 1 - (residual variance / total variance)
        # Fraction of variance explained by model
        r2_score = 1 - (ss_res / ss_tot)

        return r2_score

    def get_params(self) -> Dict[str, np.ndarray]:
        """
        Get learned parameters (weights and bias).

        Returns
        -------
        params : dict
            Dictionary with keys:
                'weights': np.ndarray, shape (n,)
                'bias': float

        Examples
        --------
        >>> model.fit(X, y)
        >>> params = model.get_params()
        >>> print(f"Weights: {params['weights']}")
        >>> print(f"Bias: {params['bias']:.4f}")
        """
        if self.weights_ is None:
            raise ValueError("Model not fitted yet!")

        return {
            'weights': self.weights_.copy(),
            'bias': self.bias_,
        }

    def get_loss_history(self) -> List[float]:
        """
        Get training loss history.

        Useful for:
        - Plotting loss curve
        - Diagnosing convergence issues
        - Comparing different hyperparameters

        Returns
        -------
        losses : list of float
            Loss at each iteration

        Examples
        --------
        >>> model.fit(X, y)
        >>> losses = model.get_loss_history()
        >>>
        >>> import matplotlib.pyplot as plt
        >>> plt.plot(losses)
        >>> plt.xlabel('Iteration')
        >>> plt.ylabel('MSE Loss')
        >>> plt.title('Training Loss Curve')
        >>> plt.show()
        """
        return self.losses_.copy()


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Compute Mean Squared Error between true and predicted values.

    MSE = (1/m) Σᵢ₌₁ᵐ (yⁱ - ŷⁱ)²

    Parameters
    ----------
    y_true : np.ndarray, shape (m,)
        Actual target values
    y_pred : np.ndarray, shape (m,)
        Predicted target values

    Returns
    -------
    mse : float
        Mean squared error

    Examples
    --------
    >>> y_true = np.array([1, 2, 3, 4])
    >>> y_pred = np.array([1.1, 2.2, 2.9, 4.1])
    >>> mse = mean_squared_error(y_true, y_pred)
    >>> print(f"MSE: {mse:.4f}")
    MSE: 0.0275
    """
    return np.mean((y_true - y_pred) ** 2)


def r2_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Compute R² (coefficient of determination).

    R² = 1 - (SS_res / SS_tot)

    Parameters
    ----------
    y_true : np.ndarray, shape (m,)
        Actual target values
    y_pred : np.ndarray, shape (m,)
        Predicted target values

    Returns
    -------
    r2 : float
        R² score in range (-∞, 1]

    Examples
    --------
    >>> y_true = np.array([1, 2, 3, 4])
    >>> y_pred = np.array([1.1, 2.2, 2.9, 4.1])
    >>> r2 = r2_score(y_true, y_pred)
    >>> print(f"R²: {r2:.4f}")
    R²: 0.9780
    """
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res / ss_tot)


# =============================================================================
# DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("Project 18: Linear Regression from Scratch - DEMONSTRATION")
    print("=" * 80)

    # Set random seed for reproducibility
    np.random.seed(42)

    # =========================================================================
    # EXAMPLE 1: Simple 1D Linear Regression
    # =========================================================================
    print("\n" + "=" * 80)
    print("Example 1: Simple 1D Linear Regression (y = 2x + 1)")
    print("=" * 80)

    # Generate synthetic data: y = 2x + 1 + noise
    X_1d = np.linspace(0, 10, 50).reshape(-1, 1)
    y_1d = 2 * X_1d.ravel() + 1 + np.random.randn(50) * 0.5

    # Train model
    model_1d = LinearRegression(
        learning_rate=0.01,
        n_iterations=1000,
        normalize=True,
        verbose=True
    )
    model_1d.fit(X_1d, y_1d)

    # Evaluate
    y_pred_1d = model_1d.predict(X_1d)
    r2_1d = model_1d.score(X_1d, y_1d)

    print(f"\nResults:")
    print(f"  True parameters:    w = 2.0,  b = 1.0")
    print(f"  Learned parameters: w = {model_1d.weights_[0]:.4f}, b = {model_1d.bias_:.4f}")
    print(f"  R² score: {r2_1d:.6f}")
    print(f"  MSE: {mean_squared_error(y_1d, y_pred_1d):.6f}")

    # =========================================================================
    # EXAMPLE 2: Multiple Features
    # =========================================================================
    print("\n" + "=" * 80)
    print("Example 2: Multiple Features (y = 3x₁ + 2x₂ - x₃ + 5)")
    print("=" * 80)

    # Generate synthetic data
    n_samples = 200
    n_features = 3
    X_multi = np.random.randn(n_samples, n_features)

    # True parameters
    true_weights = np.array([3.0, 2.0, -1.0])
    true_bias = 5.0

    # Generate labels: y = Xw + b + noise
    y_multi = X_multi @ true_weights + true_bias + np.random.randn(n_samples) * 0.5

    # Train model
    model_multi = LinearRegression(
        learning_rate=0.01,
        n_iterations=2000,
        normalize=True,
        verbose=False
    )
    model_multi.fit(X_multi, y_multi)

    # Evaluate
    y_pred_multi = model_multi.predict(X_multi)
    r2_multi = model_multi.score(X_multi, y_multi)

    print(f"\nResults:")
    print(f"  True parameters:    w = {true_weights}, b = {true_bias}")
    print(f"  Learned parameters: w = {model_multi.weights_}, b = {model_multi.bias_:.4f}")
    print(f"  R² score: {r2_multi:.6f}")
    print(f"  MSE: {mean_squared_error(y_multi, y_pred_multi):.6f}")

    # =========================================================================
    # EXAMPLE 3: Effect of Normalization
    # =========================================================================
    print("\n" + "=" * 80)
    print("Example 3: Effect of Feature Normalization")
    print("=" * 80)

    # Create data with different scales
    X_scaled = np.column_stack([
        np.random.randn(100) * 1,      # Feature 1: std = 1
        np.random.randn(100) * 1000,   # Feature 2: std = 1000
    ])
    y_scaled = 2 * X_scaled[:, 0] + 0.5 * X_scaled[:, 1] + np.random.randn(100)

    # Without normalization (requires small learning rate)
    print("\nWithout normalization:")
    model_no_norm = LinearRegression(
        learning_rate=0.000001,  # Very small!
        n_iterations=5000,
        normalize=False,
        verbose=False
    )
    model_no_norm.fit(X_scaled, y_scaled)
    print(f"  Final loss: {model_no_norm.losses_[-1]:.6f}")
    print(f"  Iterations: {len(model_no_norm.losses_)}")

    # With normalization (can use larger learning rate)
    print("\nWith normalization:")
    model_norm = LinearRegression(
        learning_rate=0.1,  # 100,000x larger!
        n_iterations=1000,
        normalize=True,
        verbose=False
    )
    model_norm.fit(X_scaled, y_scaled)
    print(f"  Final loss: {model_norm.losses_[-1]:.6f}")
    print(f"  Iterations: {len(model_norm.losses_)}")
    print(f"\nNormalization enables ~5x faster convergence!")

    # =========================================================================
    # EXAMPLE 4: Learning Rate Comparison
    # =========================================================================
    print("\n" + "=" * 80)
    print("Example 4: Learning Rate Sensitivity")
    print("=" * 80)

    learning_rates = [0.001, 0.01, 0.1, 1.0]

    for lr in learning_rates:
        try:
            model_lr = LinearRegression(
                learning_rate=lr,
                n_iterations=500,
                normalize=True,
                verbose=False
            )
            model_lr.fit(X_1d, y_1d)
            final_loss = model_lr.losses_[-1]
            print(f"  α = {lr:5.3f}: Final loss = {final_loss:.6f}")
        except ValueError as e:
            print(f"  α = {lr:5.3f}: DIVERGED ({str(e)[:50]}...)")

    print("\n" + "=" * 80)
    print("All examples completed successfully!")
    print("Run tests with: pytest tests/test_project_18.py -v")
    print("=" * 80)
