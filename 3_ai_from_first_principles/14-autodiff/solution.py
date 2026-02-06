"""
Project 24: Building an Autodiff Engine from Scratch - SOLUTION

Complete solution with detailed comments explaining automatic differentiation,
computational graphs, and how frameworks like PyTorch work under the hood.
"""

import numpy as np


class Tensor:
    """
    A tensor with automatic differentiation support.
    
    This implements a simplified version of PyTorch's autograd system.
    The key idea: as we perform operations, we build a computation graph.
    When we call backward(), we traverse this graph to compute gradients.
    
    How it works:
    1. Operations create new tensors and store references to inputs
    2. This builds a directed acyclic graph (DAG)
    3. backward() traverses graph in reverse topological order
    4. At each node, applies chain rule to compute gradients
    
    Attributes:
        data: The tensor's value (number or numpy array)
        grad: Gradient w.r.t. this tensor (computed during backward)
        requires_grad: Whether to track gradients for this tensor
        _op: Operation that created this tensor (None for leaf nodes)
        _inputs: Tuple of input tensors (for graph traversal)
    """
    
    def __init__(self, data, requires_grad=False):
        """
        Initialize a tensor.
        
        Args:
            data: Value to store (number or numpy array)
            requires_grad (bool): Whether to track gradients
                                 If False, gradients won't be computed
        """
        # Store the actual value
        self.data = np.array(data) if not isinstance(data, np.ndarray) else data
        
        # Gradient will be computed during backward pass
        # Initialize to None (not computed yet)
        self.grad = None
        
        # Whether this tensor needs gradients
        self.requires_grad = requires_grad
        
        # Graph building: store operation and inputs
        # These are used during backward pass to traverse the graph
        self._op = None  # Operation that created this tensor
        self._inputs = None  # Input tensors to that operation
    
    def backward(self, grad=None):
        """
        Backward pass: compute gradients.
        
        This is the magic of autodiff! We traverse the computation graph
        backward, applying the chain rule at each step.
        
        Algorithm:
        1. If grad is None and this is output tensor, start with grad=1.0
        2. Accumulate gradient (add to existing grad if multiple paths)
        3. If this tensor was created by an operation, propagate gradient backward
        4. Recursively call backward on input tensors
        
        Args:
            grad: Upstream gradient (how loss changes w.r.t. this tensor)
                 If None and this is output, use 1.0 (dLoss/dLoss = 1)
        """
        # If no upstream gradient provided and this is output, start with 1.0
        # This represents dLoss/dLoss = 1 (the gradient of loss w.r.t. itself)
        if grad is None:
            grad = np.array(1.0)
        else:
            grad = np.array(grad)
        
        # Accumulate gradient
        # If multiple paths lead to this tensor, gradients sum
        # Initialize to 0 if first time, then add
        if self.grad is None:
            self.grad = np.zeros_like(self.data)
        self.grad += grad
        
        # If this tensor was created by an operation, propagate gradient backward
        if self._op is not None and self._inputs is not None:
            # Call operation's backward method to get gradients for inputs
            input_grads = self._op.backward(grad, *self._inputs)
            
            # Recursively call backward on input tensors
            # Only if they require gradients
            for input_tensor, input_grad in zip(self._inputs, input_grads):
                if input_tensor.requires_grad:
                    input_tensor.backward(input_grad)
    
    def __add__(self, other):
        """
        Addition operation: self + other
        
        This builds the computation graph automatically!
        When we do a + b, Python calls this method.
        """
        # Convert other to Tensor if it's not already
        if not isinstance(other, Tensor):
            other = Tensor(other, requires_grad=False)
        
        # Create result tensor
        result = Tensor(Add.forward(self.data, other.data))
        
        # Set requires_grad if either input requires it
        result.requires_grad = self.requires_grad or other.requires_grad
        
        # Store operation and inputs for backward pass
        result._op = Add
        result._inputs = (self, other)
        
        return result
    
    def __mul__(self, other):
        """
        Multiplication operation: self * other
        
        Similar to __add__, but for multiplication.
        """
        # Convert other to Tensor if needed
        if not isinstance(other, Tensor):
            other = Tensor(other, requires_grad=False)
        
        # Create result tensor
        result = Tensor(Mul.forward(self.data, other.data))
        
        # Set requires_grad
        result.requires_grad = self.requires_grad or other.requires_grad
        
        # Store operation and inputs
        result._op = Mul
        result._inputs = (self, other)
        
        return result


class Add:
    """
    Addition operation for autograd.
    
    This knows how to:
    - Compute forward: a + b
    - Compute backward: gradients for a and b
    """
    
    @staticmethod
    def forward(a, b):
        """
        Forward pass: a + b
        
        Args:
            a: First operand
            b: Second operand
        
        Returns:
            Sum of a and b
        """
        return a + b
    
    @staticmethod
    def backward(grad_output, a, b):
        """
        Backward pass: compute gradients for addition.
        
        For addition: z = a + b
        - dz/da = 1 (gradient flows through unchanged)
        - dz/db = 1 (gradient flows through unchanged)
        
        So: dLoss/da = dLoss/dz * dz/da = grad_output * 1
            dLoss/db = dLoss/dz * dz/db = grad_output * 1
        
        Args:
            grad_output: Gradient w.r.t. output (dLoss/dz)
            a: First input tensor
            b: Second input tensor
        
        Returns:
            tuple: (grad_a, grad_b) gradients for inputs
        """
        # Addition distributes gradient equally to both inputs
        # Each input gets the full upstream gradient
        return grad_output, grad_output


class Mul:
    """
    Multiplication operation for autograd.
    
    This knows how to:
    - Compute forward: a * b
    - Compute backward: gradients for a and b
    """
    
    @staticmethod
    def forward(a, b):
        """
        Forward pass: a * b
        
        Args:
            a: First operand
            b: Second operand
        
        Returns:
            Product of a and b
        """
        return a * b
    
    @staticmethod
    def backward(grad_output, a, b):
        """
        Backward pass: compute gradients for multiplication.
        
        For multiplication: z = a * b
        - dz/da = b (derivative w.r.t. a, treating b as constant)
        - dz/db = a (derivative w.r.t. b, treating a as constant)
        
        So: dLoss/da = dLoss/dz * dz/da = grad_output * b
            dLoss/db = dLoss/dz * dz/db = grad_output * a
        
        This is the product rule from calculus!
        
        Args:
            grad_output: Gradient w.r.t. output (dLoss/dz)
            a: First input tensor
            b: Second input tensor
        
        Returns:
            tuple: (grad_a, grad_b) gradients for inputs
        """
        # Product rule: d(a*b)/da = b, d(a*b)/db = a
        # Multiply upstream gradient by the "other" input
        grad_a = grad_output * b.data
        grad_b = grad_output * a.data
        
        return grad_a, grad_b
    
    # Example trace:
    # z = x * y, where x=2, y=3
    # Forward: z = 2 * 3 = 6
    # Backward (if grad_output = 1):
    #   grad_x = 1 * 3 = 3
    #   grad_y = 1 * 2 = 2
    # This matches: d(2*3)/d2 = 3, d(2*3)/d3 = 2




