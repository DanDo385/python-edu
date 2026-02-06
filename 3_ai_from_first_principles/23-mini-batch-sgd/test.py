"""
Test suite for Project 29: Mini-Batch vs Stochastic Gradient Descent

Run with: pytest test.py -v
"""

import pytest
import numpy as np
from exercise import (
    create_batches,
    count_updates_per_epoch,
    train_with_mini_batches,
    momentum_update,
    compare_batch_sizes,
    verify_all_data_processed,
    SimpleModel,
)


class TestBatchCreation:
    """Test batch creation functions."""
    
    def test_create_batches_basic(self):
        """Test basic batch creation."""
        X = np.random.randn(100, 5)
        y = np.random.randint(0, 2, 100)
        
        batches = create_batches(X, y, batch_size=32, shuffle=False)
        
        assert len(batches) == 4  # 100 / 32 = 3.125 → 4 batches
        assert batches[0][0].shape[0] == 32  # First batch has 32 samples
        assert batches[-1][0].shape[0] == 4   # Last batch has 4 samples (remainder)
    
    def test_create_batches_shuffle(self):
        """Test that shuffling works."""
        X = np.arange(100).reshape(100, 1)
        y = np.arange(100)
        
        batches_shuffled = create_batches(X, y, batch_size=32, shuffle=True, random_seed=42)
        batches_not_shuffled = create_batches(X, y, batch_size=32, shuffle=False)
        
        # First batch should differ
        assert not np.array_equal(
            batches_shuffled[0][0],
            batches_not_shuffled[0][0]
        )
    
    def test_verify_all_data_processed(self):
        """Test that all data is included in batches."""
        X = np.random.randn(100, 5)
        y = np.random.randint(0, 2, 100)
        
        batches = create_batches(X, y, batch_size=32)
        
        assert verify_all_data_processed(batches, 100) == True
        
        # Check manually
        total_samples = sum(batch[0].shape[0] for batch in batches)
        assert total_samples == 100


class TestUpdateCounting:
    """Test update counting functions."""
    
    def test_count_updates_sgd(self):
        """Test counting updates for SGD (batch_size=1)."""
        updates = count_updates_per_epoch(100, batch_size=1)
        assert updates == 100
    
    def test_count_updates_batch_gd(self):
        """Test counting updates for Batch GD (batch_size=dataset)."""
        updates = count_updates_per_epoch(100, batch_size=100)
        assert updates == 1
    
    def test_count_updates_mini_batch(self):
        """Test counting updates for mini-batch."""
        updates = count_updates_per_epoch(100, batch_size=32)
        assert updates == 4  # ceil(100/32) = 4
    
    def test_compare_batch_sizes(self):
        """Test comparing different batch sizes."""
        result = compare_batch_sizes(100, [1, 32, 100])
        
        assert result[1] == 100   # SGD: 100 updates
        assert result[32] == 4    # Mini-batch: 4 updates
        assert result[100] == 1   # Batch GD: 1 update


class TestMomentum:
    """Test momentum update."""
    
    def test_momentum_update(self):
        """Test momentum update formula."""
        weights = np.array([1.0, 2.0])
        gradients = np.array([0.1, 0.2])
        velocity = np.array([0.0, 0.0])
        learning_rate = 0.01
        momentum = 0.9
        
        updated_weights, updated_velocity = momentum_update(
            weights, gradients, velocity, learning_rate, momentum
        )
        
        # First update: velocity = 0.9 * 0 + 0.01 * [0.1, 0.2] = [0.001, 0.002]
        expected_velocity = momentum * velocity + learning_rate * gradients
        assert np.allclose(updated_velocity, expected_velocity)
        
        # Weights: [1.0, 2.0] - [0.001, 0.002] = [0.999, 1.998]
        expected_weights = weights - updated_velocity
        assert np.allclose(updated_weights, expected_weights)
    
    def test_momentum_accumulates(self):
        """Test that momentum accumulates over multiple updates."""
        weights = np.array([1.0])
        velocity = np.array([0.0])
        learning_rate = 0.01
        momentum = 0.9
        
        # First update with constant gradient
        gradients = np.array([1.0])
        weights, velocity = momentum_update(weights, gradients, velocity, learning_rate, momentum)
        
        # Second update
        weights, velocity = momentum_update(weights, gradients, velocity, learning_rate, momentum)
        
        # Velocity should accumulate
        # After 1st: v = 0.9*0 + 0.01*1 = 0.01
        # After 2nd: v = 0.9*0.01 + 0.01*1 = 0.009 + 0.01 = 0.019
        assert velocity[0] > 0.01  # Should be larger than first update


class TestMiniBatchTraining:
    """Test mini-batch training."""
    
    def test_train_with_mini_batches(self):
        """Test training with mini-batches."""
        model = SimpleModel()
        X = np.random.randn(100, 2)
        y = np.random.randint(0, 2, 100)
        
        initial_update_count = model.update_count
        
        loss_history = train_with_mini_batches(
            model, X, y, batch_size=32, learning_rate=0.01, epochs=1
        )
        
        # Should have 4 updates (100 / 32 = 4 batches)
        assert model.update_count == initial_update_count + 4
    
    def test_batch_size_affects_updates(self):
        """Test that batch size affects number of updates."""
        model1 = SimpleModel()
        model2 = SimpleModel()
        X = np.random.randn(100, 2)
        y = np.random.randint(0, 2, 100)
        
        # Small batch size → more updates
        train_with_mini_batches(model1, X, y, batch_size=10, learning_rate=0.01)
        
        # Large batch size → fewer updates
        train_with_mini_batches(model2, X, y, batch_size=50, learning_rate=0.01)
        
        assert model1.update_count > model2.update_count
