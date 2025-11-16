"""
Project 52: Transformer Architecture Basics

This module implements the core components of the Transformer architecture
from "Attention is All You Need" (Vaswani et al., 2017).

Components implemented:
1. Scaled Dot-Product Attention
2. Multi-Head Attention
3. Positional Encoding
4. Transformer Encoder Layer
5. Full Transformer Encoder

Author: Python-Edu AI Curriculum
Mathematical Foundation: Vaswani et al., 2017
"""

import math
from typing import Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F


def scaled_dot_product_attention(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    mask: Optional[torch.Tensor] = None,
    dropout: Optional[nn.Dropout] = None
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Compute scaled dot-product attention.

    Mathematical Formulation:
        Attention(Q, K, V) = softmax(QK^T / √d_k) V

    Why it works:
        - QK^T computes similarity between all query-key pairs
        - Scaling by √d_k prevents gradient vanishing for large d_k
        - Softmax normalizes to get probability distribution
        - Weighted sum of values gives context-aware representation

    Args:
        query: Query tensor [batch_size, ..., seq_len, d_k]
               "What am I looking for?"
        key: Key tensor [batch_size, ..., seq_len, d_k]
             "What do I contain?"
        value: Value tensor [batch_size, ..., seq_len, d_v]
               "What information do I have?"
        mask: Optional mask tensor, shape broadcastable to attention scores
              True/1 for positions to attend, False/0 to mask out
        dropout: Optional dropout layer to apply to attention weights

    Returns:
        output: Attention output [batch_size, ..., seq_len, d_v]
        attention_weights: Attention weights [batch_size, ..., seq_len, seq_len]

    Example:
        >>> Q = torch.randn(2, 5, 64)  # batch=2, seq_len=5, d_k=64
        >>> K = torch.randn(2, 5, 64)
        >>> V = torch.randn(2, 5, 64)
        >>> output, weights = scaled_dot_product_attention(Q, K, V)
        >>> output.shape
        torch.Size([2, 5, 64])
        >>> weights.shape
        torch.Size([2, 5, 5])

    Complexity:
        Time: O(n²d) where n=seq_len, d=d_k
        Space: O(n²) for attention matrix
    """
    # Step 1: Get dimension of keys for scaling
    # Shape of query: [..., seq_len_q, d_k]
    d_k = query.size(-1)

    # Step 2: Compute attention scores (QK^T)
    # matmul: [..., seq_len_q, d_k] @ [..., d_k, seq_len_k] -> [..., seq_len_q, seq_len_k]
    scores = torch.matmul(query, key.transpose(-2, -1))

    # Step 3: Scale by √d_k
    # Why? For large d_k, dot products grow large in magnitude, pushing softmax
    # into regions with tiny gradients. Scaling keeps variance roughly 1.
    # Mathematical insight: If Q, K have mean 0, variance 1, then QK^T has variance d_k
    scores = scores / math.sqrt(d_k)

    # Step 4: Apply mask (if provided)
    # Mask out positions we don't want to attend to by setting them to -inf
    # After softmax, these become 0
    if mask is not None:
        # Convert boolean mask to float: True->0, False->-inf
        # Or use existing float mask and add -inf where mask is 0
        scores = scores.masked_fill(mask == 0, float('-inf'))

    # Step 5: Apply softmax to get attention weights
    # Softmax converts scores to probability distribution (sum to 1)
    # Shape: [..., seq_len_q, seq_len_k]
    attention_weights = F.softmax(scores, dim=-1)

    # Handle case where entire row is masked (would give NaN)
    # Replace NaN with 0
    attention_weights = torch.nan_to_num(attention_weights, nan=0.0)

    # Step 6: Apply dropout (if training)
    if dropout is not None:
        attention_weights = dropout(attention_weights)

    # Step 7: Compute weighted sum of values
    # matmul: [..., seq_len_q, seq_len_k] @ [..., seq_len_k, d_v] -> [..., seq_len_q, d_v]
    output = torch.matmul(attention_weights, value)

    return output, attention_weights


class MultiHeadAttention(nn.Module):
    """
    Multi-head attention mechanism.

    Key Insight: Instead of performing a single attention function,
    multi-head attention projects Q, K, V multiple times with different
    learned projections, performs attention in parallel, then combines.

    Mathematical Formulation:
        MultiHead(Q, K, V) = Concat(head_1, ..., head_h) W^O
        where head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)

    Why it works:
        - Different heads can attend to different aspects:
          * Head 1: syntactic relationships
          * Head 2: semantic relationships
          * Head 3: long-range dependencies
          * etc.
        - Increases model capacity without increasing sequence length costs
        - Allows model to jointly attend to information from different
          representation subspaces

    Architecture:
        Input: [batch, seq_len, d_model]

        1. Linear projections (separate for each head):
           Q = XW^Q -> [batch, seq_len, d_model]
           K = XW^K -> [batch, seq_len, d_model]
           V = XW^V -> [batch, seq_len, d_model]

        2. Split into heads:
           Reshape to [batch, num_heads, seq_len, d_k]
           where d_k = d_model / num_heads

        3. Apply attention to each head in parallel:
           For each head: Attention(Q_i, K_i, V_i)

        4. Concatenate heads:
           [batch, num_heads, seq_len, d_k] -> [batch, seq_len, d_model]

        5. Final linear projection:
           Output W^O -> [batch, seq_len, d_model]

    Args:
        d_model: Model dimension (e.g., 512)
        num_heads: Number of attention heads (e.g., 8)
        dropout: Dropout probability

    Attributes:
        d_k: Dimension per head (d_model // num_heads)
        W_q, W_k, W_v: Linear projections for queries, keys, values
        W_o: Output projection

    Example:
        >>> mha = MultiHeadAttention(d_model=512, num_heads=8)
        >>> x = torch.randn(32, 10, 512)  # batch=32, seq_len=10
        >>> output, attn_weights = mha(x, x, x)  # Self-attention
        >>> output.shape
        torch.Size([32, 10, 512])
        >>> attn_weights.shape
        torch.Size([32, 8, 10, 10])
    """

    def __init__(self, d_model: int, num_heads: int, dropout: float = 0.1):
        super().__init__()

        # Validate that d_model is divisible by num_heads
        assert d_model % num_heads == 0, \
            f"d_model ({d_model}) must be divisible by num_heads ({num_heads})"

        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads  # Dimension per head

        # Linear projections for Q, K, V
        # Note: We use a single linear layer for all heads, then split
        # This is more efficient than separate layers per head
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)

        # Output projection
        self.W_o = nn.Linear(d_model, d_model)

        # Dropout
        self.dropout = nn.Dropout(dropout)

        # Initialize weights
        self._reset_parameters()

    def _reset_parameters(self):
        """Initialize parameters using Xavier uniform initialization."""
        # Xavier initialization helps with gradient flow
        nn.init.xavier_uniform_(self.W_q.weight)
        nn.init.xavier_uniform_(self.W_k.weight)
        nn.init.xavier_uniform_(self.W_v.weight)
        nn.init.xavier_uniform_(self.W_o.weight)

    def _split_heads(self, x: torch.Tensor) -> torch.Tensor:
        """
        Split the last dimension into (num_heads, d_k).

        Args:
            x: [batch_size, seq_len, d_model]

        Returns:
            [batch_size, num_heads, seq_len, d_k]
        """
        batch_size, seq_len, d_model = x.size()

        # Reshape: [batch, seq_len, d_model] -> [batch, seq_len, num_heads, d_k]
        x = x.view(batch_size, seq_len, self.num_heads, self.d_k)

        # Transpose: [batch, seq_len, num_heads, d_k] -> [batch, num_heads, seq_len, d_k]
        # This puts heads in the second dimension for parallel attention computation
        return x.transpose(1, 2)

    def _combine_heads(self, x: torch.Tensor) -> torch.Tensor:
        """
        Inverse of split_heads.

        Args:
            x: [batch_size, num_heads, seq_len, d_k]

        Returns:
            [batch_size, seq_len, d_model]
        """
        batch_size, num_heads, seq_len, d_k = x.size()

        # Transpose: [batch, num_heads, seq_len, d_k] -> [batch, seq_len, num_heads, d_k]
        x = x.transpose(1, 2)

        # Reshape: [batch, seq_len, num_heads, d_k] -> [batch, seq_len, d_model]
        return x.contiguous().view(batch_size, seq_len, self.d_model)

    def forward(
        self,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        mask: Optional[torch.Tensor] = None
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Forward pass of multi-head attention.

        Args:
            query: Query tensor [batch_size, seq_len_q, d_model]
            key: Key tensor [batch_size, seq_len_k, d_model]
            value: Value tensor [batch_size, seq_len_v, d_model]
            mask: Optional mask [batch_size, 1, 1, seq_len] or
                  [batch_size, 1, seq_len, seq_len]
                  True/1 for positions to attend, False/0 to mask

        Returns:
            output: [batch_size, seq_len_q, d_model]
            attention_weights: [batch_size, num_heads, seq_len_q, seq_len_k]

        Note:
            For self-attention: query = key = value = x
            For cross-attention: query from decoder, key/value from encoder
        """
        batch_size = query.size(0)

        # Step 1: Linear projections
        # [batch, seq_len, d_model] -> [batch, seq_len, d_model]
        Q = self.W_q(query)
        K = self.W_k(key)
        V = self.W_v(value)

        # Step 2: Split into multiple heads
        # [batch, seq_len, d_model] -> [batch, num_heads, seq_len, d_k]
        Q = self._split_heads(Q)
        K = self._split_heads(K)
        V = self._split_heads(V)

        # Step 3: Apply scaled dot-product attention to all heads in parallel
        # Input: [batch, num_heads, seq_len, d_k]
        # Output: [batch, num_heads, seq_len, d_k]
        # Attention weights: [batch, num_heads, seq_len_q, seq_len_k]
        attended_values, attention_weights = scaled_dot_product_attention(
            Q, K, V, mask=mask, dropout=self.dropout
        )

        # Step 4: Concatenate heads
        # [batch, num_heads, seq_len, d_k] -> [batch, seq_len, d_model]
        concatenated = self._combine_heads(attended_values)

        # Step 5: Final linear projection
        # [batch, seq_len, d_model] -> [batch, seq_len, d_model]
        output = self.W_o(concatenated)

        return output, attention_weights


class PositionalEncoding(nn.Module):
    """
    Inject positional information using sinusoidal functions.

    Problem: Attention mechanism is permutation-invariant (order doesn't matter).
    But in sequences (sentences, time series), order is crucial!

    Solution: Add positional encodings to input embeddings.

    Mathematical Formulation:
        PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
        PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

    Where:
        - pos: Position in sequence (0, 1, 2, ...)
        - i: Dimension index (0, 1, ..., d_model-1)
        - 2i, 2i+1: Even and odd indices

    Why sinusoidal?
        1. Different frequencies for different dimensions
           - Low dimensions: slow oscillation (captures long-range structure)
           - High dimensions: fast oscillation (captures local structure)

        2. Extrapolation to longer sequences
           - Can handle sequences longer than seen during training

        3. Relative position encoding
           - PE(pos+k) can be expressed as linear function of PE(pos)
           - Allows model to learn to attend by relative positions

        4. Bounded values
           - Always in [-1, 1], prevents exploding values

    Visualization:
        - Each dimension is a sinusoid with different wavelength
        - Creates unique pattern for each position
        - Similar positions have similar encodings

    Alternative: Learned positional embeddings (BERT, GPT)
        - Pros: Can adapt to task
        - Cons: Fixed max length, no extrapolation

    Args:
        d_model: Model dimension (must be even for sin/cos pairing)
        max_len: Maximum sequence length to pre-compute
        dropout: Dropout probability to apply after adding PE

    Example:
        >>> pe = PositionalEncoding(d_model=512, max_len=1000)
        >>> embeddings = torch.randn(32, 50, 512)  # batch=32, seq_len=50
        >>> encoded = pe(embeddings)
        >>> encoded.shape
        torch.Size([32, 50, 512])
    """

    def __init__(self, d_model: int, max_len: int = 5000, dropout: float = 0.1):
        super().__init__()

        self.d_model = d_model
        self.dropout = nn.Dropout(p=dropout)

        # Create positional encoding matrix
        # Shape: [max_len, d_model]
        pe = torch.zeros(max_len, d_model)

        # Create position indices: [0, 1, 2, ..., max_len-1]
        # Shape: [max_len, 1]
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)

        # Create division term for scaling
        # div_term = 10000^(2i/d_model) for i in [0, d_model/2)
        #
        # Mathematical derivation:
        #   10000^(2i/d_model) = exp(log(10000) * 2i/d_model)
        #                      = exp(2i * log(10000)/d_model)
        #
        # We compute: exp(i * -log(10000) * 2/d_model) for efficiency
        div_term = torch.exp(
            torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model)
        )
        # Shape: [d_model/2]

        # Apply sin to even indices (0, 2, 4, ...)
        # position * div_term: [max_len, 1] * [d_model/2] -> [max_len, d_model/2]
        pe[:, 0::2] = torch.sin(position * div_term)

        # Apply cos to odd indices (1, 3, 5, ...)
        pe[:, 1::2] = torch.cos(position * div_term)

        # Add batch dimension: [max_len, d_model] -> [1, max_len, d_model]
        pe = pe.unsqueeze(0)

        # Register as buffer (not a parameter, but should be saved with model)
        # Buffers are moved to GPU with model, but not updated during training
        self.register_buffer('pe', pe)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Add positional encoding to input embeddings.

        Args:
            x: Input embeddings [batch_size, seq_len, d_model]

        Returns:
            x + positional_encoding [batch_size, seq_len, d_model]

        Note:
            We add (not concatenate) PE to embeddings.
            The model learns to use both token and position information.
        """
        # Get sequence length
        seq_len = x.size(1)

        # Add positional encoding (broadcasting over batch dimension)
        # self.pe[:, :seq_len]: [1, seq_len, d_model]
        # x: [batch_size, seq_len, d_model]
        # Result: [batch_size, seq_len, d_model]
        x = x + self.pe[:, :seq_len]

        # Apply dropout
        return self.dropout(x)


class PositionWiseFeedForward(nn.Module):
    """
    Position-wise feed-forward network (FFN).

    Architecture:
        FFN(x) = max(0, xW_1 + b_1)W_2 + b_2

        Or: Linear -> ReLU -> Linear

    Key Properties:
        1. Position-wise: Same network applied to each position independently
           - No interaction between positions (unlike attention)
           - Processes each token's representation separately

        2. Two-layer MLP with ReLU activation
           - Expansion: d_model -> d_ff (typically 4x larger)
           - Projection: d_ff -> d_model

        3. Adds non-linearity
           - Attention is largely linear (weighted sums)
           - FFN adds crucial non-linear transformations

    Why it works:
        - Attention gathers information from other positions
        - FFN processes this information with non-linear transformations
        - Together they form a powerful composition

    Args:
        d_model: Model dimension (e.g., 512)
        d_ff: Hidden dimension (e.g., 2048, typically 4*d_model)
        dropout: Dropout probability

    Example:
        >>> ffn = PositionWiseFeedForward(d_model=512, d_ff=2048)
        >>> x = torch.randn(32, 50, 512)
        >>> output = ffn(x)
        >>> output.shape
        torch.Size([32, 50, 512])
    """

    def __init__(self, d_model: int, d_ff: int, dropout: float = 0.1):
        super().__init__()

        # First linear layer: d_model -> d_ff
        self.linear1 = nn.Linear(d_model, d_ff)

        # Second linear layer: d_ff -> d_model
        self.linear2 = nn.Linear(d_ff, d_model)

        # Dropout
        self.dropout = nn.Dropout(dropout)

        # Initialize weights
        self._reset_parameters()

    def _reset_parameters(self):
        """Initialize parameters using Xavier uniform initialization."""
        nn.init.xavier_uniform_(self.linear1.weight)
        nn.init.xavier_uniform_(self.linear2.weight)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Forward pass.

        Args:
            x: Input [batch_size, seq_len, d_model]

        Returns:
            Output [batch_size, seq_len, d_model]
        """
        # First layer with ReLU activation
        # [batch, seq_len, d_model] -> [batch, seq_len, d_ff]
        x = self.linear1(x)
        x = F.relu(x)
        x = self.dropout(x)

        # Second layer
        # [batch, seq_len, d_ff] -> [batch, seq_len, d_model]
        x = self.linear2(x)

        return x


class TransformerEncoderLayer(nn.Module):
    """
    Single transformer encoder layer.

    Architecture:
        Input x
        ↓
        Multi-Head Self-Attention
        ↓
        Add & Norm (Residual + LayerNorm)
        ↓
        Feed-Forward Network
        ↓
        Add & Norm (Residual + LayerNorm)
        ↓
        Output

    Mathematical Formulation:
        # Attention block
        attn_output = MultiHeadAttention(x, x, x)
        x = LayerNorm(x + attn_output)  # Residual connection

        # Feed-forward block
        ff_output = FFN(x)
        x = LayerNorm(x + ff_output)     # Residual connection

    Key Components:

        1. Multi-Head Self-Attention:
           - Captures dependencies between all positions
           - "Self" means query, key, value all come from same sequence

        2. Residual Connections (x + sublayer(x)):
           - Enable gradient flow in deep networks
           - Allow model to learn identity function if needed
           - Combat vanishing gradients

        3. Layer Normalization:
           - Normalize across feature dimension for each example
           - Stabilizes training
           - Unlike BatchNorm, works well with variable sequence lengths

        4. Feed-Forward Network:
           - Adds non-linear transformations
           - Processes each position independently

    Why this architecture?
        - Attention: Gathers contextual information
        - FFN: Processes information with non-linearity
        - Residual: Enables deep stacking (BERT has 12-24 layers)
        - LayerNorm: Stabilizes training

    Args:
        d_model: Model dimension (e.g., 512)
        num_heads: Number of attention heads (e.g., 8)
        d_ff: Feed-forward hidden dimension (e.g., 2048)
        dropout: Dropout probability

    Example:
        >>> layer = TransformerEncoderLayer(d_model=512, num_heads=8, d_ff=2048)
        >>> x = torch.randn(32, 50, 512)
        >>> output, attn = layer(x)
        >>> output.shape
        torch.Size([32, 50, 512])
    """

    def __init__(
        self,
        d_model: int,
        num_heads: int,
        d_ff: int,
        dropout: float = 0.1
    ):
        super().__init__()

        # Multi-head self-attention
        self.self_attention = MultiHeadAttention(d_model, num_heads, dropout)

        # Feed-forward network
        self.feed_forward = PositionWiseFeedForward(d_model, d_ff, dropout)

        # Layer normalization (applied after residual connection)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)

        # Dropout for residual connections
        self.dropout1 = nn.Dropout(dropout)
        self.dropout2 = nn.Dropout(dropout)

    def forward(
        self,
        x: torch.Tensor,
        mask: Optional[torch.Tensor] = None
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Forward pass of encoder layer.

        Args:
            x: Input [batch_size, seq_len, d_model]
            mask: Optional attention mask
                  [batch_size, 1, 1, seq_len] or [batch_size, 1, seq_len, seq_len]

        Returns:
            output: [batch_size, seq_len, d_model]
            attention_weights: [batch_size, num_heads, seq_len, seq_len]
        """
        # Sublayer 1: Multi-head self-attention
        # Self-attention: query = key = value = x
        attn_output, attention_weights = self.self_attention(x, x, x, mask)

        # Add & Norm (residual connection + layer normalization)
        # Original paper: LayerNorm(x + Sublayer(x)) - "Post-LN"
        # Modern practice: x + Sublayer(LayerNorm(x)) - "Pre-LN" (better for deep networks)
        # We use Post-LN to match original paper
        x = self.norm1(x + self.dropout1(attn_output))

        # Sublayer 2: Feed-forward network
        ff_output = self.feed_forward(x)

        # Add & Norm
        x = self.norm2(x + self.dropout2(ff_output))

        return x, attention_weights


class TransformerEncoder(nn.Module):
    """
    Stack of N transformer encoder layers.

    Complete encoder architecture including:
        1. Token embeddings (vocabulary -> d_model)
        2. Positional encodings (inject position information)
        3. N encoder layers (stacked transformer layers)
        4. Optional final layer normalization

    This is the core of:
        - BERT (bidirectional encoder)
        - Encoder part of Transformer (for translation)
        - Many other models (RoBERTa, ELECTRA, etc.)

    Architecture:
        Input token IDs [batch, seq_len]
        ↓
        Token Embedding [batch, seq_len, d_model]
        ↓
        Positional Encoding (add position info)
        ↓
        Encoder Layer 1
        ↓
        Encoder Layer 2
        ↓
        ...
        ↓
        Encoder Layer N
        ↓
        Output [batch, seq_len, d_model]

    Applications:
        - Text classification: Pool output, add classifier head
        - Token classification: Use per-token outputs (NER, POS tagging)
        - Masked language modeling: Predict masked tokens (BERT pre-training)
        - Sequence-to-sequence: Use as encoder with decoder

    Args:
        vocab_size: Size of vocabulary
        d_model: Model dimension (e.g., 512)
        num_heads: Number of attention heads (e.g., 8)
        num_layers: Number of encoder layers (e.g., 6)
        d_ff: Feed-forward hidden dimension (e.g., 2048)
        max_len: Maximum sequence length
        dropout: Dropout probability

    Example:
        >>> encoder = TransformerEncoder(
        ...     vocab_size=10000,
        ...     d_model=512,
        ...     num_heads=8,
        ...     num_layers=6,
        ...     d_ff=2048
        ... )
        >>> input_ids = torch.randint(0, 10000, (32, 50))  # batch=32, seq_len=50
        >>> output, attn_weights = encoder(input_ids)
        >>> output.shape
        torch.Size([32, 50, 512])
        >>> len(attn_weights)  # One per layer
        6
    """

    def __init__(
        self,
        vocab_size: int,
        d_model: int,
        num_heads: int,
        num_layers: int,
        d_ff: int,
        max_len: int = 5000,
        dropout: float = 0.1,
        padding_idx: int = 0
    ):
        super().__init__()

        self.d_model = d_model

        # Token embedding layer
        # Maps token IDs to dense vectors
        self.embedding = nn.Embedding(vocab_size, d_model, padding_idx=padding_idx)

        # Positional encoding
        self.pos_encoding = PositionalEncoding(d_model, max_len, dropout)

        # Stack of encoder layers
        self.layers = nn.ModuleList([
            TransformerEncoderLayer(d_model, num_heads, d_ff, dropout)
            for _ in range(num_layers)
        ])

        # Final layer normalization (optional, used in some variants)
        self.norm = nn.LayerNorm(d_model)

        # Initialize embeddings
        self._reset_parameters()

    def _reset_parameters(self):
        """Initialize embedding weights."""
        # Initialize embeddings with normal distribution
        # Scale by 1/sqrt(d_model) as suggested in the paper
        nn.init.normal_(self.embedding.weight, mean=0, std=self.d_model**-0.5)

    def forward(
        self,
        x: torch.Tensor,
        mask: Optional[torch.Tensor] = None
    ) -> Tuple[torch.Tensor, list]:
        """
        Forward pass of transformer encoder.

        Args:
            x: Input token IDs [batch_size, seq_len]
            mask: Optional attention mask [batch_size, 1, 1, seq_len]
                  True/1 for real tokens, False/0 for padding

        Returns:
            output: Encoded representations [batch_size, seq_len, d_model]
            attention_weights: List of attention weights for each layer
                              Each: [batch_size, num_heads, seq_len, seq_len]
        """
        # Step 1: Token embedding
        # [batch, seq_len] -> [batch, seq_len, d_model]
        x = self.embedding(x)

        # Scale embeddings by sqrt(d_model)
        # Paper states this helps with training
        x = x * math.sqrt(self.d_model)

        # Step 2: Add positional encoding
        x = self.pos_encoding(x)

        # Step 3: Pass through encoder layers
        attention_weights_list = []

        for layer in self.layers:
            x, attention_weights = layer(x, mask)
            attention_weights_list.append(attention_weights)

        # Step 4: Final layer normalization
        x = self.norm(x)

        return x, attention_weights_list


# Utility functions for creating masks

def create_padding_mask(seq: torch.Tensor, pad_idx: int = 0) -> torch.Tensor:
    """
    Create mask for padding tokens.

    Args:
        seq: Input sequence [batch_size, seq_len]
        pad_idx: Padding token index

    Returns:
        Mask [batch_size, 1, 1, seq_len]
        True for real tokens, False for padding
    """
    # (seq != pad_idx): [batch, seq_len]
    # unsqueeze(1).unsqueeze(2): [batch, 1, 1, seq_len]
    return (seq != pad_idx).unsqueeze(1).unsqueeze(2)


def create_causal_mask(seq_len: int, device: torch.device = None) -> torch.Tensor:
    """
    Create causal (look-ahead) mask for decoder.

    Prevents positions from attending to subsequent positions.
    Used in autoregressive models (GPT, decoder, etc.)

    Args:
        seq_len: Sequence length
        device: Device to create mask on

    Returns:
        Mask [1, 1, seq_len, seq_len]
        Lower triangular matrix (True below diagonal, False above)

    Example:
        >>> create_causal_mask(4)
        tensor([[[[True, False, False, False],
                  [True,  True, False, False],
                  [True,  True,  True, False],
                  [True,  True,  True,  True]]]])
    """
    # Create lower triangular matrix
    mask = torch.tril(torch.ones(seq_len, seq_len, device=device)).bool()

    # Add batch and head dimensions
    return mask.unsqueeze(0).unsqueeze(0)


# Example usage and demonstration
if __name__ == "__main__":
    print("=" * 70)
    print("Transformer Architecture Basics - Component Demonstrations")
    print("=" * 70)

    # Set random seed for reproducibility
    torch.manual_seed(42)

    # Demo 1: Scaled Dot-Product Attention
    print("\n1. Scaled Dot-Product Attention")
    print("-" * 70)
    Q = torch.randn(2, 5, 64)  # batch=2, seq_len=5, d_k=64
    K = torch.randn(2, 5, 64)
    V = torch.randn(2, 5, 64)
    output, weights = scaled_dot_product_attention(Q, K, V)
    print(f"Input shape: {Q.shape}")
    print(f"Output shape: {output.shape}")
    print(f"Attention weights shape: {weights.shape}")
    print(f"Attention weights sum (should be ~1.0): {weights[0, 0].sum().item():.4f}")

    # Demo 2: Multi-Head Attention
    print("\n2. Multi-Head Attention")
    print("-" * 70)
    d_model, num_heads = 512, 8
    mha = MultiHeadAttention(d_model, num_heads)
    x = torch.randn(4, 10, d_model)  # batch=4, seq_len=10
    output, attn_weights = mha(x, x, x)
    print(f"Input shape: {x.shape}")
    print(f"Output shape: {output.shape}")
    print(f"Attention weights shape: {attn_weights.shape}")
    print(f"Number of parameters: {sum(p.numel() for p in mha.parameters()):,}")

    # Demo 3: Positional Encoding
    print("\n3. Positional Encoding")
    print("-" * 70)
    pe = PositionalEncoding(d_model=512, max_len=100)
    embeddings = torch.randn(4, 50, 512)
    encoded = pe(embeddings)
    print(f"Input shape: {embeddings.shape}")
    print(f"Output shape: {encoded.shape}")
    print(f"Positional encoding matrix shape: {pe.pe.shape}")

    # Demo 4: Transformer Encoder Layer
    print("\n4. Transformer Encoder Layer")
    print("-" * 70)
    layer = TransformerEncoderLayer(d_model=512, num_heads=8, d_ff=2048)
    x = torch.randn(4, 50, 512)
    output, attn = layer(x)
    print(f"Input shape: {x.shape}")
    print(f"Output shape: {output.shape}")
    print(f"Attention weights shape: {attn.shape}")
    print(f"Number of parameters: {sum(p.numel() for p in layer.parameters()):,}")

    # Demo 5: Full Transformer Encoder
    print("\n5. Complete Transformer Encoder")
    print("-" * 70)
    encoder = TransformerEncoder(
        vocab_size=10000,
        d_model=512,
        num_heads=8,
        num_layers=6,
        d_ff=2048,
        max_len=512
    )
    input_ids = torch.randint(0, 10000, (4, 50))
    output, attn_weights = encoder(input_ids)
    print(f"Input shape: {input_ids.shape}")
    print(f"Output shape: {output.shape}")
    print(f"Number of layers: {len(attn_weights)}")
    print(f"Total parameters: {sum(p.numel() for p in encoder.parameters()):,}")

    # Demo 6: Masking
    print("\n6. Attention Masking")
    print("-" * 70)

    # Padding mask
    seq = torch.tensor([[1, 2, 3, 4, 0, 0], [1, 2, 0, 0, 0, 0]])
    padding_mask = create_padding_mask(seq, pad_idx=0)
    print(f"Sequence: {seq}")
    print(f"Padding mask shape: {padding_mask.shape}")
    print(f"Padding mask:\n{padding_mask[0, 0, 0]}")

    # Causal mask
    causal_mask = create_causal_mask(5)
    print(f"\nCausal mask shape: {causal_mask.shape}")
    print(f"Causal mask:\n{causal_mask[0, 0]}")

    print("\n" + "=" * 70)
    print("All components working correctly!")
    print("=" * 70)
