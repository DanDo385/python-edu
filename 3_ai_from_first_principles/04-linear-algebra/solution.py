"""
Project 18: Linear Algebra Essentials for ML - SOLUTION

Complete solution with detailed comments explaining how linear algebra
is the mathematical foundation of machine learning.
"""

import numpy as np


def dot_product(vec1, vec2):
    """
    Compute dot product of two vectors.
    
    The dot product is the fundamental operation in neural networks.
    When you compute a weighted sum (features × weights), you're computing
    a dot product. This is how neural networks make predictions!
    
    Mathematical definition:
    dot_product = sum(vec1[i] * vec2[i] for i in range(n))
    
    Geometric interpretation:
    - Measures how "aligned" two vectors are
    - If vectors point same direction → large positive value
    - If perpendicular → zero
    - If opposite → large negative value
    
    In ML context:
    - vec1 = input features [x1, x2, x3]
    - vec2 = weights [w1, w2, w3]
    - Result = weighted sum = x1*w1 + x2*w2 + x3*w3
    - This is exactly what a neuron computes!
    
    Time complexity: O(n) where n is vector length
    Space complexity: O(1)
    
    Args:
        vec1 (np.ndarray): First vector, shape (n,)
        vec2 (np.ndarray): Second vector, shape (n,)
    
    Returns:
        float: Dot product result
    
    Example:
        dot_product([1, 2, 3], [4, 5, 6])  # Returns 32
        # 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
    """
    # Use np.dot() for dot product
    # This is optimized C code, much faster than Python loop
    return np.dot(vec1, vec2)
    
    # Alternative: vec1 @ vec2 also works (matrix multiplication operator)
    # For 1D arrays, @ computes dot product
    # return vec1 @ vec2


def matrix_vector_multiply(matrix, vector):
    """
    Multiply a matrix by a vector.
    
    This is THE core operation in neural networks. Every layer performs:
    output = input @ weights + bias
    
    How it works:
    - Each row of the matrix represents weights for one output neuron
    - Matrix-vector multiplication computes all outputs simultaneously
    - This is how neural networks transform inputs to outputs
    
    Mathematical definition:
    result[i] = sum(matrix[i, j] * vector[j] for j in range(n))
    
    Shape rules:
    - matrix: (m, n) - m outputs, n inputs
    - vector: (n,) - n input features
    - result: (m,) - m output values
    
    In neural network context:
    - matrix = weight matrix (learned parameters)
    - vector = input features (one sample)
    - result = output activations (predictions)
    
    Time complexity: O(m*n)
    Space complexity: O(m) for result
    
    Args:
        matrix (np.ndarray): Matrix, shape (m, n)
        vector (np.ndarray): Vector, shape (n,)
    
    Returns:
        np.ndarray: Result vector, shape (m,)
    
    Example:
        matrix = [[1, 2],      vector = [5, 6]
                  [3, 4]]
        Result = [17, 39]  # [1*5+2*6, 3*5+4*6]
    """
    # Use @ operator for matrix-vector multiplication
    # This is the same as np.dot(matrix, vector) but more readable
    # In neural networks, this computes: input_features @ weights
    return matrix @ vector
    
    # This single line is doing what a neural network layer does!
    # Each row of matrix multiplies with vector to produce one output


def solve_linear_system(A, b):
    """
    Solve the linear system Ax = b for x.
    
    This finds the vector x such that A @ x = b.
    This is used in:
    - Least squares regression (finding optimal weights)
    - Optimization problems
    - Solving for parameters in closed-form solutions
    
    The system Ax = b has a unique solution if A is invertible (det(A) ≠ 0).
    NumPy uses optimized algorithms (LU decomposition) to solve efficiently.
    
    In ML context:
    - A = design matrix (features)
    - b = target values
    - x = optimal weights (what we're solving for)
    - This gives us the analytical solution to linear regression!
    
    Args:
        A (np.ndarray): Coefficient matrix, shape (n, n) - must be square
        b (np.ndarray): Right-hand side vector, shape (n,)
    
    Returns:
        np.ndarray: Solution vector x, shape (n,)
    
    Example:
        A = [[2, 1],    b = [5, 10]
             [1, 3]]
        Solve: 2x + y = 5, x + 3y = 10
        Solution: x = [1, 3] (approximately)
    """
    # np.linalg.solve() uses optimized algorithms to solve Ax = b
    # It's more numerically stable than computing A^(-1) @ b
    # Uses LU decomposition internally for efficiency
    return np.linalg.solve(A, b)
    
    # Note: A must be square and invertible
    # If not, you'll get a LinAlgError
    # For overdetermined systems (more equations than unknowns),
    # use least squares: np.linalg.lstsq()


def vector_projection(vec, onto):
    """
    Project vector onto another vector.
    
    Projection finds the component of vec that lies in the direction of onto.
    This is like finding the "shadow" of vec onto the line defined by onto.
    
    Mathematical formula:
    proj = (vec · onto / ||onto||²) * onto
    
    Where:
    - vec · onto = dot product
    - ||onto||² = squared magnitude (norm) of onto
    
    Used in:
    - Principal Component Analysis (PCA)
    - Feature extraction
    - Understanding vector relationships
    
    Args:
        vec (np.ndarray): Vector to project, shape (n,)
        onto (np.ndarray): Vector to project onto, shape (n,)
    
    Returns:
        np.ndarray: Projection vector, shape (n,)
    
    Example:
        vec = [3, 4]      onto = [1, 0]  (x-axis)
        Projection = [3, 0]  (x-component only)
    """
    # Compute dot product of vec and onto
    dot = np.dot(vec, onto)
    
    # Compute squared magnitude of onto
    # ||onto||² = onto · onto = sum(onto[i]²)
    onto_squared = np.dot(onto, onto)
    
    # Avoid division by zero
    if onto_squared == 0:
        return np.zeros_like(vec)
    
    # Compute scalar projection factor
    # This tells us how much of vec lies in direction of onto
    scalar = dot / onto_squared
    
    # Multiply onto by scalar to get projection vector
    # This gives us the component of vec in direction of onto
    projection = scalar * onto
    
    return projection


def compute_matrix_determinant(matrix):
    """
    Compute determinant of a square matrix.
    
    Determinant measures how a matrix transformation scales area/volume.
    - det(A) > 0: preserves orientation, scales by |det(A)|
    - det(A) < 0: reverses orientation, scales by |det(A)|
    - det(A) = 0: collapses to lower dimension (matrix is singular/non-invertible)
    
    Used in:
    - Checking if matrix is invertible (det ≠ 0)
    - Computing eigenvalues (characteristic polynomial)
    - Understanding transformations
    
    For 2×2 matrix: det([[a,b],[c,d]]) = ad - bc
    
    Args:
        matrix (np.ndarray): Square matrix, shape (n, n)
    
    Returns:
        float: Determinant value
    
    Example:
        matrix = [[1, 2],
                  [3, 4]]
        det = 1*4 - 2*3 = -2
    """
    # np.linalg.det() computes determinant using optimized algorithms
    # For small matrices, uses direct formula
    # For larger matrices, uses LU decomposition
    return np.linalg.det(matrix)


def compute_matrix_inverse(matrix):
    """
    Compute inverse of a square matrix.
    
    The inverse matrix A^(-1) satisfies: A @ A^(-1) = I (identity matrix)
    Only square matrices can have inverses, and only if det(A) ≠ 0.
    
    Used in:
    - Solving linear systems: x = A^(-1) @ b
    - Computing gradients in some optimization methods
    - Theoretical analysis
    
    Note: In practice, prefer np.linalg.solve() over computing inverse,
    as it's more numerically stable.
    
    Args:
        matrix (np.ndarray): Square matrix, shape (n, n)
                          Must be invertible (det ≠ 0)
    
    Returns:
        np.ndarray: Inverse matrix, shape (n, n)
    
    Example:
        matrix = [[2, 1],
                  [1, 1]]
        inverse = [[1, -1],
                   [-1, 2]]
        Verify: matrix @ inverse = identity
    """
    # np.linalg.inv() computes matrix inverse
    # Uses optimized algorithms (LU decomposition)
    # Raises LinAlgError if matrix is singular (not invertible)
    return np.linalg.inv(matrix)
    
    # Warning: Computing inverse can be numerically unstable
    # For solving Ax = b, prefer: np.linalg.solve(A, b)
    # It's faster and more accurate


def compute_eigenvalues_eigenvectors(matrix):
    """
    Compute eigenvalues and eigenvectors of a matrix.
    
    Eigenvectors are special vectors that don't change direction when
    the matrix is applied - they only get scaled by the eigenvalue.
    
    Mathematical definition:
    For eigenvector v and eigenvalue λ: A @ v = λ * v
    
    Eigenvectors point in "principal directions" of the transformation.
    Eigenvalues tell us how much scaling happens in those directions.
    
    Used in:
    - Principal Component Analysis (PCA) - find principal directions
    - Understanding matrix transformations
    - Dimensionality reduction
    - Spectral methods
    
    Args:
        matrix (np.ndarray): Square matrix, shape (n, n)
    
    Returns:
        tuple: (eigenvalues, eigenvectors)
               eigenvalues: 1D array of n eigenvalues
               eigenvectors: 2D array, shape (n, n)
                            Each column is an eigenvector
    
    Example:
        matrix = [[1, 0],    (diagonal matrix)
                  [0, 2]]
        eigenvalues = [1, 2]
        eigenvectors = [[1, 0],   (columns are eigenvectors)
                        [0, 1]]
    """
    # np.linalg.eig() computes eigenvalues and eigenvectors
    # Returns:
    # - eigenvalues: 1D array (may be complex)
    # - eigenvectors: 2D array where columns are eigenvectors
    eigenvals, eigenvecs = np.linalg.eig(matrix)
    
    return eigenvals, eigenvecs
    
    # Note: Eigenvalues may be complex numbers for some matrices
    # For real symmetric matrices, eigenvalues are always real
    # In PCA, we use np.linalg.eigh() for symmetric matrices (more efficient)




