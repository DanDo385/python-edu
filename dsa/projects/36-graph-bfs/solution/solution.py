"""
Project 36: Breadth-First Search (BFS)

This module implements BFS algorithms for graph traversal, shortest path finding,
level-order traversal, and word ladder problem.

Key Concepts:
- BFS queue-based traversal
- Shortest path in unweighted graphs
- Level-order traversal
- Word transformation problems
- Pattern matching optimization

Author: Python-Edu DSA Curriculum
"""

from typing import List, Optional, Set, Dict
from collections import deque, defaultdict
import sys
import os

# Add parent directory to path to import Graph from project 35
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../35-graph-dfs/solution'))
from solution import Graph


def bfs_traversal(graph: Graph, start: int) -> List[int]:
    """
    Perform Breadth-First Search starting from a given vertex.

    BFS explores vertices level by level, visiting all neighbors before moving deeper.
    Uses a queue (FIFO) to maintain the frontier of vertices to explore.

    Algorithm:
    1. Create a queue and enqueue start vertex
    2. Create visited set to track processed vertices
    3. While queue is not empty:
       - Dequeue vertex
       - If not visited:
         - Mark as visited
         - Add to result
         - Enqueue all unvisited neighbors
    4. Return visit order

    Args:
        graph: The graph to traverse
        start: Starting vertex for BFS

    Returns:
        List of vertices in the order they were visited (level-order)

    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V) for queue and visited set

    Examples:
        >>> g = Graph(4)
        >>> g.add_edge(0, 1, directed=True)
        >>> g.add_edge(1, 2, directed=True)
        >>> g.add_edge(2, 3, directed=True)
        >>> bfs_traversal(g, 0)
        [0, 1, 2, 3]

        >>> g = Graph(4)
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> g.add_edge(1, 3)
        >>> result = bfs_traversal(g, 0)
        >>> result[0]
        0
        >>> set(result[1:3]) == {1, 2}
        True
    """
    # Initialize queue with start vertex
    queue: deque = deque([start])
    visited: Set[int] = {start}  # Mark start as visited immediately
    result: List[int] = []

    while queue:
        # Dequeue vertex from front of queue
        vertex = queue.popleft()
        result.append(vertex)

        # Enqueue all unvisited neighbors
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)  # Mark as visited when adding to queue
                queue.append(neighbor)

    return result


def shortest_path_bfs(graph: Graph, start: int, end: int) -> Optional[List[int]]:
    """
    Find the shortest path from start to end using BFS.

    In an unweighted graph, BFS guarantees the shortest path because it explores
    level by level. The first time we reach the destination, we've found the
    shortest path.

    Algorithm:
    1. Use BFS with parent tracking
    2. Keep a parent dictionary to reconstruct path
    3. When destination is reached, reconstruct path using parent pointers
    4. Return path from start to end

    Args:
        graph: The graph to search
        start: Starting vertex
        end: Destination vertex

    Returns:
        Shortest path from start to end as a list of vertices, or None if no path exists

    Time Complexity: O(V + E)
    Space Complexity: O(V) for queue and parent dictionary

    Examples:
        >>> g = Graph(4)
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(1, 3)
        >>> shortest_path_bfs(g, 0, 3)
        [0, 1, 3]

        >>> shortest_path_bfs(g, 0, 5)

    """
    # Validate vertices
    if start < 0 or start >= graph.num_vertices or end < 0 or end >= graph.num_vertices:
        return None

    # Special case: start == end
    if start == end:
        return [start]

    # Initialize BFS
    queue: deque = deque([start])
    visited: Set[int] = {start}
    parent: Dict[int, Optional[int]] = {start: None}

    while queue:
        vertex = queue.popleft()

        # Check if we reached the destination
        if vertex == end:
            # Reconstruct path from end to start
            path = []
            current = end
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        # Explore neighbors
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = vertex
                queue.append(neighbor)

    # No path found
    return None


def level_order_traversal(graph: Graph, start: int) -> List[List[int]]:
    """
    Perform level-order traversal of a graph using BFS.

    Returns vertices grouped by their distance from the start vertex.
    Level 0 contains only the start vertex, level 1 contains its neighbors,
    level 2 contains neighbors of level 1, etc.

    Algorithm:
    1. Use BFS with level tracking
    2. Process vertices level by level
    3. Track level size to separate levels
    4. Return list of levels

    Args:
        graph: The graph to traverse
        start: Starting vertex

    Returns:
        List of levels, where each level is a list of vertices at that distance

    Time Complexity: O(V + E)
    Space Complexity: O(V) for queue and result storage

    Examples:
        >>> g = Graph(5)
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> g.add_edge(1, 3)
        >>> g.add_edge(1, 4)
        >>> level_order_traversal(g, 0)
        [[0], [1, 2], [3, 4]]

        >>> g = Graph(4)
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> g.add_edge(1, 3)
        >>> g.add_edge(2, 3)
        >>> result = level_order_traversal(g, 0)
        >>> result[0]
        [0]
        >>> set(result[1]) == {1, 2}
        True
        >>> result[2]
        [3]
    """
    if start < 0 or start >= graph.num_vertices:
        return []

    queue: deque = deque([start])
    visited: Set[int] = {start}
    levels: List[List[int]] = []

    while queue:
        # Process all vertices at current level
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            vertex = queue.popleft()
            current_level.append(vertex)

            # Add unvisited neighbors to queue (they'll be in next level)
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        levels.append(current_level)

    return levels


def word_ladder(start: str, end: str, word_list: List[str]) -> List[str]:
    """
    Find the shortest transformation sequence from start word to end word.

    Each transformation changes exactly one letter, and each intermediate word
    must exist in the word list. Uses BFS to find the shortest sequence.

    Optimization: Uses pattern matching to efficiently find word neighbors.
    For each word, creates patterns like "*it", "h*t", "hi*" and groups words
    by these patterns for O(1) neighbor lookup.

    Algorithm:
    1. Build pattern dictionary mapping patterns to words
    2. Use BFS with parent tracking
    3. For each word, check all patterns to find neighbors
    4. When end word is reached, reconstruct path
    5. Return transformation sequence

    Args:
        start: Starting word
        end: Target word
        word_list: List of valid intermediate words

    Returns:
        Shortest transformation sequence, or empty list if no path exists

    Time Complexity: O(M² × N) where M is word length, N is number of words
    Space Complexity: O(M × N) for pattern dictionary and queue

    Examples:
        >>> word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
        ['hit', 'hot', 'dot', 'dog', 'cog']

        >>> word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
        []

        >>> word_ladder("hot", "dog", ["hot", "dog", "dot"])
        ['hot', 'dot', 'dog']
    """
    # End word must be in word list
    if end not in word_list:
        return []

    # Add start word to word list if not present
    word_set = set(word_list)
    if start not in word_set:
        word_set.add(start)

    # Build pattern dictionary for efficient neighbor finding
    # Pattern: "*it", "h*t", "hi*" for word "hit"
    patterns: Dict[str, List[str]] = defaultdict(list)
    word_length = len(start)

    for word in word_set:
        for i in range(word_length):
            # Create pattern by replacing character at position i with *
            pattern = word[:i] + "*" + word[i + 1:]
            patterns[pattern].append(word)

    # BFS to find shortest path
    queue: deque = deque([start])
    visited: Set[str] = {start}
    parent: Dict[str, Optional[str]] = {start: None}

    while queue:
        current_word = queue.popleft()

        # Check if we reached the end
        if current_word == end:
            # Reconstruct path
            path = []
            word = end
            while word is not None:
                path.append(word)
                word = parent[word]
            path.reverse()
            return path

        # Find all neighbors by checking all patterns
        for i in range(word_length):
            pattern = current_word[:i] + "*" + current_word[i + 1:]

            # Get all words matching this pattern
            for neighbor in patterns[pattern]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current_word
                    queue.append(neighbor)

    # No path found
    return []


if __name__ == "__main__":
    # Test the BFS implementations
    print("BFS Algorithms Demonstration")
    print("=" * 70)

    # Test 1: BFS Traversal
    print("\n1. BFS Traversal:")
    g1 = Graph(5, "adjacency_list")
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(1, 3)
    g1.add_edge(2, 4)
    result = bfs_traversal(g1, 0)
    print(f"   Graph: 0-1-3, 0-2-4")
    print(f"   BFS from 0: {result}")

    # Test 2: Shortest Path
    print("\n2. Shortest Path (BFS):")
    g2 = Graph(6)
    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(1, 3)
    g2.add_edge(2, 3)
    g2.add_edge(3, 4)
    g2.add_edge(3, 5)
    path = shortest_path_bfs(g2, 0, 5)
    print(f"   Graph: 0-1-3-4, 0-2-3-5")
    print(f"   Shortest path from 0 to 5: {path}")
    print(f"   Path length: {len(path) if path else 0}")

    # Test 3: Level-Order Traversal
    print("\n3. Level-Order Traversal:")
    g3 = Graph(7)
    g3.add_edge(0, 1)
    g3.add_edge(0, 2)
    g3.add_edge(1, 3)
    g3.add_edge(1, 4)
    g3.add_edge(2, 5)
    g3.add_edge(2, 6)
    levels = level_order_traversal(g3, 0)
    print(f"   Binary tree structure starting from 0")
    print(f"   Levels:")
    for i, level in enumerate(levels):
        print(f"   - Level {i}: {level}")

    # Test 4: Word Ladder
    print("\n4. Word Ladder:")
    words1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    sequence = word_ladder("hit", "cog", words1)
    print(f"   Start: 'hit', End: 'cog'")
    print(f"   Word list: {words1}")
    print(f"   Transformation sequence: {' → '.join(sequence) if sequence else 'No path found'}")

    words2 = ["hot", "dot", "dog", "lot", "log"]
    sequence2 = word_ladder("hit", "cog", words2)
    print(f"\n   Start: 'hit', End: 'cog' (not in list)")
    print(f"   Word list: {words2}")
    print(f"   Transformation sequence: {' → '.join(sequence2) if sequence2 else 'No path found'}")

    # Test 5: Shortest path in unweighted graph
    print("\n5. BFS vs DFS - Shortest Path:")
    g4 = Graph(4)
    g4.add_edge(0, 1)
    g4.add_edge(0, 2)
    g4.add_edge(1, 3)
    g4.add_edge(2, 1)
    g4.add_edge(2, 3)
    path1 = shortest_path_bfs(g4, 0, 3)
    print(f"   Diamond graph: 0->1->3, 0->2->3, 2->1")
    print(f"   BFS shortest path from 0 to 3: {path1}")
    print(f"   Path length: {len(path1) if path1 else 0} (guaranteed shortest)")

    print("\n" + "=" * 70)
    print("All BFS algorithms demonstrated!")
