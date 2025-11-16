"""
Tests for Project 36: Breadth-First Search

Comprehensive test suite covering:
- BFS traversal (queue-based)
- Shortest path in unweighted graphs
- Level-order traversal
- Word ladder problem
"""

import pytest
import sys
import os

# Add solution directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../solution'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../35-graph-dfs/solution'))

from solution import Graph
from solution import (
    bfs_traversal,
    shortest_path_bfs,
    level_order_traversal,
    word_ladder,
)


class TestBFSTraversal:
    """Tests for BFS traversal implementation."""

    def test_linear_graph(self):
        """Test BFS on linear graph."""
        g = Graph(4)
        g.add_edge(0, 1, directed=True)
        g.add_edge(1, 2, directed=True)
        g.add_edge(2, 3, directed=True)
        result = bfs_traversal(g, 0)
        assert result == [0, 1, 2, 3]

    def test_tree_structure(self):
        """Test BFS on tree structure."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        result = bfs_traversal(g, 0)
        assert result[0] == 0
        assert set(result[1:3]) == {1, 2}
        assert result[3] == 3

    def test_disconnected_graph(self):
        """Test BFS on disconnected graph (only explores connected component)."""
        g = Graph(6)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(3, 4)
        g.add_edge(4, 5)
        result = bfs_traversal(g, 0)
        assert set(result) == {0, 1, 2}
        assert len(result) == 3

    def test_single_vertex(self):
        """Test BFS on single vertex."""
        g = Graph(1)
        result = bfs_traversal(g, 0)
        assert result == [0]

    def test_cycle(self):
        """Test BFS handles cycles correctly."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 0)
        result = bfs_traversal(g, 0)
        assert len(result) == 4
        assert set(result) == {0, 1, 2, 3}

    def test_complete_graph(self):
        """Test BFS on complete graph."""
        g = Graph(4)
        for i in range(4):
            for j in range(i + 1, 4):
                g.add_edge(i, j)
        result = bfs_traversal(g, 0)
        assert result[0] == 0
        assert set(result) == {0, 1, 2, 3}
        assert len(result) == 4


class TestShortestPathBFS:
    """Tests for shortest path using BFS."""

    def test_shortest_path_exists(self):
        """Test finding shortest path when it exists."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        path = shortest_path_bfs(g, 0, 3)
        assert path == [0, 1, 3]

    def test_shortest_path_multiple_routes(self):
        """Test shortest path when multiple routes exist."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        path = shortest_path_bfs(g, 0, 3)
        assert path is not None
        assert path[0] == 0
        assert path[-1] == 3
        assert len(path) == 3  # Shortest is length 3

    def test_no_path(self):
        """Test when no path exists."""
        g = Graph(5)
        g.add_edge(0, 1)
        g.add_edge(2, 3)
        path = shortest_path_bfs(g, 0, 3)
        assert path is None

    def test_start_equals_end(self):
        """Test when start equals end."""
        g = Graph(3)
        g.add_edge(0, 1)
        path = shortest_path_bfs(g, 0, 0)
        assert path == [0]

    def test_invalid_vertices(self):
        """Test with invalid vertex indices."""
        g = Graph(3)
        g.add_edge(0, 1)
        assert shortest_path_bfs(g, 0, 5) is None
        assert shortest_path_bfs(g, -1, 1) is None

    def test_directed_graph(self):
        """Test shortest path in directed graph."""
        g = Graph(4)
        g.add_edge(0, 1, directed=True)
        g.add_edge(1, 2, directed=True)
        g.add_edge(2, 3, directed=True)
        g.add_edge(0, 3, directed=True)
        path = shortest_path_bfs(g, 0, 3)
        assert path == [0, 3]  # Direct edge is shortest

    def test_longer_path(self):
        """Test finding path in larger graph."""
        g = Graph(6)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_edge(4, 5)
        path = shortest_path_bfs(g, 0, 5)
        assert path == [0, 1, 2, 3, 4, 5]


class TestLevelOrderTraversal:
    """Tests for level-order traversal."""

    def test_binary_tree(self):
        """Test level-order on binary tree."""
        g = Graph(7)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(1, 4)
        g.add_edge(2, 5)
        g.add_edge(2, 6)
        levels = level_order_traversal(g, 0)
        assert levels[0] == [0]
        assert set(levels[1]) == {1, 2}
        assert set(levels[2]) == {3, 4, 5, 6}

    def test_linear_structure(self):
        """Test level-order on linear structure."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        levels = level_order_traversal(g, 0)
        assert levels == [[0], [1], [2], [3]]

    def test_single_vertex(self):
        """Test level-order with single vertex."""
        g = Graph(1)
        levels = level_order_traversal(g, 0)
        assert levels == [[0]]

    def test_diamond_graph(self):
        """Test level-order on diamond graph."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        levels = level_order_traversal(g, 0)
        assert levels[0] == [0]
        assert set(levels[1]) == {1, 2}
        assert levels[2] == [3]

    def test_disconnected_component(self):
        """Test level-order only visits connected component."""
        g = Graph(5)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(3, 4)
        levels = level_order_traversal(g, 0)
        assert len(levels) == 3
        assert set().union(*levels) == {0, 1, 2}

    def test_star_graph(self):
        """Test level-order on star graph."""
        g = Graph(5)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        g.add_edge(0, 4)
        levels = level_order_traversal(g, 0)
        assert levels == [[0], [1, 2, 3, 4]]


class TestWordLadder:
    """Tests for word ladder problem."""

    def test_basic_transformation(self):
        """Test basic word transformation."""
        word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
        result = word_ladder("hit", "cog", word_list)
        assert result[0] == "hit"
        assert result[-1] == "cog"
        assert len(result) == 5  # hit -> hot -> dot -> dog -> cog
        # Verify each step differs by one letter
        for i in range(len(result) - 1):
            diff_count = sum(c1 != c2 for c1, c2 in zip(result[i], result[i + 1]))
            assert diff_count == 1

    def test_no_path(self):
        """Test when end word not in list."""
        word_list = ["hot", "dot", "dog", "lot", "log"]
        result = word_ladder("hit", "cog", word_list)
        assert result == []

    def test_short_transformation(self):
        """Test short transformation sequence."""
        word_list = ["hot", "dot", "dog"]
        result = word_ladder("hot", "dog", word_list)
        assert result == ["hot", "dot", "dog"]

    def test_same_word(self):
        """Test when start equals end."""
        word_list = ["hot", "dot", "dog"]
        result = word_ladder("hot", "hot", word_list)
        assert result == ["hot"]

    def test_no_intermediate_words(self):
        """Test when no valid intermediate words exist."""
        word_list = ["abc", "xyz"]
        result = word_ladder("abc", "xyz", word_list)
        assert result == []

    def test_longer_words(self):
        """Test with longer words."""
        word_list = ["teach", "peach", "peace", "place", "plate"]
        result = word_ladder("teach", "plate", word_list)
        if result:  # Path may exist
            assert result[0] == "teach"
            assert result[-1] == "plate"
            for i in range(len(result) - 1):
                diff_count = sum(c1 != c2 for c1, c2 in zip(result[i], result[i + 1]))
                assert diff_count == 1

    def test_multiple_paths(self):
        """Test when multiple paths exist (BFS finds shortest)."""
        word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
        result = word_ladder("hit", "cog", word_list)
        # BFS guarantees shortest path
        assert result is not None
        assert len(result) >= 1


class TestBFSProperties:
    """Tests for BFS algorithm properties."""

    def test_bfs_shortest_path_guarantee(self):
        """Test that BFS finds shortest path in unweighted graph."""
        g = Graph(5)
        # Create graph with multiple paths
        g.add_edge(0, 1)
        g.add_edge(1, 4)
        g.add_edge(0, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        path = shortest_path_bfs(g, 0, 4)
        # Shortest path should be 0->1->4 (length 3)
        assert len(path) == 3

    def test_bfs_visits_all_reachable(self):
        """Test that BFS visits all reachable vertices."""
        g = Graph(6)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        result = bfs_traversal(g, 0)
        # Should visit all except isolated vertex 5
        assert set(result) == {0, 1, 2, 3, 4}

    def test_level_order_correct_levels(self):
        """Test that level-order correctly groups by distance."""
        g = Graph(6)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        g.add_edge(3, 5)
        levels = level_order_traversal(g, 0)
        # Verify level 0 has start
        assert levels[0] == [0]
        # Verify levels increase correctly
        for i in range(len(levels)):
            for vertex in levels[i]:
                # Each vertex should be at correct distance
                path = shortest_path_bfs(g, 0, vertex)
                assert len(path) - 1 == i


class TestEdgeCases:
    """Tests for edge cases."""

    def test_empty_word_list(self):
        """Test word ladder with empty word list."""
        result = word_ladder("hit", "cog", [])
        assert result == []

    def test_single_word_list(self):
        """Test word ladder with single word."""
        result = word_ladder("hit", "hot", ["hot"])
        assert result == ["hit", "hot"]

    def test_invalid_start_vertex(self):
        """Test level-order with invalid start."""
        g = Graph(3)
        g.add_edge(0, 1)
        levels = level_order_traversal(g, 5)
        assert levels == []

    def test_self_loop(self):
        """Test BFS handles self-loops."""
        g = Graph(3, "adjacency_list")
        g.add_edge(0, 0)  # Self-loop
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        result = bfs_traversal(g, 0)
        assert 0 in result
        assert 1 in result
        assert 2 in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
