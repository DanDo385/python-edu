"""
Tests for Project 35: Depth-First Search

Comprehensive test suite covering:
- Graph class (both representations)
- DFS recursive and iterative
- Path finding algorithms
- Connected components
- Cycle detection
- Topological sorting
- Bipartite checking
"""

import pytest
from solution.solution import (
    Graph,
    dfs_recursive,
    dfs_iterative,
    find_path_dfs,
    find_all_paths_dfs,
    find_connected_components,
    has_cycle_undirected,
    has_cycle_directed,
    topological_sort_dfs,
    is_bipartite,
)


class TestGraph:
    """Tests for Graph class implementation."""

    def test_adjacency_list_initialization(self):
        """Test initialization with adjacency list."""
        g = Graph(5, "adjacency_list")
        assert g.num_vertices == 5
        assert g.representation == "adjacency_list"
        assert g.adjacency_list is not None
        assert g.adjacency_matrix is None

    def test_adjacency_matrix_initialization(self):
        """Test initialization with adjacency matrix."""
        g = Graph(3, "adjacency_matrix")
        assert g.num_vertices == 3
        assert g.representation == "adjacency_matrix"
        assert g.adjacency_matrix is not None
        assert g.adjacency_list is None
        assert len(g.adjacency_matrix) == 3
        assert all(len(row) == 3 for row in g.adjacency_matrix)

    def test_invalid_representation(self):
        """Test that invalid representation raises error."""
        with pytest.raises(ValueError):
            Graph(5, "invalid_representation")

    def test_add_edge_undirected_adjacency_list(self):
        """Test adding undirected edge with adjacency list."""
        g = Graph(3, "adjacency_list")
        g.add_edge(0, 1)
        assert 1 in g.get_neighbors(0)
        assert 0 in g.get_neighbors(1)

    def test_add_edge_directed_adjacency_list(self):
        """Test adding directed edge with adjacency list."""
        g = Graph(3, "adjacency_list")
        g.add_edge(0, 1, directed=True)
        assert 1 in g.get_neighbors(0)
        assert 0 not in g.get_neighbors(1)

    def test_add_edge_undirected_adjacency_matrix(self):
        """Test adding undirected edge with adjacency matrix."""
        g = Graph(3, "adjacency_matrix")
        g.add_edge(0, 1)
        assert g.adjacency_matrix[0][1] == 1
        assert g.adjacency_matrix[1][0] == 1

    def test_add_edge_directed_adjacency_matrix(self):
        """Test adding directed edge with adjacency matrix."""
        g = Graph(3, "adjacency_matrix")
        g.add_edge(0, 1, directed=True)
        assert g.adjacency_matrix[0][1] == 1
        assert g.adjacency_matrix[1][0] == 0

    def test_add_edge_invalid_vertex(self):
        """Test that adding edge with invalid vertex raises error."""
        g = Graph(3)
        with pytest.raises(ValueError):
            g.add_edge(0, 5)
        with pytest.raises(ValueError):
            g.add_edge(-1, 1)

    def test_get_neighbors_adjacency_list(self):
        """Test getting neighbors with adjacency list."""
        g = Graph(4, "adjacency_list")
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        neighbors = g.get_neighbors(0)
        assert set(neighbors) == {1, 2}

    def test_get_neighbors_adjacency_matrix(self):
        """Test getting neighbors with adjacency matrix."""
        g = Graph(4, "adjacency_matrix")
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        neighbors = g.get_neighbors(0)
        assert set(neighbors) == {1, 2}

    def test_get_neighbors_invalid_vertex(self):
        """Test that getting neighbors of invalid vertex raises error."""
        g = Graph(3)
        with pytest.raises(ValueError):
            g.get_neighbors(5)

    def test_has_edge_adjacency_list(self):
        """Test checking edge existence with adjacency list."""
        g = Graph(3, "adjacency_list")
        g.add_edge(0, 1)
        assert g.has_edge(0, 1)
        assert g.has_edge(1, 0)  # Undirected
        assert not g.has_edge(0, 2)

    def test_has_edge_adjacency_matrix(self):
        """Test checking edge existence with adjacency matrix."""
        g = Graph(3, "adjacency_matrix")
        g.add_edge(0, 1)
        assert g.has_edge(0, 1)
        assert g.has_edge(1, 0)  # Undirected
        assert not g.has_edge(0, 2)

    def test_has_edge_invalid_vertex(self):
        """Test that checking edge with invalid vertex returns False."""
        g = Graph(3)
        assert not g.has_edge(0, 5)
        assert not g.has_edge(-1, 1)


class TestDFSRecursive:
    """Tests for dfs_recursive function."""

    def test_linear_graph(self):
        """Test DFS on linear graph."""
        g = Graph(4)
        g.add_edge(0, 1, directed=True)
        g.add_edge(1, 2, directed=True)
        g.add_edge(2, 3, directed=True)
        result = dfs_recursive(g, 0)
        assert result == [0, 1, 2, 3]

    def test_tree_graph(self):
        """Test DFS on tree graph."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        result = dfs_recursive(g, 0)
        assert result[0] == 0
        assert set(result) == {0, 1, 2, 3}
        assert len(result) == 4

    def test_single_vertex(self):
        """Test DFS on single vertex."""
        g = Graph(1)
        result = dfs_recursive(g, 0)
        assert result == [0]

    def test_disconnected_graph(self):
        """Test DFS on disconnected graph (from one component)."""
        g = Graph(5)
        g.add_edge(0, 1)
        g.add_edge(2, 3)
        result = dfs_recursive(g, 0)
        assert set(result) == {0, 1}

    def test_cyclic_graph(self):
        """Test DFS on graph with cycle."""
        g = Graph(3)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        result = dfs_recursive(g, 0)
        assert set(result) == {0, 1, 2}
        assert len(result) == 3


class TestDFSIterative:
    """Tests for dfs_iterative function."""

    def test_linear_graph(self):
        """Test iterative DFS on linear graph."""
        g = Graph(4)
        g.add_edge(0, 1, directed=True)
        g.add_edge(1, 2, directed=True)
        g.add_edge(2, 3, directed=True)
        result = dfs_iterative(g, 0)
        assert result == [0, 1, 2, 3]

    def test_tree_graph(self):
        """Test iterative DFS on tree graph."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        result = dfs_iterative(g, 0)
        assert result[0] == 0
        assert set(result) == {0, 1, 2, 3}
        assert len(result) == 4

    def test_single_vertex(self):
        """Test iterative DFS on single vertex."""
        g = Graph(1)
        result = dfs_iterative(g, 0)
        assert result == [0]

    def test_disconnected_graph(self):
        """Test iterative DFS on disconnected graph."""
        g = Graph(5)
        g.add_edge(0, 1)
        g.add_edge(2, 3)
        result = dfs_iterative(g, 0)
        assert set(result) == {0, 1}

    def test_cyclic_graph(self):
        """Test iterative DFS on graph with cycle."""
        g = Graph(3)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        result = dfs_iterative(g, 0)
        assert set(result) == {0, 1, 2}
        assert len(result) == 3

    def test_comparison_with_recursive(self):
        """Test that iterative and recursive DFS visit same vertices."""
        g = Graph(5)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)

        recursive_result = dfs_recursive(g, 0)
        iterative_result = dfs_iterative(g, 0)

        assert set(recursive_result) == set(iterative_result)
        assert len(recursive_result) == len(iterative_result)


class TestFindPathDFS:
    """Tests for find_path_dfs function."""

    def test_path_exists_simple(self):
        """Test finding path when it exists."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(1, 3)
        path = find_path_dfs(g, 0, 3)
        assert path is not None
        assert path[0] == 0
        assert path[-1] == 3
        assert len(path) >= 3

    def test_path_exists_multiple_routes(self):
        """Test finding path when multiple routes exist."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        path = find_path_dfs(g, 0, 3)
        assert path is not None
        assert path[0] == 0
        assert path[-1] == 3

    def test_path_no_exist(self):
        """Test when no path exists."""
        g = Graph(5)
        g.add_edge(0, 1)
        g.add_edge(2, 3)
        path = find_path_dfs(g, 0, 3)
        assert path is None

    def test_path_to_self(self):
        """Test path from vertex to itself."""
        g = Graph(3)
        g.add_edge(0, 1)
        path = find_path_dfs(g, 0, 0)
        assert path == [0]

    def test_path_invalid_vertices(self):
        """Test with invalid vertices."""
        g = Graph(3)
        g.add_edge(0, 1)
        assert find_path_dfs(g, 0, 5) is None
        assert find_path_dfs(g, -1, 1) is None

    def test_path_directed_graph(self):
        """Test path finding in directed graph."""
        g = Graph(3)
        g.add_edge(0, 1, directed=True)
        g.add_edge(1, 2, directed=True)
        path = find_path_dfs(g, 0, 2)
        assert path == [0, 1, 2]
        # Reverse path should not exist
        path_reverse = find_path_dfs(g, 2, 0)
        assert path_reverse is None


class TestFindAllPathsDFS:
    """Tests for find_all_paths_dfs function."""

    def test_diamond_graph(self):
        """Test finding all paths in diamond graph."""
        g = Graph(4)
        g.add_edge(0, 1, directed=True)
        g.add_edge(0, 2, directed=True)
        g.add_edge(1, 3, directed=True)
        g.add_edge(2, 3, directed=True)
        paths = find_all_paths_dfs(g, 0, 3)
        assert len(paths) == 2
        assert [0, 1, 3] in paths
        assert [0, 2, 3] in paths

    def test_single_path(self):
        """Test when only one path exists."""
        g = Graph(3)
        g.add_edge(0, 1, directed=True)
        g.add_edge(1, 2, directed=True)
        paths = find_all_paths_dfs(g, 0, 2)
        assert len(paths) == 1
        assert paths[0] == [0, 1, 2]

    def test_no_paths(self):
        """Test when no paths exist."""
        g = Graph(4)
        g.add_edge(0, 1, directed=True)
        g.add_edge(2, 3, directed=True)
        paths = find_all_paths_dfs(g, 0, 3)
        assert len(paths) == 0

    def test_multiple_paths_complex(self):
        """Test finding multiple paths in complex graph."""
        g = Graph(5)
        g.add_edge(0, 1, directed=True)
        g.add_edge(0, 2, directed=True)
        g.add_edge(1, 3, directed=True)
        g.add_edge(2, 3, directed=True)
        g.add_edge(3, 4, directed=True)
        paths = find_all_paths_dfs(g, 0, 4)
        assert len(paths) == 2
        assert all(p[0] == 0 and p[-1] == 4 for p in paths)

    def test_path_to_self(self):
        """Test all paths from vertex to itself."""
        g = Graph(3)
        g.add_edge(0, 1, directed=True)
        paths = find_all_paths_dfs(g, 0, 0)
        assert len(paths) == 1
        assert paths[0] == [0]


class TestConnectedComponents:
    """Tests for find_connected_components function."""

    def test_single_component(self):
        """Test graph with single connected component."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        components = find_connected_components(g)
        assert len(components) == 1
        assert set(components[0]) == {0, 1, 2, 3}

    def test_multiple_components(self):
        """Test graph with multiple connected components."""
        g = Graph(6)
        g.add_edge(0, 1)
        g.add_edge(2, 3)
        g.add_edge(4, 5)
        components = find_connected_components(g)
        assert len(components) == 3
        component_sets = [set(c) for c in components]
        assert {0, 1} in component_sets
        assert {2, 3} in component_sets
        assert {4, 5} in component_sets

    def test_isolated_vertices(self):
        """Test graph with isolated vertices."""
        g = Graph(5)
        g.add_edge(0, 1)
        components = find_connected_components(g)
        assert len(components) == 4  # {0,1}, {2}, {3}, {4}

    def test_complete_graph(self):
        """Test complete graph (single component)."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        components = find_connected_components(g)
        assert len(components) == 1
        assert set(components[0]) == {0, 1, 2, 3}

    def test_empty_graph(self):
        """Test graph with no edges."""
        g = Graph(3)
        components = find_connected_components(g)
        assert len(components) == 3
        assert all(len(c) == 1 for c in components)


class TestCycleDetectionUndirected:
    """Tests for has_cycle_undirected function."""

    def test_tree_no_cycle(self):
        """Test that tree has no cycle."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        assert not has_cycle_undirected(g)

    def test_triangle_has_cycle(self):
        """Test that triangle has cycle."""
        g = Graph(3)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        assert has_cycle_undirected(g)

    def test_square_has_cycle(self):
        """Test that square has cycle."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 0)
        assert has_cycle_undirected(g)

    def test_linear_no_cycle(self):
        """Test that linear graph has no cycle."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        assert not has_cycle_undirected(g)

    def test_single_edge_no_cycle(self):
        """Test that single edge has no cycle."""
        g = Graph(2)
        g.add_edge(0, 1)
        assert not has_cycle_undirected(g)

    def test_disconnected_with_cycle(self):
        """Test disconnected graph where one component has cycle."""
        g = Graph(5)
        g.add_edge(0, 1)  # No cycle
        g.add_edge(2, 3)  # Cycle
        g.add_edge(3, 4)
        g.add_edge(4, 2)
        assert has_cycle_undirected(g)


class TestCycleDetectionDirected:
    """Tests for has_cycle_directed function."""

    def test_dag_no_cycle(self):
        """Test that DAG has no cycle."""
        g = Graph(4)
        g.add_edge(0, 1, directed=True)
        g.add_edge(1, 2, directed=True)
        g.add_edge(1, 3, directed=True)
        assert not has_cycle_directed(g)

    def test_simple_cycle(self):
        """Test simple cycle detection."""
        g = Graph(3)
        g.add_edge(0, 1, directed=True)
        g.add_edge(1, 2, directed=True)
        g.add_edge(2, 1, directed=True)
        assert has_cycle_directed(g)

    def test_self_loop(self):
        """Test self-loop detection."""
        g = Graph(2)
        g.add_edge(0, 0, directed=True)
        assert has_cycle_directed(g)

    def test_long_cycle(self):
        """Test longer cycle."""
        g = Graph(4)
        g.add_edge(0, 1, directed=True)
        g.add_edge(1, 2, directed=True)
        g.add_edge(2, 3, directed=True)
        g.add_edge(3, 0, directed=True)
        assert has_cycle_directed(g)

    def test_tree_directed_no_cycle(self):
        """Test directed tree has no cycle."""
        g = Graph(4)
        g.add_edge(0, 1, directed=True)
        g.add_edge(0, 2, directed=True)
        g.add_edge(1, 3, directed=True)
        assert not has_cycle_directed(g)

    def test_disconnected_with_cycle(self):
        """Test disconnected directed graph with cycle in one component."""
        g = Graph(5)
        g.add_edge(0, 1, directed=True)  # No cycle
        g.add_edge(2, 3, directed=True)  # Cycle
        g.add_edge(3, 4, directed=True)
        g.add_edge(4, 2, directed=True)
        assert has_cycle_directed(g)


class TestTopologicalSort:
    """Tests for topological_sort_dfs function."""

    def test_linear_dag(self):
        """Test topological sort on linear DAG."""
        g = Graph(4)
        g.add_edge(0, 1, directed=True)
        g.add_edge(1, 2, directed=True)
        g.add_edge(2, 3, directed=True)
        result = topological_sort_dfs(g)
        assert result == [0, 1, 2, 3]

    def test_dag_with_multiple_valid_orders(self):
        """Test DAG with multiple valid topological orders."""
        g = Graph(4)
        g.add_edge(0, 1, directed=True)
        g.add_edge(0, 2, directed=True)
        g.add_edge(1, 3, directed=True)
        g.add_edge(2, 3, directed=True)
        result = topological_sort_dfs(g)
        assert result is not None
        # Verify it's a valid topological order
        assert result.index(0) < result.index(1)
        assert result.index(0) < result.index(2)
        assert result.index(1) < result.index(3)
        assert result.index(2) < result.index(3)

    def test_graph_with_cycle(self):
        """Test that graph with cycle returns None."""
        g = Graph(3)
        g.add_edge(0, 1, directed=True)
        g.add_edge(1, 2, directed=True)
        g.add_edge(2, 0, directed=True)
        result = topological_sort_dfs(g)
        assert result is None

    def test_disconnected_dag(self):
        """Test topological sort on disconnected DAG."""
        g = Graph(4)
        g.add_edge(0, 1, directed=True)
        g.add_edge(2, 3, directed=True)
        result = topological_sort_dfs(g)
        assert result is not None
        assert len(result) == 4
        assert result.index(0) < result.index(1)
        assert result.index(2) < result.index(3)

    def test_single_vertex(self):
        """Test topological sort on single vertex."""
        g = Graph(1)
        result = topological_sort_dfs(g)
        assert result == [0]

    def test_complex_dag(self):
        """Test topological sort on complex DAG."""
        g = Graph(6)
        g.add_edge(5, 2, directed=True)
        g.add_edge(5, 0, directed=True)
        g.add_edge(4, 0, directed=True)
        g.add_edge(4, 1, directed=True)
        g.add_edge(2, 3, directed=True)
        g.add_edge(3, 1, directed=True)
        result = topological_sort_dfs(g)
        assert result is not None
        # Verify all edges go from left to right in the ordering
        pos = {v: i for i, v in enumerate(result)}
        assert pos[5] < pos[2]
        assert pos[5] < pos[0]
        assert pos[4] < pos[0]
        assert pos[4] < pos[1]
        assert pos[2] < pos[3]
        assert pos[3] < pos[1]


class TestBipartite:
    """Tests for is_bipartite function."""

    def test_linear_graph_bipartite(self):
        """Test that linear graph is bipartite."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        assert is_bipartite(g)

    def test_triangle_not_bipartite(self):
        """Test that triangle (odd cycle) is not bipartite."""
        g = Graph(3)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        assert not is_bipartite(g)

    def test_square_bipartite(self):
        """Test that square (even cycle) is bipartite."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 0)
        assert is_bipartite(g)

    def test_tree_bipartite(self):
        """Test that tree is always bipartite."""
        g = Graph(5)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(1, 4)
        assert is_bipartite(g)

    def test_complete_bipartite_graph(self):
        """Test complete bipartite graph K_2,2."""
        g = Graph(4)
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        assert is_bipartite(g)

    def test_pentagon_not_bipartite(self):
        """Test that pentagon (5-cycle, odd) is not bipartite."""
        g = Graph(5)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_edge(4, 0)
        assert not is_bipartite(g)

    def test_hexagon_bipartite(self):
        """Test that hexagon (6-cycle, even) is bipartite."""
        g = Graph(6)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_edge(4, 5)
        g.add_edge(5, 0)
        assert is_bipartite(g)

    def test_disconnected_all_bipartite(self):
        """Test disconnected graph where all components are bipartite."""
        g = Graph(6)
        g.add_edge(0, 1)  # Edge
        g.add_edge(2, 3)  # Edge
        g.add_edge(3, 4)  # Triangle would make it not bipartite
        assert is_bipartite(g)

    def test_disconnected_one_not_bipartite(self):
        """Test disconnected graph where one component is not bipartite."""
        g = Graph(5)
        g.add_edge(0, 1)  # Bipartite component
        g.add_edge(2, 3)  # Not bipartite (triangle)
        g.add_edge(3, 4)
        g.add_edge(4, 2)
        assert not is_bipartite(g)

    def test_single_vertex_bipartite(self):
        """Test that single vertex is bipartite."""
        g = Graph(1)
        assert is_bipartite(g)

    def test_single_edge_bipartite(self):
        """Test that single edge is bipartite."""
        g = Graph(2)
        g.add_edge(0, 1)
        assert is_bipartite(g)


# Performance and edge case tests
class TestPerformance:
    """Performance and edge case tests."""

    def test_large_linear_graph_dfs(self):
        """Test DFS on large linear graph."""
        n = 1000
        g = Graph(n)
        for i in range(n - 1):
            g.add_edge(i, i + 1, directed=True)
        result = dfs_recursive(g, 0)
        assert len(result) == n
        assert result == list(range(n))

    def test_large_tree_dfs(self):
        """Test DFS on large tree."""
        n = 1000
        g = Graph(n)
        for i in range(1, n):
            g.add_edge(i // 2, i, directed=True)
        result = dfs_recursive(g, 0)
        assert len(result) == n

    def test_dense_graph_connected_components(self):
        """Test connected components on denser graph."""
        g = Graph(100)
        # Create 10 components of size 10 each
        for comp in range(10):
            start = comp * 10
            for i in range(start, start + 10):
                for j in range(i + 1, start + 10):
                    g.add_edge(i, j)
        components = find_connected_components(g)
        assert len(components) == 10
        assert all(len(c) == 10 for c in components)

    def test_large_dag_topological_sort(self):
        """Test topological sort on large DAG."""
        n = 100
        g = Graph(n)
        for i in range(n - 1):
            g.add_edge(i, i + 1, directed=True)
        result = topological_sort_dfs(g)
        assert result == list(range(n))


# Integration tests
class TestIntegration:
    """Integration tests combining multiple functions."""

    def test_social_network_scenario(self):
        """Test social network friend connections."""
        # 6 people, find friend groups
        g = Graph(6)
        g.add_edge(0, 1)  # Alice - Bob
        g.add_edge(0, 2)  # Alice - Carol
        g.add_edge(1, 2)  # Bob - Carol
        g.add_edge(3, 4)  # Dave - Eve
        # Frank (5) has no friends

        components = find_connected_components(g)
        assert len(components) == 3
        assert {0, 1, 2} in [set(c) for c in components]
        assert {3, 4} in [set(c) for c in components]
        assert {5} in [set(c) for c in components]

    def test_course_prerequisites(self):
        """Test course prerequisite ordering."""
        # Courses: 0=Intro, 1=DS, 2=Algo, 3=Systems
        g = Graph(4)
        g.add_edge(0, 1, directed=True)  # Intro before DS
        g.add_edge(1, 2, directed=True)  # DS before Algo
        g.add_edge(1, 3, directed=True)  # DS before Systems

        topo = topological_sort_dfs(g)
        assert topo is not None
        assert topo.index(0) < topo.index(1)
        assert topo.index(1) < topo.index(2)
        assert topo.index(1) < topo.index(3)

    def test_maze_path_finding(self):
        """Test finding path through maze-like graph."""
        # Simple 3x3 grid maze
        g = Graph(9)
        # Grid layout: 0-1-2
        #              3-4-5
        #              6-7-8
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(1, 4)
        g.add_edge(2, 5)
        g.add_edge(3, 4)
        g.add_edge(4, 5)
        g.add_edge(4, 7)
        g.add_edge(6, 7)
        g.add_edge(7, 8)

        path = find_path_dfs(g, 0, 8)
        assert path is not None
        assert path[0] == 0
        assert path[-1] == 8

    def test_dependency_cycle_detection(self):
        """Test detecting circular dependencies."""
        # Package dependencies
        g = Graph(4)
        g.add_edge(0, 1, directed=True)  # A depends on B
        g.add_edge(1, 2, directed=True)  # B depends on C
        g.add_edge(2, 3, directed=True)  # C depends on D

        assert not has_cycle_directed(g)  # No circular dependency

        # Add circular dependency
        g.add_edge(3, 0, directed=True)  # D depends on A (creates cycle)
        assert has_cycle_directed(g)  # Circular dependency detected!

    def test_matching_bipartite(self):
        """Test bipartite matching scenario (jobs and applicants)."""
        # 3 jobs, 3 applicants
        # Applicants 0,1,2 can apply to jobs 3,4,5
        g = Graph(6)
        g.add_edge(0, 3)  # Applicant 0 can do job 3
        g.add_edge(0, 4)  # Applicant 0 can do job 4
        g.add_edge(1, 4)  # Applicant 1 can do job 4
        g.add_edge(1, 5)  # Applicant 1 can do job 5
        g.add_edge(2, 3)  # Applicant 2 can do job 3
        g.add_edge(2, 5)  # Applicant 2 can do job 5

        assert is_bipartite(g)  # Valid bipartite matching possible


# Correctness verification tests
class TestCorrectnessVerification:
    """Verify correctness of implementations."""

    def test_dfs_visits_all_reachable(self):
        """Verify DFS visits all reachable vertices."""
        g = Graph(6)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(0, 3)
        g.add_edge(3, 4)
        # Vertex 5 is not reachable

        result = dfs_recursive(g, 0)
        assert set(result) == {0, 1, 2, 3, 4}
        assert 5 not in result

    def test_path_validity(self):
        """Verify found path is actually valid."""
        g = Graph(5)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)

        path = find_path_dfs(g, 0, 4)
        assert path is not None

        # Verify each consecutive pair has an edge
        for i in range(len(path) - 1):
            assert g.has_edge(path[i], path[i + 1])

    def test_topological_order_validity(self):
        """Verify topological order respects all edges."""
        g = Graph(5)
        g.add_edge(0, 1, directed=True)
        g.add_edge(0, 2, directed=True)
        g.add_edge(1, 3, directed=True)
        g.add_edge(2, 3, directed=True)
        g.add_edge(3, 4, directed=True)

        topo = topological_sort_dfs(g)
        assert topo is not None

        # Create position map
        pos = {v: i for i, v in enumerate(topo)}

        # Verify all edges go from left to right
        for u in range(g.num_vertices):
            for v in g.get_neighbors(u):
                assert pos[u] < pos[v], f"Edge {u}->{v} violates topological order"

    def test_bipartite_coloring_validity(self):
        """Verify bipartite graph can actually be 2-colored."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)

        assert is_bipartite(g)

        # Manually verify 2-coloring is possible
        # Color: 0=Red, 1=Blue, 2=Red, 3=Blue
        # Check no edge connects same color
        color = [0, 1, 0, 1]
        for u in range(g.num_vertices):
            for v in g.get_neighbors(u):
                assert color[u] != color[v]
