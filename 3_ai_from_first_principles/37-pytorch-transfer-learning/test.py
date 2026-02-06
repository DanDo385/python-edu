"""
Test suite for Project 37: Transfer Learning

Run with: pytest test.py -v
"""

import pytest
import torch
import torch.nn as nn
from torchvision import models
from exercise import (
    load_pretrained_resnet,
    freeze_pretrained_layers,
    fine_tune_resnet,
    ResidualBlock,
    SimpleResNet,
    get_pretrained_features,
)


class TestPretrainedModels:
    """Test loading pretrained models."""
    
    def test_load_pretrained_resnet(self):
        """Test loading and modifying pretrained ResNet."""
        model = load_pretrained_resnet(num_classes=10)
        
        assert isinstance(model, nn.Module)
        assert model.fc.out_features == 10
    
    def test_resnet_forward(self):
        """Test pretrained ResNet forward pass."""
        model = load_pretrained_resnet(num_classes=5)
        x = torch.randn(4, 3, 224, 224)
        
        output = model(x)
        
        assert output.shape == (4, 5)
    
    def test_freeze_layers(self):
        """Test freezing pretrained layers."""
        model = load_pretrained_resnet(num_classes=10)
        
        # Freeze
        model = freeze_pretrained_layers(model, freeze=True)
        frozen_params = sum(1 for p in model.parameters() if not p.requires_grad)
        
        assert frozen_params > 0
    
    def test_unfreeze_layers(self):
        """Test unfreezing layers."""
        model = load_pretrained_resnet(num_classes=10)
        model = freeze_pretrained_layers(model, freeze=True)
        model = freeze_pretrained_layers(model, freeze=False)
        
        trainable_params = sum(1 for p in model.parameters() if p.requires_grad)
        assert trainable_params > 0


class TestFineTuning:
    """Test fine-tuning."""
    
    def test_fine_tune_resnet(self):
        """Test fine-tuning ResNet."""
        model = load_pretrained_resnet(num_classes=10)
        model = fine_tune_resnet(model, freeze_early_layers=True)
        
        # Early layers should be frozen
        layer1_frozen = all(not p.requires_grad for p in model.layer1.parameters())
        # Later layers should be trainable
        fc_trainable = any(p.requires_grad for p in model.fc.parameters())
        
        assert layer1_frozen
        assert fc_trainable


class TestResidualBlock:
    """Test ResidualBlock."""
    
    def test_residual_block_initialization(self):
        """Test ResidualBlock can be instantiated."""
        block = ResidualBlock(64, 64)
        assert isinstance(block, nn.Module)
    
    def test_residual_block_forward(self):
        """Test ResidualBlock forward pass."""
        block = ResidualBlock(64, 64)
        x = torch.randn(4, 64, 32, 32)
        
        output = block(x)
        
        assert output.shape == x.shape
    
    def test_residual_block_stride(self):
        """Test ResidualBlock with stride."""
        block = ResidualBlock(64, 128, stride=2)
        x = torch.randn(4, 64, 32, 32)
        
        output = block(x)
        
        # With stride=2, spatial size should halve
        assert output.shape[1] == 128  # Channels doubled
        assert output.shape[2] == x.shape[2] // 2  # Spatial size halved


class TestSimpleResNet:
    """Test SimpleResNet."""
    
    def test_simple_resnet_initialization(self):
        """Test SimpleResNet can be instantiated."""
        model = SimpleResNet(num_classes=10)
        assert isinstance(model, nn.Module)
    
    def test_simple_resnet_forward(self):
        """Test SimpleResNet forward pass."""
        model = SimpleResNet(num_classes=10)
        x = torch.randn(4, 3, 32, 32)
        
        output = model(x)
        
        assert output.shape == (4, 10)
    
    def test_resnet_has_residual_blocks(self):
        """Test that ResNet has residual blocks."""
        model = SimpleResNet()
        
        has_residual = any(isinstance(m, ResidualBlock) for m in model.modules())
        assert has_residual


class TestFeatureExtraction:
    """Test feature extraction."""
    
    def test_get_pretrained_features(self):
        """Test extracting features from pretrained model."""
        model = load_pretrained_resnet(num_classes=10)
        x = torch.randn(4, 3, 224, 224)
        
        features = get_pretrained_features(model, x)
        
        assert features is not None
        assert len(features.shape) >= 2
