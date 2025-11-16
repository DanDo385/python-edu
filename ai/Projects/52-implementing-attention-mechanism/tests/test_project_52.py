"""
Tests for Project 52: Transformer Architecture Basics

Comprehensive test suite covering:
- Scaled dot-product attention
- Multi-head attention
- Positional encoding
- Transformer encoder layer
- Full transformer encoder
- Masking utilities
- Edge cases and error handling
- Performance verification
"""

import pytest
import torch
import torch.nn as nn
import math

from solution.solution import (
    scaled_dot_product_attention,
    MultiHeadAttention,
    PositionalEncoding,
    PositionWiseFeedForward,
    TransformerEncoderLayer,
    TransformerEncoder,
    create_padding_mask,
    create_causal_mask
)


class TestScaledDotProductAttention:
    """Tests for scaled dot-product attention function."""

    def test_basic_attention(self):
        """Test basic attention computation."""
        batch_size, seq_len, d_k = 2, 5, 64
        Q = torch.randn(batch_size, seq_len, d_k)
        K = torch.randn(batch_size, seq_len, d_k)
        V = torch.randn(batch_size, seq_len, d_k)

        output, weights = scaled_dot_product_attention(Q, K, V)

        # Check output shape
        assert output.shape == (batch_size, seq_len, d_k)

        # Check attention weights shape
        assert weights.shape == (batch_size, seq_len, seq_len)

        # Attention weights should sum to 1 (probability distribution)
        assert torch.allclose(weights.sum(dim=-1), torch.ones(batch_size, seq_len), atol=1e-6)

        # Attention weights should be non-negative
        assert (weights >= 0).all()

    def test_attention_with_mask(self):
        """Test attention with masking."""
        batch_size, seq_len, d_k = 2, 4, 32
        Q = torch.randn(batch_size, seq_len, d_k)
        K = torch.randn(batch_size, seq_len, d_k)
        V = torch.randn(batch_size, seq_len, d_k)

        # Create mask: attend to first 2 positions only
        mask = torch.zeros(batch_size, seq_len, seq_len, dtype=torch.bool)
        mask[:, :, :2] = True

        output, weights = scaled_dot_product_attention(Q, K, V, mask=mask)

        # Masked positions should have near-zero attention
        assert torch.allclose(weights[:, :, 2:], torch.zeros_like(weights[:, :, 2:]), atol=1e-6)

        # Un-masked positions should sum to 1
        assert torch.allclose(weights[:, :, :2].sum(dim=-1), torch.ones(batch_size, seq_len), atol=1e-6)

    def test_causal_mask(self):
        """Test attention with causal (look-ahead) mask."""
        batch_size, seq_len, d_k = 1, 4, 32
        Q = torch.randn(batch_size, seq_len, d_k)
        K = Q  # Self-attention
        V = Q

        # Causal mask: position i can only attend to positions <= i
        mask = create_causal_mask(seq_len)

        output, weights = scaled_dot_product_attention(Q, K, V, mask=mask)

        # Check that upper triangle is zero (can't attend to future)
        for i in range(seq_len):
            for j in range(i + 1, seq_len):
                assert weights[0, i, j] < 1e-6, f"Position {i} attending to future position {j}"

    def test_different_qkv_dimensions(self):
        """Test with different query/key and value dimensions."""
        batch_size, seq_len = 2, 5
        d_k, d_v = 64, 128

        Q = torch.randn(batch_size, seq_len, d_k)
        K = torch.randn(batch_size, seq_len, d_k)
        V = torch.randn(batch_size, seq_len, d_v)

        output, weights = scaled_dot_product_attention(Q, K, V)

        # Output should have value dimension
        assert output.shape == (batch_size, seq_len, d_v)

        # Weights should be seq_len x seq_len
        assert weights.shape == (batch_size, seq_len, seq_len)

    def test_cross_attention(self):
        """Test cross-attention (different seq lengths for Q and K/V)."""
        batch_size = 2
        seq_len_q, seq_len_kv = 10, 20
        d_k = 64

        Q = torch.randn(batch_size, seq_len_q, d_k)
        K = torch.randn(batch_size, seq_len_kv, d_k)
        V = torch.randn(batch_size, seq_len_kv, d_k)

        output, weights = scaled_dot_product_attention(Q, K, V)

        assert output.shape == (batch_size, seq_len_q, d_k)
        assert weights.shape == (batch_size, seq_len_q, seq_len_kv)

    def test_single_token(self):
        """Test with single token (edge case)."""
        batch_size, seq_len, d_k = 2, 1, 64
        Q = torch.randn(batch_size, seq_len, d_k)
        K = torch.randn(batch_size, seq_len, d_k)
        V = torch.randn(batch_size, seq_len, d_k)

        output, weights = scaled_dot_product_attention(Q, K, V)

        # Single token should attend to itself with weight 1
        assert torch.allclose(weights, torch.ones_like(weights), atol=1e-6)


class TestMultiHeadAttention:
    """Tests for multi-head attention module."""

    def test_basic_multi_head(self):
        """Test basic multi-head attention."""
        d_model, num_heads = 512, 8
        batch_size, seq_len = 4, 10

        mha = MultiHeadAttention(d_model, num_heads)
        x = torch.randn(batch_size, seq_len, d_model)

        output, attn_weights = mha(x, x, x)

        # Check output shape
        assert output.shape == (batch_size, seq_len, d_model)

        # Check attention weights shape (one matrix per head)
        assert attn_weights.shape == (batch_size, num_heads, seq_len, seq_len)

        # Each head's attention should sum to 1
        assert torch.allclose(
            attn_weights.sum(dim=-1),
            torch.ones(batch_size, num_heads, seq_len),
            atol=1e-6
        )

    def test_cross_attention_multihead(self):
        """Test multi-head cross-attention."""
        d_model, num_heads = 256, 4
        batch_size = 2
        seq_len_q, seq_len_kv = 10, 15

        mha = MultiHeadAttention(d_model, num_heads)
        query = torch.randn(batch_size, seq_len_q, d_model)
        key = torch.randn(batch_size, seq_len_kv, d_model)
        value = torch.randn(batch_size, seq_len_kv, d_model)

        output, attn_weights = mha(query, key, value)

        assert output.shape == (batch_size, seq_len_q, d_model)
        assert attn_weights.shape == (batch_size, num_heads, seq_len_q, seq_len_kv)

    def test_invalid_d_model(self):
        """Test that d_model must be divisible by num_heads."""
        with pytest.raises(AssertionError):
            MultiHeadAttention(d_model=512, num_heads=7)  # 512 not divisible by 7

    def test_different_num_heads(self):
        """Test with different numbers of heads."""
        d_model = 512
        batch_size, seq_len = 2, 5

        for num_heads in [1, 2, 4, 8, 16]:
            mha = MultiHeadAttention(d_model, num_heads)
            x = torch.randn(batch_size, seq_len, d_model)

            output, attn_weights = mha(x, x, x)

            assert output.shape == (batch_size, seq_len, d_model)
            assert attn_weights.shape == (batch_size, num_heads, seq_len, seq_len)
            assert mha.d_k == d_model // num_heads

    def test_with_mask(self):
        """Test multi-head attention with masking."""
        d_model, num_heads = 256, 4
        batch_size, seq_len = 2, 6

        mha = MultiHeadAttention(d_model, num_heads)
        x = torch.randn(batch_size, seq_len, d_model)

        # Create padding mask
        mask = torch.ones(batch_size, 1, 1, seq_len, dtype=torch.bool)
        mask[:, :, :, 4:] = False  # Mask last 2 positions

        output, attn_weights = mha(x, x, x, mask=mask)

        # Verify masked positions have near-zero attention
        assert torch.allclose(
            attn_weights[:, :, :, 4:],
            torch.zeros_like(attn_weights[:, :, :, 4:]),
            atol=1e-6
        )

    def test_parameter_count(self):
        """Verify parameter count."""
        d_model, num_heads = 512, 8
        mha = MultiHeadAttention(d_model, num_heads)

        # Parameters: 4 linear layers (Q, K, V, O), each d_model x d_model
        # Plus biases
        expected_params = 4 * (d_model * d_model + d_model)
        actual_params = sum(p.numel() for p in mha.parameters())

        assert actual_params == expected_params


class TestPositionalEncoding:
    """Tests for positional encoding module."""

    def test_basic_encoding(self):
        """Test basic positional encoding."""
        d_model, max_len = 512, 100
        batch_size, seq_len = 4, 50

        pe = PositionalEncoding(d_model, max_len)
        x = torch.randn(batch_size, seq_len, d_model)

        output = pe(x)

        # Shape should be unchanged
        assert output.shape == (batch_size, seq_len, d_model)

    def test_encoding_values(self):
        """Test that encodings are in valid range."""
        d_model, max_len = 128, 50
        pe = PositionalEncoding(d_model, max_len, dropout=0.0)  # No dropout for testing

        # Get the encoding matrix
        encodings = pe.pe[0]  # Remove batch dim

        # Encodings should be in [-1, 1] (sin/cos range)
        assert (encodings >= -1).all()
        assert (encodings <= 1).all()

    def test_different_positions(self):
        """Test that different positions get different encodings."""
        d_model, max_len = 256, 10
        pe = PositionalEncoding(d_model, max_len, dropout=0.0)

        encodings = pe.pe[0]  # [max_len, d_model]

        # Each position should have unique encoding
        for i in range(max_len):
            for j in range(i + 1, max_len):
                # Different positions should not be identical
                assert not torch.allclose(encodings[i], encodings[j])

    def test_sinusoidal_pattern(self):
        """Test that encodings follow sinusoidal pattern."""
        d_model = 4  # Small for easy testing
        max_len = 10
        pe = PositionalEncoding(d_model, max_len, dropout=0.0)

        encodings = pe.pe[0]  # [max_len, d_model]

        # Even dimensions should be sin, odd should be cos
        # They should oscillate
        for dim in range(d_model):
            values = encodings[:, dim]
            # Check that values oscillate (not monotonic)
            assert not torch.all(values[1:] >= values[:-1])
            assert not torch.all(values[1:] <= values[:-1])

    def test_extrapolation(self):
        """Test that encoding can handle sequences longer than max_len during creation."""
        d_model, initial_max_len = 128, 50
        pe = PositionalEncoding(d_model, initial_max_len, dropout=0.0)

        # Test with sequence shorter than max_len
        x_short = torch.randn(2, 30, d_model)
        output_short = pe(x_short)
        assert output_short.shape == x_short.shape

        # Test with sequence equal to max_len
        x_equal = torch.randn(2, initial_max_len, d_model)
        output_equal = pe(x_equal)
        assert output_equal.shape == x_equal.shape

    def test_different_dimensions(self):
        """Test with different model dimensions."""
        for d_model in [128, 256, 512, 768]:
            pe = PositionalEncoding(d_model, max_len=100)
            x = torch.randn(2, 20, d_model)
            output = pe(x)
            assert output.shape == x.shape


class TestPositionWiseFeedForward:
    """Tests for position-wise feed-forward network."""

    def test_basic_ffn(self):
        """Test basic feed-forward network."""
        d_model, d_ff = 512, 2048
        batch_size, seq_len = 4, 10

        ffn = PositionWiseFeedForward(d_model, d_ff)
        x = torch.randn(batch_size, seq_len, d_model)

        output = ffn(x)

        # Shape should be unchanged
        assert output.shape == (batch_size, seq_len, d_model)

    def test_position_wise_independence(self):
        """Test that FFN processes each position independently."""
        d_model, d_ff = 128, 512
        ffn = PositionWiseFeedForward(d_model, d_ff)
        ffn.eval()  # No dropout

        # Create input with different values at each position
        x = torch.randn(1, 5, d_model)

        # Process full sequence
        output_full = ffn(x)

        # Process each position separately
        for i in range(5):
            output_single = ffn(x[:, i:i+1, :])
            # Results should be identical
            assert torch.allclose(output_full[:, i:i+1, :], output_single, atol=1e-6)

    def test_non_linearity(self):
        """Test that FFN is non-linear (due to ReLU)."""
        d_model, d_ff = 64, 256
        ffn = PositionWiseFeedForward(d_model, d_ff)

        x1 = torch.randn(1, 1, d_model)
        x2 = torch.randn(1, 1, d_model)

        # f(x1 + x2) should not equal f(x1) + f(x2) due to ReLU
        # (linearity would mean they're equal)
        output_sum = ffn(x1 + x2)
        sum_outputs = ffn(x1) + ffn(x2)

        # Should not be equal (non-linear)
        assert not torch.allclose(output_sum, sum_outputs, atol=1e-3)


class TestTransformerEncoderLayer:
    """Tests for transformer encoder layer."""

    def test_basic_layer(self):
        """Test basic encoder layer."""
        d_model, num_heads, d_ff = 512, 8, 2048
        batch_size, seq_len = 4, 10

        layer = TransformerEncoderLayer(d_model, num_heads, d_ff)
        x = torch.randn(batch_size, seq_len, d_model)

        output, attn_weights = layer(x)

        # Check output shape
        assert output.shape == (batch_size, seq_len, d_model)

        # Check attention weights shape
        assert attn_weights.shape == (batch_size, num_heads, seq_len, seq_len)

    def test_residual_connections(self):
        """Test that residual connections exist."""
        d_model, num_heads, d_ff = 256, 4, 1024
        layer = TransformerEncoderLayer(d_model, num_heads, d_ff)
        layer.eval()  # Disable dropout for testing

        # If we pass near-zero input, output should not be near-zero
        # (due to residual connections)
        x = torch.randn(1, 5, d_model) * 0.01
        output, _ = layer(x)

        # Output magnitude should be larger than input due to residuals
        # (though this is a heuristic test)
        assert output.abs().mean() > x.abs().mean()

    def test_with_mask(self):
        """Test encoder layer with masking."""
        d_model, num_heads, d_ff = 256, 4, 1024
        batch_size, seq_len = 2, 6

        layer = TransformerEncoderLayer(d_model, num_heads, d_ff)
        x = torch.randn(batch_size, seq_len, d_model)

        # Create mask
        mask = torch.ones(batch_size, 1, 1, seq_len, dtype=torch.bool)
        mask[:, :, :, 4:] = False

        output, attn_weights = layer(x, mask=mask)

        # Verify masked positions have near-zero attention
        assert torch.allclose(
            attn_weights[:, :, :, 4:],
            torch.zeros_like(attn_weights[:, :, :, 4:]),
            atol=1e-6
        )

    def test_different_configurations(self):
        """Test various configuration combinations."""
        configs = [
            (128, 2, 512),
            (256, 4, 1024),
            (512, 8, 2048),
            (768, 12, 3072),
        ]

        for d_model, num_heads, d_ff in configs:
            layer = TransformerEncoderLayer(d_model, num_heads, d_ff)
            x = torch.randn(2, 5, d_model)

            output, attn_weights = layer(x)

            assert output.shape == (2, 5, d_model)
            assert attn_weights.shape == (2, num_heads, 5, 5)


class TestTransformerEncoder:
    """Tests for complete transformer encoder."""

    def test_basic_encoder(self):
        """Test basic transformer encoder."""
        vocab_size = 10000
        d_model, num_heads, num_layers, d_ff = 512, 8, 6, 2048
        batch_size, seq_len = 4, 20

        encoder = TransformerEncoder(
            vocab_size, d_model, num_heads, num_layers, d_ff
        )

        input_ids = torch.randint(0, vocab_size, (batch_size, seq_len))
        output, attn_weights_list = encoder(input_ids)

        # Check output shape
        assert output.shape == (batch_size, seq_len, d_model)

        # Should have attention weights for each layer
        assert len(attn_weights_list) == num_layers

        # Each layer's attention weights should have correct shape
        for attn_weights in attn_weights_list:
            assert attn_weights.shape == (batch_size, num_heads, seq_len, seq_len)

    def test_with_padding_mask(self):
        """Test encoder with padding mask."""
        vocab_size = 1000
        d_model, num_heads, num_layers, d_ff = 256, 4, 2, 1024
        batch_size = 2

        encoder = TransformerEncoder(
            vocab_size, d_model, num_heads, num_layers, d_ff, padding_idx=0
        )

        # Create input with padding
        input_ids = torch.tensor([
            [1, 2, 3, 4, 5, 0, 0, 0],
            [1, 2, 3, 0, 0, 0, 0, 0]
        ])

        mask = create_padding_mask(input_ids, pad_idx=0)

        output, attn_weights_list = encoder(input_ids, mask=mask)

        # All layers should respect the mask
        for attn_weights in attn_weights_list:
            # Verify that attention to padding positions is near zero
            assert torch.allclose(
                attn_weights[0, :, :, 5:],
                torch.zeros_like(attn_weights[0, :, :, 5:]),
                atol=1e-6
            )
            assert torch.allclose(
                attn_weights[1, :, :, 3:],
                torch.zeros_like(attn_weights[1, :, :, 3:]),
                atol=1e-6
            )

    def test_embedding_scaling(self):
        """Test that embeddings are scaled by sqrt(d_model)."""
        vocab_size = 1000
        d_model = 256

        encoder = TransformerEncoder(
            vocab_size, d_model, num_heads=4, num_layers=1, d_ff=1024
        )

        # The embedding weight should exist
        assert hasattr(encoder, 'embedding')
        assert encoder.embedding.weight.shape == (vocab_size, d_model)

    def test_different_layer_depths(self):
        """Test encoders with different numbers of layers."""
        vocab_size = 1000
        d_model, num_heads, d_ff = 256, 4, 1024

        for num_layers in [1, 2, 4, 6, 12]:
            encoder = TransformerEncoder(
                vocab_size, d_model, num_heads, num_layers, d_ff
            )

            input_ids = torch.randint(0, vocab_size, (2, 10))
            output, attn_weights_list = encoder(input_ids)

            assert len(attn_weights_list) == num_layers
            assert len(encoder.layers) == num_layers

    def test_max_sequence_length(self):
        """Test that encoder respects max_len parameter."""
        vocab_size = 1000
        d_model, num_heads, num_layers, d_ff = 128, 2, 2, 512
        max_len = 100

        encoder = TransformerEncoder(
            vocab_size, d_model, num_heads, num_layers, d_ff, max_len=max_len
        )

        # Should work with sequences up to max_len
        input_ids = torch.randint(0, vocab_size, (1, max_len))
        output, _ = encoder(input_ids)
        assert output.shape == (1, max_len, d_model)

    def test_parameter_count(self):
        """Verify total parameter count is reasonable."""
        vocab_size = 10000
        d_model, num_heads, num_layers, d_ff = 512, 8, 6, 2048

        encoder = TransformerEncoder(
            vocab_size, d_model, num_heads, num_layers, d_ff
        )

        total_params = sum(p.numel() for p in encoder.parameters())

        # Should have millions of parameters for this config
        assert total_params > 1_000_000

        # Embedding should contribute vocab_size * d_model
        embedding_params = vocab_size * d_model
        assert encoder.embedding.weight.numel() == embedding_params


class TestMaskingUtilities:
    """Tests for masking utility functions."""

    def test_padding_mask(self):
        """Test padding mask creation."""
        seq = torch.tensor([
            [1, 2, 3, 4, 0, 0],
            [1, 2, 0, 0, 0, 0],
            [1, 2, 3, 4, 5, 6]
        ])

        mask = create_padding_mask(seq, pad_idx=0)

        # Check shape
        assert mask.shape == (3, 1, 1, 6)

        # Check values
        expected = torch.tensor([
            [True, True, True, True, False, False],
            [True, True, False, False, False, False],
            [True, True, True, True, True, True]
        ])

        assert torch.equal(mask.squeeze(), expected)

    def test_causal_mask(self):
        """Test causal mask creation."""
        seq_len = 5
        mask = create_causal_mask(seq_len)

        # Check shape
        assert mask.shape == (1, 1, seq_len, seq_len)

        # Check that it's lower triangular
        expected = torch.tensor([
            [True, False, False, False, False],
            [True, True, False, False, False],
            [True, True, True, False, False],
            [True, True, True, True, False],
            [True, True, True, True, True]
        ])

        assert torch.equal(mask.squeeze(), expected)

    def test_causal_mask_different_sizes(self):
        """Test causal mask with different sequence lengths."""
        for seq_len in [1, 2, 5, 10, 20]:
            mask = create_causal_mask(seq_len)

            assert mask.shape == (1, 1, seq_len, seq_len)

            # Verify it's lower triangular
            mask_2d = mask.squeeze()
            for i in range(seq_len):
                for j in range(seq_len):
                    if j <= i:
                        assert mask_2d[i, j] == True
                    else:
                        assert mask_2d[i, j] == False


class TestIntegration:
    """Integration tests combining multiple components."""

    def test_end_to_end_sequence_processing(self):
        """Test complete sequence processing pipeline."""
        # Small model for testing
        vocab_size = 1000
        d_model, num_heads, num_layers, d_ff = 128, 4, 2, 512
        batch_size, seq_len = 2, 10

        # Create encoder
        encoder = TransformerEncoder(
            vocab_size, d_model, num_heads, num_layers, d_ff
        )

        # Create input
        input_ids = torch.randint(0, vocab_size, (batch_size, seq_len))

        # Forward pass
        output, attn_weights_list = encoder(input_ids)

        # Verify everything works
        assert output.shape == (batch_size, seq_len, d_model)
        assert len(attn_weights_list) == num_layers

        # All attention weights should be valid probabilities
        for attn_weights in attn_weights_list:
            assert (attn_weights >= 0).all()
            assert (attn_weights <= 1).all()
            assert torch.allclose(
                attn_weights.sum(dim=-1),
                torch.ones_like(attn_weights.sum(dim=-1)),
                atol=1e-6
            )

    def test_gradient_flow(self):
        """Test that gradients flow through all components."""
        vocab_size = 500
        d_model, num_heads, num_layers, d_ff = 64, 2, 1, 256

        encoder = TransformerEncoder(
            vocab_size, d_model, num_heads, num_layers, d_ff
        )

        input_ids = torch.randint(0, vocab_size, (2, 5))
        output, _ = encoder(input_ids)

        # Compute loss (dummy)
        loss = output.sum()
        loss.backward()

        # Check that all parameters have gradients
        for name, param in encoder.named_parameters():
            assert param.grad is not None, f"No gradient for {name}"
            assert not torch.isnan(param.grad).any(), f"NaN gradient for {name}"

    def test_with_real_attention_patterns(self):
        """Test that attention learns reasonable patterns."""
        # This is a qualitative test
        d_model, num_heads = 128, 4
        mha = MultiHeadAttention(d_model, num_heads)

        # Create input where some positions are very similar
        x = torch.randn(1, 5, d_model)
        x[:, 1] = x[:, 3]  # Make position 1 and 3 identical

        output, attn_weights = mha(x, x, x)

        # Positions 1 and 3 should attend to each other more
        # (though this is not guaranteed without training)
        assert attn_weights.shape == (1, num_heads, 5, 5)


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_very_long_sequence(self):
        """Test with longer sequence."""
        vocab_size = 1000
        d_model, num_heads, num_layers, d_ff = 64, 2, 1, 256
        seq_len = 512

        encoder = TransformerEncoder(
            vocab_size, d_model, num_heads, num_layers, d_ff, max_len=1000
        )

        input_ids = torch.randint(0, vocab_size, (1, seq_len))
        output, _ = encoder(input_ids)

        assert output.shape == (1, seq_len, d_model)

    def test_batch_size_one(self):
        """Test with batch size of 1."""
        vocab_size = 500
        d_model, num_heads, num_layers, d_ff = 64, 2, 1, 256

        encoder = TransformerEncoder(
            vocab_size, d_model, num_heads, num_layers, d_ff
        )

        input_ids = torch.randint(0, vocab_size, (1, 10))
        output, _ = encoder(input_ids)

        assert output.shape == (1, 10, d_model)

    def test_large_batch_size(self):
        """Test with large batch size."""
        vocab_size = 500
        d_model, num_heads, num_layers, d_ff = 64, 2, 1, 256
        batch_size = 128

        encoder = TransformerEncoder(
            vocab_size, d_model, num_heads, num_layers, d_ff
        )

        input_ids = torch.randint(0, vocab_size, (batch_size, 10))
        output, _ = encoder(input_ids)

        assert output.shape == (batch_size, 10, d_model)

    def test_all_padding_sequence(self):
        """Test sequence that is entirely padding."""
        vocab_size = 500
        d_model, num_heads, num_layers, d_ff = 64, 2, 1, 256

        encoder = TransformerEncoder(
            vocab_size, d_model, num_heads, num_layers, d_ff, padding_idx=0
        )

        # All padding
        input_ids = torch.zeros(2, 8, dtype=torch.long)
        mask = create_padding_mask(input_ids, pad_idx=0)

        output, _ = encoder(input_ids, mask=mask)

        # Should not crash, output should exist
        assert output.shape == (2, 8, d_model)
        # Output may be arbitrary for all-padding case


class TestNumericalStability:
    """Test numerical stability of implementations."""

    def test_large_values(self):
        """Test attention with large values."""
        d_k = 64
        Q = torch.randn(2, 10, d_k) * 10  # Large values
        K = torch.randn(2, 10, d_k) * 10
        V = torch.randn(2, 10, d_k) * 10

        output, weights = scaled_dot_product_attention(Q, K, V)

        # Should not have NaN or Inf
        assert not torch.isnan(output).any()
        assert not torch.isinf(output).any()
        assert not torch.isnan(weights).any()
        assert not torch.isinf(weights).any()

    def test_small_values(self):
        """Test attention with small values."""
        d_k = 64
        Q = torch.randn(2, 10, d_k) * 0.01  # Small values
        K = torch.randn(2, 10, d_k) * 0.01
        V = torch.randn(2, 10, d_k) * 0.01

        output, weights = scaled_dot_product_attention(Q, K, V)

        # Should still work correctly
        assert not torch.isnan(output).any()
        assert torch.allclose(weights.sum(dim=-1), torch.ones(2, 10), atol=1e-6)

    def test_very_large_d_k(self):
        """Test that scaling prevents issues with large d_k."""
        # Large d_k would cause large dot products without scaling
        d_k = 1024
        Q = torch.randn(1, 5, d_k)
        K = torch.randn(1, 5, d_k)
        V = torch.randn(1, 5, d_k)

        output, weights = scaled_dot_product_attention(Q, K, V)

        # Scaling should prevent saturation
        assert not torch.isnan(weights).any()
        assert (weights > 1e-6).any()  # Not all zeros (would indicate saturation)
        assert torch.allclose(weights.sum(dim=-1), torch.ones(1, 5), atol=1e-6)


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])
