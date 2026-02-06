"""
Project 30: NumPy Neural Network Capstone – MNIST Digit Classifier

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.

This is the capstone project - build a complete MNIST classifier from scratch!
"""

import numpy as np


def softmax(x):
    """
    Compute softmax activation for multi-class classification.
    
    Softmax converts logits to probabilities that sum to 1.0.
    
    Formula: softmax(x_i) = exp(x_i) / Σ exp(x_j)
    
    Args:
        x (np.ndarray): Logits, shape (batch_size, num_classes) or (num_classes,)
    
    Returns:
        np.ndarray: Probabilities, same shape as x
    
    Note:
        - Subtract max for numerical stability: exp(x - max) / Σ exp(x - max)
        - This prevents overflow while maintaining same result
    """
    # TODO: Implement softmax
    # 1. Subtract max for numerical stability (prevents overflow)
    # 2. Compute exp
    # 3. Normalize by sum
    return None


def cross_entropy_loss(y_true, y_pred):
    """
    Compute cross-entropy loss for multi-class classification.
    
    Cross-entropy measures difference between true and predicted distributions.
    
    Formula: Loss = -Σ y_true * log(y_pred)
    
    For one-hot encoded labels: Loss = -log(y_pred[true_class])
    
    Args:
        y_true (np.ndarray): True labels (one-hot encoded), shape (batch_size, num_classes)
                             OR integer labels, shape (batch_size,)
        y_pred (np.ndarray): Predicted probabilities, shape (batch_size, num_classes)
    
    Returns:
        float: Average cross-entropy loss
    
    Note:
        - Add small epsilon to y_pred to prevent log(0)
        - If y_true is integer labels, convert to one-hot or use advanced indexing
    """
    # TODO: Implement cross-entropy loss
    # Handle both one-hot encoded and integer labels
    # Add epsilon to prevent log(0)
    # Compute -mean(log(predicted_probability_for_true_class))
    return None


def relu(x):
    """ReLU activation function."""
    return np.maximum(0, x)


def relu_derivative(x):
    """Derivative of ReLU."""
    return (x > 0).astype(float)


class MNISTClassifier:
    """
    Neural network for MNIST digit classification.
    
    Architecture:
    Input (784) → Hidden (128, ReLU) → Output (10, Softmax)
    
    This network can classify handwritten digits 0-9!
    """
    
    def __init__(self, input_size=784, hidden_size=128, output_size=10):
        """
        Initialize MNIST classifier.
        
        Args:
            input_size (int): Number of input features (784 for MNIST)
            hidden_size (int): Number of hidden neurons (default 128)
            output_size (int): Number of output classes (10 for digits 0-9)
        """
        # TODO: Initialize weights and biases
        # W1: (input_size, hidden_size)
        # b1: (hidden_size,)
        # W2: (hidden_size, output_size)
        # b2: (output_size,)
        # Use small random values: np.random.randn() * 0.01
        self.W1 = None
        self.b1 = None
        self.W2 = None
        self.b2 = None
    
    def forward(self, X):
        """
        Forward pass through the network.
        
        Args:
            X (np.ndarray): Input images, shape (batch_size, 784)
        
        Returns:
            np.ndarray: Output probabilities, shape (batch_size, 10)
        """
        # TODO: Implement forward pass
        # Layer 1: z1 = X @ W1 + b1, h = ReLU(z1)
        # Layer 2: z2 = h @ W2 + b2, output = softmax(z2)
        # Store intermediate values for backprop
        return None
    
    def backward(self, X, y_true, output):
        """
        Backward pass: compute gradients.
        
        Args:
            X (np.ndarray): Input images
            y_true (np.ndarray): True labels (integer or one-hot)
            output (np.ndarray): Network output (probabilities)
        
        Returns:
            tuple: (dW1, db1, dW2, db2) gradients
        """
        # TODO: Implement backward pass
        # Step 1: Gradient w.r.t. output (cross-entropy + softmax)
        # Step 2: Gradients for output layer (W2, b2)
        # Step 3: Gradient w.r.t. hidden layer
        # Step 4: Account for ReLU derivative
        # Step 5: Gradients for hidden layer (W1, b1)
        dW1 = None
        db1 = None
        dW2 = None
        db2 = None
        return dW1, db1, dW2, db2
    
    def update_weights(self, dW1, db1, dW2, db2, learning_rate):
        """
        Update weights using gradients.
        
        Args:
            dW1, db1, dW2, db2: Gradients
            learning_rate (float): Learning rate
        """
        # TODO: Update weights: W = W - lr * dW
        pass
    
    def predict(self, X):
        """
        Make predictions on input data.
        
        Args:
            X (np.ndarray): Input images, shape (batch_size, 784)
        
        Returns:
            np.ndarray: Predicted class indices, shape (batch_size,)
        """
        # TODO: Forward pass and return class with highest probability
        # Use np.argmax to find class with max probability
        return None
    
    def train(self, X_train, y_train, X_val, y_val, 
              learning_rate=0.01, batch_size=32, epochs=10):
        """
        Train the network.
        
        Args:
            X_train, y_train: Training data
            X_val, y_val: Validation data
            learning_rate (float): Learning rate
            batch_size (int): Batch size
            epochs (int): Number of epochs
        
        Returns:
            dict: Training history with 'train_loss', 'val_loss', 'val_accuracy'
        """
        # TODO: Training loop
        # For each epoch:
        #   - Shuffle data
        #   - Process in batches:
        #     - Forward pass
        #     - Compute loss
        #     - Backward pass
        #     - Update weights
        #   - Evaluate on validation set
        #   - Track metrics
        history = {
            'train_loss': [],
            'val_loss': [],
            'val_accuracy': []
        }
        return history


def preprocess_mnist(images, labels=None):
    """
    Preprocess MNIST data for training.
    
    Args:
        images (np.ndarray): Raw images, shape (n_samples, 28, 28) or (n_samples, 784)
        labels (np.ndarray): Labels, shape (n_samples,) (optional)
    
    Returns:
        tuple: (processed_images, processed_labels) or just processed_images
    """
    # TODO: Preprocess MNIST data
    # 1. Flatten images if needed (28x28 → 784)
    # 2. Normalize to [0, 1] (divide by 255.0)
    # 3. If labels provided, return them (or one-hot encode)
    if labels is not None:
        return None, None
    return None


def compute_accuracy(y_true, y_pred):
    """
    Compute classification accuracy.
    
    Args:
        y_true (np.ndarray): True labels, shape (n_samples,)
        y_pred (np.ndarray): Predicted labels, shape (n_samples,)
    
    Returns:
        float: Accuracy between 0.0 and 1.0
    """
    # TODO: Compute accuracy
    return None
