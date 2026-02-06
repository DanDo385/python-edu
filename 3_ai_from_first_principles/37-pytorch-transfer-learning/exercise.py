"""
Project 37: Advanced CNNs and Transfer Learning

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""

import torch
import torch.nn as nn
from torchvision import models


def load_pretrained_resnet(num_classes=10):
    """
    Load pretrained ResNet18 and modify for new task.
    
    Args:
        num_classes (int): Number of output classes for new task
    
    Returns:
        nn.Module: Modified ResNet model
    
    Note:
        - Load ResNet18: models.resnet18(pretrained=True)
        - Replace final fully connected layer
        - ResNet18's fc layer: model.fc
        - New fc: nn.Linear(model.fc.in_features, num_classes)
    """
    # TODO: Load and modify pretrained ResNet
    # 1. Load: model = models.resnet18(pretrained=True)
    # 2. Get input features: in_features = model.fc.in_features
    # 3. Replace: model.fc = nn.Linear(in_features, num_classes)
    return None


def freeze_pretrained_layers(model, freeze=True):
    """
    Freeze or unfreeze pretrained layers.
    
    Args:
        model (nn.Module): Pretrained model
        freeze (bool): If True, freeze layers; if False, unfreeze
    
    Returns:
        nn.Module: Model with frozen/unfrozen layers
    
    Note:
        - Set requires_grad = False to freeze
        - Set requires_grad = True to unfreeze
        - Usually freeze early layers, train later layers
    """
    # TODO: Freeze/unfreeze layers
    # for param in model.parameters():
    #     param.requires_grad = not freeze
    return model


def fine_tune_resnet(model, freeze_early_layers=True):
    """
    Fine-tune ResNet: freeze early layers, train later layers.
    
    Args:
        model (nn.Module): ResNet model
        freeze_early_layers (bool): Whether to freeze early layers
    
    Returns:
        nn.Module: Fine-tuned model
    
    Note:
        - Freeze: layer1, layer2 (early layers)
        - Train: layer3, layer4, fc (later layers)
        - ResNet layers: model.layer1, model.layer2, etc.
    """
    # TODO: Fine-tune specific layers
    # if freeze_early_layers:
    #     for param in model.layer1.parameters():
    #         param.requires_grad = False
    #     for param in model.layer2.parameters():
    #         param.requires_grad = False
    return model


class ResidualBlock(nn.Module):
    """
    Residual block with skip connection.
    
    Architecture:
    Input → Conv → BN → ReLU → Conv → BN → Add(Input) → ReLU → Output
    """
    
    def __init__(self, in_channels, out_channels, stride=1):
        """
        Initialize residual block.
        
        Args:
            in_channels (int): Input channels
            out_channels (int): Output channels
            stride (int): Stride for first conv (default 1)
        
        Note:
            - Two conv layers with batch norm
            - Skip connection: output = F(x) + x
            - If stride > 1 or channels change, need projection
        """
        super().__init__()
        # TODO: Define residual block
        # self.conv1 = nn.Conv2d(in_channels, out_channels, 3, stride, 1)
        # self.bn1 = nn.BatchNorm2d(out_channels)
        # self.conv2 = nn.Conv2d(out_channels, out_channels, 3, 1, 1)
        # self.bn2 = nn.BatchNorm2d(out_channels)
        # 
        # # Skip connection (if needed)
        # if stride != 1 or in_channels != out_channels:
        #     self.shortcut = nn.Sequential(
        #         nn.Conv2d(in_channels, out_channels, 1, stride),
        #         nn.BatchNorm2d(out_channels)
        #     )
        # else:
        #     self.shortcut = nn.Identity()
        pass
    
    def forward(self, x):
        """
        Forward pass with skip connection.
        
        Args:
            x (torch.Tensor): Input tensor
        
        Returns:
            torch.Tensor: Output tensor
        
        Note:
            - Compute: out = conv2(relu(bn1(conv1(x))))
            - Add skip: out = out + shortcut(x)
            - Apply final ReLU
        """
        # TODO: Implement forward with skip connection
        # residual = self.shortcut(x)
        # out = F.relu(self.bn1(self.conv1(x)))
        # out = self.bn2(self.conv2(out))
        # out += residual
        # out = F.relu(out)
        return None


class SimpleResNet(nn.Module):
    """
    Simple ResNet-like architecture.
    
    Architecture:
    Conv → BN → ReLU → ResidualBlock → ResidualBlock → AvgPool → FC
    """
    
    def __init__(self, num_classes=10):
        """
        Initialize Simple ResNet.
        
        Args:
            num_classes (int): Number of output classes
        
        Note:
            - Initial conv: 3 → 64 channels
            - Two residual blocks
            - Global average pooling
            - Classifier
        """
        super().__init__()
        # TODO: Build ResNet-like architecture
        # self.conv1 = nn.Conv2d(3, 64, 7, 2, 3)
        # self.bn1 = nn.BatchNorm2d(64)
        # self.layer1 = ResidualBlock(64, 64)
        # self.layer2 = ResidualBlock(64, 128, stride=2)
        # self.avgpool = nn.AdaptiveAvgPool2d(1)
        # self.fc = nn.Linear(128, num_classes)
        pass
    
    def forward(self, x):
        """
        Forward pass through ResNet.
        
        Args:
            x (torch.Tensor): Input images, shape (batch, 3, H, W)
        
        Returns:
            torch.Tensor: Output logits
        """
        # TODO: Implement forward pass
        return None


def get_pretrained_features(model, x):
    """
    Extract features from pretrained model (before classifier).
    
    Args:
        model (nn.Module): Pretrained model
        x (torch.Tensor): Input images
    
    Returns:
        torch.Tensor: Feature vectors
    
    Note:
        - Remove final classifier layer
        - Get features before fc layer
        - For ResNet: model.avgpool(model.layer4(...))
    """
    # TODO: Extract features
    # Remove classifier: features = model.features(x) or manually
    return None
