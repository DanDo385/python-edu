# 🐍 Python-50x-Minis: From Basics to Building GPT

> **Master Python, Algorithms, Machine Learning Math, PyTorch, and LLMs through 50 progressive hands-on projects**

[![Python 3.12.12](https://img.shields.io/badge/python-3.12.12-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Projects](https://img.shields.io/badge/projects-50-brightgreen.svg)](./PROJECT_SUMMARY.md)

---

## 🎯 What is This?

**A complete, production-grade learning path** that takes you from Python syntax to training and serving GPT-style language models.  No hand-waving, no magic—just **first-principles understanding** with runnable code.

### What Makes This Different?

✅ **First Principles**: Build everything from scratch before using libraries
✅ **50 Projects**: Structured curriculum from "Hello World" to "Deploy an LLM"
✅ **Production Quality**: Heavy documentation, type hints, comprehensive tests
✅ **Math Intuition**: Linear algebra, calculus, and autodiff explained visually
✅ **Full Stack**: From pure Python → NumPy → PyTorch → Transformers

---

## 🚀 Quick Start

### Prerequisites
- Python 3.12.12 installed
- Basic programming knowledge (any language)
- 4-8 GB RAM (16 GB for Phase IV transformer training)
- Curiosity and willingness to debug!

### Installation

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd python-edu

# 2. Create virtual environment (Python 3.12 required)
python3.12 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies (phases unlock incrementally)
pip install --upgrade pip
pip install -r requirements-dev.txt

# 4. Verify setup
python --version  # Should show 3.12.12
pytest --version
python -c "import numpy; print(numpy.__version__)"
python -c "import torch; print(torch.__version__)"

# 5. Run sample tests (should pass)
pytest project-01-basic-python-syntax/test/ -v
```

### Your First 30 Minutes

```bash
# Phase I starts with ZERO dependencies (pure Python)
cd project-01-basic-python-syntax

# Read the comprehensive README
cat README.md

# Study the exercise (with TODOs and hints)
cat exercise.py

# Check the solution (HEAVILY commented)
cat solution/solution.py

# Read the human-friendly walkthrough
cat solution_in_words.md

# Run the tests
pytest test/test_project_01.py -v

# Try implementing yourself!
python exercise.py
```

---

## 📚 Curriculum Overview

### Phase I: Python & Data Structures (Projects 01–15)
**Goal**: Master Python syntax and ace coding interviews

```
01. Basic Python Syntax        ⭐
02. Control Flow & Loops        ⭐
03. Functions & Modules         ⭐
04. Lists & Tuples              ⭐
05. Dictionaries & Sets         ⭐
06. OOP Basics                  ⭐⭐
07. OOP Advanced                ⭐⭐
08. Recursion & Divide-Conquer  ⭐⭐
09. Searching Algorithms        ⭐⭐
10. Sorting Algorithms          ⭐⭐
11. Stack & Queue               ⭐⭐
12. Linked Lists                ⭐⭐
13. Binary Trees                ⭐⭐⭐
14. Graphs & Traversal          ⭐⭐⭐
15. Dynamic Programming         ⭐⭐⭐
```

**Dependencies**: NONE (pure Python standard library)

---

### Phase II: ML Math & Autodiff (Projects 16–30)
**Goal**: Build neural networks from scratch (no frameworks)

```
16. NumPy 101                   ⭐⭐
17. NumPy Advanced              ⭐⭐
18. Linear Algebra Essentials   ⭐⭐
19. Gradient Descent Basics     ⭐⭐
20. Linear Regression           ⭐⭐
21. Logistic Regression         ⭐⭐
22. Activation Functions        ⭐⭐
23. Manual Backpropagation      ⭐⭐⭐
24. Autodiff Engine             ⭐⭐⭐
25. MLP from Scratch            ⭐⭐⭐
26. Model Evaluation            ⭐⭐
27. Regularization              ⭐⭐
28. Hyperparameter Tuning       ⭐⭐
29. Batch Gradient Descent      ⭐⭐
30. MNIST NumPy Capstone        ⭐⭐⭐
```

**New Dependencies**: `numpy`, `matplotlib`
**Milestone**: Train a neural network that recognizes handwritten digits—in pure NumPy!

---

### Phase III: PyTorch Systems (Projects 31–40)
**Goal**: Production deep learning with PyTorch

```
31. PyTorch Tensors & GPU       ⭐⭐
32. PyTorch Autograd            ⭐⭐
33. PyTorch Modules             ⭐⭐
34. PyTorch MNIST Training      ⭐⭐
35. CNN on CIFAR-10             ⭐⭐⭐
36. Text Classification (IMDB)  ⭐⭐⭐
37. Advanced Training           ⭐⭐
38. Transfer Learning           ⭐⭐⭐
39. Char-RNN (Shakespeare)      ⭐⭐⭐
40. Seq2Seq + Attention         ⭐⭐⭐
```

**New Dependencies**: `torch`, `torchvision`, `torchtext`
**Milestone**: Train CNNs, RNNs, and understand attention mechanisms

---

### Phase IV: Transformers & LLMs (Projects 41–50)
**Goal**: Build and deploy GPT-style models

```
41. Scaled Dot-Product Attention  ⭐⭐⭐
42. Transformer Blocks            ⭐⭐⭐
43. GPT Decoder Model             ⭐⭐⭐⭐
44. Tokenization (BPE)            ⭐⭐⭐
45. BabyGPT Training              ⭐⭐⭐⭐
46. LLM Inference & Decoding      ⭐⭐⭐
47. Model Quantization            ⭐⭐⭐
48. LLM Serving API               ⭐⭐⭐
49. RAG System                    ⭐⭐⭐⭐
50. LLM System Design             ⭐⭐⭐⭐
```

**New Dependencies**: `einops`, `sentencepiece`, `transformers`, `faiss-cpu`, `fastapi`
**Milestone**: Train a GPT from scratch, deploy it behind an API, and build a RAG system

---

## 📖 Learning Paths

### 🎓 Complete Beginner (6-12 months)
**Start at Project 01**, work sequentially through all 50 projects.

**Time**: ~6-10 hours/week × 24-48 weeks

### 💼 Experienced Programmer (3-6 months)
**Skim Phase I** (01-15), focus on Python idioms.
**Deep dive Phase II-IV** (16-50).

**Time**: ~10-15 hours/week × 12-24 weeks

### 🤖 ML Engineer (2-4 months)
**Skip to Project 16** (NumPy).
If comfortable with PyTorch, start at **Project 31**.
Focus heavily on **Phase IV** (Transformers).

**Time**: ~15-20 hours/week × 8-16 weeks

### 🚀 Interviewing for FAANG?
**Focus on Phase I** (01-15): Data structures, algorithms, complexity analysis.

**Time**: ~20 hours/week × 4-6 weeks

---

## 🎯 By Project 50, You Will Have

✅ **Implemented from scratch**:
- Core algorithms (sorting, search, graphs, DP)
- Neural network training (backprop, autodiff)
- Transformer architecture (attention, FFN, LayerNorm)
- GPT-style decoder model
- Text tokenizer (BPE)

✅ **Trained real models**:
- MNIST digit classifier (NumPy only!)
- CIFAR-10 CNN (ResNet-style)
- IMDB sentiment classifier (LSTM/Embedding)
- BabyGPT language model (WikiText-2)

✅ **Deployed systems**:
- REST API for LLM inference (FastAPI)
- RAG question-answering system (vector DB + LLM)

✅ **Mastered concepts**:
- Python internals (types, memory, GIL)
- Complexity analysis (Big-O, space/time)
- Linear algebra & calculus for ML
- Numerical stability & optimization
- GPU programming basics
- Production ML systems

---

## 📂 Project Structure

Each of the 50 projects follows this structure:

```
project-NN-name/
├── README.md                # What, Why, When, Pitfalls, How
├── exercise.py              # Your playground (TODOs + hints)
├── solution/
│   └── solution.py          # Full implementation (HEAVILY commented)
├── test/
│   └── test_project_NN.py   # Pytest suite (positive, edge, property tests)
├── notebook.ipynb           # Jupyter notebook (Phase II+)
└── solution_in_words.md     # Human-readable walkthrough + ASCII diagrams
```

### README Template (10 Sections)
1. **What** — Mechanics & code concepts
2. **Why** — Math, architecture, intuition
3. **When** — Real-world applicability
4. **Pitfalls** — Common bugs & gotchas
5. **Performance** — Time/space complexity, CPU vs GPU
6. **Diagrams** — ASCII art visualizations
7. **Walkthrough** — Step-by-step reasoning
8. **Cross-language** — Python vs Rust/C/JS/Go
9. **Challenges** — Advanced extensions
10. **How to Run** — Test commands + expected output

---

## 🧪 Testing Philosophy

Every project includes comprehensive pytest suites:

```bash
# Run all tests
pytest

# Run tests for specific phase
pytest -m phase1
pytest -m "phase2 or phase3"

# Run single project
pytest project-05-dictionaries-sets/test/

# With coverage
pytest --cov=. --cov-report=html

# Verbose + show print statements
pytest -v -s

# Stop at first failure
pytest -x

# Run only slow tests
pytest -m slow

# Skip slow tests
pytest -m "not slow"
```

**Test categories**:
- ✅ Positive (happy path)
- ✅ Edge cases (empty, None, boundary)
- ✅ Error handling (invalid inputs)
- ✅ Property-based (Hypothesis, optional)
- ✅ Performance (benchmarks where relevant)

---

## 📚 Documentation & References

### Root Documentation
- [PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md) — 50-project curriculum
- [PYTHON_BASICS.md](./PYTHON_BASICS.md) — Syntax quick reference
- [DSA_PRIMER.md](./DSA_PRIMER.md) — Algorithm patterns & Big-O
- [MACHINE_LEARNING_MATH.md](./MACHINE_LEARNING_MATH.md) — Linear algebra, calculus, probability
- [AUTODIFF_FROM_SCRATCH.md](./AUTODIFF_FROM_SCRATCH.md) — Building backpropagation intuition
- [PYTORCH_INTERNALS.md](./PYTORCH_INTERNALS.md) — How PyTorch works under the hood
- [TRANSFORMERS_EXPLAINED.md](./TRANSFORMERS_EXPLAINED.md) — Attention mechanism deep dive
- [GPU_PRIMER.md](./GPU_PRIMER.md) — CUDA, parallelism, hardware
- [LLM_SYSTEMS_OVERVIEW.md](./LLM_SYSTEMS_OVERVIEW.md) — Production LLM architecture

### External Resources
- **Andrej Karpathy**: *Neural Networks: Zero to Hero* (YouTube)
- **Vaswani et al.**: *Attention Is All You Need* (2017)
- **Goodfellow et al.**: *Deep Learning* (book)
- **PyTorch Docs**: https://pytorch.org/docs/
- **HuggingFace**: https://huggingface.co/docs

---

## 🎓 Documentation Style

### Extreme Detail Philosophy
Every `solution/solution.py` contains:

1. **Module docstring** (100-200 lines): Overview, concepts, usage
2. **Function docstrings** (20-50 lines): Args, returns, complexity, examples
3. **Inline comments** (every line): What, why, trade-offs
4. **ASCII diagrams**: Visualize algorithms & data flow
5. **Performance notes**: Big-O, benchmarks, optimization tips
6. **Cross-language comparisons**: Python vs Rust/C/JS

**Example snippet**:
```python
"""
Project 24: Autodiff Engine from Scratch

Build a minimal automatic differentiation system (like micrograd).

WHAT YOU'LL BUILD:
- Tensor class with gradient tracking
- Computation graph (DAG of operations)
- Backward pass (reverse-mode autodiff)
- Chain rule application
- Support for: +, *, -, /, **, relu, exp, log

WHY THIS MATTERS:
Every modern DL framework (PyTorch, TensorFlow, JAX) uses autodiff.
By building one yourself, you'll understand:
- How .backward() works
- Why requires_grad=True exists
- How to debug gradient issues
- The performance of backpropagation

TIME COMPLEXITY: O(V + E) where V=nodes, E=edges in compute graph
SPACE COMPLEXITY: O(V) for gradient storage
"""

class Tensor:
    """
    A tensor with automatic differentiation support.

    Stores both the value (forward pass) and gradient (backward pass).
    Builds a computation graph for backpropagation.

    Attributes:
        data: The actual value (float or ndarray)
        grad: Accumulated gradient (same shape as data)
        _backward: Function to propagate gradients to parents
        _prev: Set of parent tensors (for graph traversal)
        _op: Operation name (for debugging)
    """
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0.0  # Accumulated gradient
        self._backward = lambda: None  # Closure for backprop
        self._prev = set(_children)  # Parent nodes
        self._op = _op  # '+', '*', 'relu', etc.

    def __add__(self, other):
        """
        Addition operation with autodiff support.

        Derivative rules:
        - d(a + b)/da = 1
        - d(a + b)/db = 1

        Gradient flows equally to both operands.
        """
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(self.data + other.data, (self, other), '+')

        def _backward():
            # Chain rule: grad flows from output to inputs
            self.grad += out.grad  # Multiply by local gradient (1)
            other.grad += out.grad
        out._backward = _backward

        return out
```

---

## 🤝 Contributing

This is a teaching repository—contributions welcome!

**How to contribute**:
1. **Found a bug?** Open an issue
2. **Better explanation?** Submit a PR
3. **Want to add content?** Discuss in issues first

**Style guidelines**:
- Match existing documentation density
- Include type hints everywhere
- Add tests for new code
- Cross-reference related projects
- Use ASCII diagrams liberally

---

## 📜 License

MIT License — use freely for learning, teaching, or any purpose!

See [LICENSE](./LICENSE) file for details.

---

## 🙏 Acknowledgments

**Inspired by**:
- Andrej Karpathy's micrograd & nanoGPT
- FastAI's teaching philosophy
- SICP's first-principles approach
- PyTorch & HuggingFace communities

**Built for**:
- Self-learners seeking depth
- Bootcamp students needing rigor
- CS students wanting practical skills
- Engineers transitioning to ML/AI

---

## 🚀 Next Steps

1. **Read** [PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md) — See full curriculum
2. **Install** dependencies — `pip install -r requirements-dev.txt`
3. **Start** [Project 01](./project-01-basic-python-syntax/) — Begin your journey!
4. **Join** discussions — Share progress, ask questions, help others

---

## 💡 Final Thoughts

> *"Understanding beats memorization. Building beats watching tutorials."*

This repository is **not**:
- ❌ A quick tutorial
- ❌ Copy-paste code snippets
- ❌ Surface-level explanations

This repository **is**:
- ✅ A rigorous, first-principles curriculum
- ✅ Production-quality code with extreme documentation
- ✅ A path from "Hello World" to "I built GPT"

By Project 50, you won't just know *how* to use PyTorch or transformers—you'll understand **why they work**, **when to use them**, and **how to build them yourself**.

---

**Happy learning! 🐍 → 🤖 → 🚀**

*Code is read more often than it's written. This repo optimizes for learning, not brevity.*

Last updated: 2025-11-16
