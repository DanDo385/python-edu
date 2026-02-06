"""
Project 34: Training a PyTorch Model (MLP on MNIST)

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.

This project demonstrates the complete PyTorch training pipeline.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset


def create_dataloader(X, y, batch_size=32, shuffle=True):
    """
    Create a DataLoader from data arrays.
    
    Args:
        X (torch.Tensor): Features, shape (n_samples, n_features)
        y (torch.Tensor): Labels, shape (n_samples,)
        batch_size (int): Batch size (default 32)
        shuffle (bool): Whether to shuffle data (default True)
    
    Returns:
        DataLoader: PyTorch DataLoader
    
    Note:
        - Convert X and y to tensors if needed
        - Create TensorDataset from X and y
        - Create DataLoader from dataset
    """
    # TODO: Create DataLoader
    # 1. Ensure X and y are tensors
    # 2. Create TensorDataset(X, y)
    # 3. Create DataLoader(dataset, batch_size, shuffle)
    return None


def train_one_epoch(model, dataloader, criterion, optimizer, device='cpu'):
    """
    Train model for one epoch.
    
    Args:
        model (nn.Module): PyTorch model
        dataloader (DataLoader): Training data loader
        criterion: Loss function
        optimizer: Optimizer
        device (str): Device to use ('cpu' or 'cuda')
    
    Returns:
        float: Average loss for the epoch
    
    Note:
        Standard training loop:
        1. Set model to train mode: model.train()
        2. For each batch:
           - Move data to device
           - Zero gradients: optimizer.zero_grad()
           - Forward pass: predictions = model(x)
           - Compute loss: loss = criterion(predictions, y)
           - Backward pass: loss.backward()
           - Update weights: optimizer.step()
        3. Return average loss
    """
    # TODO: Implement training for one epoch
    model.train()
    total_loss = 0.0
    num_batches = 0
    
    return total_loss / num_batches if num_batches > 0 else 0.0


def evaluate_model(model, dataloader, criterion, device='cpu'):
    """
    Evaluate model on dataset.
    
    Args:
        model (nn.Module): PyTorch model
        dataloader (DataLoader): Data loader
        criterion: Loss function
        device (str): Device to use
    
    Returns:
        tuple: (average_loss, accuracy)
    
    Note:
        - Set model to eval mode: model.eval()
        - Use torch.no_grad() context
        - Compute loss and accuracy
    """
    # TODO: Implement evaluation
    model.eval()
    total_loss = 0.0
    correct = 0
    total = 0
    
    with torch.no_grad():
        # TODO: Iterate through dataloader
        # Compute loss and count correct predictions
        pass
    
    accuracy = correct / total if total > 0 else 0.0
    avg_loss = total_loss / len(dataloader) if len(dataloader) > 0 else 0.0
    
    return avg_loss, accuracy


def compute_accuracy(predictions, targets):
    """
    Compute classification accuracy.
    
    Args:
        predictions (torch.Tensor): Model predictions, shape (batch_size, n_classes)
        targets (torch.Tensor): True labels, shape (batch_size,)
    
    Returns:
        float: Accuracy between 0.0 and 1.0
    
    Note:
        - Use torch.argmax to get predicted classes
        - Compare with targets
        - Return mean accuracy
    """
    # TODO: Compute accuracy
    # 1. Get predicted classes: torch.argmax(predictions, dim=1)
    # 2. Compare with targets
    # 3. Return mean
    return None


def train_model(model, train_loader, val_loader, num_epochs=10, 
                learning_rate=0.001, device='cpu'):
    """
    Complete training function.
    
    Args:
        model (nn.Module): PyTorch model
        train_loader (DataLoader): Training data loader
        val_loader (DataLoader): Validation data loader
        num_epochs (int): Number of epochs
        learning_rate (float): Learning rate
        device (str): Device to use
    
    Returns:
        dict: Training history with 'train_loss', 'val_loss', 'val_accuracy'
    
    Note:
        - Move model to device: model.to(device)
        - Define loss: nn.CrossEntropyLoss()
        - Define optimizer: optim.Adam(model.parameters(), lr=learning_rate)
        - Train for num_epochs
        - Evaluate after each epoch
    """
    # TODO: Complete training function
    # 1. Move model to device
    # 2. Define criterion and optimizer
    # 3. For each epoch:
    #    - Train one epoch
    #    - Evaluate on validation set
    #    - Track metrics
    # 4. Return history
    
    history = {
        'train_loss': [],
        'val_loss': [],
        'val_accuracy': []
    }
    
    return history


class SimpleMLP(nn.Module):
    """
    Simple MLP for MNIST classification.
    
    Architecture: Input(784) → Hidden(128, ReLU) → Output(10)
    """
    
    def __init__(self, input_size=784, hidden_size=128, output_size=10):
        """Initialize model."""
        super().__init__()
        # TODO: Define layers
        # self.layer1 = nn.Linear(input_size, hidden_size)
        # self.layer2 = nn.Linear(hidden_size, output_size)
        pass
    
    def forward(self, x):
        """Forward pass."""
        # TODO: Implement forward pass
        # x = F.relu(self.layer1(x))
        # x = self.layer2(x)
        return None
