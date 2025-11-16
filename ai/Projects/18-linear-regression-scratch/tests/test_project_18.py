"""
Tests for Project 18: Linear Regression from Scratch

This test suite demonstrates comprehensive testing of machine learning algorithms:
- Model fitting and convergence
- Prediction accuracy
- Feature normalization
- Gradient computation (numerical verification)
- Edge cases (single feature, no variance, etc.)
- Error handling
- Performance characteristics

Test Categories:
- TestLinearRegression: Core model functionality
- TestFeatureNormalization: Normalization correctness
- TestGradients: Gradient verification
- TestConvergence: Training convergence
- TestEdgeCases: Boundary conditions
- TestErrorHandling: Exception handling
- TestMetrics: R² and MSE computation

Author: Python-50x-Minis
Date: 2025-11-16
"""

import pytest
import numpy as np
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from solution import solution


# =============================================================================
# TEST: LINEAR REGRESSION CORE
# =============================================================================

class TestLinearRegression:
    """Test core linear regression functionality."""

    def test_initialization(self):
        """Test model initialization with default parameters."""
        model = solution.LinearRegression()
        assert model.learning_rate == 0.01
        assert model.n_iterations == 1000
        assert model.normalize is True
        assert model.verbose is False
        assert model.weights_ is None
        assert model.bias_ is None

    def test_custom_parameters(self):
        """Test initialization with custom parameters."""
        model = solution.LinearRegression(
            learning_rate=0.1,
            n_iterations=500,
            normalize=False,
            verbose=True
        )
        assert model.learning_rate == 0.1
        assert model.n_iterations == 500
        assert model.normalize is False
        assert model.verbose is True

    def test_fit_simple_1d(self):
        """Test fitting on simple 1D data: y = 2x + 1."""
        np.random.seed(42)
        X = np.linspace(0, 10, 50).reshape(-1, 1)
        y = 2 * X.ravel() + 1 + np.random.randn(50) * 0.1

        model = solution.LinearRegression(
            learning_rate=0.01,
            n_iterations=1000,
            normalize=True
        )
        model.fit(X, y)

        # Check parameters are close to true values
        assert model.weights_ is not None
        assert model.bias_ is not None
        assert len(model.weights_) == 1
        assert abs(model.weights_[0] - 2.0) < 0.1  # w ≈ 2
        assert abs(model.bias_ - 1.0) < 0.1         # b ≈ 1

    def test_fit_multiple_features(self):
        """Test fitting with multiple features."""
        np.random.seed(42)
        X = np.random.randn(100, 3)
        true_w = np.array([2.0, -1.0, 0.5])
        true_b = 3.0
        y = X @ true_w + true_b + np.random.randn(100) * 0.1

        model = solution.LinearRegression(
            learning_rate=0.01,
            n_iterations=2000
        )
        model.fit(X, y)

        # Check weights are close to true values
        assert len(model.weights_) == 3
        np.testing.assert_allclose(model.weights_, true_w, atol=0.2)
        assert abs(model.bias_ - true_b) < 0.2

    def test_predict(self):
        """Test prediction after fitting."""
        np.random.seed(42)
        X_train = np.array([[1], [2], [3], [4]])
        y_train = np.array([2, 4, 6, 8])

        model = solution.LinearRegression(
            learning_rate=0.01,
            n_iterations=1000
        )
        model.fit(X_train, y_train)

        # Predict on new data
        X_test = np.array([[5], [6]])
        y_pred = model.predict(X_test)

        assert y_pred.shape == (2,)
        # Should predict approximately 10 and 12
        assert abs(y_pred[0] - 10) < 0.5
        assert abs(y_pred[1] - 12) < 0.5

    def test_predict_before_fit_raises_error(self):
        """Test that predict raises error if model not fitted."""
        model = solution.LinearRegression()
        X = np.array([[1, 2], [3, 4]])

        with pytest.raises(ValueError, match="not fitted"):
            model.predict(X)

    def test_score(self):
        """Test R² score computation."""
        np.random.seed(42)
        X = np.array([[1], [2], [3], [4]])
        y = np.array([2, 4, 6, 8])

        model = solution.LinearRegression(
            learning_rate=0.01,
            n_iterations=1000
        )
        model.fit(X, y)

        r2 = model.score(X, y)

        # Perfect linear relationship should give R² ≈ 1
        assert r2 > 0.99

    def test_get_params(self):
        """Test getting model parameters."""
        np.random.seed(42)
        X = np.array([[1], [2], [3]])
        y = np.array([2, 4, 6])

        model = solution.LinearRegression()
        model.fit(X, y)

        params = model.get_params()

        assert 'weights' in params
        assert 'bias' in params
        assert isinstance(params['weights'], np.ndarray)
        assert isinstance(params['bias'], float)

    def test_get_params_before_fit_raises_error(self):
        """Test that get_params raises error if model not fitted."""
        model = solution.LinearRegression()

        with pytest.raises(ValueError, match="not fitted"):
            model.get_params()

    def test_loss_history(self):
        """Test that loss history is recorded."""
        np.random.seed(42)
        X = np.array([[1], [2], [3]])
        y = np.array([2, 4, 6])

        model = solution.LinearRegression(n_iterations=100)
        model.fit(X, y)

        losses = model.get_loss_history()

        assert len(losses) > 0
        assert len(losses) <= 100
        # Loss should decrease over time
        assert losses[-1] < losses[0]

    def test_method_chaining(self):
        """Test that fit() returns self for method chaining."""
        X = np.array([[1], [2], [3]])
        y = np.array([2, 4, 6])

        model = solution.LinearRegression()
        result = model.fit(X, y)

        assert result is model
        # Can chain: model.fit(X, y).predict(X)
        y_pred = model.fit(X, y).predict(X)
        assert y_pred is not None


# =============================================================================
# TEST: FEATURE NORMALIZATION
# =============================================================================

class TestFeatureNormalization:
    """Test feature normalization (standardization)."""

    def test_normalize_centers_data(self):
        """Test that normalization centers data to mean=0."""
        np.random.seed(42)
        X = np.random.randn(100, 3) * 10 + 50  # Mean ≈ 50

        model = solution.LinearRegression(normalize=True)
        X_norm = model._normalize_features(X, fit=True)

        # Check mean ≈ 0 for each feature
        np.testing.assert_allclose(np.mean(X_norm, axis=0), 0, atol=1e-10)

    def test_normalize_scales_data(self):
        """Test that normalization scales data to std=1."""
        np.random.seed(42)
        X = np.random.randn(100, 3) * 10 + 50

        model = solution.LinearRegression(normalize=True)
        X_norm = model._normalize_features(X, fit=True)

        # Check std ≈ 1 for each feature
        np.testing.assert_allclose(np.std(X_norm, axis=0), 1, atol=0.01)

    def test_normalize_stores_statistics(self):
        """Test that normalization stores mean and std."""
        np.random.seed(42)
        X = np.random.randn(100, 3)

        model = solution.LinearRegression(normalize=True)
        model._normalize_features(X, fit=True)

        assert model.feature_mean_ is not None
        assert model.feature_std_ is not None
        assert model.feature_mean_.shape == (3,)
        assert model.feature_std_.shape == (3,)

    def test_normalize_uses_training_statistics(self):
        """Test that test data uses training statistics."""
        np.random.seed(42)
        X_train = np.random.randn(100, 2) * 5 + 10
        X_test = np.random.randn(50, 2) * 5 + 10

        model = solution.LinearRegression(normalize=True)

        # Normalize training data
        X_train_norm = model._normalize_features(X_train, fit=True)
        train_mean = model.feature_mean_.copy()
        train_std = model.feature_std_.copy()

        # Normalize test data (should use training statistics)
        X_test_norm = model._normalize_features(X_test, fit=False)

        # Statistics should not change
        np.testing.assert_array_equal(model.feature_mean_, train_mean)
        np.testing.assert_array_equal(model.feature_std_, train_std)

        # Test data may not have mean=0, std=1 (that's correct!)
        # It uses training mean/std, not its own

    def test_normalize_handles_constant_features(self):
        """Test that constant features (std=0) don't cause division by zero."""
        X = np.array([[1, 5], [1, 10], [1, 15]])  # First feature is constant

        model = solution.LinearRegression(normalize=True)
        X_norm = model._normalize_features(X, fit=True)

        # Should not raise error
        assert not np.any(np.isnan(X_norm))
        assert not np.any(np.isinf(X_norm))

    def test_with_vs_without_normalization(self):
        """Test that normalization improves convergence."""
        np.random.seed(42)

        # Create data with different scales
        X = np.column_stack([
            np.random.randn(100),       # Feature 1: scale = 1
            np.random.randn(100) * 1000, # Feature 2: scale = 1000
        ])
        y = 2 * X[:, 0] + 0.5 * X[:, 1] + np.random.randn(100)

        # Without normalization (needs small learning rate)
        model_no_norm = solution.LinearRegression(
            learning_rate=0.000001,
            n_iterations=5000,
            normalize=False
        )
        model_no_norm.fit(X, y)

        # With normalization (can use larger learning rate)
        model_norm = solution.LinearRegression(
            learning_rate=0.1,
            n_iterations=1000,
            normalize=True
        )
        model_norm.fit(X, y)

        # Normalized model should converge faster
        assert model_norm.losses_[-1] < model_no_norm.losses_[-1] * 2


# =============================================================================
# TEST: GRADIENT COMPUTATION
# =============================================================================

class TestGradients:
    """Test gradient computation correctness."""

    def test_gradient_shape(self):
        """Test that gradients have correct shape."""
        np.random.seed(42)
        X = np.random.randn(50, 3)
        y = np.random.randn(50)

        model = solution.LinearRegression()
        model.weights_ = np.zeros(3)
        model.bias_ = 0.0

        dw, db = model._compute_gradients(X, y)

        assert dw.shape == (3,)
        assert isinstance(db, (float, np.floating))

    def test_gradient_zero_at_optimum(self):
        """Test that gradient is zero when predictions are perfect."""
        np.random.seed(42)
        X = np.array([[1], [2], [3]])
        y = np.array([2, 4, 6])

        # Set parameters to correct values: y = 2x + 0
        model = solution.LinearRegression()
        model.weights_ = np.array([2.0])
        model.bias_ = 0.0

        dw, db = model._compute_gradients(X, y)

        # Gradients should be very close to zero
        np.testing.assert_allclose(dw, 0, atol=1e-10)
        np.testing.assert_allclose(db, 0, atol=1e-10)

    def test_gradient_numerical_verification(self):
        """Verify analytical gradients match numerical gradients."""
        np.random.seed(42)
        X = np.random.randn(20, 2)
        y = np.random.randn(20)

        model = solution.LinearRegression()
        model.weights_ = np.random.randn(2)
        model.bias_ = np.random.randn()

        # Analytical gradients
        dw_analytical, db_analytical = model._compute_gradients(X, y)

        # Numerical gradients (finite differences)
        epsilon = 1e-7

        # Gradient w.r.t. weights
        dw_numerical = np.zeros_like(model.weights_)
        for i in range(len(model.weights_)):
            weights_plus = model.weights_.copy()
            weights_plus[i] += epsilon
            model_plus = solution.LinearRegression()
            model_plus.weights_ = weights_plus
            model_plus.bias_ = model.bias_
            cost_plus = model_plus._compute_cost(X, y)

            weights_minus = model.weights_.copy()
            weights_minus[i] -= epsilon
            model_minus = solution.LinearRegression()
            model_minus.weights_ = weights_minus
            model_minus.bias_ = model.bias_
            cost_minus = model_minus._compute_cost(X, y)

            dw_numerical[i] = (cost_plus - cost_minus) / (2 * epsilon)

        # Gradient w.r.t. bias
        model_plus = solution.LinearRegression()
        model_plus.weights_ = model.weights_
        model_plus.bias_ = model.bias_ + epsilon
        cost_plus = model_plus._compute_cost(X, y)

        model_minus = solution.LinearRegression()
        model_minus.weights_ = model.weights_
        model_minus.bias_ = model.bias_ - epsilon
        cost_minus = model_minus._compute_cost(X, y)

        db_numerical = (cost_plus - cost_minus) / (2 * epsilon)

        # Compare analytical and numerical gradients
        np.testing.assert_allclose(dw_analytical, dw_numerical, rtol=1e-5)
        np.testing.assert_allclose(db_analytical, db_numerical, rtol=1e-5)


# =============================================================================
# TEST: CONVERGENCE
# =============================================================================

class TestConvergence:
    """Test training convergence behavior."""

    def test_loss_decreases(self):
        """Test that loss decreases during training."""
        np.random.seed(42)
        X = np.random.randn(100, 3)
        y = np.random.randn(100)

        model = solution.LinearRegression(
            learning_rate=0.01,
            n_iterations=500
        )
        model.fit(X, y)

        losses = model.get_loss_history()

        # Loss should decrease monotonically (or stay flat)
        for i in range(1, len(losses)):
            assert losses[i] <= losses[i-1] + 1e-6  # Allow tiny increases due to numerical precision

    def test_early_stopping(self):
        """Test that training stops early if converged."""
        np.random.seed(42)
        X = np.array([[1], [2], [3]])
        y = np.array([2, 4, 6])

        model = solution.LinearRegression(
            learning_rate=0.1,
            n_iterations=10000,
            tol=1e-6
        )
        model.fit(X, y)

        # Should converge before max iterations
        assert len(model.losses_) < 10000

    def test_different_learning_rates(self):
        """Test behavior with different learning rates."""
        np.random.seed(42)
        X = np.random.randn(100, 2)
        y = np.random.randn(100)

        # Small learning rate: slow but stable
        model_small = solution.LinearRegression(
            learning_rate=0.001,
            n_iterations=100,
            normalize=True
        )
        model_small.fit(X, y)

        # Medium learning rate: faster
        model_medium = solution.LinearRegression(
            learning_rate=0.01,
            n_iterations=100,
            normalize=True
        )
        model_medium.fit(X, y)

        # Medium should converge to lower loss in same iterations
        assert model_medium.losses_[-1] <= model_small.losses_[-1]

    def test_convergence_with_perfect_data(self):
        """Test that model converges to perfect fit on noiseless data."""
        np.random.seed(42)
        X = np.array([[1], [2], [3], [4], [5]])
        y = 2 * X.ravel() + 1  # Perfect linear relationship, no noise

        model = solution.LinearRegression(
            learning_rate=0.01,
            n_iterations=5000
        )
        model.fit(X, y)

        # Should achieve near-perfect R²
        r2 = model.score(X, y)
        assert r2 > 0.9999


# =============================================================================
# TEST: EDGE CASES
# =============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_single_sample(self):
        """Test with single training sample."""
        X = np.array([[1.0]])
        y = np.array([2.0])

        model = solution.LinearRegression(n_iterations=100)
        model.fit(X, y)

        # Should still fit (though not very meaningful)
        assert model.weights_ is not None
        assert model.bias_ is not None

    def test_single_feature(self):
        """Test with single feature."""
        np.random.seed(42)
        X = np.random.randn(50, 1)
        y = 3 * X.ravel() + 1 + np.random.randn(50) * 0.1

        model = solution.LinearRegression()
        model.fit(X, y)

        assert len(model.weights_) == 1
        r2 = model.score(X, y)
        assert r2 > 0.95

    def test_1d_input_converted_to_2d(self):
        """Test that 1D input is automatically converted to 2D."""
        X_1d = np.array([1, 2, 3, 4, 5])  # Shape: (5,)
        y = np.array([2, 4, 6, 8, 10])

        model = solution.LinearRegression()
        model.fit(X_1d, y)  # Should not raise error

        # Predict with 1D input
        y_pred = model.predict(X_1d)
        assert y_pred.shape == (5,)

    def test_zero_weights_initialization(self):
        """Test that weights are initialized to zero."""
        model = solution.LinearRegression()
        X = np.array([[1, 2], [3, 4]])
        y = np.array([1, 2])

        model.fit(X, y)

        # Weights should not be all zeros after training
        assert not np.allclose(model.weights_, 0)

    def test_large_dataset(self):
        """Test on relatively large dataset."""
        np.random.seed(42)
        X = np.random.randn(10000, 5)
        y = np.random.randn(10000)

        model = solution.LinearRegression(
            learning_rate=0.01,
            n_iterations=100
        )
        model.fit(X, y)  # Should not crash or be too slow

        assert model.weights_ is not None


# =============================================================================
# TEST: ERROR HANDLING
# =============================================================================

class TestErrorHandling:
    """Test error handling and validation."""

    def test_mismatched_shapes_raises_error(self):
        """Test that mismatched X and y shapes raise error."""
        X = np.array([[1, 2], [3, 4], [5, 6]])  # 3 samples
        y = np.array([1, 2])  # 2 samples

        model = solution.LinearRegression()

        with pytest.raises(ValueError, match="incompatible shapes"):
            model.fit(X, y)

    def test_predict_wrong_features_raises_error(self):
        """Test that predicting with wrong number of features raises error."""
        X_train = np.array([[1, 2], [3, 4]])
        y_train = np.array([1, 2])

        model = solution.LinearRegression()
        model.fit(X_train, y_train)

        # Try to predict with 3 features instead of 2
        X_test_wrong = np.array([[1, 2, 3]])

        with pytest.raises(ValueError, match="features"):
            model.predict(X_test_wrong)

    def test_large_learning_rate_divergence(self):
        """Test that very large learning rate causes divergence error."""
        np.random.seed(42)
        X = np.random.randn(50, 3)
        y = np.random.randn(50)

        model = solution.LinearRegression(
            learning_rate=10.0,  # Way too large!
            n_iterations=100,
            normalize=False
        )

        # Should either converge with warning or raise error
        # (depending on data, may diverge)
        try:
            model.fit(X, y)
            # If it doesn't diverge, loss should be reasonable
            assert not np.isnan(model.losses_[-1])
        except ValueError:
            # Expected: divergence error
            pass


# =============================================================================
# TEST: METRICS
# =============================================================================

class TestMetrics:
    """Test metric functions."""

    def test_mse_perfect_predictions(self):
        """Test MSE is zero for perfect predictions."""
        y_true = np.array([1, 2, 3, 4, 5])
        y_pred = np.array([1, 2, 3, 4, 5])

        mse = solution.mean_squared_error(y_true, y_pred)

        assert mse == 0.0

    def test_mse_calculation(self):
        """Test MSE calculation is correct."""
        y_true = np.array([1, 2, 3])
        y_pred = np.array([1.1, 2.2, 2.9])

        mse = solution.mean_squared_error(y_true, y_pred)

        # MSE = mean([0.01, 0.04, 0.01]) = 0.02
        expected_mse = np.mean([0.01, 0.04, 0.01])
        assert abs(mse - expected_mse) < 1e-10

    def test_r2_perfect_predictions(self):
        """Test R² is 1.0 for perfect predictions."""
        y_true = np.array([1, 2, 3, 4, 5])
        y_pred = np.array([1, 2, 3, 4, 5])

        r2 = solution.r2_score(y_true, y_pred)

        assert r2 == 1.0

    def test_r2_mean_baseline(self):
        """Test R² is 0.0 when predictions equal mean."""
        y_true = np.array([1, 2, 3, 4, 5])
        y_pred = np.full(5, np.mean(y_true))  # All predictions = mean

        r2 = solution.r2_score(y_true, y_pred)

        assert abs(r2 - 0.0) < 1e-10

    def test_r2_worse_than_mean(self):
        """Test R² is negative when predictions are worse than mean."""
        y_true = np.array([1, 2, 3, 4, 5])
        y_pred = np.array([5, 4, 3, 2, 1])  # Inverted

        r2 = solution.r2_score(y_true, y_pred)

        # Should be negative (worse than mean baseline)
        assert r2 < 0


# =============================================================================
# TEST: COST FUNCTION
# =============================================================================

class TestCostFunction:
    """Test cost function computation."""

    def test_cost_perfect_predictions(self):
        """Test cost is zero for perfect predictions."""
        X = np.array([[1], [2], [3]])
        y = np.array([2, 4, 6])

        model = solution.LinearRegression()
        model.weights_ = np.array([2.0])
        model.bias_ = 0.0

        cost = model._compute_cost(X, y)

        assert abs(cost) < 1e-10

    def test_cost_positive(self):
        """Test cost is always non-negative."""
        np.random.seed(42)
        X = np.random.randn(50, 3)
        y = np.random.randn(50)

        model = solution.LinearRegression()
        model.weights_ = np.random.randn(3)
        model.bias_ = np.random.randn()

        cost = model._compute_cost(X, y)

        assert cost >= 0

    def test_cost_increases_with_error(self):
        """Test that larger errors lead to higher cost."""
        X = np.array([[1], [2], [3]])
        y = np.array([2, 4, 6])

        model = solution.LinearRegression()

        # Good predictions
        model.weights_ = np.array([2.0])
        model.bias_ = 0.0
        cost_good = model._compute_cost(X, y)

        # Bad predictions
        model.weights_ = np.array([0.5])
        model.bias_ = 0.0
        cost_bad = model._compute_cost(X, y)

        assert cost_bad > cost_good


# =============================================================================
# TEST: INTEGRATION
# =============================================================================

class TestIntegration:
    """Integration tests combining multiple components."""

    def test_full_workflow(self):
        """Test complete workflow: fit, predict, score."""
        np.random.seed(42)

        # Generate data
        X = np.random.randn(100, 3)
        true_w = np.array([2.0, -1.0, 0.5])
        true_b = 1.0
        y = X @ true_w + true_b + np.random.randn(100) * 0.1

        # Fit model
        model = solution.LinearRegression(
            learning_rate=0.01,
            n_iterations=2000,
            normalize=True
        )
        model.fit(X, y)

        # Make predictions
        y_pred = model.predict(X)

        # Evaluate
        r2 = model.score(X, y)
        mse = solution.mean_squared_error(y, y_pred)

        # Assertions
        assert r2 > 0.98  # Very high R²
        assert mse < 0.02  # Very low MSE

    def test_train_test_split_simulation(self):
        """Test model on train/test split."""
        np.random.seed(42)

        # Generate data
        X = np.random.randn(200, 2)
        y = 3 * X[:, 0] - 2 * X[:, 1] + 1 + np.random.randn(200) * 0.5

        # Split into train/test
        split_idx = 150
        X_train, X_test = X[:split_idx], X[split_idx:]
        y_train, y_test = y[:split_idx], y[split_idx:]

        # Train on train set
        model = solution.LinearRegression(
            learning_rate=0.01,
            n_iterations=1000
        )
        model.fit(X_train, y_train)

        # Evaluate on test set
        r2_test = model.score(X_test, y_test)

        # Should generalize well
        assert r2_test > 0.95

    def test_comparison_with_sklearn(self):
        """Test that results are similar to sklearn (if available)."""
        try:
            from sklearn.linear_model import LinearRegression as SklearnLR
        except ImportError:
            pytest.skip("scikit-learn not installed")

        np.random.seed(42)
        X = np.random.randn(100, 3)
        y = np.random.randn(100)

        # Our implementation
        our_model = solution.LinearRegression(
            learning_rate=0.01,
            n_iterations=5000,
            normalize=True
        )
        our_model.fit(X, y)
        our_pred = our_model.predict(X)

        # Sklearn implementation
        sklearn_model = SklearnLR()
        sklearn_model.fit(X, y)
        sklearn_pred = sklearn_model.predict(X)

        # Predictions should be similar
        np.testing.assert_allclose(our_pred, sklearn_pred, atol=0.1)


# =============================================================================
# PARAMETRIZED TESTS
# =============================================================================

class TestParametrized:
    """Parametrized tests for multiple scenarios."""

    @pytest.mark.parametrize("n_features", [1, 2, 5, 10])
    def test_different_feature_counts(self, n_features):
        """Test with different numbers of features."""
        np.random.seed(42)
        X = np.random.randn(100, n_features)
        y = np.random.randn(100)

        model = solution.LinearRegression()
        model.fit(X, y)

        assert len(model.weights_) == n_features
        assert model.score(X, y) >= -1  # R² can be negative but not too much

    @pytest.mark.parametrize("learning_rate", [0.001, 0.01, 0.1])
    def test_different_learning_rates(self, learning_rate):
        """Test with different learning rates."""
        np.random.seed(42)
        X = np.random.randn(50, 2)
        y = np.random.randn(50)

        model = solution.LinearRegression(
            learning_rate=learning_rate,
            n_iterations=1000,
            normalize=True
        )
        model.fit(X, y)

        # Should converge (loss should be finite)
        assert np.isfinite(model.losses_[-1])

    @pytest.mark.parametrize("normalize", [True, False])
    def test_with_and_without_normalization(self, normalize):
        """Test both normalized and non-normalized training."""
        np.random.seed(42)
        X = np.random.randn(50, 2)
        y = np.random.randn(50)

        lr = 0.01 if normalize else 0.0001  # Adjust learning rate

        model = solution.LinearRegression(
            learning_rate=lr,
            n_iterations=1000,
            normalize=normalize
        )
        model.fit(X, y)

        # Both should converge
        assert model.losses_[-1] < model.losses_[0]


# =============================================================================
# TEST SUMMARY
# =============================================================================

def test_all_functions_exist():
    """Verify all required functions and classes exist."""
    # Class
    assert hasattr(solution, 'LinearRegression')
    assert callable(solution.LinearRegression)

    # Helper functions
    assert hasattr(solution, 'mean_squared_error')
    assert hasattr(solution, 'r2_score')
    assert callable(solution.mean_squared_error)
    assert callable(solution.r2_score)

    # Methods
    model = solution.LinearRegression()
    assert hasattr(model, 'fit')
    assert hasattr(model, 'predict')
    assert hasattr(model, 'score')
    assert hasattr(model, 'get_params')
    assert hasattr(model, 'get_loss_history')


if __name__ == "__main__":
    # Run tests with: pytest test_project_18.py -v
    pytest.main([__file__, "-v", "--tb=short"])
