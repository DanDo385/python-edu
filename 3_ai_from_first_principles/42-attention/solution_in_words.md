# Solution Explanation: Attention Mechanisms

## Overview

Attention allows models to focus on relevant parts of input when producing output. It's the key innovation behind transformers.

## Key Concepts

### Scaled Dot-Product Attention

**Formula:**
```
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V
```

**Components:**
- Query (Q): What we're looking for
- Key (K): What we have
- Value (V): What we return

**Scaling:**
- Divide by sqrt(d_k) to prevent large dot products
- Stabilizes gradients

### Multi-Head Attention

- Multiple attention heads in parallel
- Each head learns different patterns
- Concatenate and project outputs
- Enables richer representations

## Implementation

Scaled dot-product attention computes attention weights and applies them to values. Multi-head attention runs multiple heads in parallel and combines them. This is the foundation for transformers!
