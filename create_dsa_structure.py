#!/usr/bin/env python3
"""
Script to create the Data Structures & Algorithms course structure.
"""

import os
from pathlib import Path

# Define all DSA projects
DSA_PROJECTS = [
    # Part 1: Python Fundamentals & Arrays (1-5)
    (1, "python-basics-review", "Python Basics Review"),
    (2, "array-operations", "Array Operations & List Manipulation"),
    (3, "two-pointer-technique", "Two Pointer Technique"),
    (4, "sliding-window", "Sliding Window Problems"),
    (5, "prefix-sum-arrays", "Prefix Sum Arrays"),

    # Part 2: Sorting & Searching (6-10)
    (6, "bubble-selection-insertion-sort", "Bubble, Selection & Insertion Sort"),
    (7, "merge-sort", "Merge Sort"),
    (8, "quick-sort", "Quick Sort"),
    (9, "binary-search", "Binary Search"),
    (10, "search-variations", "Binary Search Variations"),

    # Part 3: Stacks & Queues (11-15)
    (11, "stack-implementation", "Stack Implementation"),
    (12, "queue-implementation", "Queue Implementation"),
    (13, "monotonic-stack", "Monotonic Stack"),
    (14, "deque-problems", "Deque Problems"),
    (15, "stack-queue-applications", "Stack & Queue Applications"),

    # Part 4: Linked Lists (16-20)
    (16, "singly-linked-list", "Singly Linked List"),
    (17, "doubly-linked-list", "Doubly Linked List"),
    (18, "linked-list-two-pointers", "Linked List Two Pointers"),
    (19, "linked-list-reversal", "Linked List Reversal"),
    (20, "linked-list-advanced", "Advanced Linked List Problems"),

    # Part 5: Hash Tables (21-25)
    (21, "hash-table-implementation", "Hash Table Implementation"),
    (22, "hash-map-problems", "Hash Map Problems"),
    (23, "hash-set-problems", "Hash Set Problems"),
    (24, "frequency-counting", "Frequency Counting Patterns"),
    (25, "two-sum-variations", "Two Sum Variations"),

    # Part 6: Trees (26-30)
    (26, "binary-tree-basics", "Binary Tree Basics"),
    (27, "tree-traversals", "Tree Traversals (Inorder, Preorder, Postorder)"),
    (28, "binary-search-tree", "Binary Search Tree"),
    (29, "tree-construction", "Tree Construction Problems"),
    (30, "tree-advanced", "Advanced Tree Problems"),

    # Part 7: Heaps & Priority Queues (31-33)
    (31, "heap-implementation", "Heap Implementation"),
    (32, "heap-problems", "Heap Problems"),
    (33, "top-k-problems", "Top K Problems"),

    # Part 8: Graphs (34-40)
    (34, "graph-representation", "Graph Representation"),
    (35, "graph-dfs", "Depth-First Search"),
    (36, "graph-bfs", "Breadth-First Search"),
    (37, "graph-shortest-path", "Shortest Path Algorithms"),
    (38, "topological-sort", "Topological Sort"),
    (39, "union-find", "Union Find (Disjoint Set)"),
    (40, "graph-advanced", "Advanced Graph Problems"),

    # Part 9: Dynamic Programming (41-47)
    (41, "dp-fibonacci-patterns", "DP: Fibonacci Patterns"),
    (42, "dp-01-knapsack", "DP: 0/1 Knapsack"),
    (43, "dp-unbounded-knapsack", "DP: Unbounded Knapsack"),
    (44, "dp-longest-common-subsequence", "DP: Longest Common Subsequence"),
    (45, "dp-palindromes", "DP: Palindrome Problems"),
    (46, "dp-2d-problems", "DP: 2D Grid Problems"),
    (47, "dp-advanced", "DP: Advanced Problems"),

    # Part 10: Backtracking & Recursion (48-50)
    (48, "recursion-fundamentals", "Recursion Fundamentals"),
    (49, "backtracking-basics", "Backtracking Basics"),
    (50, "backtracking-advanced", "Advanced Backtracking Problems"),
]


def create_dsa_structure():
    """Create the directory structure for all DSA projects."""
    base_dir = Path("/home/user/python-edu/dsa/projects")
    base_dir.mkdir(parents=True, exist_ok=True)

    for num, slug, title in DSA_PROJECTS:
        # Create project directory
        project_dir = base_dir / f"{num:02d}-{slug}"
        project_dir.mkdir(exist_ok=True)

        # Create subdirectories
        (project_dir / "solution").mkdir(exist_ok=True)
        (project_dir / "tests").mkdir(exist_ok=True)

        # Create README.md stub
        readme_path = project_dir / "README.md"
        if not readme_path.exists():
            with open(readme_path, "w") as f:
                f.write(f"# Project {num:02d}: {title}\n\n")
                f.write(f"## Overview\n\n")
                f.write(f"Learn {title.lower()} through hands-on implementation.\n\n")
                f.write(f"## Learning Objectives\n\n")
                f.write(f"- Understand the theory behind {title.lower()}\n")
                f.write(f"- Implement solutions from scratch\n")
                f.write(f"- Analyze time and space complexity\n")
                f.write(f"- Solve real-world problems\n\n")
                f.write(f"## Problems\n\n")
                f.write(f"Complete the problems in `solution/solution.py`.\n\n")
                f.write(f"## Testing\n\n")
                f.write(f"```bash\n")
                f.write(f"pytest tests/ -v\n")
                f.write(f"```\n")

        # Create solution_in_words.md stub
        solution_words_path = project_dir / "solution_in_words.md"
        if not solution_words_path.exists():
            with open(solution_words_path, "w") as f:
                f.write(f"# Project {num:02d}: {title} - Solution Explained\n\n")
                f.write(f"## Concept Overview\n\n")
                f.write(f"[Explanation of {title}]\n\n")
                f.write(f"## Approach\n\n")
                f.write(f"[Problem-solving approach]\n\n")
                f.write(f"## Complexity Analysis\n\n")
                f.write(f"[Time and space complexity]\n\n")
                f.write(f"## Key Takeaways\n\n")
                f.write(f"[Important lessons]\n")

        # Create solution.py stub
        solution_file = project_dir / "solution" / "solution.py"
        if not solution_file.exists():
            with open(solution_file, "w") as f:
                f.write(f'"""\n')
                f.write(f"Project {num:02d}: {title}\n\n")
                f.write(f"Data Structures & Algorithms in Python\n")
                f.write(f'"""\n\n')
                f.write(f"# Implementation coming soon\n")

        # Create __init__.py files
        (project_dir / "solution" / "__init__.py").touch(exist_ok=True)
        (project_dir / "tests" / "__init__.py").touch(exist_ok=True)

        # Create test stub
        test_file = project_dir / "tests" / f"test_project_{num:02d}.py"
        if not test_file.exists():
            with open(test_file, "w") as f:
                f.write(f'"""\n')
                f.write(f"Tests for Project {num:02d}: {title}\n")
                f.write(f'"""\n\n')
                f.write(f"import pytest\n\n\n")
                f.write(f"def test_placeholder():\n")
                f.write(f'    """Placeholder test."""\n')
                f.write(f"    assert True\n")

        print(f"✓ Created DSA Project {num:02d}: {title}")

    print(f"\n✅ Successfully created all {len(DSA_PROJECTS)} DSA project directories!")
    print(f"📁 Location: {base_dir}")


if __name__ == "__main__":
    create_dsa_structure()
