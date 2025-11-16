"""
Project 34: Graph Representation

This module implements various graph representations including adjacency list,
adjacency matrix, and edge list, along with conversion utilities.

Key Concepts:
- Adjacency list representation (best for sparse graphs)
- Adjacency matrix representation (best for dense graphs)
- Edge list representation (best for edge-based algorithms)
- Weighted and unweighted graphs
- Directed and undirected graphs
- Graph representation conversion

Author: Python-Edu DSA Curriculum
"""

from typing import List, Tuple, Union, Dict
from collections import defaultdict


class AdjacencyListGraph:
    """
    Graph implemented using adjacency list representation.

    Each vertex maps to a list of (neighbor, weight) tuples.
    Best for sparse graphs where E << V².

    Attributes:
        num_vertices: Number of vertices in the graph
        directed: Whether the graph is directed
        adj_list: Dictionary mapping vertex to list of (neighbor, weight) tuples

    Time Complexity:
        __init__: O(V)
        add_edge: O(1) amortized
        remove_edge: O(degree(v))
        get_neighbors: O(1)
        has_edge: O(degree(v))
        get_degree: O(1)

    Space Complexity: O(V + E)
    """

    def __init__(self, num_vertices: int, directed: bool = False):
        """
        Initialize adjacency list graph.

        Args:
            num_vertices: Number of vertices (numbered 0 to n-1)
            directed: If True, edges are directed; if False, undirected

        Examples:
            >>> g = AdjacencyListGraph(5)
            >>> g.num_vertices
            5
            >>> g.directed
            False
        """
        self.num_vertices = num_vertices
        self.directed = directed
        self.adj_list: Dict[int, List[Tuple[int, int]]] = defaultdict(list)

    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """
        Add an edge from u to v with given weight.

        For undirected graphs, adds edges in both directions.

        Args:
            u: Source vertex
            v: Destination vertex
            weight: Edge weight (default 1)

        Time Complexity: O(1) amortized
        Space Complexity: O(1)

        Examples:
            >>> g = AdjacencyListGraph(3)
            >>> g.add_edge(0, 1, weight=5)
            >>> g.add_edge(1, 2, weight=3)
            >>> len(g.adj_list[0])
            1
        """
        if u < 0 or u >= self.num_vertices or v < 0 or v >= self.num_vertices:
            raise ValueError(f"Vertex must be between 0 and {self.num_vertices - 1}")

        # Add edge u -> v
        # Check if edge already exists and update weight
        edge_exists = False
        for i, (neighbor, w) in enumerate(self.adj_list[u]):
            if neighbor == v:
                self.adj_list[u][i] = (v, weight)
                edge_exists = True
                break

        if not edge_exists:
            self.adj_list[u].append((v, weight))

        # For undirected graph, also add v -> u
        if not self.directed:
            edge_exists = False
            for i, (neighbor, w) in enumerate(self.adj_list[v]):
                if neighbor == u:
                    self.adj_list[v][i] = (u, weight)
                    edge_exists = True
                    break

            if not edge_exists:
                self.adj_list[v].append((u, weight))

    def remove_edge(self, u: int, v: int) -> None:
        """
        Remove edge from u to v.

        Args:
            u: Source vertex
            v: Destination vertex

        Time Complexity: O(degree(u))
        Space Complexity: O(1)

        Examples:
            >>> g = AdjacencyListGraph(3)
            >>> g.add_edge(0, 1)
            >>> g.remove_edge(0, 1)
            >>> g.has_edge(0, 1)
            False
        """
        if u < 0 or u >= self.num_vertices or v < 0 or v >= self.num_vertices:
            return

        # Remove edge u -> v
        self.adj_list[u] = [(neighbor, w) for neighbor, w in self.adj_list[u] if neighbor != v]

        # For undirected graph, also remove v -> u
        if not self.directed:
            self.adj_list[v] = [(neighbor, w) for neighbor, w in self.adj_list[v] if neighbor != u]

    def get_neighbors(self, vertex: int) -> List[Tuple[int, int]]:
        """
        Get all neighbors of a vertex with their edge weights.

        Args:
            vertex: The vertex to get neighbors for

        Returns:
            List of (neighbor, weight) tuples

        Time Complexity: O(1)
        Space Complexity: O(1) - returns reference

        Examples:
            >>> g = AdjacencyListGraph(3)
            >>> g.add_edge(0, 1, weight=5)
            >>> g.add_edge(0, 2, weight=3)
            >>> neighbors = g.get_neighbors(0)
            >>> len(neighbors)
            2
        """
        if vertex < 0 or vertex >= self.num_vertices:
            raise ValueError(f"Vertex must be between 0 and {self.num_vertices - 1}")

        return self.adj_list[vertex]

    def has_edge(self, u: int, v: int) -> bool:
        """
        Check if edge exists from u to v.

        Args:
            u: Source vertex
            v: Destination vertex

        Returns:
            True if edge exists, False otherwise

        Time Complexity: O(degree(u))
        Space Complexity: O(1)

        Examples:
            >>> g = AdjacencyListGraph(3)
            >>> g.add_edge(0, 1)
            >>> g.has_edge(0, 1)
            True
            >>> g.has_edge(1, 2)
            False
        """
        if u < 0 or u >= self.num_vertices or v < 0 or v >= self.num_vertices:
            return False

        return any(neighbor == v for neighbor, _ in self.adj_list[u])

    def get_degree(self, vertex: int) -> int:
        """
        Get the degree of a vertex (number of edges).

        Args:
            vertex: The vertex

        Returns:
            Degree of the vertex

        Time Complexity: O(1)
        Space Complexity: O(1)

        Examples:
            >>> g = AdjacencyListGraph(4)
            >>> g.add_edge(0, 1)
            >>> g.add_edge(0, 2)
            >>> g.get_degree(0)
            2
        """
        if vertex < 0 or vertex >= self.num_vertices:
            raise ValueError(f"Vertex must be between 0 and {self.num_vertices - 1}")

        return len(self.adj_list[vertex])


class AdjacencyMatrixGraph:
    """
    Graph implemented using adjacency matrix representation.

    matrix[i][j] = weight if edge exists, 0 if no edge.
    Best for dense graphs where E ≈ V².

    Attributes:
        num_vertices: Number of vertices
        directed: Whether the graph is directed
        matrix: 2D array representing edges

    Time Complexity:
        __init__: O(V²)
        add_edge: O(1)
        remove_edge: O(1)
        get_neighbors: O(V)
        has_edge: O(1)
        get_degree: O(V)

    Space Complexity: O(V²)
    """

    def __init__(self, num_vertices: int, directed: bool = False):
        """
        Initialize adjacency matrix graph.

        Args:
            num_vertices: Number of vertices (numbered 0 to n-1)
            directed: If True, edges are directed; if False, undirected

        Examples:
            >>> g = AdjacencyMatrixGraph(3)
            >>> len(g.matrix)
            3
            >>> len(g.matrix[0])
            3
        """
        self.num_vertices = num_vertices
        self.directed = directed
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """
        Add an edge from u to v with given weight.

        Args:
            u: Source vertex
            v: Destination vertex
            weight: Edge weight (default 1)

        Time Complexity: O(1)
        Space Complexity: O(1)

        Examples:
            >>> g = AdjacencyMatrixGraph(3)
            >>> g.add_edge(0, 1, weight=5)
            >>> g.matrix[0][1]
            5
        """
        if u < 0 or u >= self.num_vertices or v < 0 or v >= self.num_vertices:
            raise ValueError(f"Vertex must be between 0 and {self.num_vertices - 1}")

        self.matrix[u][v] = weight

        if not self.directed:
            self.matrix[v][u] = weight

    def remove_edge(self, u: int, v: int) -> None:
        """
        Remove edge from u to v.

        Args:
            u: Source vertex
            v: Destination vertex

        Time Complexity: O(1)
        Space Complexity: O(1)

        Examples:
            >>> g = AdjacencyMatrixGraph(3)
            >>> g.add_edge(0, 1)
            >>> g.remove_edge(0, 1)
            >>> g.matrix[0][1]
            0
        """
        if u < 0 or u >= self.num_vertices or v < 0 or v >= self.num_vertices:
            return

        self.matrix[u][v] = 0

        if not self.directed:
            self.matrix[v][u] = 0

    def get_neighbors(self, vertex: int) -> List[Tuple[int, int]]:
        """
        Get all neighbors of a vertex with their edge weights.

        Args:
            vertex: The vertex to get neighbors for

        Returns:
            List of (neighbor, weight) tuples

        Time Complexity: O(V)
        Space Complexity: O(V) - in worst case all vertices are neighbors

        Examples:
            >>> g = AdjacencyMatrixGraph(3)
            >>> g.add_edge(0, 1, weight=5)
            >>> g.add_edge(0, 2, weight=3)
            >>> neighbors = g.get_neighbors(0)
            >>> len(neighbors)
            2
        """
        if vertex < 0 or vertex >= self.num_vertices:
            raise ValueError(f"Vertex must be between 0 and {self.num_vertices - 1}")

        neighbors = []
        for v in range(self.num_vertices):
            if self.matrix[vertex][v] != 0:
                neighbors.append((v, self.matrix[vertex][v]))

        return neighbors

    def has_edge(self, u: int, v: int) -> bool:
        """
        Check if edge exists from u to v.

        Args:
            u: Source vertex
            v: Destination vertex

        Returns:
            True if edge exists, False otherwise

        Time Complexity: O(1)
        Space Complexity: O(1)

        Examples:
            >>> g = AdjacencyMatrixGraph(3)
            >>> g.add_edge(0, 1)
            >>> g.has_edge(0, 1)
            True
            >>> g.has_edge(1, 2)
            False
        """
        if u < 0 or u >= self.num_vertices or v < 0 or v >= self.num_vertices:
            return False

        return self.matrix[u][v] != 0

    def get_degree(self, vertex: int) -> int:
        """
        Get the degree of a vertex (number of edges).

        Args:
            vertex: The vertex

        Returns:
            Degree of the vertex

        Time Complexity: O(V)
        Space Complexity: O(1)

        Examples:
            >>> g = AdjacencyMatrixGraph(4)
            >>> g.add_edge(0, 1)
            >>> g.add_edge(0, 2)
            >>> g.get_degree(0)
            2
        """
        if vertex < 0 or vertex >= self.num_vertices:
            raise ValueError(f"Vertex must be between 0 and {self.num_vertices - 1}")

        return sum(1 for weight in self.matrix[vertex] if weight != 0)


class EdgeListGraph:
    """
    Graph implemented using edge list representation.

    Stores list of (u, v, weight) tuples.
    Best for edge-centric algorithms like Kruskal's MST.

    Attributes:
        num_vertices: Number of vertices
        directed: Whether the graph is directed
        edges: List of (u, v, weight) tuples

    Time Complexity:
        __init__: O(1)
        add_edge: O(1)
        remove_edge: O(E)
        get_edges: O(1)
        has_edge: O(E)
        sort_edges_by_weight: O(E log E)

    Space Complexity: O(E)
    """

    def __init__(self, num_vertices: int, directed: bool = False):
        """
        Initialize edge list graph.

        Args:
            num_vertices: Number of vertices (numbered 0 to n-1)
            directed: If True, edges are directed; if False, undirected

        Examples:
            >>> g = EdgeListGraph(5)
            >>> g.num_vertices
            5
            >>> len(g.edges)
            0
        """
        self.num_vertices = num_vertices
        self.directed = directed
        self.edges: List[Tuple[int, int, int]] = []

    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """
        Add an edge from u to v with given weight.

        Args:
            u: Source vertex
            v: Destination vertex
            weight: Edge weight (default 1)

        Time Complexity: O(1)
        Space Complexity: O(1)

        Examples:
            >>> g = EdgeListGraph(3)
            >>> g.add_edge(0, 1, weight=5)
            >>> len(g.edges)
            1
        """
        if u < 0 or u >= self.num_vertices or v < 0 or v >= self.num_vertices:
            raise ValueError(f"Vertex must be between 0 and {self.num_vertices - 1}")

        # For undirected graphs, normalize edge representation (smaller vertex first)
        if not self.directed and u > v:
            u, v = v, u

        # Check if edge already exists
        for i, (eu, ev, ew) in enumerate(self.edges):
            if eu == u and ev == v:
                self.edges[i] = (u, v, weight)
                return

        self.edges.append((u, v, weight))

    def remove_edge(self, u: int, v: int) -> None:
        """
        Remove edge from u to v.

        Args:
            u: Source vertex
            v: Destination vertex

        Time Complexity: O(E)
        Space Complexity: O(1)

        Examples:
            >>> g = EdgeListGraph(3)
            >>> g.add_edge(0, 1)
            >>> g.remove_edge(0, 1)
            >>> len(g.edges)
            0
        """
        if u < 0 or u >= self.num_vertices or v < 0 or v >= self.num_vertices:
            return

        # For undirected graphs, normalize
        if not self.directed and u > v:
            u, v = v, u

        self.edges = [(eu, ev, ew) for eu, ev, ew in self.edges if not (eu == u and ev == v)]

    def get_edges(self) -> List[Tuple[int, int, int]]:
        """
        Get all edges in the graph.

        Returns:
            List of (u, v, weight) tuples

        Time Complexity: O(1)
        Space Complexity: O(1) - returns reference

        Examples:
            >>> g = EdgeListGraph(3)
            >>> g.add_edge(0, 1, weight=5)
            >>> g.add_edge(1, 2, weight=3)
            >>> len(g.get_edges())
            2
        """
        return self.edges

    def has_edge(self, u: int, v: int) -> bool:
        """
        Check if edge exists from u to v.

        Args:
            u: Source vertex
            v: Destination vertex

        Returns:
            True if edge exists, False otherwise

        Time Complexity: O(E)
        Space Complexity: O(1)

        Examples:
            >>> g = EdgeListGraph(3)
            >>> g.add_edge(0, 1)
            >>> g.has_edge(0, 1)
            True
            >>> g.has_edge(1, 2)
            False
        """
        if u < 0 or u >= self.num_vertices or v < 0 or v >= self.num_vertices:
            return False

        # For undirected graphs, check both directions
        if not self.directed:
            return any((eu == u and ev == v) or (eu == v and ev == u) for eu, ev, _ in self.edges)
        else:
            return any(eu == u and ev == v for eu, ev, _ in self.edges)

    def sort_edges_by_weight(self) -> List[Tuple[int, int, int]]:
        """
        Get edges sorted by weight (ascending).

        Returns:
            Sorted list of (u, v, weight) tuples

        Time Complexity: O(E log E)
        Space Complexity: O(E)

        Examples:
            >>> g = EdgeListGraph(4)
            >>> g.add_edge(0, 1, weight=10)
            >>> g.add_edge(1, 2, weight=5)
            >>> g.add_edge(2, 3, weight=8)
            >>> sorted_edges = g.sort_edges_by_weight()
            >>> sorted_edges[0][2]
            5
        """
        return sorted(self.edges, key=lambda edge: edge[2])


def convert_adjacency_list_to_matrix(adj_list: AdjacencyListGraph) -> AdjacencyMatrixGraph:
    """
    Convert adjacency list graph to adjacency matrix graph.

    Args:
        adj_list: Source graph in adjacency list format

    Returns:
        Equivalent graph in adjacency matrix format

    Time Complexity: O(V² + E)
    Space Complexity: O(V²)

    Examples:
        >>> list_graph = AdjacencyListGraph(3)
        >>> list_graph.add_edge(0, 1, weight=5)
        >>> matrix_graph = convert_adjacency_list_to_matrix(list_graph)
        >>> matrix_graph.has_edge(0, 1)
        True
    """
    matrix_graph = AdjacencyMatrixGraph(adj_list.num_vertices, adj_list.directed)

    for u in range(adj_list.num_vertices):
        for v, weight in adj_list.get_neighbors(u):
            # For undirected graphs, only add edge once (when u < v)
            if adj_list.directed or u <= v:
                matrix_graph.add_edge(u, v, weight)

    return matrix_graph


def convert_adjacency_matrix_to_list(adj_matrix: AdjacencyMatrixGraph) -> AdjacencyListGraph:
    """
    Convert adjacency matrix graph to adjacency list graph.

    Args:
        adj_matrix: Source graph in adjacency matrix format

    Returns:
        Equivalent graph in adjacency list format

    Time Complexity: O(V²)
    Space Complexity: O(V + E)

    Examples:
        >>> matrix_graph = AdjacencyMatrixGraph(3)
        >>> matrix_graph.add_edge(0, 1, weight=5)
        >>> list_graph = convert_adjacency_matrix_to_list(matrix_graph)
        >>> list_graph.has_edge(0, 1)
        True
    """
    list_graph = AdjacencyListGraph(adj_matrix.num_vertices, adj_matrix.directed)

    for u in range(adj_matrix.num_vertices):
        for v in range(adj_matrix.num_vertices):
            if adj_matrix.matrix[u][v] != 0:
                # For undirected graphs, only add edge once (when u < v)
                if adj_matrix.directed or u <= v:
                    list_graph.add_edge(u, v, adj_matrix.matrix[u][v])

    return list_graph


def convert_to_edge_list(graph: Union[AdjacencyListGraph, AdjacencyMatrixGraph]) -> EdgeListGraph:
    """
    Convert any graph representation to edge list.

    Args:
        graph: Source graph (adjacency list or matrix)

    Returns:
        Equivalent graph in edge list format

    Time Complexity: O(V²) for matrix, O(V + E) for list
    Space Complexity: O(E)

    Examples:
        >>> list_graph = AdjacencyListGraph(3)
        >>> list_graph.add_edge(0, 1, weight=5)
        >>> edge_list = convert_to_edge_list(list_graph)
        >>> len(edge_list.edges)
        1
    """
    edge_graph = EdgeListGraph(graph.num_vertices, graph.directed)

    if isinstance(graph, AdjacencyListGraph):
        for u in range(graph.num_vertices):
            for v, weight in graph.get_neighbors(u):
                # For undirected graphs, only add edge once
                if graph.directed or u <= v:
                    edge_graph.add_edge(u, v, weight)

    elif isinstance(graph, AdjacencyMatrixGraph):
        for u in range(graph.num_vertices):
            for v in range(graph.num_vertices):
                if graph.matrix[u][v] != 0:
                    # For undirected graphs, only add edge once
                    if graph.directed or u <= v:
                        edge_graph.add_edge(u, v, graph.matrix[u][v])

    return edge_graph


if __name__ == "__main__":
    # Demonstration of graph representations
    print("Graph Representation Demonstrations")
    print("=" * 70)

    # Test 1: Adjacency List
    print("\n1. Adjacency List Representation:")
    adj_list = AdjacencyListGraph(4)
    adj_list.add_edge(0, 1, weight=5)
    adj_list.add_edge(0, 2, weight=3)
    adj_list.add_edge(1, 3, weight=2)
    adj_list.add_edge(2, 3, weight=7)
    print(f"   Neighbors of vertex 0: {adj_list.get_neighbors(0)}")
    print(f"   Degree of vertex 0: {adj_list.get_degree(0)}")
    print(f"   Has edge 0→1: {adj_list.has_edge(0, 1)}")

    # Test 2: Adjacency Matrix
    print("\n2. Adjacency Matrix Representation:")
    adj_matrix = AdjacencyMatrixGraph(4)
    adj_matrix.add_edge(0, 1, weight=5)
    adj_matrix.add_edge(0, 2, weight=3)
    adj_matrix.add_edge(1, 3, weight=2)
    adj_matrix.add_edge(2, 3, weight=7)
    print(f"   Matrix row 0: {adj_matrix.matrix[0]}")
    print(f"   Neighbors of vertex 0: {adj_matrix.get_neighbors(0)}")
    print(f"   Has edge 0→1: {adj_matrix.has_edge(0, 1)}")

    # Test 3: Edge List
    print("\n3. Edge List Representation:")
    edge_list = EdgeListGraph(4)
    edge_list.add_edge(0, 1, weight=10)
    edge_list.add_edge(1, 2, weight=5)
    edge_list.add_edge(2, 3, weight=8)
    edge_list.add_edge(0, 3, weight=3)
    print(f"   All edges: {edge_list.get_edges()}")
    sorted_edges = edge_list.sort_edges_by_weight()
    print(f"   Edges sorted by weight: {sorted_edges}")

    # Test 4: Conversions
    print("\n4. Graph Conversions:")
    list_graph = AdjacencyListGraph(3)
    list_graph.add_edge(0, 1, weight=5)
    list_graph.add_edge(1, 2, weight=3)

    matrix_graph = convert_adjacency_list_to_matrix(list_graph)
    print(f"   Converted to matrix: {matrix_graph.matrix}")

    edge_graph = convert_to_edge_list(list_graph)
    print(f"   Converted to edge list: {edge_graph.edges}")

    print("\n" + "=" * 70)
    print("All graph representations demonstrated!")
