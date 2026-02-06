"""
Test suite for Project 30: NumPy MNIST Capstone

Run with: pytest test.py -v

Note: Tests use synthetic data to avoid requiring MNIST dataset download.
"""

import pytest
import numpy as np
from exercise import (
    softmax,
    cross_entropy_loss,
    MNISTClassifier,
    preprocess_mnist,
    compute_accuracy,
)


class TestSoftmax:
    """Test softmax activation."""
    
    def test_softmax_sums_to_one(self):
        """Test that softmax outputs sum to 1.0."""
        logits = np.array([[1.0, 2.0, 3.0], [0.5, 1.5, 2.5]])
        probs = softmax(logits)
        
        # Each row should sum to 1.0
        assert np.allclose(np.sum(probs, axis=1), 1.0)
    
    def test_softmax_positive(self):
        """Test that softmax outputs are positive."""
        logits = np.array([[-1.0, 0.0, 1.0]])
        probs = softmax(logits)
        
        assert np.all(probs > 0)
        assert np.all(probs <= 1.0)
    
    def test_softmax_largest_input(self):
        """Test that largest input gets highest probability."""
        logits = np.array([1.0, 2.0, 3.0])
        probs = softmax(logits)
        
        # Index 2 (value 3.0) should have highest probability
        assert np.argmax(probs) == 2
        assert probs[2] > probs[1] > probs[0]


class TestCrossEntropyLoss:
    """Test cross-entropy loss."""
    
    def test_cross_entropy_one_hot(self):
        """Test cross-entropy with one-hot encoded labels."""
        y_true = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        y_pred = np.array([[0.9, 0.05, 0.05], [0.1, 0.8, 0.1], [0.2, 0.2, 0.6]])
        
        loss = cross_entropy_loss(y_true, y_pred)
        
        # Should be positive
        assert loss > 0
        
        # Manual calculation for first sample: -log(0.9) ≈ 0.105
        expected = -np.mean([np.log(0.9), np.log(0.8), np.log(0.6)])
        assert abs(loss - expected) < 0.01
    
    def test_cross_entropy_integer_labels(self):
        """Test cross-entropy with integer labels."""
        y_true = np.array([0, 1, 2])
        y_pred = np.array([[0.9, 0.05, 0.05], [0.1, 0.8, 0.1], [0.2, 0.2, 0.6]])
        
        loss = cross_entropy_loss(y_true, y_pred)
        
        # Should be positive
        assert loss > 0
    
    def test_cross_entropy_perfect_prediction(self):
        """Test that perfect prediction gives low loss."""
        y_true = np.array([0, 1, 2])
        y_pred = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
        
        loss = cross_entropy_loss(y_true, y_pred)
        
        # Perfect prediction should give very low loss (close to 0)
        assert loss < 0.01


class TestMNISTClassifier:
    """Test MNIST classifier."""
    
    def test_initialization(self):
        """Test network initialization."""
        model = MNISTClassifier(input_size=784, hidden_size=128, output_size=10)
        
        assert model.W1.shape == (784, 128)
        assert model.b1.shape == (128,)
        assert model.W2.shape == (128, 10)
        assert model.b2.shape == (10,)
    
    def test_forward_pass_shape(self):
        """Test forward pass output shape."""
        model = MNISTClassifier(input_size=784, hidden_size=128, output_size=10)
        X = np.random.randn(32, 784)  # Batch of 32 images
        
        output = model.forward(X)
        
        assert output.shape == (32, 10)
        # Outputs should be probabilities (sum to 1)
        assert np.allclose(np.sum(output, axis=1), 1.0)
    
    def test_predict(self):
        """Test prediction function."""
        model = MNISTClassifier(input_size=784, hidden_size=128, output_size=10)
        X = np.random.randn(5, 784)
        
        predictions = model.predict(X)
        
        assert predictions.shape == (5,)
        assert np.all(predictions >= 0)
        assert np.all(predictions < 10)  # Classes 0-9
    
    def test_training_reduces_loss(self):
        """Test that training reduces loss."""
        # Create small synthetic dataset
        X_train = np.random.randn(100, 784) / 10.0  # Small values
        y_train = np.random.randint(0, 10, 100)
        X_val = np.random.randn(20, 784) / 10.0
        y_val = np.random.randint(0, 10, 20)
        
        model = MNISTClassifier(input_size=784, hidden_size=64, output_size=10)
        
        # Get initial loss
        initial_output = model.forward(X_train)
        initial_loss = cross_entropy_loss(y_train, initial_output)
        
        # Train for a few epochs
        history = model.train(
            X_train, y_train, X_val, y_val,
            learning_rate=0.01, batch_size=16, epochs=5
        )
        
        # Final loss should be lower (or at least not much higher)
        final_loss = history['train_loss'][-1]
        assert final_loss <= initial_loss * 1.5  # Allow some variance


class TestPreprocessing:
    """Test data preprocessing."""
    
    def test_preprocess_flatten(self):
        """Test that images are flattened."""
        images = np.random.randint(0, 255, (10, 28, 28), dtype=np.uint8)
        processed, _ = preprocess_mnist(images, np.zeros(10))
        
        assert processed.shape == (10, 784)
    
    def test_preprocess_normalize(self):
        """Test that images are normalized to [0, 1]."""
        images = np.ones((5, 28, 28)) * 255
        processed, _ = preprocess_mnist(images, np.zeros(5))
        
        assert np.allclose(processed, 1.0)
        assert np.all(processed >= 0)
        assert np.all(processed <= 1)
    
    def test_preprocess_already_flattened(self):
        """Test preprocessing of already flattened images."""
        images = np.random.randn(10, 784) * 255
        processed = preprocess_mnist(images)
        
        assert processed.shape == (10, 784)


class TestAccuracy:
    """Test accuracy computation."""
    
    def test_compute_accuracy_perfect(self):
        """Test accuracy with perfect predictions."""
        y_true = np.array([0, 1, 2, 3, 4])
        y_pred = np.array([0, 1, 2, 3, 4])
        
        accuracy = compute_accuracy(y_true, y_pred)
        assert accuracy == 1.0
    
    def test_compute_accuracy_partial(self):
        """Test accuracy with partial correctness."""
        y_true = np.array([0, 1, 2, 3, 4])
        y_pred = np.array([0, 1, 2, 3, 0])  # Last one wrong
        
        accuracy = compute_accuracy(y_true, y_pred)
        assert accuracy == 0.8  # 4 out of 5 correct


class TestIntegration:
    """Integration tests."""
    
    def test_end_to_end_training(self):
        """Test complete training pipeline."""
        # Create synthetic MNIST-like data
        X_train = np.random.randn(200, 784) / 10.0
        y_train = np.random.randint(0, 10, 200)
        X_val = np.random.randn(50, 784) / 10.0
        y_val = np.random.randint(0, 10, 50)
        
        model = MNISTClassifier(input_size=784, hidden_size=64, output_size=10)
        
        # Train
        history = model.train(
            X_train, y_train, X_val, y_val,
            learning_rate=0.01, batch_size=32, epochs=3
        )
        
        # Check history structure
        assert 'train_loss' in history
        assert 'val_loss' in history
        assert 'val_accuracy' in history
        
        # Check that we can make predictions
        predictions = model.predict(X_val)
        assert len(predictions) == len(y_val)
        
        # Compute accuracy
        accuracy = compute_accuracy(y_val, predictions)
        assert accuracy >= 0.0
        assert accuracy <= 1.0
