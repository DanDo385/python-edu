"""
Project 35: Convolutional Neural Networks for CIFAR-10

Complete the class definition below according to its docstring.
Run pytest test.py -v to test your solutions.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class SimpleCNN(nn.Module):
    """
    Simple CNN for CIFAR-10 classification.
    
    Architecture:
    Input (3, 32, 32) → Conv2d → ReLU → MaxPool2d → 
    Conv2d → ReLU → MaxPool2d → Flatten → Linear → Output (10)
    
    CIFAR-10: 32x32 RGB images, 10 classes
    """
    
    def __init__(self, num_classes=10):
        """
        Initialize CNN.
        
        Args:
            num_classes (int): Number of output classes (default 10 for CIFAR-10)
        
        Architecture suggestion:
        - Conv2d(3, 32, kernel_size=3, padding=1) → ReLU → MaxPool2d(2)
        - Conv2d(32, 64, kernel_size=3, padding=1) → ReLU → MaxPool2d(2)
        - Flatten
        - Linear(64*8*8, 128) → ReLU
        - Linear(128, num_classes)
        
        Note:
            - Input: (3, 32, 32) for CIFAR-10
            - After 2 MaxPool2d(2): 32 → 16 → 8
            - So flattened size is 64 * 8 * 8 = 4096
        """
        super().__init__()
        # TODO: Define layers
        # self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        # self.pool = nn.MaxPool2d(2, 2)
        # self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        # self.fc1 = nn.Linear(64 * 8 * 8, 128)
        # self.fc2 = nn.Linear(128, num_classes)
        pass
    
    def forward(self, x):
        """
        Forward pass through CNN.
        
        Args:
            x (torch.Tensor): Input images, shape (batch_size, 3, 32, 32)
        
        Returns:
            torch.Tensor: Output logits, shape (batch_size, num_classes)
        
        Note:
            - Apply conv1 → ReLU → pool
            - Apply conv2 → ReLU → pool
            - Flatten: x.view(x.size(0), -1) or torch.flatten(x, 1)
            - Apply fc1 → ReLU → fc2
        """
        # TODO: Implement forward pass
        # 1. x = self.pool(F.relu(self.conv1(x)))
        # 2. x = self.pool(F.relu(self.conv2(x)))
        # 3. x = torch.flatten(x, 1)  # Flatten except batch dimension
        # 4. x = F.relu(self.fc1(x))
        # 5. x = self.fc2(x)
        return None


def count_cnn_parameters(model):
    """
    Count total parameters in CNN model.
    
    Args:
        model (nn.Module): CNN model
    
    Returns:
        int: Total number of parameters
    """
    # TODO: Count parameters
    return None


def get_cnn_output_shape(model, input_shape=(1, 3, 32, 32)):
    """
    Get output shape of CNN for given input shape.
    
    Args:
        model (nn.Module): CNN model
        input_shape (tuple): Input shape (batch_size, channels, height, width)
    
    Returns:
        tuple: Output shape
    
    Note:
        Create dummy input, run forward pass, check output shape
    """
    # TODO: Get output shape
    model.eval()
    with torch.no_grad():
        dummy_input = torch.randn(input_shape)
        output = model(dummy_input)
    return output.shape


class CNNWithBatchNorm(nn.Module):
    """
    CNN with batch normalization for better training.
    
    Batch normalization helps stabilize training and allows higher learning rates.
    """
    
    def __init__(self, num_classes=10):
        """
        Initialize CNN with batch normalization.
        
        Architecture:
        - Conv2d → BatchNorm2d → ReLU → MaxPool2d
        - Conv2d → BatchNorm2d → ReLU → MaxPool2d
        - Flatten → Linear → BatchNorm1d → ReLU → Linear
        """
        super().__init__()
        # TODO: Define layers with batch normalization
        # Use nn.BatchNorm2d after conv layers
        # Use nn.BatchNorm1d after first linear layer
        pass
    
    def forward(self, x):
        """Forward pass with batch normalization."""
        # TODO: Implement forward pass with batch norm
        return None
