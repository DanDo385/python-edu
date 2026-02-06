"""Project 43: Language Modeling with Transformers"""

import torch
import torch.nn as nn
from project_41_transformer import TransformerBlock, positional_encoding


class LanguageModel(nn.Module):
    """Decoder-only transformer for language modeling."""
    
    def __init__(self, vocab_size, d_model=512, num_heads=8, 
                 num_layers=6, d_ff=2048, max_seq_length=5000):
        super().__init__()
        # TODO: Implement decoder-only transformer
        # self.embedding = nn.Embedding(...)
        # self.pos_encoding = positional_encoding(...)
        # self.layers = nn.ModuleList([...])
        # self.fc_out = nn.Linear(...)
        pass
    
    def forward(self, x, mask=None):
        # TODO: Implement forward pass
        return None
    
    def generate(self, start_tokens, max_length=100):
        # TODO: Implement text generation
        return None
