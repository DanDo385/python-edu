"""
Project 18: Linear Algebra Essentials for ML

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""

import numpy as np


def dot_product(vec1, vec2):
    """
    Compute dot product of two vectors.
    
    Dot product: sum(vec1[i] * vec2[i] for all i)
    
    This is fundamental in ML: it's how we compute weighted sums
    (features × weights) in neural networks.
    
    Args:
        vec1 (np.ndarray): First vector, shape (n,)
        vec2 (np.ndarray): Second vector, shape (n,)
    
    Returns:
        float: Dot product result
    """
    # TODO: Compute dot product
    # Hint: Use np.dot() or vec1 @ vec2
    return None


def matrix_vector_multiply(matrix, vector):
    """
    Multiply a matrix by a vector.
    
    This is the core operation in neural networks!
    Each row of matrix represents weights for one output.
    
    Args:
        matrix (np.ndarray): Matrix, shape (m, n)
        vector (np.ndarray): Vector, shape (n,)
    
    Returns:
        np.ndarray: Result vector, shape (m,)
    """
    # TODO: Multiply matrix by vector
    # Hint: Use @ operator or np.dot()
    return None


def solve_linear_system(A, b):
    """
    Solve the linear system Ax = b for x.
    
    This finds x such that A @ x = b.
    Used in least squares, optimization, etc.
    
    Args:
        A (np.ndarray): Coefficient matrix, shape (n, n)
        b (np.ndarray): Right-hand side vector, shape (n,)
    
    Returns:
        np.ndarray: Solution vector x, shape (n,)
    """
    # TODO: Solve linear system
    # Hint: Use np.linalg.solve()
    return None


def vector_projection(vec, onto):
    """
    Project vector onto another vector.
    
    Projection finds the component of vec in the direction of onto.
    Formula: proj = (vec · onto / ||onto||²) * onto
    
    Args:
        vec (np.ndarray): Vector to project, shape (n,)
        onto (np.ndarray): Vector to project onto, shape (n,)
    
    Returns:
        np.ndarray: Projection vector, shape (n,)
    """
    # TODO: Compute vector projection
    # Hint: Use dot product and norm
    return None


def compute_matrix_determinant(matrix):
    """
    Compute determinant of a square matrix.
    
    Determinant measures how matrix transformation scales area/volume.
    Used in: checking invertibility, computing eigenvalues, etc.
    
    Args:
        matrix (np.ndarray): Square matrix, shape (n, n)
    
    Returns:
        float: Determinant value
    """
    # TODO: Compute determinant
    # Hint: Use np.linalg.det()
    return None


def compute_matrix_inverse(matrix):
    """
    Compute inverse of a square matrix.
    
    Inverse matrix A^(-1) satisfies: A @ A^(-1) = I (identity)
    Used in: solving systems, computing gradients, etc.
    
    Args:
        matrix (np.ndarray): Square matrix, shape (n, n)
    
    Returns:
        np.ndarray: Inverse matrix, shape (n, n)
    """
    # TODO: Compute matrix inverse
    # Hint: Use np.linalg.inv()
    # Note: Only works for invertible matrices
    return None


def compute_eigenvalues_eigenvectors(matrix):
    """
    Compute eigenvalues and eigenvectors of a matrix.
    
    Eigenvectors are directions that don't change when matrix is applied.
    Eigenvalues are scaling factors.
    
    Used in: PCA, understanding transformations, etc.
    
    Args:
        matrix (np.ndarray): Square matrix, shape (n, n)
    
    Returns:
        tuple: (eigenvalues, eigenvectors)
               eigenvalues: array of eigenvalues
               eigenvectors: matrix where columns are eigenvectors
    """
    # TODO: Compute eigenvalues and eigenvectors
    # Hint: Use np.linalg.eig()
    return None, None




