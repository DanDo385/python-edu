# AI Learning Curriculum: Complete Project Index (85 Projects)

**From Python Basics to ChatGPT-Style Systems in 85 Progressive Projects**

> A comprehensive, production-grade learning path for mastering Python, algorithms, machine learning, PyTorch, transformers, LLMs, and AI system design—built from first principles.

---

## Table of Contents

- [Part 1: Python Fundamentals (Projects 1-10)](#part-1-python-fundamentals-projects-1-10)
- [Part 2: Math & Autodiff Fundamentals (Projects 11-17)](#part-2-math--autodiff-fundamentals-projects-11-17)
- [Part 3: Supervised ML Fundamentals (Projects 18-29)](#part-3-supervised-ml-fundamentals-projects-18-29)
- [Part 4: Unsupervised Learning (Projects 30-32)](#part-4-unsupervised-learning-projects-30-32)
- [Part 5: Sequence Models (Projects 33-36)](#part-5-sequence-models-projects-33-36)
- [Part 6: Word Embeddings & NLP (Projects 37-39)](#part-6-word-embeddings--nlp-projects-37-39)
- [Part 7: Advanced PyTorch (Projects 40-44)](#part-7-advanced-pytorch-projects-40-44)
- [Part 8: GPU Acceleration (Projects 45-51)](#part-8-gpu-acceleration-projects-45-51)
- [Part 9: Transformers & LLMs (Projects 52-57)](#part-9-transformers--llms-projects-52-57)
- [Part 10: Tokenization (Projects 58-61)](#part-10-tokenization-projects-58-61)
- [Part 11: Training Infrastructure (Projects 62-68)](#part-11-training-infrastructure-projects-62-68)
- [Part 12: Model Deployment (Projects 69-74)](#part-12-model-deployment-projects-69-74)
- [Part 13: RLHF & Alignment (Projects 75-78)](#part-13-rlhf--alignment-projects-75-78)
- [Part 14: Scaling Laws & Design (Projects 79-82)](#part-14-scaling-laws--design-projects-79-82)
- [Part 15: Advanced Applications (Projects 83-85)](#part-15-advanced-applications-projects-83-85)

---

## Part 1: Python Fundamentals (Projects 1-10)

**Goal**: Master Python syntax and core programming concepts

| # | Project | Description | Difficulty |
|---|---------|-------------|------------|
| 01 | [dynamic-typing-basics](Projects/01-dynamic-typing-basics/) | Variables, types, type(), print/input, dynamic typing | ⭐ Beginner |
| 02 | [control-flow-loops](Projects/02-control-flow-loops/) | if/else, for/while loops, break/continue, range() | ⭐ Beginner |
| 03 | [functions-scope](Projects/03-functions-scope/) | Function definition, parameters, return values, local/global scope | ⭐ Beginner |
| 04 | [data-structures-basics](Projects/04-data-structures-basics/) | Lists, tuples, dictionaries—operations and use cases | ⭐ Beginner |
| 05 | [strings-text-processing](Projects/05-strings-text-processing/) | String slicing, formatting, methods, text parsing | ⭐ Beginner |
| 06 | [object-oriented-basics](Projects/06-object-oriented-basics/) | Classes, objects, __init__, methods, attributes | ⭐⭐ Intermediate |
| 07 | [modules-packages](Projects/07-modules-packages/) | Importing modules, creating packages, using stdlib | ⭐⭐ Intermediate |
| 08 | [error-handling-exceptions](Projects/08-error-handling-exceptions/) | try/except/finally, raising exceptions, custom error types | ⭐⭐ Intermediate |
| 09 | [file-io-cli-basics](Projects/09-file-io-cli-basics/) | Reading/writing files, CSV, command-line arguments (argparse) | ⭐⭐ Intermediate |
| 10 | [automation-scripting-project](Projects/10-automation-scripting-project/) | Capstone: automate a task (file organizing, web scraping, etc.) | ⭐⭐ Intermediate |

---

## Part 2: Math & Autodiff Fundamentals (Projects 11-17)

**Goal**: Build mathematical foundations for machine learning

| # | Project | Description | Difficulty |
|---|---------|-------------|------------|
| 11 | [numerical-computing-numpy](Projects/11-numerical-computing-numpy/) | NumPy intro, arrays, vectorization, broadcasting | ⭐⭐ Intermediate |
| 12 | [manual-differentiation](Projects/12-manual-differentiation/) | Compute derivatives by hand and numerically | ⭐⭐ Intermediate |
| 13 | [backpropagation-from-scratch](Projects/13-backpropagation-from-scratch/) | Manual backprop on simple neural network, chain rule | ⭐⭐⭐ Advanced |
| 14 | [simple-autodiff-engine](Projects/14-simple-autodiff-engine/) | Build minimal autograd system (like micrograd) | ⭐⭐⭐ Advanced |
| 15 | [gradient-verification](Projects/15-gradient-verification/) | Verify gradients with numerical approximation | ⭐⭐ Intermediate |
| 16 | [visualizing-loss-landscapes](Projects/16-visualizing-loss-landscapes/) | Plot loss functions, visualize gradient descent paths | ⭐⭐ Intermediate |
| 17 | [exploratory-data-analysis](Projects/17-exploratory-data-analysis/) | pandas, matplotlib, summary statistics, correlations | ⭐⭐ Intermediate |

---

## Part 3: Supervised ML Fundamentals (Projects 18-29)

**Goal**: Implement ML models from scratch and master training

| # | Project | Description | Difficulty |
|---|---------|-------------|------------|
| 18 | [linear-regression-gradient-descent](Projects/18-linear-regression-gradient-descent/) | MSE loss, gradient descent, predict continuous targets | ⭐⭐ Intermediate |
| 19 | [data-preprocessing-train-test-split](Projects/19-data-preprocessing-train-test-split/) | Scaling, encoding, train/val/test splits, metrics | ⭐⭐ Intermediate |
| 20 | [logistic-regression-binary-classification](Projects/20-logistic-regression-binary-classification/) | Sigmoid, binary cross-entropy, decision boundaries | ⭐⭐ Intermediate |
| 21 | [multiclass-classification-softmax](Projects/21-multiclass-classification-softmax/) | Softmax function, multi-class cross-entropy | ⭐⭐ Intermediate |
| 22 | [vectorized-neural-network-numpy](Projects/22-vectorized-neural-network-numpy/) | MLP with NumPy, matrix operations, forward/backward | ⭐⭐⭐ Advanced |
| 23 | [training-mlp-pytorch](Projects/23-training-mlp-pytorch/) | PyTorch nn.Module, DataLoader, training loop | ⭐⭐ Intermediate |
| 24 | [overfitting-regularization](Projects/24-overfitting-regularization/) | L2 regularization, dropout, validation curves | ⭐⭐ Intermediate |
| 25 | [batch-normalization](Projects/25-batch-normalization/) | BatchNorm layers, training stability, convergence | ⭐⭐ Intermediate |
| 26 | [cnn-basics](Projects/26-cnn-basics/) | 2D convolution, pooling, feature maps | ⭐⭐ Intermediate |
| 27 | [cnn-image-classification-pytorch](Projects/27-cnn-image-classification-pytorch/) | Train CNN on CIFAR-10 or MNIST | ⭐⭐⭐ Advanced |
| 28 | [neural-network-visualization](Projects/28-neural-network-visualization/) | Visualize filters, feature maps, Grad-CAM | ⭐⭐⭐ Advanced |
| 29 | [transfer-learning-pretrained-models](Projects/29-transfer-learning-pretrained-models/) | Fine-tune ResNet, feature extraction | ⭐⭐⭐ Advanced |

---

## Part 4: Unsupervised Learning (Projects 30-32)

**Goal**: Learn pattern discovery without labels

| # | Project | Description | Difficulty |
|---|---------|-------------|------------|
| 30 | [kmeans-clustering](Projects/30-kmeans-clustering/) | K-Means algorithm from scratch, cluster assignment | ⭐⭐ Intermediate |
| 31 | [principal-component-analysis-pca](Projects/31-principal-component-analysis-pca/) | PCA for dimensionality reduction, eigenvectors | ⭐⭐ Intermediate |
| 32 | [autoencoder-dimensionality-reduction](Projects/32-autoencoder-dimensionality-reduction/) | Neural network encoder-decoder, latent representations | ⭐⭐⭐ Advanced |

---

## Part 5: Sequence Models (Projects 33-36)

**Goal**: Master recurrent networks and attention

| # | Project | Description | Difficulty |
|---|---------|-------------|------------|
| 33 | [rnn-sequence-classification](Projects/33-rnn-sequence-classification/) | Simple RNN from scratch, many-to-one task | ⭐⭐⭐ Advanced |
| 34 | [character-level-text-generation-rnn](Projects/34-character-level-text-generation-rnn/) | Vanilla RNN text generation, character-by-character | ⭐⭐⭐ Advanced |
| 35 | [lstm-improvement](Projects/35-lstm-improvement/) | LSTM architecture, gating mechanisms, long-term dependencies | ⭐⭐⭐ Advanced |
| 36 | [seq2seq-attention](Projects/36-seq2seq-attention/) | Encoder-decoder with attention (Bahdanau) | ⭐⭐⭐⭐ Expert |

---

## Part 6: Word Embeddings & NLP (Projects 37-39)

**Goal**: Learn semantic vector representations

| # | Project | Description | Difficulty |
|---|---------|-------------|------------|
| 37 | [word2vec-from-scratch](Projects/37-word2vec-from-scratch/) | Skip-gram model, negative sampling, train embeddings | ⭐⭐⭐ Advanced |
| 38 | [using-pretrained-word-embeddings](Projects/38-using-pretrained-word-embeddings/) | Load GloVe/Word2Vec, use in sentiment classifier | ⭐⭐ Intermediate |
| 39 | [evaluating-visualizing-embeddings](Projects/39-evaluating-visualizing-embeddings/) | Word similarity, analogies, t-SNE visualization | ⭐⭐ Intermediate |

---

## Part 7: Advanced PyTorch (Projects 40-44)

**Goal**: Extend PyTorch with custom components

| # | Project | Description | Difficulty |
|---|---------|-------------|------------|
| 40 | [custom-autograd-function](Projects/40-custom-autograd-function/) | Subclass torch.autograd.Function, define forward/backward | ⭐⭐⭐ Advanced |
| 41 | [building-custom-layers](Projects/41-building-custom-layers/) | Custom nn.Module layers, parameter registration | ⭐⭐⭐ Advanced |
| 42 | [writing-custom-optimizer](Projects/42-writing-custom-optimizer/) | Implement Adam or RMSprop from scratch | ⭐⭐⭐ Advanced |
| 43 | [data-pipeline-dataloader](Projects/43-data-pipeline-dataloader/) | Custom Dataset, efficient DataLoader, augmentation | ⭐⭐ Intermediate |
| 44 | [training-loop-checkpointing](Projects/44-training-loop-checkpointing/) | Flexible training loop, save/load checkpoints, early stopping | ⭐⭐ Intermediate |

---

## Part 8: GPU Acceleration (Projects 45-51)

**Goal**: Optimize performance with GPU programming

| # | Project | Description | Difficulty |
|---|---------|-------------|------------|
| 45 | [gpu-basics-speedup](Projects/45-gpu-basics-speedup/) | CUDA basics, CPU vs GPU benchmarks, .to(device) | ⭐⭐ Intermediate |
| 46 | [vectorization-vs-loops](Projects/46-vectorization-vs-loops/) | NumPy vectorization performance, loop optimization | ⭐⭐ Intermediate |
| 47 | [jit-compilation-numba](Projects/47-jit-compilation-numba/) | Numba @njit decorator, JIT speedups | ⭐⭐⭐ Advanced |
| 48 | [gpu-programming-cuda](Projects/48-gpu-programming-cuda/) | CuPy or PyCUDA, write CUDA kernels | ⭐⭐⭐⭐ Expert |
| 49 | [custom-gpu-kernels-triton](Projects/49-custom-gpu-kernels-triton/) | OpenAI Triton, write high-performance kernels | ⭐⭐⭐⭐ Expert |
| 50 | [profiling-optimization](Projects/50-profiling-optimization/) | PyTorch Profiler, find bottlenecks, optimize | ⭐⭐⭐ Advanced |
| 51 | [multi-gpu-distributed-training](Projects/51-multi-gpu-distributed-training/) | DataParallel, DistributedDataParallel, multi-GPU training | ⭐⭐⭐⭐ Expert |

---

## Part 9: Transformers & LLMs (Projects 52-57)

**Goal**: Build transformer architectures from scratch

| # | Project | Description | Difficulty |
|---|---------|-------------|------------|
| 52 | [implementing-attention-mechanism](Projects/52-implementing-attention-mechanism/) | Scaled dot-product attention: softmax(QK^T/√d)V | ⭐⭐⭐ Advanced |
| 53 | [building-transformer-block](Projects/53-building-transformer-block/) | Multi-head attention, FFN, LayerNorm, residuals | ⭐⭐⭐ Advanced |
| 54 | [gpt-style-language-model](Projects/54-gpt-style-language-model/) | Decoder-only transformer, causal masking, next-token prediction | ⭐⭐⭐⭐ Expert |
| 55 | [training-transformer-from-scratch](Projects/55-training-transformer-from-scratch/) | Train mini-GPT on text corpus, perplexity, generation | ⭐⭐⭐⭐ Expert |
| 56 | [using-pretrained-transformer](Projects/56-using-pretrained-transformer/) | Load GPT-2/BERT from Hugging Face, fine-tune | ⭐⭐⭐ Advanced |
| 57 | [bert-style-masked-lm](Projects/57-bert-style-masked-lm/) | Masked language modeling, bidirectional encoder | ⭐⭐⭐⭐ Expert |

---

## Part 10: Tokenization (Projects 58-61)

**Goal**: Master text preprocessing for LLMs

| # | Project | Description | Difficulty |
|---|---------|-------------|------------|
| 58 | [tokenization-basics](Projects/58-tokenization-basics/) | Word-level, character-level, whitespace tokenization | ⭐ Beginner |
| 59 | [byte-pair-encoding-from-scratch](Projects/59-byte-pair-encoding-from-scratch/) | Implement BPE algorithm, build subword vocabulary | ⭐⭐⭐ Advanced |
| 60 | [training-sentencepiece-tokenizer](Projects/60-training-sentencepiece-tokenizer/) | Use SentencePiece library, train tokenizer on corpus | ⭐⭐ Intermediate |
| 61 | [integrating-tokenizer-with-transformer](Projects/61-integrating-tokenizer-with-transformer/) | Connect tokenizer to LLM, encode/decode pipelines | ⭐⭐ Intermediate |

---

## Part 11: Training Infrastructure (Projects 62-68)

**Goal**: Advanced training techniques and model compression

| # | Project | Description | Difficulty |
|---|---------|-------------|------------|
| 62 | [gradient-checkpointing](Projects/62-gradient-checkpointing/) | Trade compute for memory, train deeper models | ⭐⭐⭐ Advanced |
| 63 | [mixed-precision-training](Projects/63-mixed-precision-training/) | FP16/bfloat16 training, autocast, GradScaler | ⭐⭐⭐ Advanced |
| 64 | [model-quantization-inference](Projects/64-model-quantization-inference/) | INT8 quantization, reduce model size | ⭐⭐⭐ Advanced |
| 65 | [gradient-accumulation](Projects/65-gradient-accumulation/) | Simulate large batch sizes with small GPU memory | ⭐⭐ Intermediate |
| 66 | [distributed-training-multi-node](Projects/66-distributed-training-multi-node/) | Multi-node training, process groups, DDP | ⭐⭐⭐⭐ Expert |
| 67 | [model-pruning-sparsity](Projects/67-model-pruning-sparsity/) | Prune weights, create sparse models | ⭐⭐⭐ Advanced |
| 68 | [knowledge-distillation](Projects/68-knowledge-distillation/) | Train small model from large teacher model | ⭐⭐⭐ Advanced |

---

## Part 12: Model Deployment (Projects 69-74)

**Goal**: Deploy models to production

| # | Project | Description | Difficulty |
|---|---------|-------------|------------|
| 69 | [fastapi-model-serving](Projects/69-fastapi-model-serving/) | Create REST API for model inference | ⭐⭐ Intermediate |
| 70 | [batch-inference-request-batching](Projects/70-batch-inference-request-batching/) | Batch requests for higher throughput | ⭐⭐⭐ Advanced |
| 71 | [streaming-responses-llms](Projects/71-streaming-responses-llms/) | Stream tokens in real-time (like ChatGPT) | ⭐⭐⭐ Advanced |
| 72 | [model-optimization-inference](Projects/72-model-optimization-inference/) | TorchScript, ONNX export, inference optimization | ⭐⭐⭐ Advanced |
| 73 | [dockerizing-deploying-service](Projects/73-dockerizing-deploying-service/) | Containerize API, deploy with Docker | ⭐⭐ Intermediate |
| 74 | [scalable-deployment-monitoring](Projects/74-scalable-deployment-monitoring/) | Load balancing, autoscaling, monitoring | ⭐⭐⭐⭐ Expert |

---

## Part 13: RLHF & Alignment (Projects 75-78)

**Goal**: Train ChatGPT-style aligned models

| # | Project | Description | Difficulty |
|---|---------|-------------|------------|
| 75 | [supervised-fine-tuning-instructions](Projects/75-supervised-fine-tuning-instructions/) | SFT phase of RLHF, instruction-following data | ⭐⭐⭐ Advanced |
| 76 | [reward-model-training](Projects/76-reward-model-training/) | Train model to predict human preferences | ⭐⭐⭐⭐ Expert |
| 77 | [ppo-fine-tuning](Projects/77-ppo-fine-tuning/) | Proximal Policy Optimization for RLHF | ⭐⭐⭐⭐ Expert |
| 78 | [evaluating-alignment-safety](Projects/78-evaluating-alignment-safety/) | Test model safety, add moderation filters | ⭐⭐⭐ Advanced |

---

## Part 14: Scaling Laws & Design (Projects 79-82)

**Goal**: Understand and design large-scale AI systems

| # | Project | Description | Difficulty |
|---|---------|-------------|------------|
| 79 | [scaling-law-experiment](Projects/79-scaling-law-experiment/) | Observe loss vs model/data size, power laws | ⭐⭐⭐ Advanced |
| 80 | [model-compute-scaling-strategy](Projects/80-model-compute-scaling-strategy/) | Compute-optimal training (Chinchilla approach) | ⭐⭐⭐⭐ Expert |
| 81 | [designing-gpt3-scale-training-system](Projects/81-designing-gpt3-scale-training-system/) | System design for training 100B+ parameter models | ⭐⭐⭐⭐ Expert |
| 82 | [designing-deployed-chatgpt-system](Projects/82-designing-deployed-chatgpt-system/) | Full-stack ChatGPT architecture (inference, caching, feedback) | ⭐⭐⭐⭐ Expert |

---

## Part 15: Advanced Applications (Projects 83-85)

**Goal**: Build cutting-edge AI applications

| # | Project | Description | Difficulty |
|---|---------|-------------|------------|
| 83 | [retrieval-augmented-generation-rag](Projects/83-retrieval-augmented-generation-rag/) | Vector DB (FAISS), embeddings, Q&A with retrieval | ⭐⭐⭐⭐ Expert |
| 84 | [parameter-efficient-fine-tuning-lora](Projects/84-parameter-efficient-fine-tuning-lora/) | LoRA adapters, efficient model updates | ⭐⭐⭐ Advanced |
| 85 | [chatgpt-chatbot-capstone](Projects/85-chatgpt-chatbot-capstone/) | **CAPSTONE**: Build complete ChatGPT-style chatbot | ⭐⭐⭐⭐ Expert |

---

## Curriculum Stats

- **Total Projects**: 85
- **Estimated Time**: 9-15 months (self-paced, 8-15 hrs/week)
- **Prerequisites**: Basic computer literacy
- **Languages**: Python 3.10+
- **Frameworks**: NumPy, PyTorch, Transformers, FastAPI

## What You'll Build

By Project 85, you will have:

✅ **Implemented from scratch**:
- Python fundamentals and automation tools
- Core algorithms (sorting, search, graphs, DP)
- Neural networks and backpropagation
- Autodiff engine (like micrograd)
- Transformer architecture (attention, multi-head, positional encoding)
- GPT-style decoder models
- Tokenizers (BPE, SentencePiece)

✅ **Trained real models**:
- MNIST digit classifier (NumPy and PyTorch)
- CIFAR-10 CNNs
- RNN/LSTM text generators
- Transformer language models
- RLHF-aligned chat models

✅ **Deployed systems**:
- REST APIs for LLM inference
- Streaming token generation
- RAG question-answering systems
- Dockerized production services
- Full ChatGPT-style chatbot

✅ **Mastered concepts**:
- Python internals and best practices
- Linear algebra, calculus, and optimization
- GPU programming (CUDA, Triton, Metal)
- Transformer architectures
- LLM training, fine-tuning, and alignment
- Production ML systems
- Scaling laws and system design

## Difficulty Legend

| Symbol | Level | Description |
|--------|-------|-------------|
| ⭐ | **Beginner** | Foundational concepts, step-by-step guidance |
| ⭐⭐ | **Intermediate** | Requires prior projects, some problem-solving |
| ⭐⭐⭐ | **Advanced** | Challenging, synthesizes multiple concepts |
| ⭐⭐⭐⭐ | **Expert** | Capstone-level, production-oriented, system design |

## How to Use This Curriculum

### For Learners
1. **Start at your level**: Beginners → Project 01; ML-familiar → Project 11; PyTorch users → Project 40
2. **Follow sequentially**: Each project builds on previous knowledge
3. **Read → Code → Test → Build**: Study README, run solution, pass tests, implement yourself
4. **Time per project**: 2-10 hours (varies by difficulty)

### For Educators
- Semester-long curriculum (select 15-25 projects)
- Auto-grading via pytest
- Mix lectures with hands-on projects
- Emphasize conceptual understanding

### For Job Seekers
- **Part 1**: Coding interview prep
- **Parts 2-8**: ML engineering skills
- **Parts 9-15**: LLM/AI system expertise
- Portfolio-ready projects

## Testing

Run tests for any project:

```bash
# Single project
cd Projects/01-dynamic-typing-basics
pytest tests/ -v

# All projects
pytest Projects/ -v

# With coverage
pytest Projects/ --cov=. --cov-report=html
```

## Dependencies by Part

**Part 1 (1-10)**: Python standard library only
**Part 2 (11-17)**: NumPy, matplotlib, pandas
**Part 3-7 (18-44)**: PyTorch, torchvision, scikit-learn
**Part 8 (45-51)**: CUDA toolkit, Numba, Triton
**Part 9-15 (52-85)**: Transformers, datasets, FastAPI, FAISS

See [requirements-dev.txt](requirements-dev.txt) for full dependency list.

## License

MIT License. Educational use encouraged.

---

**Start your journey from Python basics to building ChatGPT-style systems!** 🚀

*Last updated: 2025-11-16*
