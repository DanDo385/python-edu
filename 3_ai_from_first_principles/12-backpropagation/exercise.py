"""
Project 23: Manual Backpropagation in Neural Networks

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""

import numpy as np


def forward_pass_2layer(x, w1, b1, w2, b2):
    """
    Forward pass through 2-layer network.
    
    Layer 1: h = ReLU(w1*x + b1)
    Layer 2: y = w2*h + b2
    
    Args:
        x (float): Input value
        w1 (float): Weight for layer 1
        b1 (float): Bias for layer 1
        w2 (float): Weight for layer 2
        b2 (float): Bias for layer 2
    
    Returns:
        tuple: (h, y) where h is hidden layer output, y is final output
    """
    # TODO: Implement forward pass
    # Compute layer 1: linear + ReLU
    # Compute layer 2: linear
    h = None
    y = None
    return h, y


def compute_loss_mse(y_pred, y_true):
    """
    Compute MSE loss.
    
    Args:
        y_pred (float): Predicted value
        y_true (float): True value
    
    Returns:
        float: MSE loss
    """
    # TODO: Compute MSE: (y_pred - y_true)²
    return None


def backward_pass_2layer(x, h, y_pred, y_true, w1, w2):
    """
    Manual backpropagation for 2-layer network.
    
    Compute gradients using chain rule:
    dLoss/dw2, dLoss/db2, dLoss/dw1, dLoss/db1
    
    Args:
        x (float): Input value
        h (float): Hidden layer output
        y_pred (float): Predicted output
        y_true (float): True output
        w1 (float): Weight for layer 1
        w2 (float): Weight for layer 2
    
    Returns:
        tuple: (dLoss_dw1, dLoss_db1, dLoss_dw2, dLoss_db2)
    """
    # TODO: Implement backward pass
    # Step 1: dLoss/dy_pred (gradient w.r.t. output)
    # Step 2: dLoss/dw2 = dLoss/dy_pred * dy_pred/dw2
    # Step 3: dLoss/db2 = dLoss/dy_pred * dy_pred/db2
    # Step 4: dLoss/dh = dLoss/dy_pred * dy_pred/dh
    # Step 5: Account for ReLU derivative: if h <= 0, gradient = 0
    # Step 6: dLoss/dw1 = dLoss/dh * dh/dw1
    # Step 7: dLoss/db1 = dLoss/dh * dh/db1
    dLoss_dw1 = None
    dLoss_db1 = None
    dLoss_dw2 = None
    dLoss_db2 = None
    return dLoss_dw1, dLoss_db1, dLoss_dw2, dLoss_db2




