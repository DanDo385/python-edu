"""
Tests for Project 34: Graph Representation

Comprehensive test suite covering:
- Adjacency List representation
- Adjacency Matrix representation
- Edge List representation
- Graph conversions
"""

import pytest
from solution.solution import (
    AdjacencyListGraph,
    AdjacencyMatrixGraph,
    EdgeListGraph,
    convert_adjacency_list_to_matrix,
    convert_adjacency_matrix_to_list,
    convert_to_edge_list,
)


class TestAdjacencyList:
    """Tests for AdjacencyListGraph class."""

    def test_initialization(self):
        """Test graph initialization."""
        g = AdjacencyListGraph(5)
        assert g.num_vertices == 5
        assert not g.directed
        assert len(g.adj_list) == 0

    def test_initialization_directed(self):
        """Test directed graph initialization."""
        g = AdjacencyListGraph(3, directed=True)
        assert g.directed

    def test_add_edge_undirected(self):
        """Test adding undirected edge."""
        g = AdjacencyListGraph(3)
        g.add_edge(0, 1, weight=5)
        assert g.has_edge(0, 1)
        assert g.has_edge(1, 0)

    def test_add_edge_directed(self):
        """Test adding directed edge."""
        g = AdjacencyListGraph(3, directed=True)
        g.add_edge(0, 1, weight=5)
        assert g.has_edge(0, 1)
        assert not g.has_edge(1, 0)

    def test_add_edge_with_weight(self):
        """Test adding weighted edge."""
        g = AdjacencyListGraph(3)
        g.add_edge(0, 1, weight=7)
        neighbors = g.get_neighbors(0)
        assert (1, 7) in neighbors

    def test_add_duplicate_edge(self):
        """Test adding duplicate edge updates weight."""
        g = AdjacencyListGraph(3)
        g.add_edge(0, 1, weight=5)
        g.add_edge(0, 1, weight=10)
        neighbors = g.get_neighbors(0)
        assert (1, 10) in neighbors
        assert len(neighbors) == 1

    def test_add_edge_invalid_vertex(self):
        """Test adding edge with invalid vertex raises error."""
        g = AdjacencyListGraph(3)
        with pytest.raises(ValueError):
            g.add_edge(0, 5)
        with pytest.raises(ValueError):
            g.add_edge(-1, 1)

    def test_remove_edge(self):
        """Test removing edge."""
        g = AdjacencyListGraph(3)
        g.add_edge(0, 1)
        g.remove_edge(0, 1)
        assert not g.has_edge(0, 1)
        assert not g.has_edge(1, 0)

    def test_remove_nonexistent_edge(self):
        """Test removing nonexistent edge doesn't error."""
        g = AdjacencyListGraph(3)
        g.remove_edge(0, 1)  # Should not raise error

    def test_get_neighbors(self):
        """Test getting neighbors."""
        g = AdjacencyListGraph(4)
        g.add_edge(0, 1, weight=5)
        g.add_edge(0, 2, weight=3)
        neighbors = g.get_neighbors(0)
        assert len(neighbors) == 2
        assert (1, 5) in neighbors
        assert (2, 3) in neighbors

    def test_get_neighbors_empty(self):
        """Test getting neighbors of isolated vertex."""
        g = AdjacencyListGraph(3)
        neighbors = g.get_neighbors(0)
        assert len(neighbors) == 0

    def test_get_neighbors_invalid_vertex(self):
        """Test getting neighbors of invalid vertex raises error."""
        g = AdjacencyListGraph(3)
        with pytest.raises(ValueError):
            g.get_neighbors(5)

    def test_has_edge(self):
        """Test checking edge existence."""
        g = AdjacencyListGraph(3)
        g.add_edge(0, 1)
        assert g.has_edge(0, 1)
        assert not g.has_edge(0, 2)

    def test_has_edge_invalid_vertex(self):
        """Test has_edge with invalid vertex returns False."""
        g = AdjacencyListGraph(3)
        assert not g.has_edge(0, 5)
        assert not g.has_edge(-1, 1)

    def test_get_degree(self):
        """Test getting vertex degree."""
        g = AdjacencyListGraph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        assert g.get_degree(0) == 3
        assert g.get_degree(1) == 1

    def test_get_degree_isolated_vertex(self):
        """Test degree of isolated vertex is 0."""
        g = AdjacencyListGraph(3)
        assert g.get_degree(0) == 0

    def test_get_degree_invalid_vertex(self):
        """Test getting degree of invalid vertex raises error."""
        g = AdjacencyListGraph(3)
        with pytest.raises(ValueError):
            g.get_degree(5)

    def test_complex_graph(self):
        """Test more complex graph structure."""
        g = AdjacencyListGraph(5)
        g.add_edge(0, 1, weight=2)
        g.add_edge(0, 2, weight=4)
        g.add_edge(1, 3, weight=7)
        g.add_edge(2, 3, weight=3)
        g.add_edge(3, 4, weight=1)

        assert g.get_degree(3) == 3
        assert len(g.get_neighbors(0)) == 2
        assert g.has_edge(3, 4)


class TestAdjacencyMatrix:
    """Tests for AdjacencyMatrixGraph class."""

    def test_initialization(self):
        """Test graph initialization."""
        g = AdjacencyMatrixGraph(3)
        assert g.num_vertices == 3
        assert not g.directed
        assert len(g.matrix) == 3
        assert all(len(row) == 3 for row in g.matrix)

    def test_add_edge_undirected(self):
        """Test adding undirected edge."""
        g = AdjacencyMatrixGraph(3)
        g.add_edge(0, 1, weight=5)
        assert g.matrix[0][1] == 5
        assert g.matrix[1][0] == 5

    def test_add_edge_directed(self):
        """Test adding directed edge."""
        g = AdjacencyMatrixGraph(3, directed=True)
        g.add_edge(0, 1, weight=5)
        assert g.matrix[0][1] == 5
        assert g.matrix[1][0] == 0

    def test_add_edge_invalid_vertex(self):
        """Test adding edge with invalid vertex raises error."""
        g = AdjacencyMatrixGraph(3)
        with pytest.raises(ValueError):
            g.add_edge(0, 5)

    def test_remove_edge(self):
        """Test removing edge."""
        g = AdjacencyMatrixGraph(3)
        g.add_edge(0, 1, weight=5)
        g.remove_edge(0, 1)
        assert g.matrix[0][1] == 0
        assert g.matrix[1][0] == 0

    def test_get_neighbors(self):
        """Test getting neighbors."""
        g = AdjacencyMatrixGraph(4)
        g.add_edge(0, 1, weight=5)
        g.add_edge(0, 2, weight=3)
        neighbors = g.get_neighbors(0)
        assert len(neighbors) == 2
        assert (1, 5) in neighbors
        assert (2, 3) in neighbors

    def test_get_neighbors_invalid_vertex(self):
        """Test getting neighbors of invalid vertex raises error."""
        g = AdjacencyMatrixGraph(3)
        with pytest.raises(ValueError):
            g.get_neighbors(5)

    def test_has_edge(self):
        """Test checking edge existence."""
        g = AdjacencyMatrixGraph(3)
        g.add_edge(0, 1, weight=5)
        assert g.has_edge(0, 1)
        assert not g.has_edge(0, 2)

    def test_has_edge_fast_lookup(self):
        """Test O(1) edge lookup."""
        g = AdjacencyMatrixGraph(100)
        g.add_edge(50, 75, weight=10)
        assert g.has_edge(50, 75)

    def test_get_degree(self):
        """Test getting vertex degree."""
        g = AdjacencyMatrixGraph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        assert g.get_degree(0) == 3


class TestEdgeList:
    """Tests for EdgeListGraph class."""

    def test_initialization(self):
        """Test graph initialization."""
        g = EdgeListGraph(5)
        assert g.num_vertices == 5
        assert not g.directed
        assert len(g.edges) == 0

    def test_add_edge_undirected(self):
        """Test adding undirected edge (normalized)."""
        g = EdgeListGraph(3)
        g.add_edge(1, 0, weight=5)  # Should normalize to (0, 1, 5)
        assert (0, 1, 5) in g.edges

    def test_add_edge_directed(self):
        """Test adding directed edge (not normalized)."""
        g = EdgeListGraph(3, directed=True)
        g.add_edge(1, 0, weight=5)
        assert (1, 0, 5) in g.edges

    def test_add_edge_invalid_vertex(self):
        """Test adding edge with invalid vertex raises error."""
        g = EdgeListGraph(3)
        with pytest.raises(ValueError):
            g.add_edge(0, 5)

    def test_add_duplicate_edge(self):
        """Test adding duplicate edge updates weight."""
        g = EdgeListGraph(3)
        g.add_edge(0, 1, weight=5)
        g.add_edge(0, 1, weight=10)
        assert (0, 1, 10) in g.edges
        assert len(g.edges) == 1

    def test_remove_edge(self):
        """Test removing edge."""
        g = EdgeListGraph(3)
        g.add_edge(0, 1, weight=5)
        g.remove_edge(0, 1)
        assert len(g.edges) == 0

    def test_get_edges(self):
        """Test getting all edges."""
        g = EdgeListGraph(4)
        g.add_edge(0, 1, weight=5)
        g.add_edge(1, 2, weight=3)
        g.add_edge(2, 3, weight=7)
        edges = g.get_edges()
        assert len(edges) == 3

    def test_has_edge(self):
        """Test checking edge existence."""
        g = EdgeListGraph(3)
        g.add_edge(0, 1)
        assert g.has_edge(0, 1)
        assert g.has_edge(1, 0)  # Undirected
        assert not g.has_edge(0, 2)

    def test_has_edge_directed(self):
        """Test has_edge in directed graph."""
        g = EdgeListGraph(3, directed=True)
        g.add_edge(0, 1)
        assert g.has_edge(0, 1)
        assert not g.has_edge(1, 0)

    def test_sort_edges_by_weight(self):
        """Test sorting edges by weight."""
        g = EdgeListGraph(4)
        g.add_edge(0, 1, weight=10)
        g.add_edge(1, 2, weight=5)
        g.add_edge(2, 3, weight=8)
        g.add_edge(0, 3, weight=3)

        sorted_edges = g.sort_edges_by_weight()
        assert sorted_edges[0][2] == 3
        assert sorted_edges[1][2] == 5
        assert sorted_edges[2][2] == 8
        assert sorted_edges[3][2] == 10

    def test_empty_edge_list(self):
        """Test operations on empty edge list."""
        g = EdgeListGraph(3)
        assert len(g.get_edges()) == 0
        assert g.sort_edges_by_weight() == []


class TestGraphConversions:
    """Tests for graph representation conversions."""

    def test_list_to_matrix_undirected(self):
        """Test converting adjacency list to matrix (undirected)."""
        list_graph = AdjacencyListGraph(3)
        list_graph.add_edge(0, 1, weight=5)
        list_graph.add_edge(1, 2, weight=3)

        matrix_graph = convert_adjacency_list_to_matrix(list_graph)

        assert matrix_graph.num_vertices == 3
        assert not matrix_graph.directed
        assert matrix_graph.has_edge(0, 1)
        assert matrix_graph.has_edge(1, 2)
        assert matrix_graph.matrix[0][1] == 5
        assert matrix_graph.matrix[1][2] == 3

    def test_list_to_matrix_directed(self):
        """Test converting adjacency list to matrix (directed)."""
        list_graph = AdjacencyListGraph(3, directed=True)
        list_graph.add_edge(0, 1, weight=5)
        list_graph.add_edge(1, 2, weight=3)

        matrix_graph = convert_adjacency_list_to_matrix(list_graph)

        assert matrix_graph.directed
        assert matrix_graph.has_edge(0, 1)
        assert not matrix_graph.has_edge(1, 0)

    def test_matrix_to_list_undirected(self):
        """Test converting adjacency matrix to list (undirected)."""
        matrix_graph = AdjacencyMatrixGraph(3)
        matrix_graph.add_edge(0, 1, weight=5)
        matrix_graph.add_edge(1, 2, weight=3)

        list_graph = convert_adjacency_matrix_to_list(matrix_graph)

        assert list_graph.num_vertices == 3
        assert not list_graph.directed
        assert list_graph.has_edge(0, 1)
        assert list_graph.has_edge(1, 2)

    def test_matrix_to_list_directed(self):
        """Test converting adjacency matrix to list (directed)."""
        matrix_graph = AdjacencyMatrixGraph(3, directed=True)
        matrix_graph.add_edge(0, 1, weight=5)
        matrix_graph.add_edge(1, 2, weight=3)

        list_graph = convert_adjacency_matrix_to_list(matrix_graph)

        assert list_graph.directed
        assert list_graph.has_edge(0, 1)
        assert not list_graph.has_edge(1, 0)

    def test_list_to_edge_list(self):
        """Test converting adjacency list to edge list."""
        list_graph = AdjacencyListGraph(3)
        list_graph.add_edge(0, 1, weight=5)
        list_graph.add_edge(1, 2, weight=3)

        edge_graph = convert_to_edge_list(list_graph)

        assert edge_graph.num_vertices == 3
        assert len(edge_graph.edges) == 2
        assert (0, 1, 5) in edge_graph.edges
        assert (1, 2, 3) in edge_graph.edges

    def test_matrix_to_edge_list(self):
        """Test converting adjacency matrix to edge list."""
        matrix_graph = AdjacencyMatrixGraph(3)
        matrix_graph.add_edge(0, 1, weight=5)
        matrix_graph.add_edge(1, 2, weight=3)

        edge_graph = convert_to_edge_list(matrix_graph)

        assert edge_graph.num_vertices == 3
        assert len(edge_graph.edges) == 2

    def test_conversion_preserves_weights(self):
        """Test that conversions preserve edge weights."""
        list_graph = AdjacencyListGraph(4)
        list_graph.add_edge(0, 1, weight=10)
        list_graph.add_edge(1, 2, weight=20)
        list_graph.add_edge(2, 3, weight=30)

        matrix_graph = convert_adjacency_list_to_matrix(list_graph)
        edge_graph = convert_to_edge_list(matrix_graph)

        sorted_edges = edge_graph.sort_edges_by_weight()
        assert sorted_edges[0][2] == 10
        assert sorted_edges[1][2] == 20
        assert sorted_edges[2][2] == 30

    def test_roundtrip_conversion(self):
        """Test list -> matrix -> list conversion maintains structure."""
        original = AdjacencyListGraph(4)
        original.add_edge(0, 1, weight=5)
        original.add_edge(1, 2, weight=3)
        original.add_edge(2, 3, weight=7)

        matrix = convert_adjacency_list_to_matrix(original)
        converted = convert_adjacency_matrix_to_list(matrix)

        assert converted.num_vertices == original.num_vertices
        assert converted.has_edge(0, 1)
        assert converted.has_edge(1, 2)
        assert converted.has_edge(2, 3)


class TestComparisonAcrossRepresentations:
    """Tests comparing behavior across different representations."""

    def test_same_graph_different_representations(self):
        """Test same graph can be represented in all formats."""
        # Create same graph in all three representations
        adj_list = AdjacencyListGraph(4)
        adj_matrix = AdjacencyMatrixGraph(4)
        edge_list = EdgeListGraph(4)

        edges_to_add = [(0, 1, 5), (1, 2, 3), (2, 3, 7), (0, 3, 2)]

        for u, v, w in edges_to_add:
            adj_list.add_edge(u, v, weight=w)
            adj_matrix.add_edge(u, v, weight=w)
            edge_list.add_edge(u, v, weight=w)

        # Verify all have same edges
        for u, v, w in edges_to_add:
            assert adj_list.has_edge(u, v)
            assert adj_matrix.has_edge(u, v)
            assert edge_list.has_edge(u, v)

    def test_degree_consistency(self):
        """Test degree is same across representations."""
        adj_list = AdjacencyListGraph(5)
        adj_matrix = AdjacencyMatrixGraph(5)

        edges = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)]

        for u, v in edges:
            adj_list.add_edge(u, v)
            adj_matrix.add_edge(u, v)

        # Check vertex 0 degree (should be 3)
        assert adj_list.get_degree(0) == adj_matrix.get_degree(0)
        # Check vertex 2 degree (should be 3)
        assert adj_list.get_degree(2) == adj_matrix.get_degree(2)


class TestEdgeCases:
    """Tests for edge cases and special scenarios."""

    def test_single_vertex_graph(self):
        """Test graph with single vertex."""
        adj_list = AdjacencyListGraph(1)
        adj_matrix = AdjacencyMatrixGraph(1)
        edge_list = EdgeListGraph(1)

        assert adj_list.num_vertices == 1
        assert adj_matrix.num_vertices == 1
        assert edge_list.num_vertices == 1

    def test_empty_graph(self):
        """Test graph with no edges."""
        g = AdjacencyListGraph(5)
        for v in range(5):
            assert g.get_degree(v) == 0

    def test_complete_graph(self):
        """Test complete graph (all vertices connected)."""
        n = 4
        g = AdjacencyListGraph(n)

        # Add all possible edges
        for i in range(n):
            for j in range(i + 1, n):
                g.add_edge(i, j)

        # Each vertex should have degree n-1
        for v in range(n):
            assert g.get_degree(v) == n - 1

    def test_self_loop_undirected(self):
        """Test self-loop in undirected graph."""
        g = AdjacencyListGraph(3)
        g.add_edge(0, 0, weight=5)
        assert g.has_edge(0, 0)

    def test_parallel_edges(self):
        """Test handling of parallel edges (should update weight)."""
        g = AdjacencyListGraph(3)
        g.add_edge(0, 1, weight=5)
        g.add_edge(0, 1, weight=10)

        neighbors = g.get_neighbors(0)
        # Should have only one edge with updated weight
        assert len([n for n in neighbors if n[0] == 1]) == 1
        assert (1, 10) in neighbors


class TestLargeGraphs:
    """Performance tests with larger graphs."""

    def test_large_adjacency_list(self):
        """Test adjacency list with many vertices."""
        n = 100
        g = AdjacencyListGraph(n)

        # Add edges in a chain
        for i in range(n - 1):
            g.add_edge(i, i + 1)

        assert g.get_degree(0) == 1
        assert g.get_degree(50) == 2
        assert g.get_degree(99) == 1

    def test_large_adjacency_matrix(self):
        """Test adjacency matrix handles reasonable size."""
        n = 50
        g = AdjacencyMatrixGraph(n)

        # Add some edges
        for i in range(0, n, 5):
            for j in range(i + 1, min(i + 5, n)):
                g.add_edge(i, j, weight=i + j)

        assert g.has_edge(0, 1)
        assert g.matrix[0][1] == 1

    def test_large_edge_list_sorting(self):
        """Test edge list sorting with many edges."""
        g = EdgeListGraph(20)

        # Add random weighted edges
        import random

        edges = []
        for i in range(100):
            u = random.randint(0, 19)
            v = random.randint(0, 19)
            if u != v:
                w = random.randint(1, 100)
                g.add_edge(u, v, weight=w)
                edges.append((min(u, v), max(u, v), w))

        sorted_edges = g.sort_edges_by_weight()

        # Verify sorting
        for i in range(len(sorted_edges) - 1):
            assert sorted_edges[i][2] <= sorted_edges[i + 1][2]
