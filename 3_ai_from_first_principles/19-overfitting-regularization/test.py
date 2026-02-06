"""
Test suite for Project 27: Overfitting and Regularization

Run with: pytest test.py -v
"""

import pytest
import numpy as np
from exercise import (
    compute_l2_penalty,
    apply_dropout,
    compute_loss_with_l2,
    RegularizedMLP,
    detect_overfitting,
    compare_with_without_regularization,
)


class TestL2Regularization:
    """Test L2 regularization functions."""
    
    def test_compute_l2_penalty(self):
        """Test L2 penalty computation."""
        weights = np.array([[1.0, 2.0], [3.0, 4.0]])
        penalty = compute_l2_penalty(weights)
        
        # Sum of squares: 1^2 + 2^2 + 3^2 + 4^2 = 1 + 4 + 9 + 16 = 30
        assert abs(penalty - 30.0) < 0.001
    
    def test_l2_penalty_encourages_small_weights(self):
        """Test that L2 penalty is larger for larger weights."""
        small_weights = np.array([[0.1, 0.2]])
        large_weights = np.array([[1.0, 2.0]])
        
        small_penalty = compute_l2_penalty(small_weights)
        large_penalty = compute_l2_penalty(large_weights)
        
        assert large_penalty > small_penalty


class TestDropout:
    """Test dropout implementation."""
    
    def test_dropout_training_mode(self):
        """Test dropout during training."""
        activations = np.ones((10, 5))  # All ones
        dropped, mask = apply_dropout(activations, dropout_rate=0.5, training=True)
        
        # Some activations should be zeroed
        assert np.any(dropped == 0)
        
        # Mask should have zeros where dropout occurred
        assert np.any(mask == 0)
        assert np.any(mask == 1)
    
    def test_dropout_eval_mode(self):
        """Test dropout during evaluation (should scale but not zero)."""
        activations = np.ones((10, 5))
        dropped, mask = apply_dropout(activations, dropout_rate=0.5, training=False)
        
        # In eval mode, should scale by (1 - dropout_rate) = 0.5
        expected = activations * 0.5
        assert np.allclose(dropped, expected)
    
    def test_dropout_preserves_expected_value(self):
        """Test that dropout preserves expected value (on average)."""
        activations = np.ones((1000, 100))
        dropout_rate = 0.3
        
        # Run many times and average
        results = []
        for _ in range(100):
            dropped, _ = apply_dropout(activations, dropout_rate, training=True)
            results.append(np.mean(dropped))
        
        # Average should be close to original (scaling preserves expected value)
        avg_result = np.mean(results)
        assert abs(avg_result - 1.0) < 0.1  # Allow some variance


class TestLossWithL2:
    """Test loss computation with L2 regularization."""
    
    def test_loss_increases_with_regularization(self):
        """Test that adding L2 regularization increases loss."""
        y_true = np.array([1, 0, 1, 0])
        y_pred = np.array([0.9, 0.1, 0.8, 0.2])
        weights = [np.array([[1.0, 2.0]]), np.array([[3.0]])]
        
        loss_no_reg = compute_loss_with_l2(y_true, y_pred, weights, lambda_reg=0.0)
        loss_with_reg = compute_loss_with_l2(y_true, y_pred, weights, lambda_reg=0.1)
        
        assert loss_with_reg > loss_no_reg
    
    def test_regularization_penalty_scales_with_lambda(self):
        """Test that larger lambda increases regularization penalty."""
        y_true = np.array([1, 0])
        y_pred = np.array([0.9, 0.1])
        weights = [np.array([[1.0]])]
        
        loss_low = compute_loss_with_l2(y_true, y_pred, weights, lambda_reg=0.01)
        loss_high = compute_loss_with_l2(y_true, y_pred, weights, lambda_reg=0.1)
        
        assert loss_high > loss_low


class TestRegularizedMLP:
    """Test RegularizedMLP class."""
    
    def test_forward_pass_without_dropout(self):
        """Test forward pass when dropout is disabled."""
        model = RegularizedMLP(2, 4, 1, dropout_rate=0.0)
        X = np.array([[1.0, 2.0], [3.0, 4.0]])
        
        output = model.forward(X)
        
        assert output is not None
        assert output.shape == (2, 1)
        assert np.all(output >= 0) and np.all(output <= 1)  # Sigmoid output
    
    def test_forward_pass_with_dropout(self):
        """Test forward pass with dropout enabled."""
        model = RegularizedMLP(2, 4, 1, dropout_rate=0.5)
        model.train_mode()
        X = np.array([[1.0, 2.0]])
        
        output = model.forward(X)
        
        assert output is not None
        assert output.shape == (1, 1)
    
    def test_training_vs_eval_mode(self):
        """Test that training and eval modes behave differently."""
        model = RegularizedMLP(2, 4, 1, dropout_rate=0.5)
        X = np.array([[1.0, 2.0]])
        
        # Training mode
        model.train_mode()
        output_train = model.forward(X)
        
        # Eval mode
        model.eval_mode()
        output_eval = model.forward(X)
        
        # Outputs might differ due to dropout randomness
        # But both should be valid
        assert output_train is not None
        assert output_eval is not None
    
    def test_compute_loss_includes_regularization(self):
        """Test that loss computation includes L2 regularization."""
        model = RegularizedMLP(2, 4, 1, lambda_reg=0.1)
        y_true = np.array([1, 0])
        y_pred = np.array([0.9, 0.1])
        
        loss = model.compute_loss(y_true, y_pred)
        
        assert loss > 0
        # Loss should be larger than without regularization
        model_no_reg = RegularizedMLP(2, 4, 1, lambda_reg=0.0)
        loss_no_reg = model_no_reg.compute_loss(y_true, y_pred)
        assert loss > loss_no_reg


class TestOverfittingDetection:
    """Test overfitting detection functions."""
    
    def test_detect_overfitting(self):
        """Test detection of overfitting scenario."""
        # Simulate overfitting: train loss decreases, val loss increases
        train_losses = [0.5, 0.3, 0.2, 0.1, 0.05]
        val_losses = [0.5, 0.4, 0.45, 0.5, 0.55]
        
        result = detect_overfitting(train_losses, val_losses)
        
        assert result['is_overfitting'] == True
        assert result['train_final'] < result['val_final']
        assert result['gap'] < 0  # Negative gap means val > train
    
    def test_detect_no_overfitting(self):
        """Test detection when model is not overfitting."""
        # Both losses decrease together
        train_losses = [0.5, 0.4, 0.3, 0.2, 0.15]
        val_losses = [0.5, 0.45, 0.35, 0.25, 0.2]
        
        result = detect_overfitting(train_losses, val_losses)
        
        # Should not detect overfitting (both improving)
        assert result['is_overfitting'] == False
    
    def test_compare_regularization_improves_validation(self):
        """Test that regularization improves validation performance."""
        # Without regularization: overfitting
        train_no_reg = [0.5, 0.3, 0.1, 0.05]
        val_no_reg = [0.5, 0.45, 0.5, 0.55]
        
        # With regularization: better generalization
        train_reg = [0.5, 0.35, 0.25, 0.2]
        val_reg = [0.5, 0.4, 0.35, 0.3]
        
        result = compare_with_without_regularization(
            train_no_reg, val_no_reg,
            train_reg, val_reg
        )
        
        # Validation should improve (lower loss)
        assert result['val_improvement'] > 0
        # Gap should reduce
        assert result['gap_reduction'] > 0


class TestIntegration:
    """Integration tests."""
    
    def test_regularization_reduces_weight_magnitude(self):
        """Test that L2 regularization encourages smaller weights."""
        # This is a conceptual test - in practice, weights would be updated
        # during training, but we can verify the penalty encourages small weights
        
        small_weights = [np.array([[0.1, 0.2]])]
        large_weights = [np.array([[1.0, 2.0]])]
        
        y_true = np.array([1, 0])
        y_pred = np.array([0.9, 0.1])
        
        loss_small = compute_loss_with_l2(y_true, y_pred, small_weights, lambda_reg=0.1)
        loss_large = compute_loss_with_l2(y_true, y_pred, large_weights, lambda_reg=0.1)
        
        # Larger weights lead to larger penalty
        reg_penalty_small = compute_l2_penalty(small_weights[0])
        reg_penalty_large = compute_l2_penalty(large_weights[0])
        
        assert reg_penalty_large > reg_penalty_small
