# AI Learning Curriculum: Python to LLMs (85 Projects)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-ee4c2c.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Projects](https://img.shields.io/badge/projects-85-brightgreen.svg)](PROJECT_SUMMARY.md)

A comprehensive, project-based learning path from Python fundamentals to large language model (LLM) system design. This curriculum features **85 hands-on projects** that progressively build your skills from basic programming to cutting-edge AI applications.

## 🎯 Overview

This repository provides a complete learning journey integrating:
- **Python Fundamentals** (Projects 1-10): Core language features and scripting
- **Mathematical Foundations** (Projects 11-17): NumPy, calculus, and autodiff
- **Supervised Machine Learning** (Projects 18-29): From linear regression to CNNs
- **Unsupervised Learning** (Projects 30-32): Clustering, PCA, and autoencoders
- **Sequence Models** (Projects 33-36): RNNs, LSTMs, and attention mechanisms
- **NLP & Embeddings** (Projects 37-39): Word2Vec and semantic representations
- **Advanced PyTorch** (Projects 40-44): Custom layers, optimizers, and data pipelines
- **GPU Acceleration** (Projects 45-51): CUDA, Triton, and performance optimization
- **Transformers & LLMs** (Projects 52-57): Building GPT-style models from scratch
- **Tokenization** (Projects 58-61): BPE, SentencePiece, and text processing
- **Training Infrastructure** (Projects 62-68): Distributed training, quantization, distillation
- **Model Deployment** (Projects 69-74): FastAPI, Docker, and production systems
- **RLHF & Alignment** (Projects 75-78): Training ChatGPT-style models
- **Scaling & System Design** (Projects 79-82): Large-scale architecture planning
- **Advanced Applications** (Projects 83-85): RAG, LoRA, and chatbot capstone

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- (Optional) NVIDIA GPU with CUDA support or Apple Silicon (M1/M2/M3/M4) for GPU acceleration
- 8GB+ RAM recommended (16GB+ for larger models)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/DanDo385/python-edu.git
cd python-edu
```

2. **Set up your environment:**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt
```

3. **Verify your setup:**
```bash
# Check Python version
python --version

# Test PyTorch installation
python -c "import torch; print(f'PyTorch {torch.__version__}')"

# Detect GPU (NVIDIA)
python detect_nvidia_gpu.py

# Detect GPU (Apple Metal)
python detect_apple_metal_gpu.py

# Auto-detect best backend
python detect_accelerated_backend.py
```

4. **Start with Project 01:**
```bash
cd Projects/01-dynamic-typing-basics
pytest tests/
```

## 📚 Documentation

- **[SETUP.md](SETUP.md)**: Detailed environment setup for all platforms
- **[GPU_GUIDE.md](GPU_GUIDE.md)**: GPU acceleration guide (NVIDIA CUDA & Apple Metal)
- **[DOCKER.md](DOCKER.md)**: Containerized environment setup
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)**: Complete index of all 85 projects

## 🗂️ Repository Structure

```
python-edu/
├── Projects/                      # All 85 projects
│   ├── 01-dynamic-typing-basics/
│   │   ├── README.md             # Project objectives and tasks
│   │   ├── solution_in_words.md  # Conceptual explanation
│   │   ├── solution/             # Python solutions (.py + .ipynb)
│   │   └── tests/                # Pytest test suite
│   ├── 02-control-flow-loops/
│   ├── ...
│   └── 85-chatgpt-chatbot-capstone/
├── README.md                      # This file
├── PROJECT_SUMMARY.md             # Index of all projects
├── SETUP.md                       # Environment setup guide
├── GPU_GUIDE.md                   # GPU configuration details
├── DOCKER.md                      # Docker usage guide
├── Dockerfile                     # Container definition
├── docker-compose.yml             # Multi-service orchestration
├── detect_nvidia_gpu.py           # NVIDIA GPU detection
├── detect_apple_metal_gpu.py      # Apple Metal detection
├── detect_accelerated_backend.py  # Auto backend selection
├── requirements-dev.txt           # All dependencies
└── pytest.ini                     # Test configuration
```

## 🎓 Learning Path

### Part 1: Python Fundamentals (Projects 1-10)
Master Python basics: variables, control flow, functions, data structures, OOP, modules, error handling, file I/O, and automation scripting.

### Part 2: Math & Autodiff (Projects 11-17)
Build mathematical foundations for machine learning with NumPy, manual differentiation, backpropagation, autodiff engines, and gradient verification.

### Part 3: Supervised ML (Projects 18-29)
Implement ML algorithms from scratch: linear/logistic regression, neural networks, CNNs, and transfer learning. Master training, regularization, and model evaluation.

### Part 4: Unsupervised Learning (Projects 30-32)
Explore clustering (K-Means), dimensionality reduction (PCA), and neural compression (autoencoders).

### Part 5: Sequence Models (Projects 33-36)
Master RNNs, LSTMs, and attention mechanisms for sequential data and text generation.

### Part 6: Word Embeddings (Projects 37-39)
Learn representation learning with Word2Vec, pretrained embeddings, and semantic vector spaces.

### Part 7: Advanced PyTorch (Projects 40-44)
Build custom autograd functions, layers, optimizers, datasets, and training loops.

### Part 8: GPU Acceleration (Projects 45-51)
Optimize performance with CUDA, vectorization, Numba JIT, Triton kernels, profiling, and distributed training.

### Part 9: Transformers & LLMs (Projects 52-57)
Build transformer architectures from scratch: attention mechanisms, transformer blocks, GPT-style models, and BERT-style masked LM.

### Part 10: Tokenization (Projects 58-61)
Master text preprocessing with byte-pair encoding (BPE), SentencePiece, and integration with transformer models.

### Part 11: Training Infrastructure (Projects 62-68)
Learn advanced techniques: gradient checkpointing, mixed precision, quantization, pruning, knowledge distillation, and gradient accumulation.

### Part 12: Model Deployment (Projects 69-74)
Deploy models with FastAPI, batch inference, streaming responses, TorchScript/ONNX optimization, Docker, and scalable architectures.

### Part 13: RLHF & Alignment (Projects 75-78)
Train ChatGPT-style models with supervised fine-tuning, reward modeling, PPO, and safety evaluation.

### Part 14: Scaling & Design (Projects 79-82)
Understand scaling laws, compute-optimal training, and design systems for GPT-3/ChatGPT scale deployments.

### Part 15: Advanced Applications (Projects 83-85)
Build retrieval-augmented generation (RAG), parameter-efficient fine-tuning (LoRA), and a complete ChatGPT-style chatbot capstone.

## 🧪 Testing

Each project includes comprehensive pytest tests:

```bash
# Run tests for a specific project
cd Projects/01-dynamic-typing-basics
pytest tests/ -v

# Run all tests in the curriculum
pytest Projects/ -v

# Run with coverage
pytest Projects/ --cov=. --cov-report=html
```

## 🐳 Docker Usage

For a consistent, reproducible environment:

```bash
# Build and start container
docker-compose up -d

# Access Jupyter notebook
# Navigate to http://localhost:8888

# Run tests in container
docker-compose exec python-edu pytest Projects/

# Stop container
docker-compose down
```

See [DOCKER.md](DOCKER.md) for detailed instructions.

## 💻 Hardware Support

This curriculum supports multiple hardware configurations:

- **NVIDIA GPUs**: Full CUDA support with cuDNN acceleration
- **Apple Silicon (M1/M2/M3/M4)**: Metal Performance Shaders (MPS) backend
- **CPU-only**: All projects run on CPU (may be slower for larger models)

GPU detection scripts automatically select the best available backend. See [GPU_GUIDE.md](GPU_GUIDE.md) for setup instructions.

## 📖 Learning Paths

### 🎓 Complete Beginner (9-15 months)
Start at Project 01, work sequentially through all 85 projects.
- **Time**: 8-12 hours/week × 36-60 weeks

### 💼 Experienced Programmer (5-9 months)
Skim Part 1 (Projects 1-10), deep dive Parts 2-15.
- **Time**: 12-18 hours/week × 20-36 weeks

### 🤖 ML Engineer (3-6 months)
Skip to Project 11 (NumPy). If comfortable with PyTorch, start at Project 40.
Focus heavily on Parts 9-15 (Transformers, LLMs, deployment).
- **Time**: 15-25 hours/week × 12-24 weeks

### 🚀 Focus Tracks

**LLM Specialist**: Projects 1-3, 11-17, 40-85
**ML Infrastructure**: Projects 11-29, 40-44, 45-51, 62-74
**Python + Algorithms**: Projects 1-10, then explore data structures topics

## 🎯 By Project 85, You Will Have

✅ **Implemented from scratch**:
- Python fundamentals and automation tools
- Neural network training (backprop, autodiff, optimization)
- Transformer architecture (attention, multi-head, positional encoding)
- GPT-style decoder models
- Text tokenizers (BPE, SentencePiece)
- Training infrastructure (distributed, mixed-precision, quantization)

✅ **Trained real models**:
- MNIST digit classifier (NumPy and PyTorch)
- CIFAR-10 CNN with transfer learning
- RNN/LSTM text generators
- Transformer language models
- RLHF-aligned chat models

✅ **Deployed systems**:
- REST API for LLM inference (FastAPI)
- Streaming token generation
- RAG question-answering system
- Dockerized production services
- ChatGPT-style web chatbot

✅ **Mastered concepts**:
- Python internals and best practices
- Linear algebra, calculus, and optimization for ML
- GPU programming (CUDA, Triton, MPS)
- Transformer architectures and attention
- LLM training, fine-tuning, and alignment
- Production ML systems and scalability
- Scaling laws and system design

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes with tests
4. Submit a pull request

## 📖 Additional Resources

- [PyTorch Documentation](https://pytorch.org/docs/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
- [NumPy User Guide](https://numpy.org/doc/stable/user/)
- [OpenAI Research](https://openai.com/research/)
- [Attention Is All You Need (Vaswani et al., 2017)](https://arxiv.org/abs/1706.03762)
- [Training language models to follow instructions with human feedback (Ouyang et al., 2022)](https://arxiv.org/abs/2203.02155)

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

This curriculum draws inspiration from:
- The "Attention Is All You Need" paper (Vaswani et al., 2017)
- OpenAI's GPT and ChatGPT research
- Andrej Karpathy's educational content (micrograd, nanoGPT)
- Stanford CS231n and CS224n courses
- Fast.ai courses
- PyTorch and Hugging Face communities

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Start your journey from Python basics to building ChatGPT-style systems today!** 🚀

*"Understanding beats memorization. Building beats watching tutorials."*

Last updated: 2025-11-16
