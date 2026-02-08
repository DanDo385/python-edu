"""
Project: Introduction to Graphs and Traversal - SOLUTION

This file contains the complete implementation of a Graph class and the
BFS and DFS traversal algorithms.
"""
from collections import deque
from typing import List, Any, Set

class Graph:
    """
    A class to represent an undirected graph using an adjacency list.
    """
    def __init__(self):
        """Initializes an empty graph."""
        self.adj_list = {}

    def add_node(self, node: Any):
        """Adds a new node to the graph if it doesn't already exist."""
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, u: Any, v: Any):
        """Adds an undirected edge between two nodes, `u` and `v`."""
        # Ensure both nodes exist in the graph.
        self.add_node(u)
        self.add_node(v)
        
        # Add the edge in both directions for an undirected graph.
        # Check to prevent duplicate edges, though not strictly necessary.
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def bfs(self, start_node: Any) -> List[Any]:
        """
        Performs a Breadth-First Search starting from `start_node`.
        """
        if start_node not in self.adj_list:
            return []

        queue = deque([start_node])
        visited = {start_node}
        result = []

        while queue:
            # Dequeue a node and add it to the result.
            current_node = queue.popleft()
            result.append(current_node)

            # Get all neighbors of the current node.
            # Sort them to have a deterministic traversal order for testing.
            for neighbor in sorted(self.adj_list.get(current_node, [])):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result

    def dfs(self, start_node: Any) -> List[Any]:
        """
        Performs a Depth-First Search starting from `start_node`.
        """
        if start_node not in self.adj_list:
            return []
            
        visited = set()
        result = []
        self._dfs_recursive(start_node, visited, result)
        return result

    def _dfs_recursive(self, current_node: Any, visited: Set[Any], result: List[Any]):
        """Private helper method for recursive DFS."""
        # Mark the current node as visited and add it to the result.
        visited.add(current_node)
        result.append(current_node)
        
        # Recursively visit all unvisited neighbors.
        # Sort them to have a deterministic traversal order for testing.
        for neighbor in sorted(self.adj_list.get(current_node, [])):
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited, result)

# --- Example Usage ---
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')

    print("Adjacency List:")
    for node, neighbors in g.adj_list.items():
        print(f"  {node}: {neighbors}")

    print("\nBFS starting from 'A':")
    # Expected: ['A', 'B', 'C', 'D', 'E', 'F']
    print(g.bfs('A'))

    print("\nDFS starting from 'A':")
    # Expected: ['A', 'B', 'D', 'E', 'C', 'F']
    print(g.dfs('A'))