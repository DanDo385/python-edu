"""
Project 39: Sequence-to-Sequence Models - SOLUTION
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class Encoder(nn.Module):
    """Encoder for seq2seq model."""
    
    def __init__(self, input_size, hidden_size, num_layers=1):
        super().__init__()
        self.embedding = nn.Embedding(input_size, hidden_size)
        self.lstm = nn.LSTM(hidden_size, hidden_size, num_layers, batch_first=True)
    
    def forward(self, x):
        embedded = self.embedding(x)
        output, (hidden, cell) = self.lstm(embedded)
        return output, (hidden, cell)


class Decoder(nn.Module):
    """Decoder for seq2seq model."""
    
    def __init__(self, output_size, hidden_size, num_layers=1):
        super().__init__()
        self.embedding = nn.Embedding(output_size, hidden_size)
        self.lstm = nn.LSTM(hidden_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    
    def forward(self, x, hidden):
        embedded = self.embedding(x)
        output, (hidden, cell) = self.lstm(embedded, hidden)
        output = self.fc(output)
        return output, (hidden, cell)


class Seq2Seq(nn.Module):
    """Complete seq2seq model."""
    
    def __init__(self, encoder, decoder):
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder
    
    def forward(self, src, tgt, teacher_forcing_ratio=0.5):
        batch_size = src.size(0)
        tgt_len = tgt.size(1)
        vocab_size = self.decoder.fc.out_features
        
        # Encode
        encoder_output, encoder_hidden = self.encoder(src)
        
        # Initialize decoder
        decoder_input = tgt[:, 0:1]  # First token
        decoder_hidden = encoder_hidden
        outputs = []
        
        for t in range(1, tgt_len):
            decoder_output, decoder_hidden = self.decoder(decoder_input, decoder_hidden)
            outputs.append(decoder_output)
            
            # Teacher forcing
            if torch.rand(1).item() < teacher_forcing_ratio:
                decoder_input = tgt[:, t:t+1]
            else:
                decoder_input = decoder_output.argmax(dim=-1)
        
        return torch.cat(outputs, dim=1)
