"""
Project: Graph Traversal Algorithms - SOLUTION

This file provides solutions for finding the shortest path and detecting
cycles in a graph using BFS and DFS, respectively.
"""
from collections import deque
from typing import List, Any, Dict, Optional, Set

def shortest_path(graph: Dict[Any, List[Any]], start_node: Any, end_node: Any) -> Optional[List[Any]]:
    """
    Finds the shortest path between two nodes in an unweighted, undirected graph using BFS.
    """
    if start_node not in graph or end_node not in graph:
        return None

    # The queue will store paths. We start with a path containing only the start_node.
    queue = deque([[start_node]])
    visited = {start_node}

    while queue:
        # Get the first path from the queue.
        path = queue.popleft()
        last_node = path[-1]

        # If we've reached the end, this is the shortest path.
        if last_node == end_node:
            return path

        # Explore neighbors.
        for neighbor in graph.get(last_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                # Create a new path and add it to the queue.
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    # If the queue empties and we haven't found the end_node, no path exists.
    return None

def has_cycle(graph: Dict[Any, List[Any]]) -> bool:
    """
    Checks if an undirected graph contains a cycle using DFS.
    """
    visited = set()
    # We must iterate through all nodes to handle disconnected graphs.
    for node in graph:
        if node not in visited:
            # If DFS finds a cycle starting from any node, we return True.
            if _has_cycle_dfs(graph, node, visited, parent=None):
                return True
    
    return False

def _has_cycle_dfs(graph: Dict[Any, List[Any]], current_node: Any, visited: Set[Any], parent: Any) -> bool:
    """
    A recursive helper for `has_cycle` to perform the DFS.
    The `parent` parameter is key to avoiding false positives in an undirected graph.
    """
    visited.add(current_node)

    for neighbor in graph.get(current_node, []):
        if neighbor not in visited:
            # If a recursive call finds a cycle, propagate the result up.
            if _has_cycle_dfs(graph, neighbor, visited, current_node):
                return True
        # If the neighbor is visited AND it's not the immediate parent node that
        # we just came from, then we have found a "back edge," indicating a cycle.
        elif neighbor != parent:
            return True
    
    # No cycle found from this path.
    return False

# --- Example Usage ---
if __name__ == "__main__":
    # Graph with a cycle
    graph1 = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print("--- Graph 1 (has cycle) ---")
    path = shortest_path(graph1, 'A', 'D')
    print(f"Shortest path from A to D: {path}") # Expected: ['A', 'B', 'D']
    cycle = has_cycle(graph1)
    print(f"Graph 1 has cycle: {cycle}") # Expected: True

    # Graph without a cycle (a tree)
    graph2 = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A'],
        'D': ['B']
    }
    print("\n--- Graph 2 (no cycle) ---")
    path2 = shortest_path(graph2, 'C', 'D')
    print(f"Shortest path from C to D: {path2}") # Expected: ['C', 'A', 'B', 'D']
    cycle2 = has_cycle(graph2)
    print(f"Graph 2 has cycle: {cycle2}") # Expected: False

    # Disconnected graph
    graph3 = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C', 'E'],
        'E': ['D']
    }
    print("\n--- Graph 3 (disconnected) ---")
    path3 = shortest_path(graph3, 'A', 'D')
    print(f"Shortest path from A to D: {path3}") # Expected: None
    cycle3 = has_cycle(graph3)
    print(f"Graph 3 has cycle: {cycle3}") # Expected: False