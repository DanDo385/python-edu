"""
Project 41: Transformer Architecture

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""

import torch
import torch.nn as nn
import math


def positional_encoding(seq_len, d_model):
    """
    Create positional encoding for transformer.
    
    Args:
        seq_len (int): Sequence length
        d_model (int): Model dimension
    
    Returns:
        torch.Tensor: Positional encoding, shape (seq_len, d_model)
    
    Formula:
        PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
        PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
    
    Note:
        - Create position matrix
        - Apply sin/cos formulas
        - Return encoding
    """
    # TODO: Implement positional encoding
    return None


class TransformerBlock(nn.Module):
    """
    Transformer encoder block.
    
    Architecture:
    Input → Self-Attention → Add & Norm → FFN → Add & Norm → Output
    """
    
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        """
        Initialize transformer block.
        
        Args:
            d_model (int): Model dimension
            num_heads (int): Number of attention heads
            d_ff (int): Feed-forward dimension
            dropout (float): Dropout rate
        """
        super().__init__()
        # TODO: Define components
        # Use MultiHeadAttention from project 40
        # self.attention = MultiHeadAttention(d_model, num_heads)
        # self.ffn = nn.Sequential(...)
        # self.norm1 = nn.LayerNorm(d_model)
        # self.norm2 = nn.LayerNorm(d_model)
        # self.dropout = nn.Dropout(dropout)
        pass
    
    def forward(self, x, mask=None):
        """
        Forward pass through transformer block.
        
        Args:
            x (torch.Tensor): Input tensor
            mask: Optional mask
        
        Returns:
            torch.Tensor: Output tensor
        
        Note:
            - Self-attention with residual
            - Feed-forward with residual
        """
        # TODO: Implement forward pass
        return None
