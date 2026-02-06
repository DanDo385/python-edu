"""Project 44: Fine-tuning Large Language Models"""

import torch
import torch.nn as nn


class LoRALayer(nn.Module):
    """LoRA (Low-Rank Adaptation) layer."""
    
    def __init__(self, in_features, out_features, rank=8):
        super().__init__()
        # TODO: Implement LoRA
        # Low-rank matrices A and B
        # Original weights frozen
        # output = Wx + (B @ A) @ x
        pass
    
    def forward(self, x):
        # TODO: Forward pass
        return None
