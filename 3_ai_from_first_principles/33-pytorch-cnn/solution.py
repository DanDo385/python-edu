"""
Project 35: CNNs for CIFAR-10 - SOLUTION

Complete solution demonstrating CNN implementation.
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
    """
    
    def __init__(self, num_classes=10):
        """Initialize CNN."""
        super().__init__()
        # First convolutional block
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        
        # Second convolutional block
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        
        # Fully connected layers
        # After 2 MaxPool2d(2): 32 → 16 → 8
        # So: 64 channels * 8 * 8 = 4096
        self.fc1 = nn.Linear(64 * 8 * 8, 128)
        self.fc2 = nn.Linear(128, num_classes)
    
    def forward(self, x):
        """Forward pass through CNN."""
        # First conv block
        x = self.pool(F.relu(self.conv1(x)))  # (32, 32) → (16, 16)
        
        # Second conv block
        x = self.pool(F.relu(self.conv2(x)))  # (16, 16) → (8, 8)
        
        # Flatten
        x = torch.flatten(x, 1)  # Flatten except batch dimension
        
        # Fully connected layers
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        
        return x


def count_cnn_parameters(model):
    """Count total parameters in CNN model."""
    return sum(p.numel() for p in model.parameters())


def get_cnn_output_shape(model, input_shape=(1, 3, 32, 32)):
    """Get output shape of CNN for given input shape."""
    model.eval()
    with torch.no_grad():
        dummy_input = torch.randn(input_shape)
        output = model(dummy_input)
    return output.shape


class CNNWithBatchNorm(nn.Module):
    """
    CNN with batch normalization for better training.
    """
    
    def __init__(self, num_classes=10):
        """Initialize CNN with batch normalization."""
        super().__init__()
        # First conv block with batch norm
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(32)
        self.pool = nn.MaxPool2d(2, 2)
        
        # Second conv block with batch norm
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(64)
        
        # Fully connected layers
        self.fc1 = nn.Linear(64 * 8 * 8, 128)
        self.bn3 = nn.BatchNorm1d(128)
        self.fc2 = nn.Linear(128, num_classes)
    
    def forward(self, x):
        """Forward pass with batch normalization."""
        # First conv block
        x = self.pool(F.relu(self.bn1(self.conv1(x))))
        
        # Second conv block
        x = self.pool(F.relu(self.bn2(self.conv2(x))))
        
        # Flatten
        x = torch.flatten(x, 1)
        
        # Fully connected layers
        x = F.relu(self.bn3(self.fc1(x)))
        x = self.fc2(x)
        
        return x


# Example usage
if __name__ == "__main__":
    print("CNN for CIFAR-10 Demo")
    print("=" * 50)
    
    # Create model
    model = SimpleCNN(num_classes=10)
    print(f"Model created: {model}")
    
    # Count parameters
    total_params = count_cnn_parameters(model)
    print(f"\nTotal parameters: {total_params:,}")
    
    # Test forward pass
    x = torch.randn(32, 3, 32, 32)  # Batch of 32 CIFAR-10 images
    output = model(x)
    print(f"\nInput shape: {x.shape}")
    print(f"Output shape: {output.shape}")
    
    # Model with batch norm
    model_bn = CNNWithBatchNorm()
    output_bn = model_bn(x)
    print(f"\nBatchNorm model output shape: {output_bn.shape}")
    
    print("\nCNN is ready for training on CIFAR-10! 🚀")
    print("\nNote: Use training loop from Project 34 to train this model!")
