"""
Test suite for Project 40: Attention Mechanisms

Run with: pytest test.py -v
"""

import pytest
import torch
import torch.nn as nn
from exercise import (
    scaled_dot_product_attention,
    MultiHeadAttention,
    AttentionLayer,
)


class TestScaledDotProductAttention:
    """Test scaled dot-product attention."""
    
    def test_attention_shape(self):
        """Test attention output shape."""
        batch_size = 4
        seq_len_q = 10
        seq_len_k = 12
        d_k = 64
        d_v = 64
        
        query = torch.randn(batch_size, seq_len_q, d_k)
        key = torch.randn(batch_size, seq_len_k, d_k)
        value = torch.randn(batch_size, seq_len_k, d_v)
        
        output, attn_weights = scaled_dot_product_attention(query, key, value)
        
        assert output.shape == (batch_size, seq_len_q, d_v)
        assert attn_weights.shape == (batch_size, seq_len_q, seq_len_k)
    
    def test_attention_values(self):
        """Test attention produces valid values."""
        query = torch.randn(2, 5, 32)
        key = torch.randn(2, 5, 32)
        value = torch.randn(2, 5, 32)
        
        output, attn_weights = scaled_dot_product_attention(query, key, value)
        
        assert torch.isfinite(output).all()
        # Attention weights should sum to 1
        assert torch.allclose(attn_weights.sum(dim=-1), torch.ones(2, 5))


class TestMultiHeadAttention:
    """Test MultiHeadAttention."""
    
    def test_multi_head_initialization(self):
        """Test multi-head attention can be instantiated."""
        mha = MultiHeadAttention(d_model=128, num_heads=8)
        assert isinstance(mha, nn.Module)
    
    def test_multi_head_forward(self):
        """Test multi-head attention forward pass."""
        mha = MultiHeadAttention(d_model=128, num_heads=8)
        x = torch.randn(4, 10, 128)
        
        output = mha(x, x, x)
        
        assert output.shape == x.shape
    
    def test_multi_head_different_inputs(self):
        """Test with different query/key/value."""
        mha = MultiHeadAttention(d_model=64, num_heads=4)
        query = torch.randn(2, 5, 64)
        key = torch.randn(2, 8, 64)
        value = torch.randn(2, 8, 64)
        
        output = mha(query, key, value)
        
        assert output.shape == (2, 5, 64)


class TestAttentionLayer:
    """Test AttentionLayer."""
    
    def test_attention_layer_initialization(self):
        """Test attention layer can be instantiated."""
        layer = AttentionLayer(d_model=128, num_heads=8)
        assert isinstance(layer, nn.Module)
    
    def test_attention_layer_forward(self):
        """Test attention layer forward pass."""
        layer = AttentionLayer(d_model=128, num_heads=8)
        x = torch.randn(4, 10, 128)
        
        output = layer(x)
        
        assert output.shape == x.shape
