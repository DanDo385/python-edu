"""
Test suite for Project 39: Sequence-to-Sequence Models

Run with: pytest test.py -v
"""

import pytest
import torch
import torch.nn as nn
from exercise import Encoder, Decoder, Seq2Seq


class TestEncoder:
    """Test Encoder."""
    
    def test_encoder_initialization(self):
        """Test encoder can be instantiated."""
        encoder = Encoder(input_size=100, hidden_size=64)
        assert isinstance(encoder, nn.Module)
    
    def test_encoder_forward(self):
        """Test encoder forward pass."""
        encoder = Encoder(input_size=100, hidden_size=64)
        x = torch.randint(0, 100, (4, 10))  # (batch, seq_len)
        
        output, (hidden, cell) = encoder(x)
        
        assert output is not None
        assert hidden is not None


class TestDecoder:
    """Test Decoder."""
    
    def test_decoder_initialization(self):
        """Test decoder can be instantiated."""
        decoder = Decoder(output_size=50, hidden_size=64)
        assert isinstance(decoder, nn.Module)
    
    def test_decoder_forward(self):
        """Test decoder forward pass."""
        decoder = Decoder(output_size=50, hidden_size=64)
        x = torch.randint(0, 50, (4, 1))  # (batch, 1)
        hidden = (torch.randn(1, 4, 64), torch.randn(1, 4, 64))
        
        output, (hidden_out, cell_out) = decoder(x, hidden)
        
        assert output is not None
        assert output.shape[1] == 50  # Output vocabulary size


class TestSeq2Seq:
    """Test Seq2Seq model."""
    
    def test_seq2seq_initialization(self):
        """Test seq2seq can be instantiated."""
        encoder = Encoder(input_size=100, hidden_size=64)
        decoder = Decoder(output_size=50, hidden_size=64)
        model = Seq2Seq(encoder, decoder)
        
        assert isinstance(model, nn.Module)
    
    def test_seq2seq_forward(self):
        """Test seq2seq forward pass."""
        encoder = Encoder(input_size=100, hidden_size=64)
        decoder = Decoder(output_size=50, hidden_size=64)
        model = Seq2Seq(encoder, decoder)
        
        src = torch.randint(0, 100, (4, 10))
        tgt = torch.randint(0, 50, (4, 8))
        
        output = model(src, tgt)
        
        assert output is not None
