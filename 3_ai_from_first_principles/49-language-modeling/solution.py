"""Project 43: Language Modeling - SOLUTION"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from project_41_transformer import TransformerBlock, positional_encoding


class LanguageModel(nn.Module):
    """Decoder-only transformer for language modeling."""
    
    def __init__(self, vocab_size, d_model=512, num_heads=8, 
                 num_layers=6, d_ff=2048, max_seq_length=5000):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoding = positional_encoding(max_seq_length, d_model)
        self.layers = nn.ModuleList([
            TransformerBlock(d_model, num_heads, d_ff) 
            for _ in range(num_layers)
        ])
        self.fc_out = nn.Linear(d_model, vocab_size)
    
    def forward(self, x, mask=None):
        seq_len = x.size(1)
        x = self.embedding(x) + self.pos_encoding[:seq_len, :].to(x.device)
        for layer in self.layers:
            x = layer(x, mask)
        return self.fc_out(x)
    
    def generate(self, start_tokens, max_length=100):
        self.eval()
        with torch.no_grad():
            generated = start_tokens.clone()
            for _ in range(max_length):
                output = self.forward(generated)
                next_token = output[:, -1, :].argmax(dim=-1, keepdim=True)
                generated = torch.cat([generated, next_token], dim=1)
        return generated
