"""
Project 30: NumPy MNIST Capstone - SOLUTION

Complete solution for MNIST digit classification from scratch.
"""

import numpy as np


def softmax(x):
    """
    Compute softmax activation for multi-class classification.
    
    Subtracting max for numerical stability.
    """
    # Subtract max for numerical stability (prevents overflow)
    x_shifted = x - np.max(x, axis=-1, keepdims=True)
    
    # Compute exp
    exp_x = np.exp(x_shifted)
    
    # Normalize by sum
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)


def cross_entropy_loss(y_true, y_pred):
    """
    Compute cross-entropy loss for multi-class classification.
    """
    # Add small epsilon to prevent log(0)
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    
    # Handle integer labels (convert to one-hot indexing)
    if y_true.ndim == 1:
        # Integer labels: use advanced indexing
        batch_size = len(y_true)
        loss = -np.mean(np.log(y_pred[np.arange(batch_size), y_true]))
    else:
        # One-hot encoded labels
        loss = -np.mean(np.sum(y_true * np.log(y_pred), axis=1))
    
    return loss


def relu(x):
    """ReLU activation function."""
    return np.maximum(0, x)


def relu_derivative(x):
    """Derivative of ReLU."""
    return (x > 0).astype(float)


class MNISTClassifier:
    """
    Neural network for MNIST digit classification.
    
    Architecture: Input (784) → Hidden (128, ReLU) → Output (10, Softmax)
    """
    
    def __init__(self, input_size=784, hidden_size=128, output_size=10):
        """Initialize MNIST classifier."""
        np.random.seed(42)
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros(hidden_size)
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros(output_size)
    
    def forward(self, X):
        """Forward pass through the network."""
        # Layer 1: Hidden layer
        self.z1 = X @ self.W1 + self.b1
        self.h = relu(self.z1)
        
        # Layer 2: Output layer
        self.z2 = self.h @ self.W2 + self.b2
        self.output = softmax(self.z2)
        
        return self.output
    
    def backward(self, X, y_true, output):
        """Backward pass: compute gradients."""
        batch_size = len(X)
        
        # Convert integer labels to one-hot if needed
        if y_true.ndim == 1:
            y_one_hot = np.zeros((batch_size, 10))
            y_one_hot[np.arange(batch_size), y_true] = 1
            y_true = y_one_hot
        
        # Gradient w.r.t. output (cross-entropy + softmax)
        # dL/dz2 = output - y_true (for softmax + cross-entropy)
        dz2 = output - y_true
        dz2 /= batch_size  # Average over batch
        
        # Gradients for output layer
        dW2 = self.h.T @ dz2
        db2 = np.sum(dz2, axis=0)
        
        # Gradient w.r.t. hidden layer
        dh = dz2 @ self.W2.T
        
        # Account for ReLU derivative
        dz1 = dh * relu_derivative(self.z1)
        
        # Gradients for hidden layer
        dW1 = X.T @ dz1
        db1 = np.sum(dz1, axis=0)
        
        return dW1, db1, dW2, db2
    
    def update_weights(self, dW1, db1, dW2, db2, learning_rate):
        """Update weights using gradients."""
        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1
        self.W2 -= learning_rate * dW2
        self.b2 -= learning_rate * db2
    
    def predict(self, X):
        """Make predictions on input data."""
        output = self.forward(X)
        return np.argmax(output, axis=1)
    
    def train(self, X_train, y_train, X_val, y_val, 
              learning_rate=0.01, batch_size=32, epochs=10):
        """Train the network."""
        history = {
            'train_loss': [],
            'val_loss': [],
            'val_accuracy': []
        }
        
        n_train = len(X_train)
        
        for epoch in range(epochs):
            # Shuffle data
            indices = np.random.permutation(n_train)
            X_train_shuffled = X_train[indices]
            y_train_shuffled = y_train[indices]
            
            epoch_losses = []
            
            # Process in batches
            for i in range(0, n_train, batch_size):
                batch_X = X_train_shuffled[i:i+batch_size]
                batch_y = y_train_shuffled[i:i+batch_size]
                
                # Forward pass
                output = self.forward(batch_X)
                
                # Compute loss
                loss = cross_entropy_loss(batch_y, output)
                epoch_losses.append(loss)
                
                # Backward pass
                dW1, db1, dW2, db2 = self.backward(batch_X, batch_y, output)
                
                # Update weights
                self.update_weights(dW1, db1, dW2, db2, learning_rate)
            
            # Average loss for epoch
            avg_loss = np.mean(epoch_losses)
            history['train_loss'].append(avg_loss)
            
            # Evaluate on validation set
            val_output = self.forward(X_val)
            val_loss = cross_entropy_loss(y_val, val_output)
            val_pred = self.predict(X_val)
            val_acc = compute_accuracy(y_val, val_pred)
            
            history['val_loss'].append(val_loss)
            history['val_accuracy'].append(val_acc)
            
            if (epoch + 1) % 5 == 0:
                print(f"Epoch {epoch+1}/{epochs} - Train Loss: {avg_loss:.4f}, "
                      f"Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}")
        
        return history


def preprocess_mnist(images, labels=None):
    """
    Preprocess MNIST data for training.
    """
    # Flatten if needed
    if images.ndim == 3:
        images = images.reshape(images.shape[0], -1)
    
    # Normalize to [0, 1]
    images = images.astype(np.float32) / 255.0
    
    if labels is not None:
        return images, labels
    return images


def compute_accuracy(y_true, y_pred):
    """Compute classification accuracy."""
    return np.mean(y_true == y_pred)


# Example usage
if __name__ == "__main__":
    print("MNIST Classifier from Scratch!")
    print("=" * 50)
    
    # Create synthetic MNIST-like data for demonstration
    np.random.seed(42)
    X_train = np.random.randn(1000, 784) / 10.0
    y_train = np.random.randint(0, 10, 1000)
    X_test = np.random.randn(200, 784) / 10.0
    y_test = np.random.randint(0, 10, 200)
    
    # Preprocess
    X_train = preprocess_mnist(X_train)
    X_test = preprocess_mnist(X_test)
    
    # Create and train model
    model = MNISTClassifier(input_size=784, hidden_size=128, output_size=10)
    
    print("\nTraining model...")
    history = model.train(
        X_train, y_train, X_test, y_test,
        learning_rate=0.01, batch_size=32, epochs=10
    )
    
    # Final evaluation
    test_pred = model.predict(X_test)
    test_acc = compute_accuracy(y_test, test_pred)
    
    print(f"\nFinal Test Accuracy: {test_acc:.4f}")
    print("\nThis demonstrates a complete neural network from scratch!")
    print("Next: PyTorch will make this much easier! 🚀")
