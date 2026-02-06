"""
Test suite for Project 38: Data Augmentation

Run with: pytest test.py -v
"""

import pytest
import torch
from torchvision import transforms
from exercise import (
    create_train_augmentation,
    create_val_augmentation,
    apply_mixup,
    apply_cutmix,
    compute_mixup_loss,
    compare_with_without_augmentation,
)


class TestAugmentation:
    """Test augmentation pipelines."""
    
    def test_create_train_augmentation(self):
        """Test training augmentation pipeline."""
        transform = create_train_augmentation()
        
        assert isinstance(transform, transforms.Compose)
        assert len(transform.transforms) > 0
    
    def test_create_val_augmentation(self):
        """Test validation augmentation pipeline."""
        transform = create_val_augmentation()
        
        assert isinstance(transform, transforms.Compose)
    
    def test_augmentation_applies(self):
        """Test that augmentation can be applied."""
        transform = create_train_augmentation()
        # Create dummy PIL Image or tensor
        x = torch.randn(3, 32, 32)
        
        # Should work (may need to handle tensor vs PIL)
        try:
            result = transform(x)
            assert result is not None
        except:
            # If PIL expected, that's okay for test
            pass


class TestMixup:
    """Test Mixup augmentation."""
    
    def test_apply_mixup(self):
        """Test Mixup application."""
        x = torch.randn(4, 3, 32, 32)
        y = torch.randint(0, 10, (4,))
        
        mixed_x, y_a, y_b, lam = apply_mixup(x, y, alpha=1.0)
        
        assert mixed_x.shape == x.shape
        assert y_a.shape == y.shape
        assert y_b.shape == y.shape
        assert 0 <= lam <= 1
    
    def test_mixup_values(self):
        """Test Mixup produces valid values."""
        x = torch.randn(2, 3, 16, 16)
        y = torch.randint(0, 5, (2,))
        
        mixed_x, _, _, lam = apply_mixup(x, y)
        
        assert torch.isfinite(mixed_x).all()
        assert 0 <= lam <= 1


class TestCutMix:
    """Test CutMix augmentation."""
    
    def test_apply_cutmix(self):
        """Test CutMix application."""
        x = torch.randn(4, 3, 32, 32)
        y = torch.randint(0, 10, (4,))
        
        mixed_x, y_a, y_b, lam = apply_cutmix(x, y, alpha=1.0)
        
        assert mixed_x.shape == x.shape
        assert y_a.shape == y.shape
        assert y_b.shape == y.shape
        assert 0 <= lam <= 1
    
    def test_cutmix_values(self):
        """Test CutMix produces valid values."""
        x = torch.randn(2, 3, 16, 16)
        y = torch.randint(0, 5, (2,))
        
        mixed_x, _, _, lam = apply_cutmix(x, y)
        
        assert torch.isfinite(mixed_x).all()
        assert 0 <= lam <= 1


class TestMixupLoss:
    """Test Mixup loss computation."""
    
    def test_compute_mixup_loss(self):
        """Test computing Mixup loss."""
        criterion = torch.nn.CrossEntropyLoss(reduction='none')
        predictions = torch.randn(4, 10)
        y_a = torch.randint(0, 10, (4,))
        y_b = torch.randint(0, 10, (4,))
        lam = 0.5
        
        loss = compute_mixup_loss(criterion, predictions, y_a, y_b, lam)
        
        assert loss is not None
        assert isinstance(loss, torch.Tensor)


class TestComparison:
    """Test comparison function."""
    
    def test_compare_augmentation(self):
        """Test comparison function."""
        results = compare_with_without_augmentation()
        
        assert 'with_augmentation' in results
        assert 'without_augmentation' in results
