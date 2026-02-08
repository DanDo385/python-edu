"""
Project: Introduction to Graphs and Traversal

This project introduces the graph data structure and two fundamental
traversal algorithms: Breadth-First Search (BFS) and Depth-First Search (DFS).
You will implement a graph using an adjacency list representation.
"""
from collections import deque
from typing import List, Any, Set

class Graph:
    """
    A class to represent a graph using an adjacency list.
    The graph is undirected.
    """
    def __init__(self):
        """Initializes an empty graph."""
        # TODO: Initialize `self.adj_list` as a dictionary.
        # The keys will be the nodes, and the values will be a list
        # of their neighbors.
        pass

    def add_node(self, node: Any):
        """Adds a new node to the graph."""
        # TODO: If the node is not already in the adjacency list,
        # add it with an empty list of neighbors.
        pass

    def add_edge(self, u: Any, v: Any):
        """
        Adds an undirected edge between two nodes, `u` and `v`.
        This means you need to add `v` to `u`'s neighbors and `u` to `v`'s.
        """
        # TODO: Ensure both nodes exist in the graph by adding them.
        # TODO: Add the edge in both directions.
        pass

    def bfs(self, start_node: Any) -> List[Any]:
        """
        Performs a Breadth-First Search starting from `start_node`.
        BFS explores the graph layer by layer.

        Returns:
            A list of nodes in the order they were visited.
        """
        # TODO: Check if start_node is in the graph. If not, return [].
        # TODO: Initialize a queue for BFS and add the start_node.
        # TODO: Initialize a set to keep track of visited nodes.
        # TODO: Initialize a list to store the traversal order.

        # TODO: Loop while the queue is not empty:
        # 1. Dequeue a node.
        # 2. If it hasn't been visited, add it to the visited set and the result list.
        # 3. Enqueue all of its unvisited neighbors.
        
        # TODO: Return the result list.
        return []

    def dfs(self, start_node: Any) -> List[Any]:
        """
        Performs a Depth-First Search starting from `start_node`.
        DFS explores as far as possible along each branch before backtracking.
        This will be implemented recursively.

        Returns:
            A list of nodes in the order they were visited.
        """
        # TODO: Initialize a set for visited nodes and a list for the result.
        # TODO: Call the recursive helper function `_dfs_recursive`.
        # TODO: Return the result list.
        return []

    def _dfs_recursive(self, current_node: Any, visited: Set[Any], result: List[Any]):
        """A private helper method for the recursive DFS implementation."""
        # TODO: Base case: If the node has been visited, do nothing.

        # TODO: Mark the current node as visited and add it to the result list.
        
        # TODO: Recursively call `_dfs_recursive` for all unvisited neighbors.
        pass

# Example Usage
# if __name__ == "__main__":
#     # Create a graph
#     g = Graph()
#     g.add_edge('A', 'B')
#     g.add_edge('A', 'C')
#     g.add_edge('B', 'D')
#     g.add_edge('B', 'E')
#     g.add_edge('C', 'F')

#     print("BFS starting from 'A':")
#     # Expected: ['A', 'B', 'C', 'D', 'E', 'F'] (order of D,E,F might vary)
#     print(g.bfs('A'))

#     print("\nDFS starting from 'A':")
#     # Expected: ['A', 'B', 'D', 'E', 'C', 'F'] (order might vary)
#     print(g.dfs('A'))