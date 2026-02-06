"""
Project 42: Complete Transformer Implementation

Complete the Transformer class below.
Run pytest test.py -v to test your solutions.
"""

import torch
import torch.nn as nn
from project_41_transformer import TransformerBlock, positional_encoding
from project_40_attention import MultiHeadAttention


class Transformer(nn.Module):
    """
    Complete Transformer model.
    
    Combines encoder and decoder stacks.
    """
    
    def __init__(self, src_vocab_size, tgt_vocab_size, d_model=512, 
                 num_heads=8, num_layers=6, d_ff=2048, max_seq_length=5000):
        """
        Initialize Transformer.
        
        Args:
            src_vocab_size: Source vocabulary size
            tgt_vocab_size: Target vocabulary size
            d_model: Model dimension
            num_heads: Number of attention heads
            num_layers: Number of encoder/decoder layers
            d_ff: Feed-forward dimension
            max_seq_length: Maximum sequence length
        """
        super().__init__()
        # TODO: Define embeddings, encoder, decoder, output projection
        # self.src_embedding = nn.Embedding(...)
        # self.tgt_embedding = nn.Embedding(...)
        # self.pos_encoding = positional_encoding(max_seq_length, d_model)
        # self.encoder_layers = nn.ModuleList([...])
        # self.decoder_layers = nn.ModuleList([...])
        # self.fc_out = nn.Linear(...)
        pass
    
    def forward(self, src, tgt, src_mask=None, tgt_mask=None):
        """
        Forward pass through transformer.
        
        Args:
            src: Source sequence
            tgt: Target sequence
            src_mask: Source mask
            tgt_mask: Target mask (for masking future tokens)
        
        Returns:
            Output logits
        """
        # TODO: Implement forward pass
        return None
