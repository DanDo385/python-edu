"""
Tests for Project 37: Shortest Path Algorithms

Comprehensive test suite covering:
- Dijkstra's algorithm
- Bellman-Ford algorithm
- Floyd-Warshall algorithm
- Network delay time problem
"""

import pytest
import sys
import os

# Add solution directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../solution'))

from solution import (
    WeightedGraph,
    dijkstra,
    bellman_ford,
    floyd_warshall,
    network_delay_time,
    get_shortest_path,
)


class TestDijkstra:
    """Tests for Dijkstra's algorithm."""

    def test_simple_path(self):
        """Test Dijkstra on simple path."""
        g = WeightedGraph(4)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 2)
        g.add_edge(2, 3, 3)
        distances, parents = dijkstra(g, 0)
        assert distances[3] == 6
        path = get_shortest_path(0, 3, parents)
        assert path == [0, 1, 2, 3]

    def test_multiple_paths(self):
        """Test Dijkstra chooses shortest path."""
        g = WeightedGraph(4)
        g.add_edge(0, 1, 1)
        g.add_edge(0, 2, 4)
        g.add_edge(1, 2, 2)
        g.add_edge(1, 3, 5)
        g.add_edge(2, 3, 1)
        distances, parents = dijkstra(g, 0)
        assert distances[3] == 4  # 0->1->2->3
        path = get_shortest_path(0, 3, parents)
        assert len(path) == 4

    def test_unreachable_vertex(self):
        """Test Dijkstra with unreachable vertices."""
        g = WeightedGraph(5)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 1)
        g.add_edge(3, 4, 1)
        distances, _ = dijkstra(g, 0)
        assert distances[0] == 0
        assert distances[2] == 2
        assert distances[3] == float('inf')
        assert distances[4] == float('inf')

    def test_self_loop(self):
        """Test Dijkstra with self-loop."""
        g = WeightedGraph(3)
        g.add_edge(0, 0, 1)  # Self-loop
        g.add_edge(0, 1, 2)
        g.add_edge(1, 2, 3)
        distances, _ = dijkstra(g, 0)
        assert distances[0] == 0
        assert distances[2] == 5


class TestBellmanFord:
    """Tests for Bellman-Ford algorithm."""

    def test_with_negative_weights(self):
        """Test Bellman-Ford with negative weights."""
        g = WeightedGraph(4)
        g.add_edge(0, 1, -1)
        g.add_edge(0, 2, 4)
        g.add_edge(1, 2, 3)
        g.add_edge(1, 3, 2)
        result = bellman_ford(g, 0)
        assert result is not None
        distances, _ = result
        assert distances[1] == -1
        assert distances[2] == 2
        assert distances[3] == 1

    def test_negative_cycle_detection(self):
        """Test Bellman-Ford detects negative cycles."""
        g = WeightedGraph(3)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, -3)
        g.add_edge(2, 1, 2)  # Creates negative cycle
        result = bellman_ford(g, 0)
        assert result is None  # Negative cycle detected

    def test_no_negative_cycle(self):
        """Test Bellman-Ford with negative weights but no cycle."""
        g = WeightedGraph(3)
        g.add_edge(0, 1, -1)
        g.add_edge(1, 2, -1)
        result = bellman_ford(g, 0)
        assert result is not None
        distances, _ = result
        assert distances[2] == -2

    def test_disconnected_graph(self):
        """Test Bellman-Ford on disconnected graph."""
        g = WeightedGraph(4)
        g.add_edge(0, 1, 1)
        g.add_edge(2, 3, 1)
        result = bellman_ford(g, 0)
        assert result is not None
        distances, _ = result
        assert distances[1] == 1
        assert distances[2] == float('inf')


class TestFloydWarshall:
    """Tests for Floyd-Warshall algorithm."""

    def test_all_pairs_shortest_paths(self):
        """Test Floyd-Warshall computes all-pairs shortest paths."""
        g = WeightedGraph(4)
        g.add_edge(0, 1, 3)
        g.add_edge(0, 3, 7)
        g.add_edge(1, 2, 1)
        g.add_edge(1, 3, 2)
        g.add_edge(2, 3, 1)
        dist = floyd_warshall(g)
        assert dist is not None
        assert dist[0][3] == 5  # 0->1->3
        assert dist[0][2] == 4  # 0->1->2

    def test_direct_edges(self):
        """Test Floyd-Warshall with direct edges."""
        g = WeightedGraph(3)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 1)
        g.add_edge(0, 2, 5)
        dist = floyd_warshall(g)
        assert dist[0][2] == 2  # 0->1->2 is shorter than 0->2

    def test_negative_weights(self):
        """Test Floyd-Warshall with negative weights."""
        g = WeightedGraph(3)
        g.add_edge(0, 1, -1)
        g.add_edge(1, 2, -1)
        dist = floyd_warshall(g)
        assert dist is not None
        assert dist[0][2] == -2

    def test_negative_cycle_detection(self):
        """Test Floyd-Warshall detects negative cycles."""
        g = WeightedGraph(3)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 1)
        g.add_edge(2, 0, -5)  # Creates negative cycle
        dist = floyd_warshall(g)
        assert dist is None

    def test_single_vertex(self):
        """Test Floyd-Warshall with single vertex."""
        g = WeightedGraph(1)
        dist = floyd_warshall(g)
        assert dist[0][0] == 0


class TestNetworkDelayTime:
    """Tests for network delay time problem."""

    def test_basic_network(self):
        """Test basic network delay."""
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        result = network_delay_time(times, 4, 2)
        assert result == 2

    def test_single_edge(self):
        """Test network with single edge."""
        times = [[1, 2, 1]]
        result = network_delay_time(times, 2, 1)
        assert result == 1

    def test_unreachable_node(self):
        """Test network with unreachable node."""
        times = [[1, 2, 1]]
        result = network_delay_time(times, 2, 2)
        assert result == -1

    def test_complete_network(self):
        """Test fully connected network."""
        times = [[1, 2, 1], [1, 3, 2], [2, 3, 1]]
        result = network_delay_time(times, 3, 1)
        assert result == 2

    def test_single_node(self):
        """Test network with single node."""
        times = []
        result = network_delay_time(times, 1, 1)
        assert result == 0


class TestEdgeCases:
    """Tests for edge cases."""

    def test_empty_graph(self):
        """Test algorithms on empty graph."""
        g = WeightedGraph(1)
        distances, _ = dijkstra(g, 0)
        assert distances[0] == 0

    def test_multiple_edges_same_vertices(self):
        """Test graph with multiple edges between same vertices."""
        g = WeightedGraph(2)
        g.add_edge(0, 1, 5)
        g.add_edge(0, 1, 2)  # Should take shorter edge
        distances, _ = dijkstra(g, 0)
        assert distances[1] == 2

    def test_large_weights(self):
        """Test with large weights."""
        g = WeightedGraph(3)
        g.add_edge(0, 1, 1000000)
        g.add_edge(1, 2, 1000000)
        distances, _ = dijkstra(g, 0)
        assert distances[2] == 2000000

    def test_zero_weights(self):
        """Test with zero weights."""
        g = WeightedGraph(3)
        g.add_edge(0, 1, 0)
        g.add_edge(1, 2, 0)
        distances, _ = dijkstra(g, 0)
        assert distances[2] == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
