"""
Project 35: Depth-First Search (DFS)

This module implements graph data structures and DFS algorithms for graph traversal,
path finding, cycle detection, and other graph-related problems.

Key Concepts:
- Graph representations (adjacency list and adjacency matrix)
- DFS recursive and iterative implementations
- Path finding algorithms
- Connected components
- Cycle detection (directed and undirected)
- Topological sorting
- Bipartite graph checking

Author: Python-Edu DSA Curriculum
"""

from typing import List, Optional, Set, Dict
from collections import defaultdict


class Graph:
    """
    Graph data structure supporting both adjacency list and adjacency matrix representations.

    A graph is a collection of vertices (nodes) connected by edges. This implementation
    supports both directed and undirected graphs.

    Attributes:
        num_vertices: Number of vertices in the graph (numbered 0 to n-1)
        representation: Type of representation ("adjacency_list" or "adjacency_matrix")
        adjacency_list: Dictionary mapping vertex to list of neighbors (if using list representation)
        adjacency_matrix: 2D array representing edges (if using matrix representation)

    Time Complexity:
        __init__: O(V²) for matrix, O(V) for list
        add_edge: O(1) for both representations
        get_neighbors: O(1) for list, O(V) for matrix
        has_edge: O(V) for list, O(1) for matrix

    Space Complexity: O(V²) for matrix, O(V + E) for list
    """

    def __init__(self, num_vertices: int, representation: str = "adjacency_list"):
        """
        Initialize a graph with specified number of vertices and representation type.

        Args:
            num_vertices: Number of vertices in the graph (vertices numbered 0 to n-1)
            representation: Type of representation - "adjacency_list" or "adjacency_matrix"

        Raises:
            ValueError: If representation type is invalid

        Examples:
            >>> g = Graph(5, "adjacency_list")
            >>> g.num_vertices
            5
            >>> g = Graph(3, "adjacency_matrix")
            >>> len(g.adjacency_matrix)
            3
        """
        if representation not in ["adjacency_list", "adjacency_matrix"]:
            raise ValueError("Representation must be 'adjacency_list' or 'adjacency_matrix'")

        self.num_vertices = num_vertices
        self.representation = representation

        if representation == "adjacency_list":
            # Initialize adjacency list as dictionary of lists
            self.adjacency_list: Dict[int, List[int]] = defaultdict(list)
            self.adjacency_matrix = None
        else:
            # Initialize adjacency matrix as 2D array of zeros
            self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
            self.adjacency_list = None

    def add_edge(self, u: int, v: int, directed: bool = False) -> None:
        """
        Add an edge from vertex u to vertex v.

        For undirected graphs, this adds edges in both directions.
        For directed graphs, only adds edge from u to v.

        Args:
            u: Source vertex
            v: Destination vertex
            directed: If True, edge is directed (u → v). If False, edge is undirected (u ↔ v)

        Time Complexity: O(1) for both representations
        Space Complexity: O(1)

        Examples:
            >>> g = Graph(3, "adjacency_list")
            >>> g.add_edge(0, 1)
            >>> g.get_neighbors(0)
            [1]
            >>> g.get_neighbors(1)
            [0]
        """
        # Validate vertices
        if u < 0 or u >= self.num_vertices or v < 0 or v >= self.num_vertices:
            raise ValueError(f"Vertex must be between 0 and {self.num_vertices - 1}")

        if self.representation == "adjacency_list":
            # Add edge to adjacency list
            if v not in self.adjacency_list[u]:
                self.adjacency_list[u].append(v)

            # For undirected graph, add reverse edge
            if not directed and u not in self.adjacency_list[v]:
                self.adjacency_list[v].append(u)
        else:
            # Add edge to adjacency matrix
            self.adjacency_matrix[u][v] = 1

            # For undirected graph, add reverse edge
            if not directed:
                self.adjacency_matrix[v][u] = 1

    def get_neighbors(self, vertex: int) -> List[int]:
        """
        Get all neighbors of a vertex.

        Args:
            vertex: The vertex to get neighbors for

        Returns:
            List of neighboring vertices

        Time Complexity: O(1) for adjacency list, O(V) for adjacency matrix
        Space Complexity: O(degree(vertex)) for adjacency list, O(V) for matrix

        Examples:
            >>> g = Graph(3)
            >>> g.add_edge(0, 1)
            >>> g.add_edge(0, 2)
            >>> sorted(g.get_neighbors(0))
            [1, 2]
        """
        if vertex < 0 or vertex >= self.num_vertices:
            raise ValueError(f"Vertex must be between 0 and {self.num_vertices - 1}")

        if self.representation == "adjacency_list":
            return self.adjacency_list[vertex]
        else:
            # For adjacency matrix, find all vertices with edge
            neighbors = []
            for v in range(self.num_vertices):
                if self.adjacency_matrix[vertex][v] == 1:
                    neighbors.append(v)
            return neighbors

    def has_edge(self, u: int, v: int) -> bool:
        """
        Check if an edge exists from vertex u to vertex v.

        Args:
            u: Source vertex
            v: Destination vertex

        Returns:
            True if edge exists, False otherwise

        Time Complexity: O(degree(u)) for adjacency list, O(1) for matrix
        Space Complexity: O(1)

        Examples:
            >>> g = Graph(3)
            >>> g.add_edge(0, 1)
            >>> g.has_edge(0, 1)
            True
            >>> g.has_edge(1, 2)
            False
        """
        if u < 0 or u >= self.num_vertices or v < 0 or v >= self.num_vertices:
            return False

        if self.representation == "adjacency_list":
            return v in self.adjacency_list[u]
        else:
            return self.adjacency_matrix[u][v] == 1


def dfs_recursive(graph: Graph, start: int) -> List[int]:
    """
    Perform Depth-First Search starting from a given vertex (recursive implementation).

    DFS explores as far as possible along each branch before backtracking.
    This implementation uses the call stack implicitly for recursion.

    Algorithm:
    1. Create a visited set to track visited vertices
    2. Create a result list to store visit order
    3. Define recursive helper function:
       - Mark current vertex as visited
       - Add to result list
       - Recursively visit all unvisited neighbors
    4. Call helper function on start vertex
    5. Return the visit order

    Args:
        graph: The graph to traverse
        start: Starting vertex for DFS

    Returns:
        List of vertices in the order they were visited

    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V) for visited set and recursion stack

    Examples:
        >>> g = Graph(4)
        >>> g.add_edge(0, 1, directed=True)
        >>> g.add_edge(1, 2, directed=True)
        >>> g.add_edge(2, 3, directed=True)
        >>> dfs_recursive(g, 0)
        [0, 1, 2, 3]

        >>> g = Graph(4)
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> g.add_edge(1, 3)
        >>> result = dfs_recursive(g, 0)
        >>> result[0]
        0
    """
    visited: Set[int] = set()
    result: List[int] = []

    def dfs_helper(vertex: int) -> None:
        """Recursive helper function for DFS."""
        # Mark as visited
        visited.add(vertex)
        result.append(vertex)

        # Recursively visit all unvisited neighbors
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs_helper(neighbor)

    # Start DFS from the starting vertex
    dfs_helper(start)
    return result


def dfs_iterative(graph: Graph, start: int) -> List[int]:
    """
    Perform Depth-First Search starting from a given vertex (iterative implementation).

    This implementation uses an explicit stack instead of recursion.
    The visit order may differ slightly from recursive DFS due to the order
    neighbors are pushed onto the stack, but both are valid DFS traversals.

    Algorithm:
    1. Create a stack and push start vertex
    2. Create visited set and result list
    3. While stack is not empty:
       - Pop vertex from stack
       - If not visited:
         - Mark as visited
         - Add to result
         - Push all unvisited neighbors to stack
    4. Return visit order

    Args:
        graph: The graph to traverse
        start: Starting vertex for DFS

    Returns:
        List of vertices in the order they were visited

    Time Complexity: O(V + E)
    Space Complexity: O(V) for stack and visited set

    Examples:
        >>> g = Graph(4)
        >>> g.add_edge(0, 1, directed=True)
        >>> g.add_edge(1, 2, directed=True)
        >>> g.add_edge(2, 3, directed=True)
        >>> dfs_iterative(g, 0)
        [0, 1, 2, 3]
    """
    visited: Set[int] = set()
    result: List[int] = []
    stack: List[int] = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            # Mark as visited and add to result
            visited.add(vertex)
            result.append(vertex)

            # Push all unvisited neighbors to stack
            # Note: We push in reverse order to maintain similar order to recursive DFS
            for neighbor in reversed(graph.get_neighbors(vertex)):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


def find_path_dfs(graph: Graph, start: int, end: int) -> Optional[List[int]]:
    """
    Find a path from start to end using DFS.

    This function finds ANY path from start to end, not necessarily the shortest.
    Returns None if no path exists.

    Algorithm:
    1. Use DFS to explore from start
    2. Keep track of current path
    3. When destination is reached, return the path
    4. On backtrack, remove vertex from current path
    5. If no path found, return None

    Args:
        graph: The graph to search
        start: Starting vertex
        end: Destination vertex

    Returns:
        A path from start to end as a list of vertices, or None if no path exists

    Time Complexity: O(V + E)
    Space Complexity: O(V) for recursion stack and path storage

    Examples:
        >>> g = Graph(4)
        >>> g.add_edge(0, 1)
        >>> g.add_edge(1, 3)
        >>> g.add_edge(0, 2)
        >>> g.add_edge(2, 3)
        >>> path = find_path_dfs(g, 0, 3)
        >>> path[0] == 0 and path[-1] == 3
        True
        >>> find_path_dfs(g, 0, 5) is None
        True
    """
    # Validate vertices
    if start < 0 or start >= graph.num_vertices or end < 0 or end >= graph.num_vertices:
        return None

    visited: Set[int] = set()
    path: List[int] = []

    def dfs_helper(vertex: int) -> bool:
        """
        Recursive helper for path finding.

        Returns:
            True if path to end is found, False otherwise
        """
        # Mark as visited and add to current path
        visited.add(vertex)
        path.append(vertex)

        # Check if we reached the destination
        if vertex == end:
            return True

        # Explore neighbors
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                if dfs_helper(neighbor):
                    return True

        # Backtrack: remove vertex from path
        path.pop()
        return False

    # Start DFS from start vertex
    if dfs_helper(start):
        return path
    return None


def find_all_paths_dfs(graph: Graph, start: int, end: int) -> List[List[int]]:
    """
    Find all paths from start to end using DFS with backtracking.

    This function finds ALL possible paths from start to end.
    Can be exponential in time complexity for dense graphs.

    Algorithm:
    1. Use DFS with backtracking
    2. Maintain current path
    3. When destination is reached, add copy of path to results
    4. Continue exploring to find all paths
    5. Backtrack by removing vertex from path

    Args:
        graph: The graph to search
        start: Starting vertex
        end: Destination vertex

    Returns:
        List of all paths from start to end, where each path is a list of vertices

    Time Complexity: O(V! · V) in worst case (complete graph)
    Space Complexity: O(V) for recursion depth and path storage

    Examples:
        >>> g = Graph(4)
        >>> g.add_edge(0, 1, directed=True)
        >>> g.add_edge(0, 2, directed=True)
        >>> g.add_edge(1, 3, directed=True)
        >>> g.add_edge(2, 3, directed=True)
        >>> paths = find_all_paths_dfs(g, 0, 3)
        >>> len(paths)
        2
        >>> [0, 1, 3] in paths and [0, 2, 3] in paths
        True
    """
    # Validate vertices
    if start < 0 or start >= graph.num_vertices or end < 0 or end >= graph.num_vertices:
        return []

    all_paths: List[List[int]] = []
    visited: Set[int] = set()
    path: List[int] = []

    def dfs_helper(vertex: int) -> None:
        """Recursive helper for finding all paths."""
        # Mark as visited and add to current path
        visited.add(vertex)
        path.append(vertex)

        # If we reached the destination, save this path
        if vertex == end:
            all_paths.append(path.copy())
        else:
            # Continue exploring neighbors
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs_helper(neighbor)

        # Backtrack: remove vertex from path and visited set
        path.pop()
        visited.remove(vertex)

    # Start DFS from start vertex
    dfs_helper(start)
    return all_paths


def find_connected_components(graph: Graph) -> List[List[int]]:
    """
    Find all connected components in an undirected graph.

    A connected component is a maximal set of vertices such that there is a
    path between any two vertices in the set.

    Algorithm:
    1. Initialize visited set
    2. For each unvisited vertex:
       - Start DFS to find all vertices in this component
       - Add component to results
    3. Return list of all components

    Args:
        graph: The undirected graph to analyze

    Returns:
        List of connected components, where each component is a list of vertices

    Time Complexity: O(V + E) - Visit each vertex and edge once
    Space Complexity: O(V) - Visited set and recursion stack

    Examples:
        >>> g = Graph(5)
        >>> g.add_edge(0, 1)
        >>> g.add_edge(2, 3)
        >>> components = find_connected_components(g)
        >>> len(components)
        3
        >>> sorted([sorted(c) for c in components])
        [[0, 1], [2, 3], [4]]
    """
    visited: Set[int] = set()
    components: List[List[int]] = []

    def dfs_component(vertex: int, component: List[int]) -> None:
        """DFS to find all vertices in current component."""
        visited.add(vertex)
        component.append(vertex)

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs_component(neighbor, component)

    # Find all connected components
    for vertex in range(graph.num_vertices):
        if vertex not in visited:
            component: List[int] = []
            dfs_component(vertex, component)
            components.append(component)

    return components


def has_cycle_undirected(graph: Graph) -> bool:
    """
    Detect if an undirected graph contains a cycle.

    For undirected graphs, we use DFS with parent tracking. If we visit a
    vertex that's already visited AND it's not the parent of current vertex,
    then we've found a cycle.

    Algorithm:
    1. Use DFS with parent tracking
    2. For each vertex, explore neighbors
    3. If we visit a vertex that's already visited AND it's not the parent:
       - Cycle detected!
    4. If DFS completes without finding cycle, return False

    Args:
        graph: The undirected graph to check

    Returns:
        True if graph contains a cycle, False otherwise

    Time Complexity: O(V + E)
    Space Complexity: O(V)

    Examples:
        >>> g = Graph(4)
        >>> g.add_edge(0, 1)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(1, 3)
        >>> has_cycle_undirected(g)
        False

        >>> g = Graph(3)
        >>> g.add_edge(0, 1)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(2, 0)
        >>> has_cycle_undirected(g)
        True
    """
    visited: Set[int] = set()

    def dfs_cycle(vertex: int, parent: int) -> bool:
        """
        DFS to detect cycle with parent tracking.

        Args:
            vertex: Current vertex
            parent: Parent vertex in DFS tree (-1 for root)

        Returns:
            True if cycle is detected, False otherwise
        """
        visited.add(vertex)

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                # Recursively check neighbor
                if dfs_cycle(neighbor, vertex):
                    return True
            elif neighbor != parent:
                # Visited neighbor that's not parent → cycle!
                return True

        return False

    # Check each component (graph might be disconnected)
    for vertex in range(graph.num_vertices):
        if vertex not in visited:
            if dfs_cycle(vertex, -1):
                return True

    return False


def has_cycle_directed(graph: Graph) -> bool:
    """
    Detect if a directed graph contains a cycle.

    For directed graphs, we use DFS with three states:
    - White (0): Unvisited
    - Gray (1): Being processed (in recursion stack)
    - Black (2): Completely processed

    If we visit a gray vertex during DFS, we've found a back edge → cycle!

    Algorithm:
    1. Use DFS with three states for each vertex
    2. If we visit a gray vertex during DFS:
       - Back edge detected → cycle exists!
    3. Mark vertices black when DFS completes

    Args:
        graph: The directed graph to check

    Returns:
        True if graph contains a cycle, False otherwise

    Time Complexity: O(V + E)
    Space Complexity: O(V)

    Examples:
        >>> g = Graph(4)
        >>> g.add_edge(0, 1, directed=True)
        >>> g.add_edge(1, 2, directed=True)
        >>> g.add_edge(1, 3, directed=True)
        >>> has_cycle_directed(g)
        False

        >>> g = Graph(3)
        >>> g.add_edge(0, 1, directed=True)
        >>> g.add_edge(1, 2, directed=True)
        >>> g.add_edge(2, 1, directed=True)
        >>> has_cycle_directed(g)
        True
    """
    # Color states: 0 = White (unvisited), 1 = Gray (in stack), 2 = Black (done)
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * graph.num_vertices

    def dfs_cycle(vertex: int) -> bool:
        """
        DFS to detect cycle using 3-color marking.

        Args:
            vertex: Current vertex

        Returns:
            True if cycle is detected, False otherwise
        """
        # Mark as being processed
        color[vertex] = GRAY

        for neighbor in graph.get_neighbors(vertex):
            if color[neighbor] == GRAY:
                # Found back edge → cycle!
                return True

            if color[neighbor] == WHITE:
                if dfs_cycle(neighbor):
                    return True

        # Mark as completely processed
        color[vertex] = BLACK
        return False

    # Check all vertices (graph might be disconnected)
    for vertex in range(graph.num_vertices):
        if color[vertex] == WHITE:
            if dfs_cycle(vertex):
                return True

    return False


def topological_sort_dfs(graph: Graph) -> Optional[List[int]]:
    """
    Perform topological sort on a Directed Acyclic Graph (DAG) using DFS.

    Topological sort is a linear ordering of vertices such that for every
    directed edge u → v, vertex u comes before v in the ordering.
    Only possible for Directed Acyclic Graphs (DAGs).

    Algorithm:
    1. Check if graph has cycle (topological sort only works on DAGs)
    2. Use DFS to process vertices
    3. Add vertices to result in post-order (after processing all descendants)
    4. Reverse the result to get topological order

    Args:
        graph: The directed acyclic graph to sort

    Returns:
        Topologically sorted list of vertices, or None if graph has a cycle

    Time Complexity: O(V + E)
    Space Complexity: O(V)

    Examples:
        >>> g = Graph(4)
        >>> g.add_edge(0, 1, directed=True)
        >>> g.add_edge(1, 2, directed=True)
        >>> g.add_edge(1, 3, directed=True)
        >>> result = topological_sort_dfs(g)
        >>> result[0] == 0 and result[1] == 1
        True

        >>> g = Graph(2)
        >>> g.add_edge(0, 1, directed=True)
        >>> g.add_edge(1, 0, directed=True)
        >>> topological_sort_dfs(g) is None
        True
    """
    # First check if graph has a cycle
    if has_cycle_directed(graph):
        return None

    visited: Set[int] = set()
    result: List[int] = []

    def dfs_topo(vertex: int) -> None:
        """DFS to add vertices in post-order."""
        visited.add(vertex)

        # Visit all neighbors first
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs_topo(neighbor)

        # Add vertex to result in post-order
        result.append(vertex)

    # Process all vertices
    for vertex in range(graph.num_vertices):
        if vertex not in visited:
            dfs_topo(vertex)

    # Reverse to get topological order
    result.reverse()
    return result


def is_bipartite(graph: Graph) -> bool:
    """
    Determine if a graph is bipartite using DFS and 2-coloring.

    A graph is bipartite if it can be colored with 2 colors such that no
    adjacent vertices have the same color. Equivalently, a graph is bipartite
    if and only if it contains no odd-length cycles.

    Algorithm:
    1. Use DFS with color assignment
    2. Color start vertex with color 0
    3. Color all neighbors with opposite color (1)
    4. If we try to color a vertex that's already colored:
       - Check if color matches expected color
       - If not, graph is not bipartite
    5. Repeat for all components

    Args:
        graph: The graph to check

    Returns:
        True if graph is bipartite, False otherwise

    Time Complexity: O(V + E)
    Space Complexity: O(V)

    Examples:
        >>> g = Graph(4)
        >>> g.add_edge(0, 1)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(1, 3)
        >>> is_bipartite(g)
        True

        >>> g = Graph(3)
        >>> g.add_edge(0, 1)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(2, 0)
        >>> is_bipartite(g)
        False
    """
    # Color array: -1 = uncolored, 0 and 1 are the two colors
    color = [-1] * graph.num_vertices

    def dfs_color(vertex: int, c: int) -> bool:
        """
        DFS to try 2-coloring the graph.

        Args:
            vertex: Current vertex
            c: Color to assign (0 or 1)

        Returns:
            True if coloring is successful, False if conflict occurs
        """
        # Color the vertex
        color[vertex] = c

        # Try to color all neighbors with opposite color
        for neighbor in graph.get_neighbors(vertex):
            if color[neighbor] == -1:
                # Neighbor is uncolored, color it with opposite color
                if not dfs_color(neighbor, 1 - c):
                    return False
            elif color[neighbor] == c:
                # Neighbor has same color → not bipartite!
                return False

        return True

    # Check all components (graph might be disconnected)
    for vertex in range(graph.num_vertices):
        if color[vertex] == -1:
            if not dfs_color(vertex, 0):
                return False

    return True


if __name__ == "__main__":
    # Test the Graph and DFS implementations
    print("Graph and DFS Demonstrations")
    print("=" * 70)

    # Test 1: Graph Creation and DFS Traversal
    print("\n1. Graph Creation (Adjacency List):")
    g1 = Graph(5, "adjacency_list")
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(1, 3)
    g1.add_edge(2, 4)
    print(f"   Graph with {g1.num_vertices} vertices")
    print(f"   Neighbors of 0: {g1.get_neighbors(0)}")
    print(f"   Neighbors of 1: {g1.get_neighbors(1)}")

    # Test 2: DFS Recursive
    print("\n2. DFS Recursive Traversal:")
    result = dfs_recursive(g1, 0)
    print(f"   Starting from vertex 0: {result}")

    # Test 3: DFS Iterative
    print("\n3. DFS Iterative Traversal:")
    result = dfs_iterative(g1, 0)
    print(f"   Starting from vertex 0: {result}")

    # Test 4: Path Finding
    print("\n4. Path Finding:")
    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    path = find_path_dfs(g2, 0, 3)
    print(f"   Path from 0 to 3: {path}")

    # Test 5: All Paths
    print("\n5. Find All Paths:")
    g3 = Graph(4)
    g3.add_edge(0, 1, directed=True)
    g3.add_edge(0, 2, directed=True)
    g3.add_edge(1, 3, directed=True)
    g3.add_edge(2, 3, directed=True)
    all_paths = find_all_paths_dfs(g3, 0, 3)
    print(f"   All paths from 0 to 3:")
    for path in all_paths:
        print(f"   - {path}")

    # Test 6: Connected Components
    print("\n6. Connected Components:")
    g4 = Graph(6)
    g4.add_edge(0, 1)
    g4.add_edge(2, 3)
    g4.add_edge(4, 5)
    components = find_connected_components(g4)
    print(f"   Found {len(components)} components:")
    for i, comp in enumerate(components):
        print(f"   - Component {i + 1}: {sorted(comp)}")

    # Test 7: Cycle Detection (Undirected)
    print("\n7. Cycle Detection (Undirected Graph):")
    g5 = Graph(4)
    g5.add_edge(0, 1)
    g5.add_edge(1, 2)
    g5.add_edge(1, 3)
    print(f"   Tree (0-1-2, 1-3): Has cycle? {has_cycle_undirected(g5)}")

    g6 = Graph(3)
    g6.add_edge(0, 1)
    g6.add_edge(1, 2)
    g6.add_edge(2, 0)
    print(f"   Triangle (0-1-2-0): Has cycle? {has_cycle_undirected(g6)}")

    # Test 8: Cycle Detection (Directed)
    print("\n8. Cycle Detection (Directed Graph):")
    g7 = Graph(4)
    g7.add_edge(0, 1, directed=True)
    g7.add_edge(1, 2, directed=True)
    g7.add_edge(1, 3, directed=True)
    print(f"   DAG: Has cycle? {has_cycle_directed(g7)}")

    g8 = Graph(3)
    g8.add_edge(0, 1, directed=True)
    g8.add_edge(1, 2, directed=True)
    g8.add_edge(2, 1, directed=True)
    print(f"   Cycle (1→2→1): Has cycle? {has_cycle_directed(g8)}")

    # Test 9: Topological Sort
    print("\n9. Topological Sort:")
    g9 = Graph(6)
    g9.add_edge(5, 2, directed=True)
    g9.add_edge(5, 0, directed=True)
    g9.add_edge(4, 0, directed=True)
    g9.add_edge(4, 1, directed=True)
    g9.add_edge(2, 3, directed=True)
    g9.add_edge(3, 1, directed=True)
    topo = topological_sort_dfs(g9)
    print(f"   Topological order: {topo}")

    # Test 10: Bipartite Check
    print("\n10. Bipartite Graph Check:")
    g10 = Graph(4)
    g10.add_edge(0, 1)
    g10.add_edge(1, 2)
    g10.add_edge(2, 3)
    print(f"   Linear graph (0-1-2-3): Is bipartite? {is_bipartite(g10)}")

    g11 = Graph(3)
    g11.add_edge(0, 1)
    g11.add_edge(1, 2)
    g11.add_edge(2, 0)
    print(f"   Triangle (0-1-2-0): Is bipartite? {is_bipartite(g11)}")

    g12 = Graph(4)
    g12.add_edge(0, 1)
    g12.add_edge(1, 2)
    g12.add_edge(2, 3)
    g12.add_edge(3, 0)
    print(f"   Square (0-1-2-3-0): Is bipartite? {is_bipartite(g12)}")

    print("\n" + "=" * 70)
    print("All DFS algorithms demonstrated!")
