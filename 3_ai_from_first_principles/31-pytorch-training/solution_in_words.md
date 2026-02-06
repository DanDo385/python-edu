# Solution Explanation: Training PyTorch Model

## Overview

This project demonstrates the complete PyTorch training pipeline. It brings together tensors, autograd, modules, and training utilities into a working system.

## Key Concepts Explained

### The Training Loop

**Standard Pattern:**
```python
for epoch in range(epochs):
    for batch_x, batch_y in dataloader:
        optimizer.zero_grad()
        predictions = model(batch_x)
        loss = criterion(predictions, batch_y)
        loss.backward()
        optimizer.step()
```

**Key Steps:**
1. Zero gradients
2. Forward pass
3. Compute loss
4. Backward pass (autograd!)
5. Update weights

### DataLoader

**Purpose:**
- Automatic batching
- Shuffling
- Parallel data loading

**Usage:**
```python
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

for batch_x, batch_y in dataloader:
    # Process batch
```

### Optimizer

**Purpose:**
- Updates model weights
- Handles learning rate
- Manages gradient accumulation

**Usage:**
```python
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

optimizer.zero_grad()  # Zero gradients
loss.backward()        # Compute gradients
optimizer.step()       # Update weights
```

### Loss Function

**Purpose:**
- Measures model error
- Provides gradients for training

**Usage:**
```python
criterion = nn.CrossEntropyLoss()

loss = criterion(predictions, targets)
```

### Training vs Evaluation

**Training Mode:**
```python
model.train()  # Enable dropout, batch norm training
```

**Evaluation Mode:**
```python
model.eval()   # Disable dropout, batch norm eval
with torch.no_grad():  # Disable gradient tracking
    predictions = model(x)
```

## Implementation Details

### Complete Training Function

```python
def train_model(model, train_loader, val_loader, num_epochs, lr, device):
    model = model.to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    
    for epoch in range(num_epochs):
        # Train
        train_loss = train_one_epoch(...)
        
        # Evaluate
        val_loss, val_acc = evaluate_model(...)
        
        # Track history
        history['train_loss'].append(train_loss)
        history['val_loss'].append(val_loss)
        history['val_accuracy'].append(val_acc)
    
    return history
```

**Key Points:**
- Move model to device
- Define criterion and optimizer
- Train and evaluate each epoch
- Track metrics

### Training One Epoch

```python
def train_one_epoch(model, dataloader, criterion, optimizer, device):
    model.train()
    
    for batch_x, batch_y in dataloader:
        batch_x, batch_y = batch_x.to(device), batch_y.to(device)
        
        optimizer.zero_grad()
        predictions = model(batch_x)
        loss = criterion(predictions, batch_y)
        loss.backward()
        optimizer.step()
    
    return average_loss
```

**Key Points:**
- Set model to train mode
- Move data to device
- Standard training loop
- Return average loss

### Evaluation

```python
def evaluate_model(model, dataloader, criterion, device):
    model.eval()
    
    with torch.no_grad():
        for batch_x, batch_y in dataloader:
            predictions = model(batch_x)
            loss = criterion(predictions, batch_y)
            # Compute accuracy
    
    return avg_loss, accuracy
```

**Key Points:**
- Set model to eval mode
- Use `torch.no_grad()` context
- Compute loss and accuracy
- Return metrics

## Common Pitfalls

1. **Forgetting zero_grad()**: Gradients accumulate incorrectly
2. **Not setting train/eval mode**: Dropout/batch norm behave wrong
3. **Not moving to device**: Slow CPU training
4. **Wrong loss function**: CrossEntropyLoss for classification

## Real-World Application

**In Practice:**
- This is the standard PyTorch training pattern
- Used in all deep learning projects
- Works for any model architecture
- Scales to large datasets with DataLoader

**Next Steps:**
- Project 35: CNNs (same pattern!)
- All future projects use this training loop

## Why This Matters

This training pattern is **essential**:
- Standard in all PyTorch projects
- Much simpler than pure NumPy (Project 30)
- Industry standard approach
- Foundation for all deep learning

**Comparison to Project 30:**
- Project 30: Manual training in NumPy (educational)
- Project 34: PyTorch training (practical)
- Same concepts, but PyTorch handles details!

This project establishes the training pattern used in all PyTorch projects!
