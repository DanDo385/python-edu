"""
Project 36: RNNs and LSTMs for Sequence Modeling

Complete the class definitions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class SimpleRNN(nn.Module):
    """
    Simple RNN for sequence classification.
    
    Architecture:
    RNN → Final hidden state → Linear → Output
    """
    
    def __init__(self, input_size=10, hidden_size=64, num_layers=1, num_classes=2):
        """
        Initialize Simple RNN.
        
        Args:
            input_size (int): Size of input features at each time step
            hidden_size (int): Size of hidden state
            num_layers (int): Number of RNN layers
            num_classes (int): Number of output classes
        
        Note:
            - Use nn.RNN for simple RNN
            - Set batch_first=True for (batch, seq, features) input format
            - Add linear layer for classification
        """
        super().__init__()
        # TODO: Define RNN and classifier
        # self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
        # self.fc = nn.Linear(hidden_size, num_classes)
        pass
    
    def forward(self, x):
        """
        Forward pass through RNN.
        
        Args:
            x (torch.Tensor): Input sequences, shape (batch_size, sequence_length, input_size)
        
        Returns:
            torch.Tensor: Output logits, shape (batch_size, num_classes)
        
        Note:
            - Pass through RNN: output, hidden = self.rnn(x)
            - Use final hidden state (last time step)
            - Pass through linear layer
        """
        # TODO: Implement forward pass
        # 1. output, hidden = self.rnn(x)
        # 2. Get final output: output[:, -1, :] or hidden[-1]
        # 3. Pass through fc layer
        return None


class LSTMModel(nn.Module):
    """
    LSTM model for sequence classification.
    
    Architecture:
    LSTM → Final hidden state → Linear → Output
    """
    
    def __init__(self, input_size=10, hidden_size=64, num_layers=1, num_classes=2):
        """
        Initialize LSTM model.
        
        Args:
            input_size (int): Size of input features
            hidden_size (int): Size of hidden state
            num_layers (int): Number of LSTM layers
            num_classes (int): Number of output classes
        
        Note:
            - Use nn.LSTM instead of nn.RNN
            - LSTM returns (output, (hidden, cell))
        """
        super().__init__()
        # TODO: Define LSTM and classifier
        # self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        # self.fc = nn.Linear(hidden_size, num_classes)
        pass
    
    def forward(self, x):
        """
        Forward pass through LSTM.
        
        Args:
            x (torch.Tensor): Input sequences, shape (batch_size, sequence_length, input_size)
        
        Returns:
            torch.Tensor: Output logits, shape (batch_size, num_classes)
        
        Note:
            - LSTM returns (output, (hidden, cell))
            - Use final hidden state or final output
        """
        # TODO: Implement forward pass
        return None


class GRUModel(nn.Module):
    """
    GRU (Gated Recurrent Unit) model.
    
    GRU is similar to LSTM but simpler (fewer gates).
    """
    
    def __init__(self, input_size=10, hidden_size=64, num_layers=1, num_classes=2):
        """Initialize GRU model."""
        super().__init__()
        # TODO: Define GRU and classifier
        # self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True)
        # self.fc = nn.Linear(hidden_size, num_classes)
        pass
    
    def forward(self, x):
        """Forward pass through GRU."""
        # TODO: Implement forward pass
        return None


def create_sequence_batch(sequences, max_length=None, padding_value=0):
    """
    Create batched sequences with padding.
    
    Args:
        sequences (list): List of sequences (each is a tensor or list)
        max_length (int): Maximum sequence length (None = use max in batch)
        padding_value (float): Value to pad with
    
    Returns:
        torch.Tensor: Padded batch, shape (batch_size, max_length, feature_size)
        torch.Tensor: Lengths of each sequence
    
    Note:
        - Pad sequences to same length
        - Track original lengths
        - Use torch.nn.utils.rnn.pad_sequence or manual padding
    """
    # TODO: Create padded batch
    # Option 1: Use torch.nn.utils.rnn.pad_sequence
    # Option 2: Manual padding
    return None, None


def get_rnn_output_shape(model, input_shape=(32, 20, 10)):
    """
    Get output shape of RNN model.
    
    Args:
        model (nn.Module): RNN model
        input_shape (tuple): Input shape (batch_size, sequence_length, input_size)
    
    Returns:
        tuple: Output shape
    """
    # TODO: Get output shape
    model.eval()
    with torch.no_grad():
        dummy_input = torch.randn(input_shape)
        output = model(dummy_input)
    return output.shape
