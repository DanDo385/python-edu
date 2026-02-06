"""
Project 20: Linear Regression from Scratch - SOLUTION

Complete solution with detailed comments explaining how linear regression
works and how it demonstrates all core ML concepts.
"""

import numpy as np


def predict(x, w, b):
    """
    Make predictions using linear model: y = w*x + b
    
    This is the forward pass - the model making predictions.
    In neural networks, this is called the "forward pass" through the network.
    
    The model is simple: a linear function (straight line).
    - w controls the slope (how steep the line is)
    - b controls the y-intercept (where line crosses y-axis)
    
    This function takes inputs and produces outputs - this is what
    any ML model does, just with different complexity.
    
    Args:
        x (np.ndarray): Input features, shape (n,)
        w (float): Weight (slope of the line)
        b (float): Bias (y-intercept)
    
    Returns:
        np.ndarray: Predictions, shape (n,)
    
    Example:
        x = [1, 2, 3]
        w = 2.0, b = 1.0
        predict(x, w, b)  # Returns [3, 5, 7] (2*x + 1)
    """
    # Linear model: y = w*x + b
    # This is vectorized - works on entire array at once
    # NumPy automatically broadcasts w (scalar) to multiply each element of x
    # Then adds b (scalar) to each result
    y_pred = w * x + b
    
    return y_pred
    
    # This is exactly what a neural network layer does, just simpler:
    # Neural network: output = input @ weights + bias
    # Linear regression: output = input * weight + bias
    # Same concept, different dimensionality!


def compute_loss(y_pred, y_true):
    """
    Compute Mean Squared Error (MSE) loss.
    
    Loss function measures how wrong our predictions are.
    MSE is the most common loss for regression problems.
    
    Formula: MSE = (1/n) * sum((y_pred - y_true)²)
    
    Why squared?
    - Penalizes large errors more than small errors
    - Always positive (easier to work with)
    - Smooth function (good for gradient descent)
    
    In ML context:
    - Lower loss = better model
    - We minimize loss during training
    - Loss guides gradient descent (tells us how to improve)
    
    Args:
        y_pred (np.ndarray): Predicted values, shape (n,)
        y_true (np.ndarray): True values, shape (n,)
    
    Returns:
        float: MSE loss value
    
    Example:
        y_pred = [1, 2, 3]
        y_true = [1, 3, 3]
        compute_loss(y_pred, y_true)  # MSE = mean((0, -1, 0)²) = 1/3
    """
    # Compute squared differences: (y_pred - y_true)²
    # This is vectorized - computes for all elements at once
    squared_errors = (y_pred - y_true) ** 2
    
    # Take mean to get average squared error
    # This gives us a single number representing overall error
    mse = np.mean(squared_errors)
    
    return mse
    
    # Alternative: np.mean((y_pred - y_true)**2) in one line
    # But breaking it down helps understand the steps


def compute_gradients(x, y_pred, y_true):
    """
    Compute gradients of MSE loss with respect to w and b.
    
    Gradients tell us how to adjust w and b to reduce loss.
    This is the key to learning - gradients guide parameter updates.
    
    Mathematical derivation:
    Loss = (1/n) * sum((y_pred - y_true)²)
    where y_pred = w*x + b
    
    Gradient w.r.t. w:
    dLoss/dw = d/dw [(1/n) * sum((w*x + b - y_true)²)]
            = (1/n) * sum(2 * (w*x + b - y_true) * x)
            = (2/n) * sum(x * (y_pred - y_true))
    
    Gradient w.r.t. b:
    dLoss/db = (2/n) * sum(y_pred - y_true)
    
    These gradients tell us:
    - If gradient is positive: increasing parameter increases loss (decrease it!)
    - If gradient is negative: increasing parameter decreases loss (increase it!)
    
    Args:
        x (np.ndarray): Input features, shape (n,)
        y_pred (np.ndarray): Predicted values, shape (n,)
        y_true (np.ndarray): True values, shape (n,)
    
    Returns:
        tuple: (grad_w, grad_b) gradients
    
    Example:
        x = [1, 2, 3]
        y_pred = [2, 4, 6]
        y_true = [1, 3, 5]
        grad_w, grad_b = compute_gradients(x, y_pred, y_true)
        # Gradients tell us how to adjust w and b
    """
    # Compute errors: difference between predictions and true values
    errors = y_pred - y_true
    
    # Gradient w.r.t. w: (2/n) * sum(x * errors)
    # Multiply x by errors element-wise, then sum
    # This measures how much each x contributes to the error
    grad_w = (2.0 / len(x)) * np.sum(x * errors)
    
    # Gradient w.r.t. b: (2/n) * sum(errors)
    # Sum of errors (no x multiplication)
    # This measures overall bias in predictions
    grad_b = (2.0 / len(x)) * np.sum(errors)
    
    return grad_w, grad_b
    
    # These gradients are used in gradient descent:
    # w = w - learning_rate * grad_w
    # b = b - learning_rate * grad_b
    # This moves parameters in direction that reduces loss


def train_linear_regression(x, y, learning_rate=0.01, epochs=1000):
    """
    Train linear regression model using gradient descent.
    
    This is the complete training loop - the heart of machine learning!
    It brings together:
    - Model (predict function)
    - Loss (compute_loss function)
    - Gradients (compute_gradients function)
    - Optimization (gradient descent updates)
    
    Training process:
    1. Initialize parameters randomly (or to zeros)
    2. For each epoch (iteration):
       a. Forward pass: Make predictions
       b. Compute loss: Measure error
       c. Backward pass: Compute gradients
       d. Update parameters: Move toward minimum
    3. Return trained parameters
    
    This exact pattern is used in all neural network training!
    
    Args:
        x (np.ndarray): Input features, shape (n,)
        y (np.ndarray): Target values, shape (n,)
        learning_rate (float): Step size for gradient descent
                              Controls how big steps we take
                              Too small: slow convergence
                              Too large: may overshoot or diverge
        epochs (int): Number of training iterations
                     More epochs = more training (but may overfit)
    
    Returns:
        tuple: (w, b, loss_history)
               w: Learned weight
               b: Learned bias
               loss_history: List of loss values (for plotting/analysis)
    
    Example:
        x = [1, 2, 3, 4, 5]
        y = [3, 5, 7, 9, 11]  # y = 2*x + 1
        w, b, history = train_linear_regression(x, y)
        # Should learn w ≈ 2.0, b ≈ 1.0
    """
    # Initialize parameters
    # Small random values help break symmetry
    # In practice, initialization matters a lot for neural networks
    np.random.seed(42)  # For reproducibility
    w = np.random.randn() * 0.01  # Small random weight
    b = np.random.randn() * 0.01  # Small random bias
    
    # Track loss history to monitor training
    # This helps us see if model is learning (loss decreasing)
    loss_history = []
    
    # Training loop: iterate for specified number of epochs
    for epoch in range(epochs):
        # Forward pass: Make predictions using current parameters
        # This is what the model "thinks" the outputs should be
        y_pred = predict(x, w, b)
        
        # Compute loss: How wrong are our predictions?
        # Lower loss = better model
        loss = compute_loss(y_pred, y)
        loss_history.append(loss)
        
        # Backward pass: Compute gradients
        # Gradients tell us how to adjust w and b to reduce loss
        grad_w, grad_b = compute_gradients(x, y_pred, y)
        
        # Update parameters: Move in direction that reduces loss
        # This is gradient descent - the core optimization algorithm
        w = w - learning_rate * grad_w
        b = b - learning_rate * grad_b
        
        # Optional: Print progress (useful for debugging)
        # if epoch % 100 == 0:
        #     print(f"Epoch {epoch}, Loss: {loss:.4f}, w: {w:.4f}, b: {b:.4f}")
    
    return w, b, loss_history
    
    # This training loop is exactly what happens in neural networks:
    # 1. Forward pass through network
    # 2. Compute loss
    # 3. Backward pass (backpropagation) to compute gradients
    # 4. Update weights using gradients
    # The only difference is complexity - neural networks have more layers!


def evaluate_model(x, y, w, b):
    """
    Evaluate model performance.
    
    After training, we need to assess how good our model is.
    We use multiple metrics:
    - MSE: Average squared error (what we optimized)
    - R²: Coefficient of determination (how much variance we explain)
    
    R² score interpretation:
    - R² = 1.0: Perfect predictions (model explains all variance)
    - R² = 0.0: Model is as good as predicting the mean
    - R² < 0.0: Model is worse than predicting the mean
    
    Args:
        x (np.ndarray): Input features
        y (np.ndarray): True target values
        w (float): Model weight
        b (float): Model bias
    
    Returns:
        dict: Dictionary with evaluation metrics
              'mse': Mean Squared Error
              'r2': R² score
              'predictions': Predicted values
    """
    # Make predictions using trained model
    y_pred = predict(x, w, b)
    
    # Compute MSE (same as loss function)
    mse = compute_loss(y_pred, y)
    
    # Compute R² score (coefficient of determination)
    # R² = 1 - (SS_res / SS_tot)
    # SS_res = sum of squared residuals (errors)
    # SS_tot = total sum of squares (variance of y)
    
    # Sum of squared residuals: sum((y_true - y_pred)²)
    ss_res = np.sum((y - y_pred) ** 2)
    
    # Total sum of squares: sum((y_true - mean(y_true))²)
    # This is the variance of y
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    
    # R² score
    # If ss_tot is 0 (all y values are the same), R² is undefined
    if ss_tot == 0:
        r2 = 0.0
    else:
        r2 = 1.0 - (ss_res / ss_tot)
    
    return {
        'mse': mse,
        'r2': r2,
        'predictions': y_pred
    }
    
    # These metrics help us understand model performance:
    # - MSE: Lower is better (what we optimized)
    # - R²: Higher is better (closer to 1.0 is better)
    # - Predictions: Can plot to visualize fit




