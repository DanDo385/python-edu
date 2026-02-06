# Solution in Words: Manual Backpropagation

## How to Think About This Problem

### Understanding Backpropagation

Think of backpropagation like retracing your steps backward, figuring out how each step contributed to the final result.

**Mental Model:**
```
Forward: Input → Layer1 → Layer2 → Output → Loss
Backward: Loss → Output → Layer2 → Layer1 → Input
         (compute how each layer contributed to loss)
```

### Understanding Chain Rule

**What we're doing:** Breaking down complex derivatives into simpler ones.

**How to think about it:**
- Loss depends on output
- Output depends on hidden layer
- Hidden layer depends on input
- To find dLoss/dinput, chain: dLoss/doutput * doutput/dhidden * dhidden/dinput

### Step-by-Step Thinking

1. **Forward pass**: Compute all values (save them!)
2. **Compute loss**: How wrong are we?
3. **Output layer gradient**: How does loss change with output?
4. **Hidden layer gradient**: Chain backward through activation
5. **Weight gradients**: How do weights affect loss?

### Problem-Solving Strategy

1. **Draw the computation graph**: Visualize data flow
2. **Forward pass**: Compute and save intermediate values
3. **Backward pass**: Start from loss, work backward
4. **Apply chain rule**: Multiply derivatives along the path
5. **Update weights**: Use gradients to improve




