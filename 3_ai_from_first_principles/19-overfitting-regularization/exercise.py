"""
Project 27: Overfitting and Regularization Techniques

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.

This project builds on Project 25's SimpleMLP and adds regularization.
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
    
    This encourages weights to stay small, preventing overfitting.
    
    Args:
        weights (np.ndarray): Weight matrix or array
    
    Returns:
        float: L2 penalty (sum of squared weights)
    """
    # TODO: Compute sum of squared weights
    return None


def apply_dropout(activations, dropout_rate, training=True):
    """
    Apply dropout to activations.
    
    During training: Randomly zero out activations with probability dropout_rate
    During inference: Return activations scaled by (1 - dropout_rate)
    
    Args:
        activations (np.ndarray): Layer activations
        dropout_rate (float): Probability of dropping a neuron (0.0 to 1.0)
        training (bool): Whether in training mode (default True)
    
    Returns:
        np.ndarray: Dropped out activations
        np.ndarray: Dropout mask (for backprop, if needed)
    
    Note:
        - During training: activations * mask / (1 - dropout_rate)
        - During inference: activations * (1 - dropout_rate)
        - The scaling ensures expected value is preserved
    """
    # TODO: Implement dropout
    # If training:
    #   1. Create random mask (values > dropout_rate)
    #   2. Apply mask to activations
    #   3. Scale by (1 - dropout_rate) to preserve expected value
    # Else:
    #   Scale activations by (1 - dropout_rate)
    mask = None
    return None, mask


def compute_loss_with_l2(y_true, y_pred, weights, lambda_reg=0.01):
    """
    Compute loss with L2 regularization penalty.
    
    Total Loss = Binary Cross-Entropy Loss + λ * L2_penalty
    
    Args:
        y_true (np.ndarray): True labels
        y_pred (np.ndarray): Predicted probabilities
        weights (list): List of weight matrices [W1, W2, ...]
        lambda_reg (float): Regularization strength (default 0.01)
    
    Returns:
        float: Total loss (data loss + regularization)
    """
    # TODO: Compute binary cross-entropy loss
    # BCE = -mean(y_true * log(y_pred) + (1 - y_true) * log(1 - y_pred))
    # Then add L2 penalty for all weights
    # Hint: Use compute_l2_penalty for each weight matrix
    return None


class RegularizedMLP:
    """
    MLP with regularization capabilities (L2 and dropout).
    
    This extends SimpleMLP from Project 25 with:
    - L2 regularization in loss computation
    - Dropout in forward pass
    - Training vs evaluation modes
    """
    
    def __init__(self, input_size, hidden_size, output_size, 
                 dropout_rate=0.0, lambda_reg=0.0):
        """
        Initialize regularized MLP.
        
        Args:
            input_size (int): Number of input features
            hidden_size (int): Number of hidden neurons
            output_size (int): Number of output neurons
            dropout_rate (float): Dropout probability (0.0 = no dropout)
            lambda_reg (float): L2 regularization strength (0.0 = no regularization)
        """
        # Initialize weights (same as SimpleMLP)
        np.random.seed(42)
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros(hidden_size)
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros(output_size)
        
        self.dropout_rate = dropout_rate
        self.lambda_reg = lambda_reg
        self.training = True  # Training mode flag
    
    def forward(self, X):
        """
        Forward pass with optional dropout.
        
        Args:
            X (np.ndarray): Input data, shape (batch_size, input_size)
        
        Returns:
            np.ndarray: Output predictions
        """
        # TODO: Implement forward pass with dropout
        # Layer 1: z1 = X @ W1 + b1, h = ReLU(z1)
        # Apply dropout to h if dropout_rate > 0 and training
        # Layer 2: z2 = h @ W2 + b2, output = sigmoid(z2)
        # Store dropout mask for potential backprop use
        return None
    
    def compute_loss(self, y_true, y_pred):
        """
        Compute loss with L2 regularization.
        
        Args:
            y_true (np.ndarray): True labels
            y_pred (np.ndarray): Predicted probabilities
        
        Returns:
            float: Total loss
        """
        # TODO: Use compute_loss_with_l2
        return None
    
    def train_mode(self):
        """Set model to training mode (dropout enabled)."""
        # TODO: Set training flag to True
        pass
    
    def eval_mode(self):
        """Set model to evaluation mode (dropout disabled)."""
        # TODO: Set training flag to False
        pass


def detect_overfitting(train_losses, val_losses):
    """
    Detect if model is overfitting by comparing training and validation losses.
    
    Overfitting occurs when:
    - Training loss decreases
    - Validation loss increases or plateaus
    - Gap between train and val loss grows
    
    Args:
        train_losses (list): Training loss per epoch
        val_losses (list): Validation loss per epoch
    
    Returns:
        dict: Dictionary with keys:
            - 'is_overfitting' (bool): True if overfitting detected
            - 'train_final' (float): Final training loss
            - 'val_final' (float): Final validation loss
            - 'gap' (float): Final gap (train - val)
    
    Note:
        Overfitting is detected if:
        - Final validation loss > initial validation loss, AND
        - Final training loss < initial training loss
    """
    # TODO: Detect overfitting
    # Check if val loss increased while train loss decreased
    return {
        'is_overfitting': None,
        'train_final': None,
        'val_final': None,
        'gap': None
    }


def compare_with_without_regularization(train_losses_no_reg, val_losses_no_reg,
                                        train_losses_reg, val_losses_reg):
    """
    Compare model performance with and without regularization.
    
    Regularization should:
    - Increase training loss (model is constrained)
    - Decrease validation loss (better generalization)
    - Reduce generalization gap
    
    Args:
        train_losses_no_reg (list): Training losses without regularization
        val_losses_no_reg (list): Validation losses without regularization
        train_losses_reg (list): Training losses with regularization
        val_losses_reg (list): Validation losses with regularization
    
    Returns:
        dict: Comparison results with improvement metrics
    """
    # TODO: Compare final losses and gaps
    # Regularization should improve validation performance
    return {
        'val_improvement': None,  # val_loss_no_reg - val_loss_reg (positive = improvement)
        'gap_reduction': None,   # gap_no_reg - gap_reg (positive = improvement)
    }
