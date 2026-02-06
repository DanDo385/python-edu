"""
Test suite for Project 36: RNNs and LSTMs

Run with: pytest test.py -v
"""

import pytest
import torch
import torch.nn as nn
from exercise import (
    SimpleRNN,
    LSTMModel,
    GRUModel,
    create_sequence_batch,
    get_rnn_output_shape,
)


class TestSimpleRNN:
    """Test SimpleRNN model."""
    
    def test_model_initialization(self):
        """Test model can be instantiated."""
        model = SimpleRNN(input_size=10, hidden_size=64, num_classes=2)
        assert isinstance(model, nn.Module)
    
    def test_forward_pass_shape(self):
        """Test forward pass produces correct output shape."""
        model = SimpleRNN(input_size=10, hidden_size=64, num_classes=2)
        x = torch.randn(32, 20, 10)  # (batch, seq_len, features)
        
        output = model(x)
        
        assert output.shape == (32, 2)
    
    def test_forward_pass_values(self):
        """Test forward pass produces valid values."""
        model = SimpleRNN(input_size=5, hidden_size=32, num_classes=3)
        x = torch.randn(1, 10, 5)
        
        output = model(x)
        
        assert torch.isfinite(output).all()
        assert output.dtype == torch.float32
    
    def test_model_has_rnn(self):
        """Test that model has RNN layer."""
        model = SimpleRNN()
        
        has_rnn = any(isinstance(m, nn.RNN) for m in model.modules())
        assert has_rnn


class TestLSTMModel:
    """Test LSTMModel."""
    
    def test_model_initialization(self):
        """Test model can be instantiated."""
        model = LSTMModel(input_size=10, hidden_size=64, num_classes=2)
        assert isinstance(model, nn.Module)
    
    def test_forward_pass_shape(self):
        """Test forward pass produces correct output shape."""
        model = LSTMModel(input_size=10, hidden_size=64, num_classes=2)
        x = torch.randn(16, 15, 10)
        
        output = model(x)
        
        assert output.shape == (16, 2)
    
    def test_model_has_lstm(self):
        """Test that model has LSTM layer."""
        model = LSTMModel()
        
        has_lstm = any(isinstance(m, nn.LSTM) for m in model.modules())
        assert has_lstm


class TestGRUModel:
    """Test GRUModel."""
    
    def test_model_initialization(self):
        """Test model can be instantiated."""
        model = GRUModel(input_size=10, hidden_size=64, num_classes=2)
        assert isinstance(model, nn.Module)
    
    def test_forward_pass_shape(self):
        """Test forward pass produces correct output shape."""
        model = GRUModel(input_size=10, hidden_size=64, num_classes=2)
        x = torch.randn(8, 12, 10)
        
        output = model(x)
        
        assert output.shape == (8, 2)
    
    def test_model_has_gru(self):
        """Test that model has GRU layer."""
        model = GRUModel()
        
        has_gru = any(isinstance(m, nn.GRU) for m in model.modules())
        assert has_gru


class TestSequenceBatching:
    """Test sequence batching."""
    
    def test_create_sequence_batch(self):
        """Test creating batched sequences."""
        sequences = [
            torch.randn(5, 10),  # Length 5
            torch.randn(8, 10),  # Length 8
            torch.randn(3, 10),  # Length 3
        ]
        
        batch, lengths = create_sequence_batch(sequences)
        
        assert batch.shape[0] == 3  # Batch size
        assert batch.shape[1] == 8  # Max length
        assert batch.shape[2] == 10  # Feature size
        assert len(lengths) == 3
    
    def test_padding(self):
        """Test that sequences are padded correctly."""
        sequences = [
            torch.randn(3, 5),
            torch.randn(5, 5),
        ]
        
        batch, lengths = create_sequence_batch(sequences)
        
        # Check that shorter sequence is padded
        assert batch.shape[1] == 5  # Max length
        assert lengths[0] == 3
        assert lengths[1] == 5


class TestHelperFunctions:
    """Test helper functions."""
    
    def test_get_output_shape(self):
        """Test getting output shape."""
        model = SimpleRNN(input_size=10, hidden_size=64, num_classes=2)
        
        output_shape = get_rnn_output_shape(model, (16, 20, 10))
        
        assert output_shape[0] == 16  # Batch size
        assert output_shape[1] == 2  # Num classes


class TestRNNVariants:
    """Test different RNN variants."""
    
    def test_rnn_vs_lstm_vs_gru(self):
        """Test that all variants work."""
        x = torch.randn(4, 10, 5)
        
        rnn_model = SimpleRNN(input_size=5, hidden_size=32, num_classes=3)
        lstm_model = LSTMModel(input_size=5, hidden_size=32, num_classes=3)
        gru_model = GRUModel(input_size=5, hidden_size=32, num_classes=3)
        
        rnn_out = rnn_model(x)
        lstm_out = lstm_model(x)
        gru_out = gru_model(x)
        
        assert rnn_out.shape == lstm_out.shape == gru_out.shape == (4, 3)
