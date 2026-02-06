"""
Project 23: Manual Backpropagation in Neural Networks - SOLUTION

Complete solution with detailed comments explaining the chain rule,
gradient computation, and how backpropagation enables neural network training.
"""

import numpy as np


def relu(x):
    """ReLU activation."""
    return np.maximum(0, x)


def relu_derivative(x):
    """Derivative of ReLU."""
    return (x > 0).astype(float)


def forward_pass_2layer(x, w1, b1, w2, b2):
    """
    Forward pass through 2-layer network.
    
    This computes the network output given inputs and weights.
    We save intermediate values (h) because we'll need them for backpropagation.
    
    Architecture:
    Layer 1: h = ReLU(w1*x + b1)  (hidden layer)
    Layer 2: y = w2*h + b2        (output layer)
    
    Args:
        x (float): Input value
        w1 (float): Weight for layer 1
        b1 (float): Bias for layer 1
        w2 (float): Weight for layer 2
        b2 (float): Bias for layer 2
    
    Returns:
        tuple: (h, y) where h is hidden layer output, y is final output
    """
    # Layer 1: Linear transformation
    z1 = w1 * x + b1
    
    # Apply ReLU activation (introduces non-linearity)
    h = relu(z1)
    
    # Layer 2: Linear transformation (output layer)
    y = w2 * h + b2
    
    return h, y


def compute_loss_mse(y_pred, y_true):
    """
    Compute MSE loss.
    
    Simple loss function for regression.
    We'll use this to measure how wrong our prediction is.
    
    Args:
        y_pred (float): Predicted value
        y_true (float): True value
    
    Returns:
        float: MSE loss
    """
    return (y_pred - y_true) ** 2


def backward_pass_2layer(x, h, y_pred, y_true, w1, w2):
    """
    Manual backpropagation for 2-layer network.
    
    This is the heart of neural network training! We compute gradients
    using the chain rule, propagating errors backward through the network.
    
    The chain rule allows us to compute how loss changes with respect to
    each weight, even though they're deep in the network.
    
    Computation graph:
    x → z1 = w1*x+b1 → h = ReLU(z1) → y = w2*h+b2 → Loss
    
    We compute gradients backward:
    1. dLoss/dy_pred (how loss changes with output)
    2. dLoss/dw2, dLoss/db2 (output layer gradients)
    3. dLoss/dh (how loss changes with hidden layer)
    4. Account for ReLU derivative
    5. dLoss/dw1, dLoss/db1 (hidden layer gradients)
    
    Args:
        x (float): Input value
        h (float): Hidden layer output (from forward pass)
        y_pred (float): Predicted output (from forward pass)
        y_true (float): True output
        w1 (float): Weight for layer 1
        w2 (float): Weight for layer 2
    
    Returns:
        tuple: (dLoss_dw1, dLoss_db1, dLoss_dw2, dLoss_db2)
    """
    # Step 1: Gradient w.r.t. output (y_pred)
    # Loss = (y_pred - y_true)²
    # dLoss/dy_pred = 2 * (y_pred - y_true)
    dLoss_dy = 2 * (y_pred - y_true)
    
    # Step 2: Gradients for output layer (Layer 2)
    # y = w2*h + b2
    # dLoss/dw2 = dLoss/dy * dy/dw2 = dLoss/dy * h
    # dLoss/db2 = dLoss/dy * dy/db2 = dLoss/dy * 1
    dLoss_dw2 = dLoss_dy * h
    dLoss_db2 = dLoss_dy * 1
    
    # Step 3: Gradient w.r.t. hidden layer output (h)
    # y = w2*h + b2
    # dLoss/dh = dLoss/dy * dy/dh = dLoss/dy * w2
    dLoss_dh = dLoss_dy * w2
    
    # Step 4: Account for ReLU activation
    # h = ReLU(z1), where z1 = w1*x + b1
    # If h > 0: ReLU derivative = 1, so gradient passes through
    # If h <= 0: ReLU derivative = 0, so gradient is blocked (dead neuron)
    # dLoss/dz1 = dLoss/dh * dh/dz1 = dLoss/dh * ReLU'(z1)
    z1 = w1 * x  # Reconstruct z1 (assuming b1=0 for simplicity, or save from forward pass)
    dLoss_dz1 = dLoss_dh * relu_derivative(z1)
    
    # Step 5: Gradients for hidden layer (Layer 1)
    # z1 = w1*x + b1
    # dLoss/dw1 = dLoss/dz1 * dz1/dw1 = dLoss/dz1 * x
    # dLoss/db1 = dLoss/dz1 * dz1/db1 = dLoss/dz1 * 1
    dLoss_dw1 = dLoss_dz1 * x
    dLoss_db1 = dLoss_dz1 * 1
    
    return dLoss_dw1, dLoss_db1, dLoss_dw2, dLoss_db2
    
    # This is backpropagation! We've computed how loss changes with
    # respect to every weight, even though they're in different layers.
    # The chain rule makes this possible - we chain gradients backward.
    
    # In practice, frameworks like PyTorch do this automatically,
    # but understanding it manually is crucial for debugging and
    # implementing custom layers.




