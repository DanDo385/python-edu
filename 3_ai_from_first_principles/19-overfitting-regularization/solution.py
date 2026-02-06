"""
Project 27: Overfitting and Regularization Techniques - SOLUTION

Complete solution demonstrating how regularization prevents overfitting.
"""

import numpy as np


def sigmoid(x):
    """Sigmoid activation."""
    return 1 / (1 + np.exp(-np.clip(x, -250, 250)))


def relu(x):
    """ReLU activation."""
    return np.maximum(0, x)


def relu_derivative(x):
    """Derivative of ReLU."""
    return (x > 0).astype(float)


def compute_l2_penalty(weights):
    """
    Compute L2 regularization penalty for a set of weights.
    
    L2 penalty = sum(weights^2)
    This encourages weights to stay small.
    """
    return np.sum(weights ** 2)


def apply_dropout(activations, dropout_rate, training=True):
    """
    Apply dropout to activations.
    
    During training: Randomly zero out activations
    During inference: Scale activations by (1 - dropout_rate)
    """
    if training and dropout_rate > 0:
        # Create random mask: values > dropout_rate are kept
        mask = (np.random.rand(*activations.shape) > dropout_rate).astype(float)
        
        # Apply mask and scale to preserve expected value
        # Scaling by (1 - dropout_rate) ensures E[output] = E[input]
        dropped = activations * mask / (1 - dropout_rate)
        return dropped, mask
    else:
        # During inference: scale by (1 - dropout_rate)
        if dropout_rate > 0:
            return activations * (1 - dropout_rate), None
        else:
            return activations, None


def compute_loss_with_l2(y_true, y_pred, weights, lambda_reg=0.01):
    """
    Compute loss with L2 regularization penalty.
    
    Total Loss = Binary Cross-Entropy + λ * sum(weights^2)
    """
    # Binary cross-entropy loss
    epsilon = 1e-15  # Small value to prevent log(0)
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    bce_loss = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    
    # L2 regularization penalty
    l2_penalty = 0.0
    for weight_matrix in weights:
        l2_penalty += compute_l2_penalty(weight_matrix)
    
    # Total loss
    total_loss = bce_loss + lambda_reg * l2_penalty
    
    return total_loss


class RegularizedMLP:
    """
    MLP with regularization capabilities (L2 and dropout).
    
    This demonstrates how regularization prevents overfitting by:
    1. L2 regularization: Penalizing large weights
    2. Dropout: Preventing co-adaptation of neurons
    """
    
    def __init__(self, input_size, hidden_size, output_size, 
                 dropout_rate=0.0, lambda_reg=0.0):
        """Initialize regularized MLP."""
        np.random.seed(42)
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros(hidden_size)
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros(output_size)
        
        self.dropout_rate = dropout_rate
        self.lambda_reg = lambda_reg
        self.training = True
        self.dropout_mask = None  # Store mask for potential backprop
    
    def forward(self, X):
        """Forward pass with optional dropout."""
        # Layer 1
        z1 = X @ self.W1 + self.b1
        h = relu(z1)
        
        # Apply dropout to hidden layer
        if self.dropout_rate > 0:
            h, self.dropout_mask = apply_dropout(h, self.dropout_rate, self.training)
        
        # Layer 2
        z2 = h @ self.W2 + self.b2
        output = sigmoid(z2)
        
        return output
    
    def compute_loss(self, y_true, y_pred):
        """Compute loss with L2 regularization."""
        return compute_loss_with_l2(y_true, y_pred, [self.W1, self.W2], self.lambda_reg)
    
    def train_mode(self):
        """Set model to training mode (dropout enabled)."""
        self.training = True
    
    def eval_mode(self):
        """Set model to evaluation mode (dropout disabled)."""
        self.training = False


def detect_overfitting(train_losses, val_losses):
    """
    Detect if model is overfitting.
    
    Overfitting occurs when:
    - Training loss decreases
    - Validation loss increases
    """
    initial_train = train_losses[0]
    initial_val = val_losses[0]
    final_train = train_losses[-1]
    final_val = val_losses[-1]
    
    # Overfitting: train decreases AND val increases
    is_overfitting = (final_train < initial_train) and (final_val > initial_val)
    
    gap = final_train - final_val
    
    return {
        'is_overfitting': is_overfitting,
        'train_final': final_train,
        'val_final': final_val,
        'gap': gap
    }


def compare_with_without_regularization(train_losses_no_reg, val_losses_no_reg,
                                        train_losses_reg, val_losses_reg):
    """
    Compare model performance with and without regularization.
    
    Regularization should improve validation performance.
    """
    # Final losses
    val_no_reg = val_losses_no_reg[-1]
    val_reg = val_losses_reg[-1]
    
    # Gaps (train - val)
    gap_no_reg = train_losses_no_reg[-1] - val_losses_no_reg[-1]
    gap_reg = train_losses_reg[-1] - val_losses_reg[-1]
    
    # Improvements (positive = better)
    val_improvement = val_no_reg - val_reg  # Lower loss is better
    gap_reduction = gap_no_reg - gap_reg
    
    return {
        'val_improvement': val_improvement,
        'gap_reduction': gap_reduction,
    }


# Example usage
if __name__ == "__main__":
    # Create small dataset (prone to overfitting)
    np.random.seed(42)
    X = np.random.randn(50, 2)
    y = (X[:, 0] + X[:, 1] > 0).astype(float)
    
    # Model without regularization (will overfit)
    model_no_reg = RegularizedMLP(2, 20, 1, dropout_rate=0.0, lambda_reg=0.0)
    
    # Model with regularization (should generalize better)
    model_reg = RegularizedMLP(2, 20, 1, dropout_rate=0.3, lambda_reg=0.01)
    
    print("Regularization helps prevent overfitting!")
    print(f"L2 penalty for W1: {compute_l2_penalty(model_reg.W1):.4f}")
    
    # Test dropout
    model_reg.train_mode()
    X_test = np.array([[1.0, 2.0]])
    output_train = model_reg.forward(X_test)
    
    model_reg.eval_mode()
    output_eval = model_reg.forward(X_test)
    
    print(f"\nDropout during training: {output_train[0, 0]:.4f}")
    print(f"Dropout during eval: {output_eval[0, 0]:.4f}")
