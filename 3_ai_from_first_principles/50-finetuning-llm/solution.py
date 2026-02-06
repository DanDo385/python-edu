"""Project 44: Fine-tuning LLMs - SOLUTION"""

import torch
import torch.nn as nn


class LoRALayer(nn.Module):
    """LoRA (Low-Rank Adaptation) layer."""
    
    def __init__(self, in_features, out_features, rank=8):
        super().__init__()
        self.rank = rank
        self.A = nn.Parameter(torch.randn(rank, in_features) * 0.02)
        self.B = nn.Parameter(torch.zeros(out_features, rank))
    
    def forward(self, x):
        # LoRA: Wx + (B @ A) @ x
        lora_output = torch.matmul(x, self.A.T)
        lora_output = torch.matmul(lora_output, self.B.T)
        return lora_output
