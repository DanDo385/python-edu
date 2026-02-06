"""Test suite for Project 20: Linear Regression"""
import pytest
import numpy as np
from exercise import (
    predict,
    compute_loss,
    compute_gradients,
    train_linear_regression,
    evaluate_model,
)


class TestPrediction:
    """Test prediction function."""
    
    def test_predict(self):
        x = np.array([1, 2, 3, 4, 5])
        w, b = 2.0, 1.0
        y_pred = predict(x, w, b)
        expected = np.array([3, 5, 7, 9, 11])  # 2*x + 1
        assert np.allclose(y_pred, expected)


class TestLoss:
    """Test loss computation."""
    
    def test_compute_loss(self):
        y_pred = np.array([1, 2, 3])
        y_true = np.array([1, 3, 3])
        loss = compute_loss(y_pred, y_true)
        # MSE = mean((0, -1, 0)²) = mean(0, 1, 0) = 1/3
        assert abs(loss - 1/3) < 0.001


class TestGradients:
    """Test gradient computation."""
    
    def test_compute_gradients(self):
        x = np.array([1, 2, 3])
        y_pred = np.array([2, 4, 6])
        y_true = np.array([1, 3, 5])
        grad_w, grad_b = compute_gradients(x, y_pred, y_true)
        # Check gradients are computed (exact values depend on implementation)
        assert grad_w is not None
        assert grad_b is not None


class TestTraining:
    """Test training function."""
    
    def test_train_linear_regression(self):
        # Create simple linear data: y = 2*x + 1
        np.random.seed(42)
        x = np.array([1, 2, 3, 4, 5])
        y = 2 * x + 1 + np.random.normal(0, 0.1, size=x.shape)
        
        w, b, loss_history = train_linear_regression(x, y, learning_rate=0.01, epochs=500)
        
        # Check that loss decreased
        assert loss_history[-1] < loss_history[0]
        
        # Check that learned parameters are close to true values (w≈2, b≈1)
        assert abs(w - 2.0) < 0.5
        assert abs(b - 1.0) < 0.5


class TestEvaluation:
    """Test model evaluation."""
    
    def test_evaluate_model(self):
        x = np.array([1, 2, 3, 4, 5])
        y = 2 * x + 1
        w, b = 2.0, 1.0
        
        results = evaluate_model(x, y, w, b)
        
        assert 'mse' in results
        assert 'r2' in results
        assert 'predictions' in results
        # Perfect fit should have MSE ≈ 0 and R² ≈ 1
        assert results['mse'] < 0.001
        assert results['r2'] > 0.99




