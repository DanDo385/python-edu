"""Tests for Project 38: Topological Sort"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../solution'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../35-graph-dfs/solution'))

from solution import Graph, kahns_algorithm, topological_sort_dfs, can_finish, find_order


class TestTopologicalSort:
    def test_kahns_dag(self):
        """Test Kahn's algorithm on DAG."""
        g = Graph(6)
        g.add_edge(5, 2, directed=True)
        g.add_edge(5, 0, directed=True)
        g.add_edge(4, 0, directed=True)
        g.add_edge(4, 1, directed=True)
        g.add_edge(2, 3, directed=True)
        g.add_edge(3, 1, directed=True)
        result = kahns_algorithm(g)
        assert result is not None
        assert len(result) == 6

    def test_kahns_cycle(self):
        """Test Kahn's algorithm detects cycle."""
        g = Graph(3)
        g.add_edge(0, 1, directed=True)
        g.add_edge(1, 2, directed=True)
        g.add_edge(2, 0, directed=True)
        assert kahns_algorithm(g) is None

    def test_dfs_dag(self):
        """Test DFS topological sort."""
        g = Graph(4)
        g.add_edge(0, 1, directed=True)
        g.add_edge(0, 2, directed=True)
        g.add_edge(1, 3, directed=True)
        g.add_edge(2, 3, directed=True)
        result = topological_sort_dfs(g)
        assert result is not None
        assert len(result) == 4
        assert result.index(0) < result.index(1)
        assert result.index(0) < result.index(2)
        assert result.index(1) < result.index(3)

    def test_can_finish_possible(self):
        """Test can_finish when possible."""
        assert can_finish(2, [[1, 0]]) == True
        assert can_finish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == True

    def test_can_finish_impossible(self):
        """Test can_finish when impossible."""
        assert can_finish(2, [[1, 0], [0, 1]]) == False

    def test_find_order_valid(self):
        """Test find_order returns valid ordering."""
        result = find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
        assert len(result) == 4
        assert result.index(0) < result.index(1)
        assert result.index(0) < result.index(2)

    def test_find_order_invalid(self):
        """Test find_order returns empty for cycle."""
        assert find_order(2, [[1, 0], [0, 1]]) == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
