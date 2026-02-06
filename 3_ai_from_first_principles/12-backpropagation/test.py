"""Test suite for Project 23: Backpropagation"""
import pytest
import numpy as np
from exercise import forward_pass_2layer, compute_loss_mse, backward_pass_2layer


def test_forward_pass_2layer():
    h, y = forward_pass_2layer(2.0, 1.0, 0.0, 1.0, 0.0)
    assert h == 2.0  # ReLU(1*2 + 0) = 2
    assert y == 2.0  # 1*2 + 0 = 2


def test_compute_loss_mse():
    loss = compute_loss_mse(3.0, 1.0)
    assert loss == 4.0  # (3-1)² = 4


def test_backward_pass_2layer():
    x, y_true = 2.0, 1.0
    w1, b1, w2, b2 = 1.0, 0.0, 1.0, 0.0
    h, y_pred = forward_pass_2layer(x, w1, b1, w2, b2)
    
    dLoss_dw1, dLoss_db1, dLoss_dw2, dLoss_db2 = backward_pass_2layer(
        x, h, y_pred, y_true, w1, w2
    )
    
    # Check gradients are computed
    assert dLoss_dw1 is not None
    assert dLoss_db1 is not None
    assert dLoss_dw2 is not None
    assert dLoss_db2 is not None




