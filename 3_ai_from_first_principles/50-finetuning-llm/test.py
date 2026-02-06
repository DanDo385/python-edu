"""Test suite for Project 44"""

import pytest
import torch
from exercise import LoRALayer


def test_lora_layer():
    layer = LoRALayer(128, 64, rank=8)
    x = torch.randn(4, 10, 128)
    output = layer(x)
    assert output is not None
