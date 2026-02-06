"""
Project 20: Linear Regression from Scratch

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""

import numpy as np


def predict(x, w, b):
    """
    Make predictions using linear model: y = w*x + b
    
    This is the forward pass - computing outputs from inputs.
    
    Args:
        x (np.ndarray): Input features, shape (n,)
        w (float): Weight (slope)
        b (float): Bias (y-intercept)
    
    Returns:
        np.ndarray: Predictions, shape (n,)
    """
    # TODO: Compute predictions: y = w*x + b
    return None


def compute_loss(y_pred, y_true):
    """
    Compute Mean Squared Error (MSE) loss.
    
    MSE = (1/n) * sum((y_pred - y_true)²)
    
    Args:
        y_pred (np.ndarray): Predicted values, shape (n,)
        y_true (np.ndarray): True values, shape (n,)
    
    Returns:
        float: MSE loss value
    """
    # TODO: Compute MSE loss
    # Hint: Use np.mean() and squared differences
    return None


def compute_gradients(x, y_pred, y_true):
    """
    Compute gradients of MSE loss with respect to w and b.
    
    Gradients:
    dMSE/dw = (2/n) * sum(x * (y_pred - y_true))
    dMSE/db = (2/n) * sum(y_pred - y_true)
    
    Args:
        x (np.ndarray): Input features, shape (n,)
        y_pred (np.ndarray): Predicted values, shape (n,)
        y_true (np.ndarray): True values, shape (n,)
    
    Returns:
        tuple: (grad_w, grad_b) gradients
    """
    # TODO: Compute gradients
    # Hint: Use vectorized operations, np.mean() or np.sum()
    grad_w = None
    grad_b = None
    return grad_w, grad_b


def train_linear_regression(x, y, learning_rate=0.01, epochs=1000):
    """
    Train linear regression model using gradient descent.
    
    Training process:
    1. Initialize w and b randomly
    2. For each epoch:
       a. Make predictions
       b. Compute loss
       c. Compute gradients
       d. Update w and b
    3. Return trained parameters
    
    Args:
        x (np.ndarray): Input features, shape (n,)
        y (np.ndarray): Target values, shape (n,)
        learning_rate (float): Step size for gradient descent
        epochs (int): Number of training iterations
    
    Returns:
        tuple: (w, b, loss_history)
               w: Learned weight
               b: Learned bias
               loss_history: List of loss values during training
    """
    # TODO: Initialize w and b (use small random values, e.g., np.random.randn() * 0.01)
    w = None
    b = None
    
    loss_history = []
    
    # TODO: Training loop
    # For each epoch:
    #   1. Make predictions
    #   2. Compute loss, append to loss_history
    #   3. Compute gradients
    #   4. Update w and b
    #   5. (Optional) Print progress every 100 epochs
    
    return w, b, loss_history


def evaluate_model(x, y, w, b):
    """
    Evaluate model performance.
    
    Computes:
    - Predictions
    - MSE loss
    - R² score (coefficient of determination)
    
    Args:
        x (np.ndarray): Input features
        y (np.ndarray): True target values
        w (float): Model weight
        b (float): Model bias
    
    Returns:
        dict: Dictionary with 'mse', 'r2', and 'predictions'
    """
    # TODO: Make predictions
    y_pred = None
    
    # TODO: Compute MSE
    mse = None
    
    # TODO: Compute R² score
    # R² = 1 - (sum((y_true - y_pred)²) / sum((y_true - mean(y_true))²))
    r2 = None
    
    return {'mse': mse, 'r2': r2, 'predictions': y_pred}




