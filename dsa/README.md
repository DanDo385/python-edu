# Data Structures & Algorithms in Python (50 Projects)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE)
[![Projects](https://img.shields.io/badge/projects-50-brightgreen.svg)](PROJECT_SUMMARY.md)

Master data structures and algorithms through 50 hands-on projects designed for coding interviews, competitive programming, and building a strong foundation in computer science.

## 🎯 Overview

This curriculum provides a comprehensive learning path for:
- **Coding Interview Preparation** (FAANG, tech companies)
- **Competitive Programming** (LeetCode, HackerRank, Codeforces)
- **Computer Science Fundamentals**
- **Algorithm Design & Analysis**

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Basic programming knowledge
- Willingness to solve problems!

### Installation

```bash
# Navigate to DSA curriculum
cd dsa

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# No dependencies needed - pure Python!
```

###Your First Project

```bash
# Start with Project 01
cd projects/01-python-basics-review

# Read the README
cat README.md

# Implement solutions
code solution/solution.py

# Run tests
pytest tests/ -v
```

## 📚 Curriculum Structure

### Part 1: Python Fundamentals & Arrays (Projects 1-5)
Master Python basics and array manipulation techniques.

### Part 2: Sorting & Searching (Projects 6-10)
Implement classic sorting algorithms and binary search variations.

### Part 3: Stacks & Queues (Projects 11-15)
Build and apply stack and queue data structures.

### Part 4: Linked Lists (Projects 16-20)
Implement linked list variations and solve pointer manipulation problems.

### Part 5: Hash Tables (Projects 21-25)
Master hash-based data structures and pattern recognition.

### Part 6: Trees (Projects 26-30)
Work with binary trees, BSTs, and tree traversal algorithms.

### Part 7: Heaps & Priority Queues (Projects 31-33)
Implement heaps and solve top-K problems.

### Part 8: Graphs (Projects 34-40)
Master graph algorithms including DFS, BFS, shortest paths, and more.

### Part 9: Dynamic Programming (Projects 41-47)
Learn DP patterns from Fibonacci to advanced 2D problems.

### Part 10: Backtracking & Recursion (Projects 48-50)
Master recursive problem-solving and backtracking techniques.

## 🎓 Learning Path

### For Beginners (3-4 months)
**Start at Project 01**, work sequentially through all 50 projects.
- **Time**: 10-15 hours/week × 12-16 weeks
- **Focus**: Understanding concepts, implementing from scratch
- **Goal**: Build strong foundation in DSA

### For Interview Preparation (6-8 weeks)
**Focus on key patterns** and problem-solving techniques.
- **Time**: 15-25 hours/week × 6-8 weeks
- **Focus**: Projects 3-5, 9-10, 13-15, 18-20, 22-25, 27-30, 35-40, 41-47
- **Goal**: Pass technical interviews at top companies

### For Competitive Programming (2-3 months)
**Master advanced techniques** and optimize for speed.
- **Time**: 20-30 hours/week × 8-12 weeks
- **Focus**: All projects, emphasize Part 8-10
- **Goal**: Compete effectively in programming contests

## 📊 By Project 50, You Will Have

✅ **Implemented from scratch**:
- 10+ sorting and searching algorithms
- All major data structures (arrays, linked lists, trees, graphs, heaps)
- 40+ algorithm patterns (two-pointer, sliding window, DFS, BFS, DP)
- Classic CS algorithms (Dijkstra, Topological Sort, Union-Find)

✅ **Solved 200+ problems** across:
- LeetCode-style coding challenges
- Real interview questions
- Competitive programming problems

✅ **Mastered**:
- Time and space complexity analysis (Big-O)
- Algorithm design techniques
- Problem-solving patterns
- Code optimization strategies

## 🧪 Testing

Each project includes comprehensive tests:

```bash
# Run tests for specific project
cd projects/09-binary-search
pytest tests/ -v

# Run all tests
pytest projects/ -v

# Run with coverage
pytest projects/ --cov=. --cov-report=html
```

## 📖 Project Structure

Each project follows this structure:

```
projects/NN-name/
├── README.md                # Problem description, examples, constraints
├── solution_in_words.md     # Detailed explanation and approach
├── solution/
│   └── solution.py          # Fully implemented and commented solution
└── tests/
    └── test_project_NN.py   # Comprehensive test suite
```

## 🎯 Difficulty Levels

| Symbol | Level | Description |
|--------|-------|-------------|
| ⭐ | **Easy** | Fundamental concepts, straightforward implementation |
| ⭐⭐ | **Medium** | Requires problem-solving, multiple concepts |
| ⭐⭐⭐ | **Hard** | Complex algorithms, optimization needed |
| ⭐⭐⭐⭐ | **Expert** | Advanced techniques, contest-level problems |

## 💡 Study Tips

### 1. **Understand Before Implementing**
- Read the problem thoroughly
- Draw examples and edge cases
- Plan your approach before coding

### 2. **Implement from Scratch First**
- Don't look at solutions immediately
- Struggle is part of learning
- Use hints only when truly stuck

### 3. **Analyze Complexity**
- Always determine time and space complexity
- Optimize after getting a working solution
- Learn to recognize patterns

### 4. **Practice Consistently**
- Solve 1-2 problems daily
- Review previous solutions weekly
- Gradually increase difficulty

### 5. **Test Thoroughly**
- Think of edge cases
- Test with provided test suite
- Add your own test cases

## 🔗 Additional Resources

- [LeetCode](https://leetcode.com/) - Practice platform
- [HackerRank](https://www.hackerrank.com/) - Coding challenges
- [Visualgo](https://visualgo.net/) - Algorithm visualizations
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) - Complexity reference

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add your solution/improvement
4. Submit a pull request

## 📄 License

MIT License. See [LICENSE](../LICENSE) for details.

## 🙏 Acknowledgments

Inspired by:
- *Introduction to Algorithms* (CLRS)
- *Cracking the Coding Interview* (Gayle Laakmann McDowell)
- LeetCode problem collections
- Competitive programming community

---

**Start your journey to DSA mastery today!** 🚀

*"The best way to learn algorithms is to implement them."*

Last updated: 2025-11-16
