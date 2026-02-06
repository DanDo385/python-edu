"""
Project 25: Training a Shallow Neural Network (MLP) from Scratch

Complete the class definition below according to its docstring.
Run pytest test.py -v to test your solutions.
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


class SimpleMLP:
    """
    Simple Multi-Layer Perceptron (MLP) with one hidden layer.
    
    Architecture:
    Input → Hidden (ReLU) → Output (Sigmoid)
    
    This can learn non-linear patterns like XOR!
    """
    
    def __init__(self, input_size, hidden_size, output_size):
        """
        Initialize MLP with random weights.
        
        Args:
            input_size (int): Number of input features
            hidden_size (int): Number of hidden neurons
            output_size (int): Number of output neurons
        """
        # TODO: Initialize weights and biases
        # Use small random values: np.random.randn() * 0.01
        # W1: (input_size, hidden_size)
        # b1: (hidden_size,)
        # W2: (hidden_size, output_size)
        # b2: (output_size,)
        self.W1 = None
        self.b1 = None
        self.W2 = None
        self.b2 = None
    
    def forward(self, X):
        """
        Forward pass through the network.
        
        Args:
            X (np.ndarray): Input data, shape (batch_size, input_size)
        
        Returns:
            np.ndarray: Output predictions, shape (batch_size, output_size)
        """
        # TODO: Implement forward pass
        # Layer 1: z1 = X @ W1 + b1, h = ReLU(z1)
        # Layer 2: z2 = h @ W2 + b2, output = sigmoid(z2)
        # Return output
        return None
    
    def backward(self, X, y, output):
        """
        Backward pass: compute gradients.
        
        Args:
            X (np.ndarray): Input data
            y (np.ndarray): True labels
            output (np.ndarray): Network output
        
        Returns:
            tuple: (dW1, db1, dW2, db2) gradients
        """
        # TODO: Implement backward pass
        # Step 1: dLoss/doutput (for binary cross-entropy)
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
    
    def train(self, X, y, learning_rate=0.1, epochs=1000):
        """
        Train the network.
        
        Args:
            X (np.ndarray): Training data
            y (np.ndarray): Training labels
            learning_rate (float): Learning rate
            epochs (int): Number of epochs
        
        Returns:
            list: Loss history
        """
        # TODO: Training loop
        # For each epoch:
        #   1. Forward pass
        #   2. Compute loss (binary cross-entropy)
        #   3. Backward pass
        #   4. Update weights
        loss_history = []
        return loss_history




