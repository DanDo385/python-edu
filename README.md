# Python Learning Hub: DSA + AI Curriculum

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**A comprehensive learning platform featuring two complete curricula: Data Structures & Algorithms and AI/Machine Learning**

---

## 🎓 Two Complete Learning Paths

### 📊 [Data Structures & Algorithms (DSA)](dsa/)
**50 Projects | 3-4 Months | Interview Preparation**

Master computer science fundamentals through hands-on implementation:
- Arrays, Linked Lists, Trees, Graphs
- Sorting & Searching Algorithms
- Dynamic Programming & Backtracking
- Interview-ready problem-solving

[**Start DSA Curriculum →**](dsa/README.md)

### 🤖 [AI & Machine Learning](ai/)
**85 Projects | 9-15 Months | Build ChatGPT-Style Systems**

Journey from Python basics to deploying production LLMs:
- Neural Networks from Scratch
- PyTorch & Deep Learning
- Transformers & LLMs
- RLHF, RAG, and Production Deployment

[**Start AI Curriculum →**](ai/README.md)

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/DanDo385/python-edu.git
cd python-edu

# Choose your path:

# Option 1: Data Structures & Algorithms
cd dsa
cat README.md  # Read the guide
cd projects/01-python-basics-review

# Option 2: AI & Machine Learning
cd ai
cat README.md  # Read the guide
cd Projects/01-dynamic-typing-basics

# Set up environment (see SETUP.md for details)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements-dev.txt  # For AI curriculum
```

---

## 📚 Curriculum Comparison

| Feature | DSA Curriculum | AI Curriculum |
|---------|----------------|---------------|
| **Projects** | 50 | 85 |
| **Duration** | 3-4 months | 9-15 months |
| **Prerequisites** | Basic Python | Basic programming |
| **Focus** | Algorithms & Interviews | ML & AI Systems |
| **Dependencies** | Pure Python | NumPy, PyTorch, Transformers |
| **Best For** | Job interviews, CS fundamentals | ML engineering, AI development |

---

## 🎯 Learning Paths

### Path 1: Interview Preparation (2-3 months)
**Focus**: DSA curriculum
- Master all 50 DSA projects
- Practice daily on LeetCode/HackerRank
- Goal: Pass technical interviews at FAANG companies

### Path 2: Full-Stack AI Engineer (12-18 months)
**Combined**: Both curricula
1. **Months 1-3**: DSA projects 1-30 (core algorithms)
2. **Months 4-12**: AI projects 1-60 (ML fundamentals to transformers)
3. **Months 13-18**: AI projects 61-85 (production LLM systems)
- Goal: Build and deploy production AI systems

### Path 3: ML Specialist (9-12 months)
**Focus**: AI curriculum (skip DSA or minimal coverage)
- Start AI from project 1 or 11 (depending on Python level)
- Deep dive into neural networks, transformers, and LLMs
- Goal: Research or ML engineering roles

### Path 4: Rapid Interview Prep (6-8 weeks)
**Focus**: Key DSA projects
- Projects: 3-5, 9-10, 13-15, 18-20, 22-25, 27-30, 35-40, 41-47
- 15-25 hours/week
- Goal: Quick interview preparation

---

## 📖 Documentation

### General Setup
- **[SETUP.md](SETUP.md)** - Environment setup for all platforms
- **[GPU_GUIDE.md](GPU_GUIDE.md)** - GPU setup (NVIDIA CUDA & Apple Metal)
- **[DOCKER.md](DOCKER.md)** - Docker containerization guide

### Curriculum-Specific
- **[DSA README](dsa/README.md)** - DSA curriculum overview
- **[DSA Projects](dsa/PROJECT_SUMMARY.md)** - All 50 DSA projects
- **[AI README](ai/README.md)** - AI curriculum overview
- **[AI Projects](ai/PROJECT_SUMMARY.md)** - All 85 AI projects

---

## 🛠️ Tech Stack

### DSA Curriculum
- **Python 3.10+** (pure Python, no dependencies)
- Standard library only
- Focus on algorithm implementation

### AI Curriculum
- **Python 3.10+**
- **NumPy** - Numerical computing
- **PyTorch** - Deep learning framework
- **Transformers** - LLM library (Hugging Face)
- **FastAPI** - Model serving
- **Docker** - Containerization

See [requirements-dev.txt](requirements-dev.txt) for complete dependency list.

---

## 🧪 Testing

Both curricula include comprehensive test suites:

```bash
# DSA tests (no setup required)
cd dsa
pytest projects/ -v

# AI tests (requires dependencies)
cd ai
pip install -r ../requirements-dev.txt
pytest Projects/ -v

# Run specific project
pytest Projects/01-dynamic-typing-basics/tests/ -v
```

---

## 🐳 Docker Support

Run everything in a consistent, reproducible environment:

```bash
# Build and start
docker-compose up -d

# Access Jupyter (for AI projects)
# Navigate to http://localhost:8888

# Run tests
docker-compose exec python-edu pytest dsa/projects/ -v
docker-compose exec python-edu pytest ai/Projects/ -v

# Stop
docker-compose down
```

See [DOCKER.md](DOCKER.md) for details.

---

## 💻 Hardware Support

**DSA Curriculum:**
- Runs on any system (pure Python)
- No GPU needed

**AI Curriculum:**
- **CPU**: All projects work (slower for large models)
- **NVIDIA GPU**: Full CUDA support (recommended for projects 45+)
- **Apple Silicon**: Metal Performance Shaders (MPS) support

GPU detection scripts:
```bash
python detect_nvidia_gpu.py
python detect_apple_metal_gpu.py
python detect_accelerated_backend.py
```

---

## 🎯 What You'll Build

### DSA Curriculum
✅ 10+ sorting/searching algorithms  
✅ All major data structures  
✅ 40+ algorithm patterns  
✅ 200+ solved problems  
✅ Interview-ready skills  

### AI Curriculum
✅ Neural networks from scratch  
✅ Transformer architecture  
✅ GPT-style language models  
✅ Production ML systems  
✅ RAG & ChatGPT-style chatbot  

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

**DSA Curriculum inspired by:**
- *Introduction to Algorithms* (CLRS)
- *Cracking the Coding Interview*
- LeetCode & HackerRank

**AI Curriculum inspired by:**
- *Attention Is All You Need* (Vaswani et al.)
- Andrej Karpathy's educational content
- Stanford CS231n & CS224n
- Fast.ai courses

---

## 📧 Contact

Questions or feedback? Open an issue on GitHub.

---

**Choose your path and start learning today!** 🚀

| I want to... | Start here |
|-------------|------------|
| Prepare for coding interviews | [DSA Curriculum](dsa/) |
| Learn ML and AI | [AI Curriculum](ai/) |
| Become a full-stack AI engineer | Both (DSA first) |
| Build ChatGPT-like systems | [AI Curriculum](ai/) |

*Last updated: 2025-11-16*
