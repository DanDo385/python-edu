"""Project 42: Complete Transformer - SOLUTION"""

import torch
import torch.nn as nn
from project_41_transformer import TransformerBlock, positional_encoding
from project_40_attention import MultiHeadAttention


class Transformer(nn.Module):
    """Complete Transformer model."""
    
    def __init__(self, src_vocab_size, tgt_vocab_size, d_model=512, 
                 num_heads=8, num_layers=6, d_ff=2048, max_seq_length=5000):
        super().__init__()
        self.src_embedding = nn.Embedding(src_vocab_size, d_model)
        self.tgt_embedding = nn.Embedding(tgt_vocab_size, d_model)
        self.pos_encoding = positional_encoding(max_seq_length, d_model)
        
        self.encoder_layers = nn.ModuleList([
            TransformerBlock(d_model, num_heads, d_ff) 
            for _ in range(num_layers)
        ])
        self.decoder_layers = nn.ModuleList([
            TransformerBlock(d_model, num_heads, d_ff) 
            for _ in range(num_layers)
        ])
        
        self.fc_out = nn.Linear(d_model, tgt_vocab_size)
    
    def forward(self, src, tgt, src_mask=None, tgt_mask=None):
        # Embeddings + positional encoding
        src_emb = self.src_embedding(src) + self.pos_encoding[:src.size(1), :].to(src.device)
        tgt_emb = self.tgt_embedding(tgt) + self.pos_encoding[:tgt.size(1), :].to(tgt.device)
        
        # Encoder
        enc_out = src_emb
        for layer in self.encoder_layers:
            enc_out = layer(enc_out, src_mask)
        
        # Decoder
        dec_out = tgt_emb
        for layer in self.decoder_layers:
            dec_out = layer(dec_out, tgt_mask)
        
        # Output projection
        output = self.fc_out(dec_out)
        return output
