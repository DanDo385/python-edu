"""
Project 14: Graphs and Graph Traversal Algorithms - SOLUTION

Complete solution with detailed comments explaining graph representation and traversal algorithms.
"""


class Graph:
    """
    A graph implementation using adjacency list.
    
    An adjacency list stores, for each node, a list of its neighbors.
    This is efficient for sparse graphs (few edges relative to nodes).
    
    Example:
        graph = {
            0: [1, 2],
            1: [0, 3],
            2: [0],
            3: [1]
        }
    
    Attributes:
        graph (dict): Adjacency list representation
                     {node: [neighbor1, neighbor2, ...]}
    """
    
    def __init__(self):
        """
        Initialize an empty graph.
        
        We use a dictionary where keys are nodes and values are lists
        of neighboring nodes.
        """
        # Initialize empty dictionary for adjacency list
        self.graph = {}
    
    def add_edge(self, u, v):
        """
        Add an undirected edge between u and v.
        
        For an undirected graph, if there's an edge between u and v,
        then v is a neighbor of u AND u is a neighbor of v.
        So we add each node to the other's neighbor list.
        
        Args:
            u: First node
            v: Second node
        
        Example:
            g.add_edge(0, 1)
            # Now 1 is in graph[0] and 0 is in graph[1]
        """
        # If u doesn't exist in graph yet, initialize its neighbor list
        if u not in self.graph:
            self.graph[u] = []
        
        # If v doesn't exist in graph yet, initialize its neighbor list
        if v not in self.graph:
            self.graph[v] = []
        
        # Add v to u's neighbors (u → v edge)
        self.graph[u].append(v)
        
        # Add u to v's neighbors (v → u edge, since undirected)
        self.graph[v].append(u)
    
    def dfs(self, start):
        """
        Perform DFS traversal starting from start node.
        
        Depth-First Search explores as far as possible along each branch
        before backtracking. It uses a stack (we use recursion which uses
        the call stack).
        
        Algorithm:
        1. Mark current node as visited
        2. Process current node
        3. For each unvisited neighbor:
           a. Recursively visit neighbor
        
        Time complexity: O(V + E) where V = vertices, E = edges
        Space complexity: O(V) for visited set and recursion stack
        
        Args:
            start: Starting node
        
        Returns:
            list: List of nodes visited in DFS order
        
        Example:
            Graph: 0-1-3
                   |
                   2
            DFS(0) might return [0, 1, 3, 2] (order depends on neighbor order)
        """
        # Set to track visited nodes (prevents infinite loops in cycles)
        visited = set()
        # List to store traversal order
        result = []
        
        def dfs_helper(node):
            """
            Helper function for recursive DFS.
            
            This inner function has access to visited and result from outer scope.
            """
            # Mark node as visited
            visited.add(node)
            # Add to result
            result.append(node)
            
            # Visit all neighbors that haven't been visited
            # self.graph.get(node, []) returns neighbors or empty list if node doesn't exist
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    # Recursively visit unvisited neighbor
                    dfs_helper(neighbor)
        
        # Start DFS from start node
        if start in self.graph:
            dfs_helper(start)
        
        return result
    
    def bfs(self, start):
        """
        Perform BFS traversal starting from start node.
        
        Breadth-First Search explores all neighbors at current level before
        moving to next level. It uses a queue to ensure level-by-level exploration.
        BFS guarantees shortest path in unweighted graphs.
        
        Algorithm:
        1. Add start to queue and mark as visited
        2. While queue not empty:
           a. Dequeue a node
           b. Process it
           c. Add all unvisited neighbors to queue
        
        Time complexity: O(V + E) where V = vertices, E = edges
        Space complexity: O(V) for visited set and queue
        
        Args:
            start: Starting node
        
        Returns:
            list: List of nodes visited in BFS order
        
        Example:
            Graph: 0-1-3
                   |
                   2
            BFS(0) returns [0, 1, 2, 3] (level order)
        """
        # Import deque for efficient queue operations
        # deque.popleft() is O(1), list.pop(0) is O(n)
        from collections import deque
        
        # Set to track visited nodes
        visited = set()
        # Queue for BFS (FIFO)
        queue = deque()
        # List to store traversal order
        result = []
        
        # If start node doesn't exist, return empty list
        if start not in self.graph:
            return result
        
        # Initialize: add start to queue and mark as visited
        queue.append(start)
        visited.add(start)
        
        # Process nodes level by level
        while queue:
            # Dequeue front node (FIFO)
            node = queue.popleft()
            # Add to result
            result.append(node)
            
            # Add all unvisited neighbors to queue
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    # Mark as visited before adding to queue
                    # This prevents adding same node multiple times
                    visited.add(neighbor)
                    # Add to back of queue
                    queue.append(neighbor)
        
        return result

