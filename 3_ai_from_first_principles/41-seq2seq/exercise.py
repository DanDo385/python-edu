"""
Project 39: Sequence-to-Sequence Models

Complete the class definitions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class Encoder(nn.Module):
    """
    Encoder for seq2seq model.
    
    Processes input sequence and produces hidden states.
    """
    
    def __init__(self, input_size, hidden_size, num_layers=1):
        """
        Initialize encoder.
        
        Args:
            input_size (int): Input vocabulary size
            hidden_size (int): Hidden state size
            num_layers (int): Number of LSTM layers
        """
        super().__init__()
        # TODO: Define embedding and LSTM
        # self.embedding = nn.Embedding(input_size, hidden_size)
        # self.lstm = nn.LSTM(hidden_size, hidden_size, num_layers, batch_first=True)
        pass
    
    def forward(self, x):
        """
        Forward pass through encoder.
        
        Args:
            x (torch.Tensor): Input sequences, shape (batch, seq_len)
        
        Returns:
            tuple: (output, (hidden, cell))
                - output: All hidden states
                - hidden, cell: Final states
        """
        # TODO: Implement forward pass
        return None, (None, None)


class Decoder(nn.Module):
    """
    Decoder for seq2seq model.
    
    Generates output sequence from encoder context.
    """
    
    def __init__(self, output_size, hidden_size, num_layers=1):
        """
        Initialize decoder.
        
        Args:
            output_size (int): Output vocabulary size
            hidden_size (int): Hidden state size
            num_layers (int): Number of LSTM layers
        """
        super().__init__()
        # TODO: Define embedding, LSTM, and output layer
        # self.embedding = nn.Embedding(output_size, hidden_size)
        # self.lstm = nn.LSTM(hidden_size, hidden_size, num_layers, batch_first=True)
        # self.fc = nn.Linear(hidden_size, output_size)
        pass
    
    def forward(self, x, hidden):
        """
        Forward pass through decoder.
        
        Args:
            x (torch.Tensor): Input token, shape (batch, 1)
            hidden (tuple): Hidden and cell states from encoder
        
        Returns:
            tuple: (output, (hidden, cell))
                - output: Logits for next token
                - hidden, cell: Updated states
        """
        # TODO: Implement forward pass
        return None, (None, None)


class Seq2Seq(nn.Module):
    """
    Complete seq2seq model combining encoder and decoder.
    """
    
    def __init__(self, encoder, decoder):
        """
        Initialize seq2seq model.
        
        Args:
            encoder (Encoder): Encoder model
            decoder (Decoder): Decoder model
        """
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder
    
    def forward(self, src, tgt, teacher_forcing_ratio=0.5):
        """
        Forward pass through seq2seq model.
        
        Args:
            src (torch.Tensor): Source sequence
            tgt (torch.Tensor): Target sequence
            teacher_forcing_ratio (float): Probability of using ground truth
        
        Returns:
            torch.Tensor: Output logits for each time step
        """
        # TODO: Implement seq2seq forward
        # 1. Encode source: encoder_output, encoder_hidden = encoder(src)
        # 2. Initialize decoder with encoder hidden state
        # 3. For each time step:
        #    - Use teacher forcing or previous prediction
        #    - Decode one token
        #    - Collect outputs
        return None
