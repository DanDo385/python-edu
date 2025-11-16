# Project 52: Transformer Architecture Basics

## Overview

This project implements the foundational components of the Transformer architecture from the groundbreaking paper "Attention is All You Need" (Vaswani et al., 2017). You'll build self-attention mechanisms, multi-head attention, positional encodings, and a complete transformer encoder layer from scratch using PyTorch.

The Transformer architecture revolutionized NLP and deep learning by replacing recurrence and convolution with pure attention mechanisms, enabling:
- Parallel processing of sequences (vs sequential RNNs)
- Better handling of long-range dependencies
- State-of-the-art performance on language tasks
- Foundation for GPT, BERT, T5, and modern LLMs

## Learning Objectives

- Understand the self-attention mechanism and its mathematical foundations
- Implement scaled dot-product attention from scratch
- Build multi-head attention for learning diverse representations
- Create positional encodings to inject sequence order information
- Construct a complete transformer encoder layer
- Visualize attention patterns and learned representations
- Apply transformers to real NLP tasks

## Theory

### Self-Attention Mechanism

**Core Idea**: Each position in a sequence attends to all positions to compute its representation.

**Mathematical Formulation**:
```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

Where:
- **Q** (Query): "What am I looking for?"
- **K** (Key): "What do I contain?"
- **V** (Value): "What information do I have?"
- **d_k**: Dimension of key vectors (scaling factor)

**Steps**:
1. Compute attention scores: `scores = QK^T / √d_k`
2. Apply softmax to get attention weights: `weights = softmax(scores)`
3. Weighted sum of values: `output = weights @ V`

**Why Scaling?**: Division by √d_k prevents dot products from growing too large, which would push softmax into regions with tiny gradients.

### Multi-Head Attention

Instead of single attention, use multiple "heads" in parallel:

```
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) W^O

where head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)
```

**Benefits**:
- Different heads learn different types of relationships
- Head 1 might learn syntax, Head 2 semantics, Head 3 long-range deps
- Increases model capacity without increasing sequence length costs

**Parameters**:
- `h` heads, each with dimension `d_k = d_model / h`
- Projection matrices: `W^Q, W^K, W^V ∈ R^(d_model × d_k)` per head
- Output projection: `W^O ∈ R^(d_model × d_model)`

### Positional Encoding

**Problem**: Attention has no notion of position/order (permutation invariant).

**Solution**: Add positional encodings to embeddings.

**Sinusoidal Encoding** (original paper):
```
PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
```

**Properties**:
- Different frequency for each dimension
- Allows extrapolation to longer sequences
- Encodes relative positions: PE(pos+k) is a linear function of PE(pos)

**Alternative**: Learned positional embeddings (used in BERT, GPT)

### Transformer Encoder Layer

Complete encoder layer with:

```
1. Multi-head self-attention
2. Add & Norm (residual connection + layer normalization)
3. Feed-forward network (2-layer MLP)
4. Add & Norm
```

**Full Equation**:
```python
# Attention block
attn_output = MultiHeadAttention(x, x, x)
x = LayerNorm(x + attn_output)  # Residual + norm

# Feed-forward block
ff_output = FFN(x)  # FFN(x) = max(0, xW1 + b1)W2 + b2
x = LayerNorm(x + ff_output)    # Residual + norm
```

**Key Components**:
- **Residual Connections**: Enable gradient flow in deep networks
- **Layer Normalization**: Stabilize training
- **Feed-Forward Network**: Position-wise (same network applied to each position independently)

## Problems

Implement the following components in `solution/solution.py`:

### Problem 1: Scaled Dot-Product Attention (Medium)

```python
def scaled_dot_product_attention(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    mask: Optional[torch.Tensor] = None
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Compute scaled dot-product attention.

    Args:
        query: Query tensor [batch_size, seq_len, d_k]
        key: Key tensor [batch_size, seq_len, d_k]
        value: Value tensor [batch_size, seq_len, d_v]
        mask: Optional mask [batch_size, seq_len, seq_len]
              (1 for positions to attend, 0 to mask)

    Returns:
        output: Attention output [batch_size, seq_len, d_v]
        attention_weights: Attention weights [batch_size, seq_len, seq_len]

    Mathematical Steps:
        1. scores = (Q @ K^T) / √d_k
        2. Apply mask if provided (set masked positions to -inf)
        3. weights = softmax(scores)
        4. output = weights @ V
    """
```

**Examples**:
```python
# Simple attention example
Q = torch.randn(2, 5, 64)  # 2 sequences, 5 tokens, 64 dims
K = torch.randn(2, 5, 64)
V = torch.randn(2, 5, 64)
output, weights = scaled_dot_product_attention(Q, K, V)
# output.shape: [2, 5, 64]
# weights.shape: [2, 5, 5] - each token attends to all tokens
```

### Problem 2: Multi-Head Attention (Hard)

```python
class MultiHeadAttention(nn.Module):
    """
    Multi-head attention mechanism.

    Args:
        d_model: Model dimension (e.g., 512)
        num_heads: Number of attention heads (e.g., 8)
        dropout: Dropout probability

    Attributes:
        d_k: Dimension per head (d_model // num_heads)
        W_q, W_k, W_v: Linear projections for Q, K, V
        W_o: Output projection

    Forward Pass:
        1. Linear projections: Q = XW_q, K = XW_k, V = XW_v
        2. Split into heads: reshape to [batch, num_heads, seq_len, d_k]
        3. Apply attention to each head in parallel
        4. Concatenate heads
        5. Final linear projection
    """

    def __init__(self, d_model: int, num_heads: int, dropout: float = 0.1):
        pass

    def forward(
        self,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        mask: Optional[torch.Tensor] = None
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Args:
            query, key, value: [batch_size, seq_len, d_model]
            mask: Optional [batch_size, 1, 1, seq_len] or [batch_size, 1, seq_len, seq_len]

        Returns:
            output: [batch_size, seq_len, d_model]
            attention_weights: [batch_size, num_heads, seq_len, seq_len]
        """
```

**Examples**:
```python
# Multi-head attention
mha = MultiHeadAttention(d_model=512, num_heads=8)
x = torch.randn(32, 10, 512)  # batch=32, seq_len=10, d_model=512
output, attn_weights = mha(x, x, x)  # Self-attention
# output.shape: [32, 10, 512]
# attn_weights.shape: [32, 8, 10, 10] - 8 heads, each 10x10 attention matrix
```

### Problem 3: Positional Encoding (Medium)

```python
class PositionalEncoding(nn.Module):
    """
    Inject positional information using sinusoidal functions.

    Args:
        d_model: Model dimension
        max_len: Maximum sequence length
        dropout: Dropout probability

    Encoding:
        PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
        PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

    Why this works:
        - Each dimension oscillates at different frequency
        - Allows model to easily learn to attend by relative positions
        - sin(α+β) = sin(α)cos(β) + cos(α)sin(β) enables linear interpolation
    """

    def __init__(self, d_model: int, max_len: int = 5000, dropout: float = 0.1):
        pass

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Input embeddings [batch_size, seq_len, d_model]

        Returns:
            x + positional_encoding: [batch_size, seq_len, d_model]
        """
```

**Examples**:
```python
# Positional encoding
pe = PositionalEncoding(d_model=512, max_len=1000)
embeddings = torch.randn(32, 50, 512)  # batch=32, seq_len=50
encoded = pe(embeddings)
# encoded.shape: [32, 50, 512] - same shape, with position info added
```

### Problem 4: Transformer Encoder Layer (Hard)

```python
class TransformerEncoderLayer(nn.Module):
    """
    Single transformer encoder layer with:
        1. Multi-head self-attention
        2. Add & Norm
        3. Position-wise feed-forward network
        4. Add & Norm

    Args:
        d_model: Model dimension (e.g., 512)
        num_heads: Number of attention heads (e.g., 8)
        d_ff: Feed-forward hidden dimension (e.g., 2048)
        dropout: Dropout probability

    Architecture:
        x -> [MultiHeadAttn + Residual + LayerNorm] -> [FFN + Residual + LayerNorm] -> output

    Feed-Forward Network:
        FFN(x) = max(0, xW1 + b1)W2 + b2
        Typically: d_model -> 4*d_model -> d_model
    """

    def __init__(
        self,
        d_model: int,
        num_heads: int,
        d_ff: int,
        dropout: float = 0.1
    ):
        pass

    def forward(
        self,
        x: torch.Tensor,
        mask: Optional[torch.Tensor] = None
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Args:
            x: Input [batch_size, seq_len, d_model]
            mask: Optional attention mask

        Returns:
            output: [batch_size, seq_len, d_model]
            attention_weights: [batch_size, num_heads, seq_len, seq_len]
        """
```

**Examples**:
```python
# Complete encoder layer
encoder_layer = TransformerEncoderLayer(d_model=512, num_heads=8, d_ff=2048)
x = torch.randn(32, 50, 512)
output, attn = encoder_layer(x)
# output.shape: [32, 50, 512]
```

### Problem 5: Simple Transformer Encoder (Hard)

```python
class TransformerEncoder(nn.Module):
    """
    Stack of N transformer encoder layers.

    Includes:
        - Token embeddings
        - Positional encodings
        - N encoder layers
        - Optional final layer norm

    This is the core of BERT-style models.
    """

    def __init__(
        self,
        vocab_size: int,
        d_model: int,
        num_heads: int,
        num_layers: int,
        d_ff: int,
        max_len: int = 5000,
        dropout: float = 0.1
    ):
        pass
```

## Applications in NLP

### 1. Machine Translation
- **Encoder**: Process source sentence
- **Decoder**: Generate target sentence with cross-attention to encoder

### 2. Language Modeling (GPT)
- Decoder-only architecture with causal masking
- Next token prediction
- Foundation for ChatGPT, GPT-4

### 3. Masked Language Modeling (BERT)
- Encoder-only architecture
- Bidirectional context
- Pre-training for downstream tasks (classification, NER, QA)

### 4. Text Classification
- Use encoder to get sequence representation
- Add classification head on top
- Sentiment analysis, topic classification, etc.

### 5. Named Entity Recognition (NER)
- Token-level classification
- Each position outputs entity tag

### 6. Question Answering
- Encode question + context
- Predict start and end positions of answer

## Mathematical Insights

### Why Attention Works

1. **Dynamic Weighting**: Each token gets custom representation based on context
2. **Long-Range Dependencies**: Direct connections between all positions (vs RNN's sequential path)
3. **Parallelization**: All positions computed simultaneously (vs RNN's sequential bottleneck)
4. **Interpretability**: Attention weights show what model focuses on

### Computational Complexity

For sequence length `n` and dimension `d`:

| Operation | Complexity | Memory |
|-----------|------------|--------|
| Self-Attention | O(n²d) | O(n²) |
| Feed-Forward | O(nd²) | O(nd) |
| RNN (for comparison) | O(nd²) | O(nd) |

**Key Insight**: Attention is O(n²) in sequence length (quadratic), which limits maximum context size. Modern variants (Linformer, Performer, FlashAttention) address this.

## Constraints

- Sequence lengths: 1 ≤ seq_len ≤ 512
- Model dimensions: d_model ∈ {128, 256, 512, 768, 1024}
- Number of heads must divide d_model evenly
- Feed-forward dimension typically: d_ff = 4 × d_model
- Vocabulary size: vocab_size ≤ 50,000

## Testing

Run comprehensive tests:

```bash
# Run all tests
pytest tests/test_project_52.py -v

# Run specific test class
pytest tests/test_project_52.py::TestScaledDotProductAttention -v

# Test with coverage
pytest tests/test_project_52.py --cov=solution --cov-report=html
```

Run the interactive notebook:

```bash
jupyter notebook solution/solution.ipynb
```

## Implementation Tips

1. **Batch First**: Use `[batch_size, seq_len, d_model]` convention consistently
2. **Masking**: Remember to handle padding masks and causal masks correctly
3. **Scaling**: Don't forget the √d_k scaling factor in attention
4. **Initialization**: Use Xavier/Glorot initialization for linear layers
5. **Testing**: Test with small dimensions first (d_model=64, seq_len=10)
6. **Debugging**: Visualize attention weights to understand what model learns
7. **Numerical Stability**: Use `torch.nn.functional.softmax` with dim parameter
8. **Gradients**: Check for vanishing/exploding gradients in deep stacks

## Visualization Ideas

1. **Attention Heatmaps**: Visualize attention weights as matrices
2. **Multi-Head Patterns**: See what different heads learn
3. **Positional Encodings**: Plot PE values across positions/dimensions
4. **Token Trajectories**: Track how representations change through layers
5. **Gradient Flow**: Verify residual connections help gradients

## References

### Essential Papers

1. **"Attention is All You Need"** (Vaswani et al., 2017)
   - Original Transformer paper
   - https://arxiv.org/abs/1706.03762

2. **"BERT: Pre-training of Deep Bidirectional Transformers"** (Devlin et al., 2018)
   - Encoder-only, bidirectional context
   - https://arxiv.org/abs/1810.04805

3. **"Language Models are Unsupervised Multitask Learners"** (GPT-2, Radford et al., 2019)
   - Decoder-only, autoregressive
   - https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf

4. **"The Illustrated Transformer"** (Jay Alammar)
   - Excellent visual guide
   - http://jalammar.github.io/illustrated-transformer/

### Additional Resources

- **Annotated Transformer**: http://nlp.seas.harvard.edu/annotated-transformer/
- **PyTorch Transformer Tutorial**: https://pytorch.org/tutorials/beginner/transformer_tutorial.html
- **Hugging Face Transformers**: https://huggingface.co/docs/transformers/

## Next Steps

After completing this project, you'll be ready for:

- **Project 53**: Building Transformer Block - Complete encoder/decoder
- **Project 54**: GPT-Style Language Model - Decoder-only architecture
- **Project 55**: Training Transformer from Scratch - Full training pipeline
- **Project 56**: Using Pre-trained Transformers - BERT, GPT-2 fine-tuning
- **Project 57**: BERT-Style Masked LM - Bidirectional pre-training

## Key Takeaways

1. **Attention is Universal**: The core mechanism behind modern NLP and beyond
2. **Parallelization Matters**: Transformers unlocked massive scale
3. **Position is Critical**: Must explicitly encode sequence order
4. **Multi-Head is Powerful**: Different heads capture different patterns
5. **Residuals Enable Depth**: Essential for training deep networks
6. **Simple but Effective**: Elegant mathematical formulation with huge impact

---

**Note**: This project focuses on understanding and implementing the core mechanisms. Production systems use optimized implementations (PyTorch's `nn.MultiheadAttention`, FlashAttention for efficiency). Understanding the fundamentals enables you to debug, customize, and innovate on these architectures.
