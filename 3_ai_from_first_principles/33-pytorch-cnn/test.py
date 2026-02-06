"""
Test suite for Project 35: CNNs for CIFAR-10

Run with: pytest test.py -v
"""

import pytest
import torch
import torch.nn as nn
from exercise import (
    SimpleCNN,
    count_cnn_parameters,
    get_cnn_output_shape,
    CNNWithBatchNorm,
)


class TestSimpleCNN:
    """Test SimpleCNN model."""
    
    def test_model_initialization(self):
        """Test model can be instantiated."""
        model = SimpleCNN(num_classes=10)
        assert isinstance(model, nn.Module)
    
    def test_forward_pass_shape(self):
        """Test forward pass produces correct output shape."""
        model = SimpleCNN(num_classes=10)
        x = torch.randn(32, 3, 32, 32)  # Batch of 32 CIFAR-10 images
        
        output = model(x)
        
        assert output.shape == (32, 10)
    
    def test_forward_pass_values(self):
        """Test forward pass produces valid values."""
        model = SimpleCNN(num_classes=10)
        x = torch.randn(1, 3, 32, 32)
        
        output = model(x)
        
        assert torch.isfinite(output).all()
        assert output.dtype == torch.float32
    
    def test_model_has_conv_layers(self):
        """Test that model has convolutional layers."""
        model = SimpleCNN()
        
        has_conv = any(isinstance(m, nn.Conv2d) for m in model.modules())
        assert has_conv
    
    def test_model_has_pooling_layers(self):
        """Test that model has pooling layers."""
        model = SimpleCNN()
        
        has_pool = any(isinstance(m, nn.MaxPool2d) for m in model.modules())
        assert has_pool


class TestHelperFunctions:
    """Test helper functions."""
    
    def test_count_parameters(self):
        """Test parameter counting."""
        model = SimpleCNN()
        
        count = count_cnn_parameters(model)
        
        assert isinstance(count, int)
        assert count > 0
    
    def test_get_output_shape(self):
        """Test getting output shape."""
        model = SimpleCNN(num_classes=10)
        
        output_shape = get_cnn_output_shape(model, (16, 3, 32, 32))
        
        assert output_shape[0] == 16  # Batch size preserved
        assert output_shape[1] == 10  # 10 classes
    
    def test_output_shape_different_batch(self):
        """Test output shape with different batch sizes."""
        model = SimpleCNN()
        
        shape1 = get_cnn_output_shape(model, (8, 3, 32, 32))
        shape2 = get_cnn_output_shape(model, (64, 3, 32, 32))
        
        assert shape1[0] == 8
        assert shape2[0] == 64
        assert shape1[1] == shape2[1] == 10


class TestCNNWithBatchNorm:
    """Test CNN with batch normalization."""
    
    def test_model_initialization(self):
        """Test model can be instantiated."""
        model = CNNWithBatchNorm(num_classes=10)
        assert isinstance(model, nn.Module)
    
    def test_forward_pass(self):
        """Test forward pass works."""
        model = CNNWithBatchNorm(num_classes=10)
        x = torch.randn(16, 3, 32, 32)
        
        output = model(x)
        
        assert output.shape == (16, 10)
    
    def test_has_batch_norm(self):
        """Test that model has batch normalization."""
        model = CNNWithBatchNorm()
        
        has_bn = any(isinstance(m, (nn.BatchNorm2d, nn.BatchNorm1d)) for m in model.modules())
        assert has_bn


class TestCNNArchitecture:
    """Test CNN architecture details."""
    
    def test_conv_layer_channels(self):
        """Test convolutional layer channel configuration."""
        model = SimpleCNN()
        
        # Find conv layers
        conv_layers = [m for m in model.modules() if isinstance(m, nn.Conv2d)]
        
        # First conv should have 3 input channels (RGB)
        assert conv_layers[0].in_channels == 3
        
        # Should have at least 2 conv layers
        assert len(conv_layers) >= 2
    
    def test_output_classes(self):
        """Test output has correct number of classes."""
        model = SimpleCNN(num_classes=10)
        x = torch.randn(1, 3, 32, 32)
        
        output = model(x)
        
        assert output.shape[1] == 10  # 10 classes for CIFAR-10
