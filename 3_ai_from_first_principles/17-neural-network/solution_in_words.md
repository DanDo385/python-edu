# Solution in Words: Training a Neural Network

## How to Think About This Problem

### Understanding the Complete System

Think of a neural network like a factory assembly line:
- Input comes in
- Goes through processing stations (layers)
- Output comes out
- We measure quality (loss)
- Adjust machines (weights) to improve

### Understanding Forward Pass

**What we're doing:** Computing predictions layer by layer.

**How to think about it:**
1. Input → multiply by weights → add bias
2. Apply activation (ReLU for hidden, sigmoid for output)
3. Repeat for next layer
4. Final output is prediction

### Understanding Backward Pass

**What we're doing:** Computing how each weight affects the loss.

**How to think about it:**
1. Start from loss
2. Compute gradient w.r.t. output
3. Propagate backward through each layer
4. Compute gradient for each weight
5. Update weights

### Understanding XOR Problem

**What we're doing:** Learning a non-linear pattern.

**How to think about it:**
- Linear model can't separate XOR
- Hidden layer creates non-linear transformation
- Network can learn the pattern!

### Problem-Solving Strategy

1. **Design architecture**: How many layers? How many neurons?
2. **Initialize weights**: Small random values
3. **Forward pass**: Compute predictions
4. **Compute loss**: How wrong are we?
5. **Backward pass**: How to improve?
6. **Update weights**: Move toward better values
7. **Repeat**: Until loss is low




