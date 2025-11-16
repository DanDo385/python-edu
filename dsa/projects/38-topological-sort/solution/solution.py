"""
Project 38: Topological Sort

Implementations of topological sorting algorithms for Directed Acyclic Graphs (DAGs).

Author: Python-Edu DSA Curriculum
"""

from typing import List, Optional, Set, Dict
from collections import deque, defaultdict
import sys
import os

# Import Graph from project 35
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../35-graph-dfs/solution'))
from solution import Graph


def kahns_algorithm(graph: Graph) -> Optional[List[int]]:
    """
    Topological sort using Kahn's algorithm (BFS-based with in-degree tracking).

    Time: O(V + E), Space: O(V)
    """
    # Compute in-degrees
    in_degree = {i: 0 for i in range(graph.num_vertices)}
    for u in range(graph.num_vertices):
        for v in graph.get_neighbors(u):
            in_degree[v] += 1

    # Add vertices with in-degree 0 to queue
    queue = deque([v for v in range(graph.num_vertices) if in_degree[v] == 0])
    result = []

    while queue:
        u = queue.popleft()
        result.append(u)

        # Reduce in-degree for neighbors
        for v in graph.get_neighbors(u):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # If not all vertices included, cycle exists
    return result if len(result) == graph.num_vertices else None


def topological_sort_dfs(graph: Graph) -> Optional[List[int]]:
    """
    Topological sort using DFS with post-order traversal.

    Time: O(V + E), Space: O(V)
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * graph.num_vertices
    result = []

    def dfs(u: int) -> bool:
        """Returns False if cycle detected."""
        color[u] = GRAY
        for v in graph.get_neighbors(u):
            if color[v] == GRAY:
                return False  # Cycle detected
            if color[v] == WHITE and not dfs(v):
                return False
        color[u] = BLACK
        result.append(u)
        return True

    # Visit all vertices
    for u in range(graph.num_vertices):
        if color[u] == WHITE:
            if not dfs(u):
                return None  # Cycle detected

    result.reverse()  # Reverse post-order
    return result


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    Determine if all courses can be finished given prerequisites (LeetCode 207).

    Args:
        num_courses: Number of courses (0 to num_courses-1)
        prerequisites: List of [course, prerequisite] pairs

    Returns:
        True if possible to finish all courses, False otherwise
    """
    # Build graph
    graph = Graph(num_courses)
    for course, prereq in prerequisites:
        graph.add_edge(prereq, course, directed=True)

    # Check if topological sort exists (no cycle)
    return kahns_algorithm(graph) is not None


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Find valid course ordering, or empty if impossible (LeetCode 210).

    Args:
        num_courses: Number of courses
        prerequisites: List of [course, prerequisite] pairs

    Returns:
        Valid course ordering, or empty list if impossible
    """
    # Build graph
    graph = Graph(num_courses)
    for course, prereq in prerequisites:
        graph.add_edge(prereq, course, directed=True)

    # Get topological ordering
    result = kahns_algorithm(graph)
    return result if result is not None else []


if __name__ == "__main__":
    print("Topological Sort Demonstrations")
    print("=" * 70)

    # Test 1: Kahn's Algorithm
    print("\n1. Kahn's Algorithm:")
    g1 = Graph(6)
    g1.add_edge(5, 2, directed=True)
    g1.add_edge(5, 0, directed=True)
    g1.add_edge(4, 0, directed=True)
    g1.add_edge(4, 1, directed=True)
    g1.add_edge(2, 3, directed=True)
    g1.add_edge(3, 1, directed=True)
    order = kahns_algorithm(g1)
    print(f"   Topological ordering: {order}")

    # Test 2: DFS-based Topological Sort
    print("\n2. DFS-based Topological Sort:")
    order_dfs = topological_sort_dfs(g1)
    print(f"   Topological ordering: {order_dfs}")

    # Test 3: Course Schedule I
    print("\n3. Course Schedule I:")
    print(f"   2 courses, [[1,0]]: {can_finish(2, [[1, 0]])}")
    print(f"   2 courses, [[1,0],[0,1]]: {can_finish(2, [[1, 0], [0, 1]])}")

    # Test 4: Course Schedule II
    print("\n4. Course Schedule II:")
    print(f"   4 courses, [[1,0],[2,0],[3,1],[3,2]]: {find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])}")
    print(f"   2 courses, [[1,0],[0,1]]: {find_order(2, [[1, 0], [0, 1]])}")

    print("\n" + "=" * 70)
