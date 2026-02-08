"""
Project: Graph Traversal Algorithms

This project builds on the previous one by using BFS and DFS to solve
common graph problems: finding the shortest path in an unweighted graph
and detecting cycles.
"""
from collections import deque
from typing import List, Any, Dict, Optional

# We can reuse the Graph class structure, but for this exercise, we'll
# work with the adjacency list directly as a dictionary.

def shortest_path(graph: Dict[Any, List[Any]], start_node: Any, end_node: Any) -> Optional[List[Any]]:
    """
    Finds the shortest path between two nodes in an unweighted, undirected graph.
    This is a classic application of Breadth-First Search (BFS).

    Args:
        graph: An adjacency list representation of the graph.
        start_node: The starting node.
        end_node: The target node.

    Returns:
        A list of nodes representing the shortest path from start_node to
        end_node. If no path exists, returns None.
    """
    # TODO: Handle edge case where start or end node is not in the graph.
    
    # TODO: Initialize a queue for BFS and add the starting path, which is just [start_node].
    
    # TODO: Initialize a set to keep track of visited nodes to avoid cycles and redundant paths.

    # TODO: Loop while the queue is not empty:
    # 1. Dequeue the current path.
    # 2. Get the last node from the path.
    # 3. If this node is the end_node, you've found the shortest path. Return it.
    # 4. For each neighbor of the last node:
    #    a. If the neighbor has not been visited:
    #       i. Mark it as visited.
    #       ii. Create a new path by extending the current path.
    #       iii. Enqueue the new path.

    # TODO: If the loop finishes without finding a path, return None.
    return None


def has_cycle(graph: Dict[Any, List[Any]]) -> bool:
    """
    Checks if an undirected graph contains a cycle.
    This can be solved using Depth-First Search (DFS).

    Args:
        graph: An adjacency list representation of the graph.

    Returns:
        True if the graph contains a cycle, False otherwise.
    """
    # TODO: Initialize a set to keep track of all visited nodes globally.
    
    # TODO: Iterate through each node in the graph.
    # This is to handle disconnected graphs. If a node hasn't been visited yet,
    # start a DFS from it.
    pass

    # TODO: If any of the DFS calls return True (meaning a cycle was found),
    # return True immediately.

    # TODO: If the loop completes, no cycles were found. Return False.
    return False
def _has_cycle_dfs(graph: Dict[Any, List[Any]], current_node: Any, visited: set, parent: Any) -> bool:
    """
    A recursive helper for `has_cycle` to perform the DFS.

    Args:
        graph: The graph's adjacency list.
        current_node: The node to visit.
        visited: The set of visited nodes.
        parent: The node from which we reached the current_node.

    Returns:
        True if a cycle is detected, False otherwise.
    """
    # TODO: Mark the current node as visited.

    # TODO: For each neighbor of the current node:
    # 1. If the neighbor has not been visited, recursively call the DFS helper on it.
    #    If that recursive call returns True, a cycle was found, so propagate True up.
    # 2. If the neighbor IS visited AND it's not the parent of the current node,
    #    we have found a back edge, which means there is a cycle. Return True.
    
    # TODO: If the loop completes without finding a cycle, return False.
    return False

# Example Usage
# if __name__ == "__main__":
#     # Graph 1: A graph with a path but no cycle
#     graph1 = {
#         'A': ['B', 'C'],
#         'B': ['A', 'D', 'E'],
#         'C': ['A', 'F'],
#         'D': ['B'],
#         'E': ['B', 'F'],
#         'F': ['C', 'E']
#     }
#     print("--- Graph 1 ---")
#     path = shortest_path(graph1, 'A', 'F')
#     print(f"Shortest path from A to F: {path}") # Expected: ['A', 'C', 'F'] or ['A', 'B', 'E', 'F']
#     cycle = has_cycle(graph1)
#     print(f"Graph 1 has cycle: {cycle}") # Expected: True

#     # Graph 2: A simple tree (no cycles)
#     graph2 = {
#         'A': ['B', 'C'],
#         'B': ['A'],
#         'C': ['A']
#     }
#     print("\n--- Graph 2 ---")
#     path2 = shortest_path(graph2, 'B', 'C')
#     print(f"Shortest path from B to C: {path2}") # Expected: ['B', 'A', 'C']
#     cycle2 = has_cycle(graph2)
#     print(f"Graph 2 has cycle: {cycle2}") # Expected: False