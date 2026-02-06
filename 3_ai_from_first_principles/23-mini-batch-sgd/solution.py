"""
Project 29: Mini-Batch vs Stochastic Gradient Descent - SOLUTION

Complete solution demonstrating batch processing and momentum.
"""

import numpy as np


def create_batches(X, y, batch_size, shuffle=True, random_seed=42):
    """
    Create mini-batches from dataset.
    """
    n_samples = len(X)
    
    # Create indices
    indices = np.arange(n_samples)
    
    # Shuffle if requested
    if shuffle:
        np.random.seed(random_seed)
        np.random.shuffle(indices)
    
    # Create batches
    batches = []
    for i in range(0, n_samples, batch_size):
        batch_indices = indices[i:i+batch_size]
        batch_X = X[batch_indices]
        batch_y = y[batch_indices]
        batches.append((batch_X, batch_y))
    
    return batches


def count_updates_per_epoch(n_samples, batch_size):
    """
    Count how many weight updates occur per epoch.
    """
    # Ceiling division: (n_samples + batch_size - 1) // batch_size
    num_batches = (n_samples + batch_size - 1) // batch_size
    return num_batches


def train_with_mini_batches(model, X, y, batch_size, learning_rate, epochs=1):
    """
    Train model using mini-batch gradient descent.
    """
    loss_history = []
    
    for epoch in range(epochs):
        # Create batches
        batches = create_batches(X, y, batch_size, shuffle=True)
        
        for batch_X, batch_y in batches:
            # Forward pass
            output = model.forward(batch_X)
            
            # Compute loss (simplified)
            loss = np.mean((output - batch_y) ** 2)
            loss_history.append(loss)
            
            # Backward pass
            gradients = model.backward(batch_X, batch_y, output)
            
            # Update weights
            model.update(gradients, learning_rate)
    
    return loss_history


def momentum_update(weights, gradients, velocity, learning_rate, momentum=0.9):
    """
    Update weights using momentum.
    
    Momentum accumulates velocity in direction of persistent gradients.
    """
    # Update velocity: accumulate gradient direction
    velocity = momentum * velocity + learning_rate * gradients
    
    # Update weights: move in direction of velocity
    updated_weights = weights - velocity
    
    return updated_weights, velocity


def compare_batch_sizes(n_samples, batch_sizes):
    """
    Compare different batch sizes and their effect on training.
    """
    result = {}
    for batch_size in batch_sizes:
        result[batch_size] = count_updates_per_epoch(n_samples, batch_size)
    return result


def verify_all_data_processed(batches, original_size):
    """
    Verify that all data is included in batches.
    """
    total_samples = sum(batch[0].shape[0] for batch in batches)
    return total_samples == original_size


class SimpleModel:
    """
    Simple model for testing mini-batch training.
    """
    
    def __init__(self):
        self.update_count = 0
        self.weights = np.array([1.0, 2.0])
    
    def forward(self, X):
        """Forward pass."""
        return X @ self.weights
    
    def backward(self, X, y, output):
        """Backward pass."""
        # Simplified gradient
        return np.ones_like(self.weights)
    
    def update(self, gradients, learning_rate):
        """Update weights."""
        self.weights -= learning_rate * gradients
        self.update_count += 1


# Example usage
if __name__ == "__main__":
    # Create sample data
    X = np.random.randn(100, 5)
    y = np.random.randint(0, 2, 100)
    
    # Compare batch sizes
    batch_sizes = [1, 32, 64, 100]
    comparison = compare_batch_sizes(100, batch_sizes)
    
    print("Updates per epoch for different batch sizes:")
    for bs, updates in comparison.items():
        print(f"  Batch size {bs}: {updates} updates")
    
    # Test momentum
    weights = np.array([1.0, 2.0])
    velocity = np.array([0.0, 0.0])
    gradients = np.array([0.1, 0.2])
    
    print("\nMomentum update:")
    print(f"  Initial weights: {weights}")
    print(f"  Initial velocity: {velocity}")
    
    weights, velocity = momentum_update(weights, gradients, velocity, 0.01, 0.9)
    print(f"  After update - weights: {weights}")
    print(f"  After update - velocity: {velocity}")
