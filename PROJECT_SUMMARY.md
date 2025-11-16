# Python-50x-Minis: Complete Project Curriculum

**From Python Basics to LLM Engineering in 50 Progressive Projects**

> A production-grade learning path for mastering Python, data structures, machine learning math, PyTorch systems, and transformer-based language models—built from first principles.

---

## Phase I — Python & DSA Fundamentals (Projects 01–15)

**Goal**: Master Python syntax and interview-ready algorithms

| # | Project Name | One-Line Description | Difficulty |
|---|--------------|---------------------|------------|
| 01 | `basic-python-syntax` | Variables, types, I/O, arithmetic—your first Python program | ⭐ Beginner |
| 02 | `control-flow-loops` | Conditionals, for/while loops, FizzBuzz, break/continue | ⭐ Beginner |
| 03 | `functions-modules` | Function definitions, scope, imports, docstrings, code organization | ⭐ Beginner |
| 04 | `lists-tuples` | Sequence operations, slicing, comprehensions, mutability vs immutability | ⭐ Beginner |
| 05 | `dictionaries-sets` | Hash maps, set operations, word frequency, uniqueness checks | ⭐ Beginner |
| 06 | `oop-basics` | Classes, objects, `__init__`, methods, encapsulation, BankAccount example | ⭐⭐ Intermediate |
| 07 | `oop-advanced` | Inheritance, polymorphism, exceptions, custom error types, Shape hierarchy | ⭐⭐ Intermediate |
| 08 | `recursion-divide-conquer` | Factorial, Fibonacci, GCD, recursive binary search, call stack visualization | ⭐⭐ Intermediate |
| 09 | `searching-algorithms` | Linear search O(n), binary search O(log n), complexity analysis | ⭐⭐ Intermediate |
| 10 | `sorting-algorithms` | Insertion sort, merge sort, quicksort, stability, in-place vs out-of-place | ⭐⭐ Intermediate |
| 11 | `stack-queue` | LIFO/FIFO structures, balanced parentheses, BFS simulation, deque usage | ⭐⭐ Intermediate |
| 12 | `linked-lists` | Node-based structures, insertion, deletion, reversal, pointer manipulation | ⭐⭐ Intermediate |
| 13 | `binary-trees` | Tree traversals (in/pre/post-order), BST operations, height calculation | ⭐⭐⭐ Advanced |
| 14 | `graphs-traversal` | Adjacency lists/matrix, DFS, BFS, path finding, connected components | ⭐⭐⭐ Advanced |
| 15 | `dynamic-programming` | Memoization, tabulation, coin change, knapsack, subproblem optimization | ⭐⭐⭐ Advanced |

---

## Phase II — ML Math & Autodiff (Projects 16–30)

**Goal**: Build ML intuition and implement neural networks from scratch

| # | Project Name | One-Line Description | Difficulty |
|---|--------------|---------------------|------------|
| 16 | `numpy-101` | Ndarrays, vectorization, broadcasting basics, shape manipulation, dtype | ⭐⭐ Intermediate |
| 17 | `numpy-advanced` | Broadcasting rules, matrix ops, @-operator, performance optimization | ⭐⭐ Intermediate |
| 18 | `linear-algebra-essentials` | Dot products, matrix multiplication, solving Ax=b, projections, eigenvalues | ⭐⭐ Intermediate |
| 19 | `gradient-descent-basics` | 1D optimization, learning rate α, convergence criteria, loss landscapes | ⭐⭐ Intermediate |
| 20 | `linear-regression-scratch` | MSE loss, gradient ∂L/∂w, fitting y=wx+b, visualization with matplotlib | ⭐⭐ Intermediate |
| 21 | `logistic-regression` | Sigmoid σ(z), binary cross-entropy, classification, decision boundaries | ⭐⭐ Intermediate |
| 22 | `activation-functions` | ReLU, tanh, softmax, derivatives for backprop, dead neuron problem | ⭐⭐ Intermediate |
| 23 | `manual-backpropagation` | Chain rule ∂L/∂w, gradient flow, 2-layer MLP, numerical gradient checks | ⭐⭐⭐ Advanced |
| 24 | `autodiff-engine` | Computational graphs, reverse-mode AD, Tensor class, .backward() | ⭐⭐⭐ Advanced |
| 25 | `mlp-from-scratch` | Multi-layer perceptron, XOR problem, non-linear separation, training loop | ⭐⭐⭐ Advanced |
| 26 | `model-evaluation` | Train/val/test splits, accuracy/precision/recall, confusion matrix, k-fold CV | ⭐⭐ Intermediate |
| 27 | `regularization` | L1/L2 penalty, dropout, early stopping, overfitting vs underfitting curves | ⭐⭐ Intermediate |
| 28 | `hyperparameter-tuning` | Grid search, random search, LR schedules, validation-based selection | ⭐⭐ Intermediate |
| 29 | `batch-gradient-descent` | SGD vs batch vs mini-batch, momentum, RMSprop, Adam optimizer concepts | ⭐⭐ Intermediate |
| 30 | `mnist-numpy-capstone` | Full MNIST digit classifier in pure NumPy—Phase II capstone project | ⭐⭐⭐ Advanced |

---

## Phase III — PyTorch Systems & Deep Learning (Projects 31–40)

**Goal**: Master PyTorch for production deep learning

| # | Project Name | One-Line Description | Difficulty |
|---|--------------|---------------------|------------|
| 31 | `pytorch-tensors-gpu` | torch.Tensor, .to('cuda'), device management, CPU vs GPU benchmarking | ⭐⭐ Intermediate |
| 32 | `pytorch-autograd` | requires_grad=True, .backward(), .grad, detach(), no_grad() context | ⭐⭐ Intermediate |
| 33 | `pytorch-modules` | nn.Module subclassing, custom layers, parameter registration, forward() | ⭐⭐ Intermediate |
| 34 | `pytorch-mnist-training` | DataLoader, SGD/Adam, training loop, validation, checkpoint saving (.pth) | ⭐⭐ Intermediate |
| 35 | `cnn-cifar10` | nn.Conv2d, pooling, batch norm, image classification on CIFAR-10 | ⭐⭐⭐ Advanced |
| 36 | `embeddings-text-classification` | nn.Embedding, LSTM/GRU, IMDB sentiment, padding/packing sequences | ⭐⭐⭐ Advanced |
| 37 | `advanced-training` | Adam optimizer, LR schedulers, gradient clipping, TensorBoard logging | ⭐⭐ Intermediate |
| 38 | `transfer-learning` | Pretrained ResNet-18, fine-tuning, layer freezing, feature extraction | ⭐⭐⭐ Advanced |
| 39 | `char-rnn-shakespeare` | Character-level language model, LSTM, text generation, sampling strategies | ⭐⭐⭐ Advanced |
| 40 | `seq2seq-attention` | Encoder-decoder RNN, Bahdanau attention, toy translation task | ⭐⭐⭐ Advanced |

---

## Phase IV — Transformers & LLMs (Projects 41–50)

**Goal**: Build and deploy GPT-style models from scratch

| # | Project Name | One-Line Description | Difficulty |
|---|--------------|---------------------|------------|
| 41 | `scaled-dot-product-attention` | Q/K/V mechanics, softmax(QK^T/√d_k)V, masking, attention from scratch | ⭐⭐⭐ Advanced |
| 42 | `transformer-blocks` | Multi-head attention, FFN, LayerNorm, residuals, sinusoidal pos encoding | ⭐⭐⭐ Advanced |
| 43 | `gpt-decoder-model` | Full GPT architecture, causal masking, stacked decoder layers, LM head | ⭐⭐⭐⭐ Expert |
| 44 | `tokenization-bpe` | Byte-pair encoding, SentencePiece training, vocab building, dataset prep | ⭐⭐⭐ Advanced |
| 45 | `babygpt-training` | Train GPT from scratch on WikiText-2, loss curves, perplexity, sampling | ⭐⭐⭐⭐ Expert |
| 46 | `llm-inference-decoding` | Greedy, beam search, top-k/top-p (nucleus), temperature τ scaling | ⭐⭐⭐ Advanced |
| 47 | `model-quantization` | INT8/FP16 quantization, torch.quantization, memory/speed tradeoffs | ⭐⭐⭐ Advanced |
| 48 | `llm-serving-api` | FastAPI endpoints, batching, concurrent requests, model deployment | ⭐⭐⭐ Advanced |
| 49 | `rag-system` | Vector DB (FAISS), embeddings, retrieval-augmented generation, Q&A | ⭐⭐⭐⭐ Expert |
| 50 | `llm-system-design` | Architecture planning, scaling, monitoring, ethics, production LLM systems | ⭐⭐⭐⭐ Expert |

---

## Learning Path Overview

### Stats at a Glance
- **Total Projects**: 50
- **Estimated Time**: 6–12 months (self-paced, 10–15 hrs/week)
- **Prerequisites**: Basic computer literacy, curiosity, willingness to debug
- **Language**: Python 3.12.12
- **Target Audience**: Self-learners, bootcamp students, CS undergrads, career-switchers into AI/ML

### What You'll Build
By project 50, you will have:
- ✅ Implemented core CS algorithms (sorting, search, graphs, DP)
- ✅ Built neural networks from scratch (no frameworks)
- ✅ Created your own autodiff engine (like micrograd)
- ✅ Trained CNNs, RNNs, and Transformers in PyTorch
- ✅ Implemented GPT-style decoder from first principles
- ✅ Trained a "BabyGPT" language model on real text
- ✅ Deployed LLMs via API with quantization and RAG
- ✅ Designed production-scale LLM systems

### Progression Philosophy
Each project builds incrementally:
1. **Phase I** (01–15): Pure Python—no dependencies. Algorithmic thinking.
2. **Phase II** (16–30): NumPy only. Math intuition. Build ML from scratch.
3. **Phase III** (31–40): PyTorch introduced. Scale to real datasets (MNIST, CIFAR-10, IMDB).
4. **Phase IV** (41–50): Transformers & LLMs. Production systems. Deployment.

---

## Difficulty Legend

| Symbol | Level | Description |
|--------|-------|-------------|
| ⭐ | **Beginner** | Foundational concepts, minimal prerequisites, step-by-step guidance |
| ⭐⭐ | **Intermediate** | Requires prior projects or equivalent knowledge, some problem-solving |
| ⭐⭐⭐ | **Advanced** | Challenging, synthesizes multiple concepts, debugging skills needed |
| ⭐⭐⭐⭐ | **Expert** | Capstone-level, production-oriented, system design thinking required |

---

## How to Use This Curriculum

### For Learners
1. **Start at your level**: Beginners start at 01. ML-familiar can skip to 16. PyTorch users jump to 31.
2. **Follow sequentially**: Each project assumes knowledge from previous ones.
3. **Read-Code-Test-Build**: Read README → Study solution → Run tests → Build exercise from scratch.
4. **Time commitment**: ~2–6 hours per project (varies by difficulty).
5. **Get stuck?**: Check `solution_in_words.md` for narrative walkthrough.

### For Educators
- Use as semester-long curriculum (pick 15–20 projects)
- Assign projects as homework with auto-grading via pytest
- Mix lectures with hands-on project work
- Emphasize `Why` sections in READMEs for conceptual understanding

### For Interviewers/Job Seekers
- **Phase I** preps for coding interviews (FAANG-style)
- **Phase II–III** demonstrates ML engineering skills
- **Phase IV** shows cutting-edge LLM/transformer expertise
- Portfolio-ready: Each project is GitHub-showcase quality

---

## Repo Structure

```
python-edu/
├── project-01-basic-python-syntax/
│   ├── README.md                    # What, Why, When, Pitfalls, How
│   ├── exercise.py                   # TODOs + partial impl + hints
│   ├── solution/
│   │   └── solution.py               # Full impl + heavy comments
│   ├── test/
│   │   └── test_project_01.py        # pytest suite
│   ├── notebook.ipynb                # (optional for 01-15, required 16+)
│   └── solution_in_words.md          # Human-readable walkthrough
├── project-02-control-flow-loops/
│   └── ... (same structure)
├── ...
├── project-50-llm-system-design/
│   └── ...
├── README.md                          # Repo overview + quickstart
├── PROJECT_SUMMARY.md                 # This file
├── PYTHON_BASICS.md                   # Syntax reference
├── DSA_PRIMER.md                      # Algorithm patterns
├── MACHINE_LEARNING_MATH.md           # Lin alg, calculus, probability
├── AUTODIFF_FROM_SCRATCH.md           # Backprop deep dive
├── PYTORCH_INTERNALS.md               # How PyTorch works
├── TRANSFORMERS_EXPLAINED.md          # Attention mechanism guide
├── GPU_PRIMER.md                      # CUDA, parallelism, hardware
├── LLM_SYSTEMS_OVERVIEW.md            # Production LLM architecture
├── requirements-dev.txt               # Pinned dependencies
└── pytest.ini                         # Test configuration
```

---

## Testing Philosophy

Every project includes pytest-based tests:
- ✅ **Positive cases**: Happy path, expected behavior
- ✅ **Edge cases**: Empty inputs, boundary conditions, None handling
- ✅ **Property tests**: Randomized inputs, invariant checking (Hypothesis optional)
- ✅ **Performance tests**: Benchmarks for algorithm efficiency (where relevant)
- ✅ **Numerical stability**: Tolerance checks for ML code (np.allclose)

Run tests:
```bash
# Single project
cd project-01-basic-python-syntax
pytest test/

# All projects
pytest

# With coverage
pytest --cov=. --cov-report=html
```

---

## Dependencies

### Phase I (01–15): ZERO external dependencies
Pure Python standard library only.

### Phase II (16–30): NumPy + viz
```
numpy>=1.24.0
matplotlib>=3.7.0
scipy>=1.10.0  (optional, for advanced linalg)
```

### Phase III (31–40): PyTorch ecosystem
```
torch>=2.0.0
torchvision>=0.15.0
torchtext>=0.15.0
tqdm>=4.65.0
```

### Phase IV (41–50): LLM tools
```
torch>=2.0.0
einops>=0.6.1
sentencepiece>=0.1.99
transformers>=4.30.0  (for comparison, not from-scratch impl)
datasets>=2.12.0
faiss-cpu>=1.7.4
fastapi>=0.95.0
uvicorn>=0.22.0
```

### Dev/Testing
```
pytest>=7.3.0
pytest-cov>=4.1.0
hypothesis>=6.75.0  (property-based testing)
black>=23.3.0  (code formatting)
mypy>=1.3.0  (type checking)
```

---

## Contributing

We welcome contributions! See existing projects 01–02 for style examples.

**Style guide**:
- Heavy inline comments (explain *why*, not just *what*)
- Type hints everywhere (`def func(x: int) -> int:`)
- Docstrings with Args/Returns/Examples
- ASCII diagrams in READMEs
- Cross-language comparisons (Python vs Rust/C/JS)
- Performance notes (Big-O, memory, cache behavior)

---

## Credits & References

Inspired by:
- Andrej Karpathy's *Neural Networks: Zero to Hero*
- *Attention Is All You Need* (Vaswani et al., 2017)
- *Deep Learning* (Goodfellow, Bengio, Courville)
- *Structure and Interpretation of Computer Programs* (SICP pedagogy)
- FastAI, PyTorch tutorials, HuggingFace docs

---

## License

MIT License. Educational use encouraged. See LICENSE file.

---

## Questions?

- 📖 Start here: [README.md](./README.md)
- 🐍 Python refresher: [PYTHON_BASICS.md](./PYTHON_BASICS.md)
- 💡 First project: [project-01-basic-python-syntax/](./project-01-basic-python-syntax/)
- 🤝 Stuck? Open an issue or discussion

---

*"The best way to learn is to build."* — This curriculum is your 50-project gym.

Last updated: 2025-11-16
