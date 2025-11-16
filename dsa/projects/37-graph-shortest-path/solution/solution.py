"""
Project 37: Shortest Path Algorithms

This module implements shortest path algorithms for weighted graphs:
- Dijkstra's algorithm (non-negative weights)
- Bellman-Ford algorithm (handles negative weights)
- Floyd-Warshall algorithm (all-pairs shortest paths)
- Network delay time problem

Key Concepts:
- Weighted graphs
- Single-source shortest path (SSSP)
- All-pairs shortest path (APSP)
- Negative cycle detection
- Priority queues / min-heaps

Author: Python-Edu DSA Curriculum
"""

from typing import List, Dict, Optional, Tuple
from collections import defaultdict
import heapq


class WeightedGraph:
    """
    Weighted directed graph using adjacency list representation.

    Attributes:
        num_vertices: Number of vertices in graph
        adjacency_list: Dict mapping vertex -> list of (neighbor, weight) tuples
        edges: List of all edges as (u, v, weight) tuples
    """

    def __init__(self, num_vertices: int):
        """Initialize weighted graph with given number of vertices."""
        self.num_vertices = num_vertices
        self.adjacency_list: Dict[int, List[Tuple[int, float]]] = defaultdict(list)
        self.edges: List[Tuple[int, int, float]] = []

    def add_edge(self, u: int, v: int, weight: float, directed: bool = True) -> None:
        """
        Add weighted edge from u to v.

        Args:
            u: Source vertex
            v: Destination vertex
            weight: Edge weight
            directed: If True, add only u→v. If False, add both u→v and v→u
        """
        self.adjacency_list[u].append((v, weight))
        self.edges.append((u, v, weight))

        if not directed:
            self.adjacency_list[v].append((u, weight))
            self.edges.append((v, u, weight))

    def get_neighbors(self, vertex: int) -> List[Tuple[int, float]]:
        """Get neighbors of vertex as list of (neighbor, weight) tuples."""
        return self.adjacency_list[vertex]


def dijkstra(graph: WeightedGraph, start: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]:
    """
    Find shortest paths from start vertex using Dijkstra's algorithm.

    Dijkstra's algorithm finds shortest paths from a source to all other vertices
    in graphs with non-negative edge weights. Uses a priority queue to greedily
    select the unvisited vertex with minimum distance.

    Algorithm:
    1. Initialize distances: dist[start] = 0, all others = ∞
    2. Use min-heap priority queue with (distance, vertex)
    3. While queue not empty:
       - Pop vertex with minimum distance
       - For each neighbor:
         - Calculate new distance via current vertex
         - If new distance < current distance:
           - Update distance and parent
           - Add to queue
    4. Return distances and parents

    Args:
        graph: Weighted graph
        start: Starting vertex

    Returns:
        Tuple of (distances dict, parents dict)
        - distances[v] = shortest distance from start to v
        - parents[v] = parent of v in shortest path tree

    Time Complexity: O((V + E) log V) with binary heap
    Space Complexity: O(V)

    Examples:
        >>> g = WeightedGraph(5)
        >>> g.add_edge(0, 1, 4)
        >>> g.add_edge(0, 2, 1)
        >>> g.add_edge(2, 1, 2)
        >>> g.add_edge(1, 3, 1)
        >>> distances, parents = dijkstra(g, 0)
        >>> distances[1]
        3
        >>> distances[3]
        4
    """
    # Initialize distances and parents
    distances = {i: float('inf') for i in range(graph.num_vertices)}
    parents: Dict[int, Optional[int]] = {i: None for i in range(graph.num_vertices)}
    distances[start] = 0

    # Priority queue: (distance, vertex)
    pq = [(0, start)]
    visited = set()

    while pq:
        current_dist, u = heapq.heappop(pq)

        # Skip if already visited (may have duplicate entries in queue)
        if u in visited:
            continue

        visited.add(u)

        # Relaxation: check all neighbors
        for v, weight in graph.get_neighbors(u):
            new_dist = current_dist + weight

            # Update if found shorter path
            if new_dist < distances[v]:
                distances[v] = new_dist
                parents[v] = u
                heapq.heappush(pq, (new_dist, v))

    return distances, parents


def bellman_ford(graph: WeightedGraph, start: int) -> Optional[Tuple[Dict[int, float], Dict[int, Optional[int]]]]:
    """
    Find shortest paths using Bellman-Ford algorithm (handles negative weights).

    Bellman-Ford can handle graphs with negative edge weights and detects
    negative cycles. It relaxes all edges V-1 times, then checks for negative cycles.

    Algorithm:
    1. Initialize distances: dist[start] = 0, all others = ∞
    2. Relax all edges V-1 times:
       - For each edge (u, v, weight):
         - If dist[u] + weight < dist[v]:
           - Update dist[v] and parent[v]
    3. Check for negative cycles:
       - Try relaxing all edges one more time
       - If any distance improves → negative cycle exists
    4. Return distances and parents (or None if negative cycle)

    Args:
        graph: Weighted graph
        start: Starting vertex

    Returns:
        Tuple of (distances dict, parents dict), or None if negative cycle detected

    Time Complexity: O(V × E)
    Space Complexity: O(V)

    Examples:
        >>> g = WeightedGraph(4)
        >>> g.add_edge(0, 1, -1)
        >>> g.add_edge(0, 2, 4)
        >>> g.add_edge(1, 2, 3)
        >>> distances, parents = bellman_ford(g, 0)
        >>> distances[1]
        -1
        >>> distances[2]
        2
    """
    # Initialize distances and parents
    distances = {i: float('inf') for i in range(graph.num_vertices)}
    parents: Dict[int, Optional[int]] = {i: None for i in range(graph.num_vertices)}
    distances[start] = 0

    # Relax all edges V-1 times
    for _ in range(graph.num_vertices - 1):
        for u, v, weight in graph.edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                parents[v] = u

    # Check for negative cycles
    for u, v, weight in graph.edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            # Negative cycle detected
            return None

    return distances, parents


def floyd_warshall(graph: WeightedGraph) -> Optional[List[List[float]]]:
    """
    Find all-pairs shortest paths using Floyd-Warshall algorithm.

    Floyd-Warshall computes shortest paths between all pairs of vertices.
    Uses dynamic programming with intermediate vertices.

    Algorithm:
    1. Initialize distance matrix:
       - dist[i][i] = 0
       - dist[i][j] = edge weight if edge exists
       - dist[i][j] = ∞ otherwise
    2. For each intermediate vertex k:
       - For each pair (i, j):
         - dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    3. Check for negative cycles:
       - If any dist[i][i] < 0 → negative cycle
    4. Return distance matrix

    Args:
        graph: Weighted graph

    Returns:
        2D distance matrix, or None if negative cycle detected
        dist[i][j] = shortest distance from vertex i to vertex j

    Time Complexity: O(V³)
    Space Complexity: O(V²)

    Examples:
        >>> g = WeightedGraph(3)
        >>> g.add_edge(0, 1, 4)
        >>> g.add_edge(1, 2, 3)
        >>> g.add_edge(0, 2, 10)
        >>> dist = floyd_warshall(g)
        >>> dist[0][2]
        7.0
    """
    n = graph.num_vertices

    # Initialize distance matrix
    dist = [[float('inf')] * n for _ in range(n)]

    # Distance from vertex to itself is 0
    for i in range(n):
        dist[i][i] = 0

    # Set distances for existing edges
    for u, v, weight in graph.edges:
        dist[u][v] = min(dist[u][v], weight)  # Handle multiple edges

    # Floyd-Warshall: consider each vertex as intermediate
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Check for negative cycles
    for i in range(n):
        if dist[i][i] < 0:
            return None  # Negative cycle detected

    return dist


def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    """
    Calculate time for signal to reach all nodes in network (LeetCode 743).

    Given directed weighted graph where times[i] = [u, v, w] means signal
    takes w time to travel from node u to node v. Starting from node k,
    return time for all nodes to receive signal. Return -1 if impossible.

    Approach: Use Dijkstra's algorithm
    1. Build weighted graph from times
    2. Run Dijkstra from node k
    3. Find maximum distance (bottleneck)
    4. Return max distance, or -1 if any node unreachable

    Args:
        times: List of [u, v, w] edges (1-indexed nodes)
        n: Number of nodes (1 to n)
        k: Starting node (1-indexed)

    Returns:
        Minimum time for all nodes to receive signal, or -1 if impossible

    Time Complexity: O((V + E) log V)
    Space Complexity: O(V + E)

    Examples:
        >>> network_delay_time([[2,1,1], [2,3,1], [3,4,1]], 4, 2)
        2
        >>> network_delay_time([[1,2,1]], 2, 1)
        1
        >>> network_delay_time([[1,2,1]], 2, 2)
        -1
    """
    # Build weighted graph (convert to 0-indexed)
    graph = WeightedGraph(n + 1)  # Nodes 1 to n, ignore index 0
    for u, v, w in times:
        graph.add_edge(u, v, w, directed=True)

    # Run Dijkstra from node k
    distances, _ = dijkstra(graph, k)

    # Find maximum distance among nodes 1 to n
    max_time = 0
    for node in range(1, n + 1):
        if distances[node] == float('inf'):
            return -1  # Node unreachable
        max_time = max(max_time, distances[node])

    return int(max_time)


def get_shortest_path(start: int, end: int, parents: Dict[int, Optional[int]]) -> Optional[List[int]]:
    """
    Reconstruct shortest path from start to end using parent pointers.

    Args:
        start: Starting vertex
        end: Ending vertex
        parents: Parent dictionary from shortest path algorithm

    Returns:
        Path from start to end, or None if no path exists

    Examples:
        >>> parents = {0: None, 1: 0, 2: 1, 3: 2}
        >>> get_shortest_path(0, 3, parents)
        [0, 1, 2, 3]
    """
    if parents[end] is None and start != end:
        return None  # No path exists

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parents[current]

    path.reverse()
    return path


if __name__ == "__main__":
    print("Shortest Path Algorithms Demonstration")
    print("=" * 70)

    # Test 1: Dijkstra's Algorithm
    print("\n1. Dijkstra's Algorithm:")
    g1 = WeightedGraph(5)
    g1.add_edge(0, 1, 4)
    g1.add_edge(0, 2, 1)
    g1.add_edge(2, 1, 2)
    g1.add_edge(1, 3, 1)
    g1.add_edge(2, 3, 5)
    g1.add_edge(3, 4, 3)

    distances, parents = dijkstra(g1, 0)
    print(f"   Distances from vertex 0: {dict(sorted(distances.items()))}")
    path = get_shortest_path(0, 4, parents)
    print(f"   Shortest path 0→4: {path}")
    print(f"   Total distance: {distances[4]}")

    # Test 2: Bellman-Ford Algorithm
    print("\n2. Bellman-Ford Algorithm (with negative weights):")
    g2 = WeightedGraph(5)
    g2.add_edge(0, 1, -1)
    g2.add_edge(0, 2, 4)
    g2.add_edge(1, 2, 3)
    g2.add_edge(1, 3, 2)
    g2.add_edge(1, 4, 2)
    g2.add_edge(3, 2, 5)
    g2.add_edge(3, 1, 1)
    g2.add_edge(4, 3, -3)

    result = bellman_ford(g2, 0)
    if result:
        distances, parents = result
        print(f"   Distances from vertex 0: {dict(sorted(distances.items()))}")
    else:
        print(f"   Negative cycle detected!")

    # Test 3: Bellman-Ford with negative cycle
    print("\n3. Bellman-Ford with Negative Cycle:")
    g3 = WeightedGraph(3)
    g3.add_edge(0, 1, 1)
    g3.add_edge(1, 2, -3)
    g3.add_edge(2, 1, 2)  # Creates negative cycle

    result = bellman_ford(g3, 0)
    if result:
        print(f"   No negative cycle")
    else:
        print(f"   Negative cycle detected! (1→2→1 has total weight -1)")

    # Test 4: Floyd-Warshall Algorithm
    print("\n4. Floyd-Warshall Algorithm (All-Pairs Shortest Paths):")
    g4 = WeightedGraph(4)
    g4.add_edge(0, 1, 3)
    g4.add_edge(0, 3, 7)
    g4.add_edge(1, 2, 1)
    g4.add_edge(1, 3, 2)
    g4.add_edge(2, 3, 1)

    dist_matrix = floyd_warshall(g4)
    if dist_matrix:
        print(f"   Distance matrix:")
        for i, row in enumerate(dist_matrix):
            formatted_row = [f"{d:5.0f}" if d != float('inf') else "  INF" for d in row]
            print(f"   {i}: [{', '.join(formatted_row)}]")
        print(f"\n   Shortest distance 0→3: {dist_matrix[0][3]} (via 0→1→3)")
        print(f"   Shortest distance 0→2: {dist_matrix[0][2]} (via 0→1→2)")

    # Test 5: Network Delay Time
    print("\n5. Network Delay Time:")
    times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n1, k1 = 4, 2
    delay = network_delay_time(times1, n1, k1)
    print(f"   Network: {times1}")
    print(f"   Starting from node {k1}")
    print(f"   Time to reach all nodes: {delay}")

    times2 = [[1, 2, 1]]
    n2, k2 = 2, 2
    delay2 = network_delay_time(times2, n2, k2)
    print(f"\n   Network: {times2}")
    print(f"   Starting from node {k2}")
    print(f"   Time to reach all nodes: {delay2} (impossible - node 1 unreachable)")

    print("\n" + "=" * 70)
    print("All shortest path algorithms demonstrated!")
