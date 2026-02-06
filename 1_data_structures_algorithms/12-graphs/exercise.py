"""
Project 14: Graphs and Graph Traversal Algorithms

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""


class Graph:
    """
    A graph implementation using adjacency list.
    
    Attributes:
        graph (dict): Adjacency list representation
                     {node: [neighbor1, neighbor2, ...]}
    """
    
    def __init__(self):
        """Initialize an empty graph."""
        # TODO: Initialize self.graph as empty dict
        pass
    
    def add_edge(self, u, v):
        """
        Add an undirected edge between u and v.
        
        Args:
            u: First node
            v: Second node
        """
        # TODO: Add v to u's neighbors and u to v's neighbors
        pass
    
    def dfs(self, start):
        """
        Perform DFS traversal starting from start node.
        
        Args:
            start: Starting node
        
        Returns:
            list: List of nodes visited in DFS order
        """
        # TODO: Implement DFS recursively
        # Use visited set to track visited nodes
        visited = set()
        result = []
        # TODO: Define helper function for recursion
        return result
    
    def bfs(self, start):
        """
        Perform BFS traversal starting from start node.
        
        Args:
            start: Starting node
        
        Returns:
            list: List of nodes visited in BFS order
        """
        # TODO: Implement BFS using queue
        # Use queue and visited set
        from collections import deque
        return []

