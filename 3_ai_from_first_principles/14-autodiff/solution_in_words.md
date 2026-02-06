# Solution in Words: Building an Autodiff Engine

## How to Think About This Problem

### Understanding Autodiff

Think of autodiff like a GPS that remembers your route and can tell you how to get back, but for mathematical computations.

**Mental Model:**
```
Forward: Build graph as you compute
Backward: Trace back, computing gradients at each step
```

### Understanding Computational Graph

**What we're doing:** Recording how values were computed.

**How to think about it:**
- Each operation creates a node
- Nodes remember their inputs
- When we call backward(), we traverse nodes in reverse
- At each node, compute gradient using chain rule

### Step-by-Step Thinking

1. **Create Tensor**: Store value, initialize grad to None
2. **Operations**: Create new Tensor, remember operation and inputs
3. **Backward**: Start from result, work backward
4. **Chain rule**: Multiply gradients along the path
5. **Accumulate**: If multiple paths, sum gradients

### Problem-Solving Strategy

1. **Design Tensor class**: What information to store?
2. **Implement operations**: How to build graph?
3. **Implement backward**: How to traverse and compute?
4. **Test**: Verify gradients are correct




