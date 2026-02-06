"""Test suite for Project 42: Complete Transformer"""

import pytest
import torch
import torch.nn as nn
from exercise import Transformer


def test_transformer_initialization():
    model = Transformer(src_vocab_size=1000, tgt_vocab_size=1000)
    assert isinstance(model, nn.Module)


def test_transformer_forward():
    model = Transformer(src_vocab_size=100, tgt_vocab_size=100, d_model=128)
    src = torch.randint(0, 100, (4, 10))
    tgt = torch.randint(0, 100, (4, 8))
    output = model(src, tgt)
    assert output is not None
