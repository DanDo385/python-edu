"""Test suite for Project 25: Neural Network"""
import pytest
import numpy as np
from exercise import SimpleMLP


def test_mlp_initialization():
    mlp = SimpleMLP(input_size=2, hidden_size=4, output_size=1)
    assert mlp.W1.shape == (2, 4)
    assert mlp.b1.shape == (4,)
    assert mlp.W2.shape == (4, 1)
    assert mlp.b2.shape == (1,)


def test_forward_pass():
    mlp = SimpleMLP(input_size=2, hidden_size=4, output_size=1)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    output = mlp.forward(X)
    assert output.shape == (4, 1)


def test_xor_problem():
    # XOR problem: not linearly separable
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])  # XOR
    
    mlp = SimpleMLP(input_size=2, hidden_size=4, output_size=1)
    loss_history = mlp.train(X, y, learning_rate=0.5, epochs=2000)
    
    # Check that loss decreased
    assert loss_history[-1] < loss_history[0]
    
    # Check that network learned (predictions should be close to targets)
    predictions = mlp.forward(X)
    predictions_binary = (predictions > 0.5).astype(int)
    accuracy = np.mean(predictions_binary == y)
    assert accuracy >= 0.75  # Should learn XOR pattern




