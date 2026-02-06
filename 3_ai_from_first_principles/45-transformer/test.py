"""
Test suite for Project 41: Transformer Architecture

Run with: pytest test.py -v
"""

import pytest
import torch
import torch.nn as nn
from exercise import positional_encoding, TransformerBlock


class TestPositionalEncoding:
    """Test positional encoding."""
    
    def test_positional_encoding_shape(self):
        """Test positional encoding shape."""
        pe = positional_encoding(seq_len=10, d_model=64)
        assert pe.shape == (10, 64)
    
    def test_positional_encoding_values(self):
        """Test positional encoding values."""
        pe = positional_encoding(seq_len=5, d_model=32)
        assert torch.isfinite(pe).all()


class TestTransformerBlock:
    """Test TransformerBlock."""
    
    def test_transformer_block_initialization(self):
        """Test transformer block can be instantiated."""
        block = TransformerBlock(d_model=128, num_heads=8, d_ff=512)
        assert isinstance(block, nn.Module)
    
    def test_transformer_block_forward(self):
        """Test transformer block forward pass."""
        block = TransformerBlock(d_model=128, num_heads=8, d_ff=512)
        x = torch.randn(4, 10, 128)
        
        output = block(x)
        
        assert output.shape == x.shape
