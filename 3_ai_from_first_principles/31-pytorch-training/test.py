"""
Test suite for Project 34: Training PyTorch Model

Run with: pytest test.py -v
"""

import pytest
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from exercise import (
    create_dataloader,
    train_one_epoch,
    evaluate_model,
    compute_accuracy,
    train_model,
    SimpleMLP,
)


class TestDataLoader:
    """Test DataLoader creation."""
    
    def test_create_dataloader(self):
        """Test creating DataLoader."""
        X = torch.randn(100, 784)
        y = torch.randint(0, 10, (100,))
        
        dataloader = create_dataloader(X, y, batch_size=32, shuffle=True)
        
        assert isinstance(dataloader, DataLoader)
        assert dataloader.batch_size == 32
    
    def test_dataloader_iteration(self):
        """Test iterating through DataLoader."""
        X = torch.randn(100, 784)
        y = torch.randint(0, 10, (100,))
        
        dataloader = create_dataloader(X, y, batch_size=32)
        
        batch_count = 0
        for batch_x, batch_y in dataloader:
            batch_count += 1
            assert batch_x.shape[0] <= 32
            assert batch_y.shape[0] == batch_x.shape[0]
        
        assert batch_count > 0


class TestTraining:
    """Test training functions."""
    
    def test_train_one_epoch(self):
        """Test training for one epoch."""
        model = SimpleMLP(input_size=784, hidden_size=64, output_size=10)
        X = torch.randn(100, 784)
        y = torch.randint(0, 10, (100,))
        dataloader = create_dataloader(X, y, batch_size=32)
        
        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
        
        loss = train_one_epoch(model, dataloader, criterion, optimizer)
        
        assert isinstance(loss, float)
        assert loss >= 0
    
    def test_evaluate_model(self):
        """Test model evaluation."""
        model = SimpleMLP(input_size=784, hidden_size=64, output_size=10)
        X = torch.randn(50, 784)
        y = torch.randint(0, 10, (50,))
        dataloader = create_dataloader(X, y, batch_size=32, shuffle=False)
        
        criterion = nn.CrossEntropyLoss()
        
        loss, accuracy = evaluate_model(model, dataloader, criterion)
        
        assert isinstance(loss, float)
        assert isinstance(accuracy, float)
        assert 0 <= accuracy <= 1


class TestAccuracy:
    """Test accuracy computation."""
    
    def test_compute_accuracy_perfect(self):
        """Test accuracy with perfect predictions."""
        predictions = torch.tensor([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
        targets = torch.tensor([0, 1, 2])
        
        accuracy = compute_accuracy(predictions, targets)
        
        assert accuracy == 1.0
    
    def test_compute_accuracy_partial(self):
        """Test accuracy with partial correctness."""
        predictions = torch.tensor([[1.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
        targets = torch.tensor([0, 1, 2])
        
        accuracy = compute_accuracy(predictions, targets)
        
        assert abs(accuracy - 2/3) < 0.001  # 2 out of 3 correct


class TestCompleteTraining:
    """Test complete training pipeline."""
    
    def test_train_model(self):
        """Test complete training function."""
        model = SimpleMLP(input_size=784, hidden_size=64, output_size=10)
        
        # Create synthetic data
        X_train = torch.randn(200, 784)
        y_train = torch.randint(0, 10, (200,))
        X_val = torch.randn(50, 784)
        y_val = torch.randint(0, 10, (50,))
        
        train_loader = create_dataloader(X_train, y_train, batch_size=32)
        val_loader = create_dataloader(X_val, y_val, batch_size=32, shuffle=False)
        
        history = train_model(
            model, train_loader, val_loader,
            num_epochs=3, learning_rate=0.01
        )
        
        assert 'train_loss' in history
        assert 'val_loss' in history
        assert 'val_accuracy' in history
        assert len(history['train_loss']) == 3
    
    def test_training_reduces_loss(self):
        """Test that training reduces loss."""
        model = SimpleMLP(input_size=784, hidden_size=64, output_size=10)
        
        X_train = torch.randn(100, 784)
        y_train = torch.randint(0, 10, (100,))
        X_val = torch.randn(20, 784)
        y_val = torch.randint(0, 10, (20,))
        
        train_loader = create_dataloader(X_train, y_train, batch_size=32)
        val_loader = create_dataloader(X_val, y_val, batch_size=32, shuffle=False)
        
        history = train_model(
            model, train_loader, val_loader,
            num_epochs=5, learning_rate=0.01
        )
        
        # Loss should generally decrease (or at least not increase dramatically)
        initial_loss = history['train_loss'][0]
        final_loss = history['train_loss'][-1]
        
        # Allow some variance, but shouldn't increase dramatically
        assert final_loss <= initial_loss * 1.5


class TestModel:
    """Test SimpleMLP model."""
    
    def test_model_forward(self):
        """Test model forward pass."""
        model = SimpleMLP(input_size=784, hidden_size=128, output_size=10)
        x = torch.randn(32, 784)
        
        output = model(x)
        
        assert output.shape == (32, 10)
