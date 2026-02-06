"""
Project 36: RNNs and LSTMs - SOLUTION

Complete solution demonstrating RNN/LSTM implementation.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.utils.rnn import pad_sequence


class SimpleRNN(nn.Module):
    """
    Simple RNN for sequence classification.
    """
    
    def __init__(self, input_size=10, hidden_size=64, num_layers=1, num_classes=2):
        """Initialize Simple RNN."""
        super().__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        """Forward pass through RNN."""
        # RNN returns (output, hidden)
        # output: (batch, seq_len, hidden_size) - hidden states at each time step
        # hidden: (num_layers, batch, hidden_size) - final hidden state
        output, hidden = self.rnn(x)
        
        # Use final output (last time step)
        final_output = output[:, -1, :]  # (batch, hidden_size)
        
        # Classify
        logits = self.fc(final_output)
        return logits


class LSTMModel(nn.Module):
    """
    LSTM model for sequence classification.
    """
    
    def __init__(self, input_size=10, hidden_size=64, num_layers=1, num_classes=2):
        """Initialize LSTM model."""
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        """Forward pass through LSTM."""
        # LSTM returns (output, (hidden, cell))
        output, (hidden, cell) = self.lstm(x)
        
        # Use final hidden state (last layer)
        final_hidden = hidden[-1]  # (batch, hidden_size)
        
        # Classify
        logits = self.fc(final_hidden)
        return logits


class GRUModel(nn.Module):
    """
    GRU (Gated Recurrent Unit) model.
    """
    
    def __init__(self, input_size=10, hidden_size=64, num_layers=1, num_classes=2):
        """Initialize GRU model."""
        super().__init__()
        self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        """Forward pass through GRU."""
        # GRU returns (output, hidden) like RNN
        output, hidden = self.gru(x)
        
        # Use final hidden state
        final_hidden = hidden[-1]  # (batch, hidden_size)
        
        # Classify
        logits = self.fc(final_hidden)
        return logits


def create_sequence_batch(sequences, max_length=None, padding_value=0):
    """
    Create batched sequences with padding.
    """
    # Convert to tensors if needed
    sequences = [torch.tensor(s) if not isinstance(s, torch.Tensor) else s for s in sequences]
    
    # Use pad_sequence utility
    padded = pad_sequence(sequences, batch_first=True, padding_value=padding_value)
    
    # Get lengths
    lengths = torch.tensor([len(s) for s in sequences])
    
    return padded, lengths


def get_rnn_output_shape(model, input_shape=(32, 20, 10)):
    """Get output shape of RNN model."""
    model.eval()
    with torch.no_grad():
        dummy_input = torch.randn(input_shape)
        output = model(dummy_input)
    return output.shape


# Example usage
if __name__ == "__main__":
    print("RNN/LSTM Demo")
    print("=" * 50)
    
    # Create models
    rnn_model = SimpleRNN(input_size=10, hidden_size=64, num_classes=2)
    lstm_model = LSTMModel(input_size=10, hidden_size=64, num_classes=2)
    
    # Test forward pass
    x = torch.randn(32, 20, 10)  # (batch, seq_len, features)
    
    rnn_out = rnn_model(x)
    lstm_out = lstm_model(x)
    
    print(f"Input shape: {x.shape}")
    print(f"RNN output shape: {rnn_out.shape}")
    print(f"LSTM output shape: {lstm_out.shape}")
    
    # Test sequence batching
    sequences = [
        torch.randn(5, 10),
        torch.randn(8, 10),
        torch.randn(3, 10),
    ]
    batch, lengths = create_sequence_batch(sequences)
    print(f"\nBatched sequences shape: {batch.shape}")
    print(f"Sequence lengths: {lengths}")
    
    print("\nRNNs are ready for sequence modeling! 🚀")
