"""
Project 40: Attention Mechanisms

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import math


def scaled_dot_product_attention(query, key, value, mask=None):
    """
    Compute scaled dot-product attention.
    
    Args:
        query (torch.Tensor): Query tensor, shape (..., seq_len_q, d_k)
        key (torch.Tensor): Key tensor, shape (..., seq_len_k, d_k)
        value (torch.Tensor): Value tensor, shape (..., seq_len_v, d_v)
        mask (torch.Tensor): Optional mask, shape (..., seq_len_q, seq_len_k)
    
    Returns:
        tuple: (output, attention_weights)
            - output: Attention output, shape (..., seq_len_q, d_v)
            - attention_weights: Attention weights, shape (..., seq_len_q, seq_len_k)
    
    Formula:
        Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V
    
    Note:
        - Compute scores: scores = Q @ K^T / sqrt(d_k)
        - Apply mask if provided (set masked positions to -inf)
        - Apply softmax
        - Multiply by V
    """
    # TODO: Implement scaled dot-product attention
    # 1. Compute scores: scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)
    # 2. Apply mask if provided
    # 3. Apply softmax
    # 4. Multiply by value
    return None, None


class MultiHeadAttention(nn.Module):
    """
    Multi-head attention mechanism.
    """
    
    def __init__(self, d_model, num_heads):
        """
        Initialize multi-head attention.
        
        Args:
            d_model (int): Model dimension
            num_heads (int): Number of attention heads
        
        Note:
            - d_k = d_v = d_model / num_heads
            - Create linear layers for Q, K, V projections
            - Create output projection layer
        """
        super().__init__()
        assert d_model % num_heads == 0
        
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        
        # TODO: Define linear layers
        # self.W_q = nn.Linear(d_model, d_model)
        # self.W_k = nn.Linear(d_model, d_model)
        # self.W_v = nn.Linear(d_model, d_model)
        # self.W_o = nn.Linear(d_model, d_model)
        pass
    
    def forward(self, query, key, value, mask=None):
        """
        Forward pass through multi-head attention.
        
        Args:
            query, key, value: Input tensors, shape (batch, seq_len, d_model)
            mask: Optional mask
        
        Returns:
            torch.Tensor: Output tensor, shape (batch, seq_len, d_model)
        
        Note:
            - Project Q, K, V
            - Reshape for multi-head: (batch, seq_len, num_heads, d_k)
            - Transpose: (batch, num_heads, seq_len, d_k)
            - Apply scaled_dot_product_attention
            - Concatenate heads
            - Apply output projection
        """
        # TODO: Implement multi-head attention
        batch_size = query.size(0)
        
        return None


class AttentionLayer(nn.Module):
    """
    Complete attention layer with residual connection and layer norm.
    """
    
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.attention = MultiHeadAttention(d_model, num_heads)
        self.norm = nn.LayerNorm(d_model)
    
    def forward(self, x, mask=None):
        """
        Forward pass with residual connection.
        
        Args:
            x (torch.Tensor): Input tensor
            mask: Optional mask
        
        Returns:
            torch.Tensor: Output tensor
        
        Note:
            - Apply attention
            - Add residual: output = x + attention(x)
            - Apply layer norm
        """
        # TODO: Implement with residual connection
        attn_output = self.attention(x, x, x, mask)
        output = self.norm(x + attn_output)
        return output
