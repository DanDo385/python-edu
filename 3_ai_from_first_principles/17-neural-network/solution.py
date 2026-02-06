"""
Project 25: Training a Shallow Neural Network (MLP) from Scratch - SOLUTION

Complete solution with detailed comments explaining the full neural network
training pipeline from first principles.
"""

import numpy as np


def sigmoid(x):
    """Sigmoid activation function."""
    # Clip to prevent overflow
    return 1 / (1 + np.exp(-np.clip(x, -250, 250)))


def relu(x):
    """ReLU activation function."""
    return np.maximum(0, x)


def relu_derivative(x):
    """Derivative of ReLU."""
    return (x > 0).astype(float)


class SimpleMLP:
    """
    Simple Multi-Layer Perceptron (MLP) with one hidden layer.
    
    This is a complete neural network implementation from scratch!
    It demonstrates all core concepts:
    - Forward pass (computing predictions)
    - Loss computation (measuring error)
    - Backward pass (computing gradients)
    - Weight updates (learning)
    
    Architecture:
    Input (2 features) → Hidden Layer (4 neurons, ReLU) → Output (1 neuron, Sigmoid)
    
    This network can learn non-linear patterns, demonstrated by solving XOR.
    """
    
    def __init__(self, input_size, hidden_size, output_size):
        """
        Initialize MLP with random weights.
        
        Weight initialization is crucial:
        - Too large: Gradients explode, training unstable
        - Too small: Gradients vanish, training slow
        - Just right: Enables effective learning
        
        We use small random values from normal distribution.
        
        Args:
            input_size (int): Number of input features
            hidden_size (int): Number of hidden neurons
            output_size (int): Number of output neurons
        """
        # Initialize weights with small random values
        # np.random.randn() samples from standard normal distribution
        # Multiply by 0.01 to make values small
        
        # Weights for hidden layer: (input_size, hidden_size)
        # Each column represents weights for one hidden neuron
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        # Bias for hidden layer: (hidden_size,)
        self.b1 = np.zeros(hidden_size)
        
        # Weights for output layer: (hidden_size, output_size)
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        # Bias for output layer: (output_size,)
        self.b2 = np.zeros(output_size)
    
    def forward(self, X):
        """
        Forward pass through the network.
        
        This computes predictions given inputs.
        Each layer transforms the data:
        - Layer 1: Linear transformation + ReLU (non-linearity)
        - Layer 2: Linear transformation + Sigmoid (probability)
        
        Args:
            X (np.ndarray): Input data, shape (batch_size, input_size)
        
        Returns:
            np.ndarray: Output predictions, shape (batch_size, output_size)
        """
        # Layer 1: Hidden layer
        # Linear transformation: z1 = X @ W1 + b1
        # Matrix multiplication: (batch, input) @ (input, hidden) = (batch, hidden)
        # Broadcasting adds bias to each sample
        self.z1 = X @ self.W1 + self.b1
        
        # Apply ReLU activation (introduces non-linearity)
        # Without this, multiple layers would collapse to one linear layer!
        self.h = relu(self.z1)
        
        # Layer 2: Output layer
        # Linear transformation: z2 = h @ W2 + b2
        # (batch, hidden) @ (hidden, output) = (batch, output)
        self.z2 = self.h @ self.W2 + self.b2
        
        # Apply sigmoid to get probabilities (for binary classification)
        # Output range: (0, 1) - probability of class 1
        output = sigmoid(self.z2)
        
        return output
    
    def backward(self, X, y, output):
        """
        Backward pass: compute gradients using backpropagation.
        
        This is where the magic happens! We compute how loss changes
        with respect to each weight, enabling gradient descent.
        
        We use the chain rule to propagate gradients backward:
        1. Compute gradient w.r.t. output
        2. Propagate through sigmoid
        3. Compute gradients for W2, b2
        4. Propagate through ReLU
        5. Compute gradients for W1, b1
        
        Args:
            X (np.ndarray): Input data
            y (np.ndarray): True labels
            output (np.ndarray): Network output (predictions)
        
        Returns:
            tuple: (dW1, db1, dW2, db2) gradients for all parameters
        """
        batch_size = X.shape[0]
        
        # Step 1: Gradient w.r.t. output (for binary cross-entropy loss)
        # Loss = -mean(y*log(output) + (1-y)*log(1-output))
        # dLoss/doutput = -(y/output - (1-y)/(1-output)) / batch_size
        # Simplified: (output - y) / batch_size
        dLoss_doutput = (output - y) / batch_size
        
        # Step 2: Gradient w.r.t. z2 (before sigmoid)
        # output = sigmoid(z2)
        # doutput/dz2 = sigmoid(z2) * (1 - sigmoid(z2)) = output * (1 - output)
        # dLoss/dz2 = dLoss/doutput * doutput/dz2
        dLoss_dz2 = dLoss_doutput * output * (1 - output)
        
        # Step 3: Gradients for output layer weights and bias
        # z2 = h @ W2 + b2
        # dLoss/dW2 = dLoss/dz2 * dz2/dW2 = dLoss/dz2 @ h^T
        # dLoss/db2 = dLoss/dz2 * dz2/db2 = sum(dLoss/dz2)
        dW2 = self.h.T @ dLoss_dz2  # (hidden, batch) @ (batch, output) = (hidden, output)
        db2 = np.sum(dLoss_dz2, axis=0)  # Sum over batch dimension
        
        # Step 4: Gradient w.r.t. hidden layer output (h)
        # z2 = h @ W2 + b2
        # dLoss/dh = dLoss/dz2 * dz2/dh = dLoss_dz2 @ W2^T
        dLoss_dh = dLoss_dz2 @ self.W2.T  # (batch, output) @ (output, hidden) = (batch, hidden)
        
        # Step 5: Gradient w.r.t. z1 (before ReLU)
        # h = ReLU(z1)
        # dLoss/dz1 = dLoss/dh * dh/dz1 = dLoss/dh * ReLU'(z1)
        # ReLU derivative: 1 if z1 > 0, else 0
        dLoss_dz1 = dLoss_dh * relu_derivative(self.z1)
        
        # Step 6: Gradients for hidden layer weights and bias
        # z1 = X @ W1 + b1
        # dLoss/dW1 = dLoss/dz1 * dz1/dW1 = X^T @ dLoss/dz1
        # dLoss/db1 = dLoss/dz1 * dz1/db1 = sum(dLoss/dz1)
        dW1 = X.T @ dLoss_dz1  # (input, batch) @ (batch, hidden) = (input, hidden)
        db1 = np.sum(dLoss_dz1, axis=0)  # Sum over batch dimension
        
        return dW1, db1, dW2, db2
    
    def update_weights(self, dW1, db1, dW2, db2, learning_rate):
        """
        Update weights using gradients (gradient descent step).
        
        This is the final step: use gradients to improve the model.
        We move weights in the direction that reduces loss.
        
        Args:
            dW1, db1, dW2, db2: Gradients computed during backward pass
            learning_rate (float): Step size for gradient descent
        """
        # Update weights: move opposite to gradient (toward minimum)
        # W = W - learning_rate * dLoss/dW
        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1
        self.W2 -= learning_rate * dW2
        self.b2 -= learning_rate * db2
    
    def train(self, X, y, learning_rate=0.1, epochs=1000):
        """
        Train the network using gradient descent.
        
        This is the complete training loop that brings everything together:
        1. Forward pass: Make predictions
        2. Compute loss: Measure error
        3. Backward pass: Compute gradients
        4. Update weights: Improve model
        5. Repeat until converged
        
        Args:
            X (np.ndarray): Training data, shape (batch_size, input_size)
            y (np.ndarray): Training labels, shape (batch_size, output_size)
            learning_rate (float): Learning rate (step size)
            epochs (int): Number of training iterations
        
        Returns:
            list: Loss history (for monitoring training)
        """
        loss_history = []
        
        for epoch in range(epochs):
            # Forward pass: Compute predictions
            output = self.forward(X)
            
            # Compute loss: Binary cross-entropy
            # Loss = -mean(y*log(output) + (1-y)*log(1-output))
            # Clip output to avoid log(0)
            epsilon = 1e-15
            output_clipped = np.clip(output, epsilon, 1 - epsilon)
            loss = -np.mean(y * np.log(output_clipped) + (1 - y) * np.log(1 - output_clipped))
            loss_history.append(loss)
            
            # Backward pass: Compute gradients
            dW1, db1, dW2, db2 = self.backward(X, y, output)
            
            # Update weights: Gradient descent step
            self.update_weights(dW1, db1, dW2, db2, learning_rate)
            
            # Optional: Print progress
            # if epoch % 100 == 0:
            #     print(f"Epoch {epoch}, Loss: {loss:.4f}")
        
        return loss_history
    
    # This is a complete neural network!
    # It can learn non-linear patterns, demonstrated by solving XOR.
    # The same principles apply to much larger networks - just more layers and neurons.




