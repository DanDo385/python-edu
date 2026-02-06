"""
Project 37: Transfer Learning - SOLUTION

Complete solution demonstrating transfer learning.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import models


def load_pretrained_resnet(num_classes=10):
    """
    Load pretrained ResNet18 and modify for new task.
    """
    # Load pretrained ResNet18
    model = models.resnet18(pretrained=True)
    
    # Get input features of final layer
    in_features = model.fc.in_features
    
    # Replace final layer for new task
    model.fc = nn.Linear(in_features, num_classes)
    
    return model


def freeze_pretrained_layers(model, freeze=True):
    """
    Freeze or unfreeze pretrained layers.
    """
    for param in model.parameters():
        param.requires_grad = not freeze
    
    return model


def fine_tune_resnet(model, freeze_early_layers=True):
    """
    Fine-tune ResNet: freeze early layers, train later layers.
    """
    if freeze_early_layers:
        # Freeze early layers
        for param in model.layer1.parameters():
            param.requires_grad = False
        for param in model.layer2.parameters():
            param.requires_grad = False
        
        # Keep later layers trainable
        for param in model.layer3.parameters():
            param.requires_grad = True
        for param in model.layer4.parameters():
            param.requires_grad = True
        for param in model.fc.parameters():
            param.requires_grad = True
    
    return model


class ResidualBlock(nn.Module):
    """
    Residual block with skip connection.
    """
    
    def __init__(self, in_channels, out_channels, stride=1):
        """Initialize residual block."""
        super().__init__()
        
        # Main path
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(out_channels)
        
        # Skip connection
        if stride != 1 or in_channels != out_channels:
            # Need projection to match dimensions
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride),
                nn.BatchNorm2d(out_channels)
            )
        else:
            # Identity mapping
            self.shortcut = nn.Identity()
    
    def forward(self, x):
        """Forward pass with skip connection."""
        # Main path
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        
        # Skip connection
        residual = self.shortcut(x)
        out += residual
        
        # Final activation
        out = F.relu(out)
        
        return out


class SimpleResNet(nn.Module):
    """
    Simple ResNet-like architecture.
    """
    
    def __init__(self, num_classes=10):
        """Initialize Simple ResNet."""
        super().__init__()
        
        # Initial conv layer
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3)
        self.bn1 = nn.BatchNorm2d(64)
        
        # Residual blocks
        self.layer1 = ResidualBlock(64, 64)
        self.layer2 = ResidualBlock(64, 128, stride=2)
        
        # Global average pooling
        self.avgpool = nn.AdaptiveAvgPool2d(1)
        
        # Classifier
        self.fc = nn.Linear(128, num_classes)
    
    def forward(self, x):
        """Forward pass through ResNet."""
        # Initial conv
        x = F.relu(self.bn1(self.conv1(x)))
        
        # Residual blocks
        x = self.layer1(x)
        x = self.layer2(x)
        
        # Global pooling
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        
        # Classifier
        x = self.fc(x)
        
        return x


def get_pretrained_features(model, x):
    """
    Extract features from pretrained model (before classifier).
    """
    # Remove final classifier
    model.eval()
    with torch.no_grad():
        # Forward through all layers except fc
        x = model.conv1(x)
        x = model.bn1(x)
        x = F.relu(x)
        x = model.maxpool(x)
        
        x = model.layer1(x)
        x = model.layer2(x)
        x = model.layer3(x)
        x = model.layer4(x)
        
        x = model.avgpool(x)
        x = torch.flatten(x, 1)
        
        # Features before classifier
        features = x
    
    return features


# Example usage
if __name__ == "__main__":
    print("Transfer Learning Demo")
    print("=" * 50)
    
    # Load pretrained model
    model = load_pretrained_resnet(num_classes=10)
    print(f"Loaded pretrained ResNet18")
    print(f"Modified for 10 classes")
    
    # Test forward pass
    x = torch.randn(4, 3, 224, 224)
    output = model(x)
    print(f"\nInput shape: {x.shape}")
    print(f"Output shape: {output.shape}")
    
    # Fine-tuning
    model = fine_tune_resnet(model, freeze_early_layers=True)
    print("\nFine-tuned: Early layers frozen, later layers trainable")
    
    # Simple ResNet
    simple_resnet = SimpleResNet(num_classes=10)
    x_small = torch.randn(4, 3, 32, 32)
    output_small = simple_resnet(x_small)
    print(f"\nSimple ResNet output shape: {output_small.shape}")
    
    print("\nTransfer learning ready! 🚀")
