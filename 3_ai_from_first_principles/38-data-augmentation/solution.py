"""
Project 38: Data Augmentation - SOLUTION

Complete solution demonstrating data augmentation.
"""

import torch
import torch.nn as nn
from torchvision import transforms
import numpy as np


def create_train_augmentation():
    """Create training augmentation pipeline."""
    return transforms.Compose([
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomRotation(degrees=15),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])


def create_val_augmentation():
    """Create validation augmentation pipeline (minimal)."""
    return transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])


def apply_mixup(x, y, alpha=1.0):
    """
    Apply Mixup augmentation.
    """
    if alpha > 0:
        lam = np.random.beta(alpha, alpha)
    else:
        lam = 1
    
    batch_size = x.size(0)
    index = torch.randperm(batch_size).to(x.device)
    
    mixed_x = lam * x + (1 - lam) * x[index, :]
    y_a, y_b = y, y[index]
    
    return mixed_x, y_a, y_b, lam


def apply_cutmix(x, y, alpha=1.0):
    """
    Apply CutMix augmentation.
    """
    if alpha > 0:
        lam = np.random.beta(alpha, alpha)
    else:
        lam = 1
    
    batch_size = x.size(0)
    index = torch.randperm(batch_size).to(x.device)
    
    # Get bounding box
    W, H = x.size(3), x.size(2)
    cut_rat = np.sqrt(1.0 - lam)
    cut_w = np.int(W * cut_rat)
    cut_h = np.int(H * cut_rat)
    
    # Random center
    cx = np.random.randint(W)
    cy = np.random.randint(H)
    
    # Bounding box
    bbx1 = np.clip(cx - cut_w // 2, 0, W)
    bby1 = np.clip(cy - cut_h // 2, 0, H)
    bbx2 = np.clip(cx + cut_w // 2, 0, W)
    bby2 = np.clip(cy + cut_h // 2, 0, H)
    
    # Apply CutMix
    x[:, :, bby1:bby2, bbx1:bbx2] = x[index, :, bby1:bby2, bbx1:bbx2]
    
    # Adjust lambda to match actual area ratio
    lam = 1 - ((bbx2 - bbx1) * (bby2 - bby1) / (W * H))
    
    y_a, y_b = y, y[index]
    
    return x, y_a, y_b, lam


def compute_mixup_loss(criterion, predictions, y_a, y_b, lam):
    """
    Compute loss for Mixup/CutMix.
    """
    loss_a = criterion(predictions, y_a)
    loss_b = criterion(predictions, y_b)
    
    # Handle reduction
    if loss_a.dim() == 0:  # Already reduced
        loss = lam * loss_a + (1 - lam) * loss_b
    else:  # Per-sample loss
        loss = lam * loss_a + (1 - lam) * loss_b
        loss = loss.mean()
    
    return loss


def compare_with_without_augmentation():
    """
    Compare training with and without augmentation.
    
    Note: This is conceptual - in practice, you'd train models
    and compare metrics.
    """
    return {
        'with_augmentation': {
            'train_acc': 0.85,
            'val_acc': 0.82,
            'generalization_gap': 0.03
        },
        'without_augmentation': {
            'train_acc': 0.95,
            'val_acc': 0.75,
            'generalization_gap': 0.20
        }
    }


# Example usage
if __name__ == "__main__":
    print("Data Augmentation Demo")
    print("=" * 50)
    
    # Create augmentation pipelines
    train_transform = create_train_augmentation()
    val_transform = create_val_augmentation()
    
    print("Training augmentation:", train_transform)
    print("Validation augmentation:", val_transform)
    
    # Test Mixup
    x = torch.randn(4, 3, 32, 32)
    y = torch.randint(0, 10, (4,))
    
    mixed_x, y_a, y_b, lam = apply_mixup(x, y)
    print(f"\nMixup: lambda = {lam:.3f}")
    print(f"Mixed image shape: {mixed_x.shape}")
    
    # Test CutMix
    cutmix_x, y_a_cm, y_b_cm, lam_cm = apply_cutmix(x, y)
    print(f"\nCutMix: lambda = {lam_cm:.3f}")
    print(f"CutMix image shape: {cutmix_x.shape}")
    
    print("\nData augmentation ready! 🚀")
