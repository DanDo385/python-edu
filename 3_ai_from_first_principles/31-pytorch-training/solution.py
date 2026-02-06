"""
Project 34: Training PyTorch Model - SOLUTION

Complete solution demonstrating PyTorch training pipeline.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset


def create_dataloader(X, y, batch_size=32, shuffle=True):
    """Create a DataLoader from data arrays."""
    # Ensure tensors
    if not isinstance(X, torch.Tensor):
        X = torch.tensor(X, dtype=torch.float32)
    if not isinstance(y, torch.Tensor):
        y = torch.tensor(y, dtype=torch.long)
    
    # Create dataset and dataloader
    dataset = TensorDataset(X, y)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
    
    return dataloader


def train_one_epoch(model, dataloader, criterion, optimizer, device='cpu'):
    """Train model for one epoch."""
    model.train()
    total_loss = 0.0
    num_batches = 0
    
    for batch_x, batch_y in dataloader:
        # Move to device
        batch_x = batch_x.to(device)
        batch_y = batch_y.to(device)
        
        # Zero gradients
        optimizer.zero_grad()
        
        # Forward pass
        predictions = model(batch_x)
        
        # Compute loss
        loss = criterion(predictions, batch_y)
        
        # Backward pass
        loss.backward()
        
        # Update weights
        optimizer.step()
        
        # Accumulate loss
        total_loss += loss.item()
        num_batches += 1
    
    return total_loss / num_batches if num_batches > 0 else 0.0


def evaluate_model(model, dataloader, criterion, device='cpu'):
    """Evaluate model on dataset."""
    model.eval()
    total_loss = 0.0
    correct = 0
    total = 0
    
    with torch.no_grad():
        for batch_x, batch_y in dataloader:
            # Move to device
            batch_x = batch_x.to(device)
            batch_y = batch_y.to(device)
            
            # Forward pass
            predictions = model(batch_x)
            
            # Compute loss
            loss = criterion(predictions, batch_y)
            total_loss += loss.item()
            
            # Compute accuracy
            predicted_classes = torch.argmax(predictions, dim=1)
            correct += (predicted_classes == batch_y).sum().item()
            total += batch_y.size(0)
    
    accuracy = correct / total if total > 0 else 0.0
    avg_loss = total_loss / len(dataloader) if len(dataloader) > 0 else 0.0
    
    return avg_loss, accuracy


def compute_accuracy(predictions, targets):
    """Compute classification accuracy."""
    predicted_classes = torch.argmax(predictions, dim=1)
    correct = (predicted_classes == targets).sum().item()
    total = targets.size(0)
    return correct / total if total > 0 else 0.0


def train_model(model, train_loader, val_loader, num_epochs=10, 
                learning_rate=0.001, device='cpu'):
    """Complete training function."""
    # Move model to device
    model = model.to(device)
    
    # Define loss and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    
    history = {
        'train_loss': [],
        'val_loss': [],
        'val_accuracy': []
    }
    
    for epoch in range(num_epochs):
        # Train
        train_loss = train_one_epoch(model, train_loader, criterion, optimizer, device)
        history['train_loss'].append(train_loss)
        
        # Evaluate
        val_loss, val_acc = evaluate_model(model, val_loader, criterion, device)
        history['val_loss'].append(val_loss)
        history['val_accuracy'].append(val_acc)
        
        if (epoch + 1) % 5 == 0:
            print(f"Epoch {epoch+1}/{num_epochs} - "
                  f"Train Loss: {train_loss:.4f}, "
                  f"Val Loss: {val_loss:.4f}, "
                  f"Val Acc: {val_acc:.4f}")
    
    return history


class SimpleMLP(nn.Module):
    """Simple MLP for MNIST classification."""
    
    def __init__(self, input_size=784, hidden_size=128, output_size=10):
        """Initialize model."""
        super().__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.layer2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        """Forward pass."""
        x = F.relu(self.layer1(x))
        x = self.layer2(x)
        return x


# Example usage
if __name__ == "__main__":
    print("PyTorch Training Demo")
    print("=" * 50)
    
    # Create synthetic MNIST-like data
    X_train = torch.randn(1000, 784)
    y_train = torch.randint(0, 10, (1000,))
    X_val = torch.randn(200, 784)
    y_val = torch.randint(0, 10, (200,))
    
    # Create data loaders
    train_loader = create_dataloader(X_train, y_train, batch_size=32)
    val_loader = create_dataloader(X_val, y_val, batch_size=32, shuffle=False)
    
    # Create model
    model = SimpleMLP(input_size=784, hidden_size=128, output_size=10)
    
    # Train
    print("\nTraining model...")
    history = train_model(
        model, train_loader, val_loader,
        num_epochs=10, learning_rate=0.001
    )
    
    print(f"\nFinal validation accuracy: {history['val_accuracy'][-1]:.4f}")
    print("\nTraining complete! 🚀")
