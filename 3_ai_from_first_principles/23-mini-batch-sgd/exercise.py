"""
Project 29: Mini-Batch vs Stochastic Gradient Descent

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""

import numpy as np


def create_batches(X, y, batch_size, shuffle=True, random_seed=42):
    """
    Create mini-batches from dataset.
    
    Args:
        X (np.ndarray): Features, shape (n_samples, n_features)
        y (np.ndarray): Labels, shape (n_samples,)
        batch_size (int): Size of each batch
        shuffle (bool): Whether to shuffle data before batching (default True)
        random_seed (int): Random seed for shuffling (default 42)
    
    Returns:
        list: List of tuples (batch_X, batch_y) for each batch
    
    Note:
        - If batch_size doesn't divide dataset evenly, last batch may be smaller
        - Shuffling is important to avoid order bias
    """
    # TODO: Create batches
    # 1. Set random seed if shuffling
    # 2. Shuffle indices if shuffle=True
    # 3. Create batches by slicing X and y
    # 4. Return list of (batch_X, batch_y) tuples
    return []


def count_updates_per_epoch(n_samples, batch_size):
    """
    Count how many weight updates occur per epoch for given batch size.
    
    Args:
        n_samples (int): Total number of samples
        batch_size (int): Size of each batch
    
    Returns:
        int: Number of updates per epoch
    
    Examples:
        n_samples=100, batch_size=32 → 4 updates (last batch smaller)
        n_samples=100, batch_size=1 → 100 updates (SGD)
        n_samples=100, batch_size=100 → 1 update (Batch GD)
    """
    # TODO: Calculate number of batches/updates
    # Hint: Use ceiling division: (n_samples + batch_size - 1) // batch_size
    return None


def train_with_mini_batches(model, X, y, batch_size, learning_rate, epochs=1):
    """
    Train model using mini-batch gradient descent.
    
    Args:
        model: Model object with forward() and backward() methods
        X (np.ndarray): Training features
        y (np.ndarray): Training labels
        batch_size (int): Batch size
        learning_rate (float): Learning rate
        epochs (int): Number of epochs
    
    Returns:
        list: Loss history (one loss per batch)
    
    Note:
        This simulates training - in practice, model would have train() method
        For this exercise, we'll track number of updates
    """
    # TODO: Implement mini-batch training
    # 1. Create batches
    # 2. For each epoch:
    #    - For each batch:
    #      - Forward pass
    #      - Compute loss
    #      - Backward pass (compute gradients)
    #      - Update weights
    #      - Track loss
    # 3. Return loss history
    
    # For this exercise, simulate by counting updates
    loss_history = []
    return loss_history


def momentum_update(weights, gradients, velocity, learning_rate, momentum=0.9):
    """
    Update weights using momentum.
    
    Momentum accumulates velocity in direction of persistent gradients.
    
    Args:
        weights (np.ndarray): Current weights
        gradients (np.ndarray): Current gradients
        velocity (np.ndarray): Current velocity (from previous update)
        learning_rate (float): Learning rate
        momentum (float): Momentum coefficient (default 0.9)
    
    Returns:
        tuple: (updated_weights, updated_velocity)
    
    Formula:
        velocity = momentum * velocity + learning_rate * gradients
        weights = weights - velocity
    """
    # TODO: Implement momentum update
    # 1. Update velocity: momentum * velocity + lr * gradients
    # 2. Update weights: weights - velocity
    # 3. Return updated weights and velocity
    updated_weights = None
    updated_velocity = None
    return updated_weights, updated_velocity


def compare_batch_sizes(n_samples, batch_sizes):
    """
    Compare different batch sizes and their effect on training.
    
    Args:
        n_samples (int): Total number of samples
        batch_sizes (list): List of batch sizes to compare
    
    Returns:
        dict: Dictionary mapping batch_size to number of updates per epoch
    
    Note:
        This helps understand trade-offs:
        - Small batch → more updates (faster convergence potentially)
        - Large batch → fewer updates (more stable)
    """
    # TODO: Count updates for each batch size
    result = {}
    return result


def verify_all_data_processed(batches, original_size):
    """
    Verify that all data is included in batches (no data lost).
    
    Args:
        batches (list): List of (batch_X, batch_y) tuples
        original_size (int): Original dataset size
    
    Returns:
        bool: True if all data is included
    
    Note:
        Sum of all batch sizes should equal original_size
    """
    # TODO: Check that sum of batch sizes equals original_size
    return None


class SimpleModel:
    """
    Simple model for testing mini-batch training.
    
    This is a minimal model that tracks updates.
    """
    
    def __init__(self):
        self.update_count = 0
        self.weights = np.array([1.0, 2.0])
    
    def forward(self, X):
        """Forward pass (simplified)."""
        return X @ self.weights
    
    def backward(self, X, y, output):
        """Backward pass (simplified)."""
        # Simulate gradient computation
        return np.ones_like(self.weights)
    
    def update(self, gradients, learning_rate):
        """Update weights."""
        self.weights -= learning_rate * gradients
        self.update_count += 1
