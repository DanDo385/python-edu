"""Test suite for Project 18: Linear Algebra"""
import pytest
import numpy as np
from exercise import (
    dot_product,
    matrix_vector_multiply,
    solve_linear_system,
    vector_projection,
    compute_matrix_determinant,
    compute_matrix_inverse,
    compute_eigenvalues_eigenvectors,
)


class TestDotProduct:
    """Test dot product computation."""
    
    def test_dot_product(self):
        vec1 = np.array([1, 2, 3])
        vec2 = np.array([4, 5, 6])
        result = dot_product(vec1, vec2)
        assert result == 32  # 1*4 + 2*5 + 3*6 = 32


class TestMatrixVectorMultiply:
    """Test matrix-vector multiplication."""
    
    def test_matrix_vector_multiply(self):
        matrix = np.array([[1, 2], [3, 4]])
        vector = np.array([5, 6])
        result = matrix_vector_multiply(matrix, vector)
        expected = np.array([17, 39])  # [1*5+2*6, 3*5+4*6]
        assert np.allclose(result, expected)


class TestLinearSystems:
    """Test solving linear systems."""
    
    def test_solve_linear_system(self):
        A = np.array([[2, 1], [1, 3]])
        b = np.array([5, 10])
        x = solve_linear_system(A, b)
        # Verify solution: A @ x should equal b
        assert np.allclose(A @ x, b)


class TestVectorProjection:
    """Test vector projection."""
    
    def test_vector_projection(self):
        vec = np.array([3, 4])
        onto = np.array([1, 0])  # Unit vector along x-axis
        proj = vector_projection(vec, onto)
        # Projection should be [3, 0] (x-component only)
        assert np.allclose(proj, [3, 0])


class TestMatrixProperties:
    """Test matrix properties."""
    
    def test_determinant(self):
        matrix = np.array([[1, 2], [3, 4]])
        det = compute_matrix_determinant(matrix)
        assert abs(det - (-2.0)) < 0.001  # 1*4 - 2*3 = -2
    
    def test_inverse(self):
        matrix = np.array([[2, 1], [1, 1]])
        inv = compute_matrix_inverse(matrix)
        # Verify: matrix @ inv should be identity
        identity = matrix @ inv
        assert np.allclose(identity, np.eye(2))


class TestEigenvalues:
    """Test eigenvalue/eigenvector computation."""
    
    def test_eigenvalues_eigenvectors(self):
        matrix = np.array([[1, 0], [0, 2]])  # Diagonal matrix
        eigenvals, eigenvecs = compute_eigenvalues_eigenvectors(matrix)
        # Eigenvalues should be 1 and 2
        assert len(eigenvals) == 2
        assert 1 in eigenvals or 2 in eigenvals




