"""
Project 24: Building an Autodiff Engine from Scratch

Complete the class definitions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""

import numpy as np


class Tensor:
    """
    A tensor with automatic differentiation support.
    
    This is a simplified version of PyTorch's Tensor.
    It stores a value and can compute gradients automatically.
    
    Attributes:
        data: The tensor's value
        grad: Gradient (computed during backward pass)
        _op: Operation that created this tensor (for graph building)
        _inputs: Input tensors (for graph traversal)
    """
    
    def __init__(self, data, requires_grad=False):
        """
        Initialize a tensor.
        
        Args:
            data: Value to store (number or numpy array)
            requires_grad (bool): Whether to track gradients
        """
        # TODO: Store data, initialize grad to None, store requires_grad
        # TODO: Initialize _op and _inputs to None (for graph building)
        pass
    
    def backward(self, grad=None):
        """
        Backward pass: compute gradients.
        
        Traverses the computation graph backward, computing gradients.
        
        Args:
            grad: Upstream gradient (default 1.0 for leaf nodes)
        """
        # TODO: Implement backward pass
        # If grad is None and this is output, use 1.0
        # Accumulate gradient in self.grad
        # If _op exists, call its backward method
        pass
    
    def __add__(self, other):
        """Addition operation."""
        # TODO: Create new tensor, store operation info
        # Hint: Create Add operation
        return None
    
    def __mul__(self, other):
        """Multiplication operation."""
        # TODO: Create new tensor, store operation info
        # Hint: Create Mul operation
        return None


class Add:
    """Addition operation for autograd."""
    
    @staticmethod
    def forward(a, b):
        """Forward pass: a + b"""
        # TODO: Return a + b
        return None
    
    @staticmethod
    def backward(grad_output, a, b):
        """Backward pass: gradients for addition."""
        # TODO: Return gradients for a and b
        # Hint: Addition distributes gradient equally
        return None, None


class Mul:
    """Multiplication operation for autograd."""
    
    @staticmethod
    def forward(a, b):
        """Forward pass: a * b"""
        # TODO: Return a * b
        return None
    
    @staticmethod
    def backward(grad_output, a, b):
        """Backward pass: gradients for multiplication."""
        # TODO: Return gradients for a and b
        # Hint: d(a*b)/da = b, d(a*b)/db = a
        return None, None




