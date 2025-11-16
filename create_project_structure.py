#!/usr/bin/env python3
"""
Script to create the 85-project directory structure for the AI Learning Curriculum.
"""

import os
from pathlib import Path

# Define all 85 projects with their details
PROJECTS = [
    # Part 1: Python Fundamentals (1-10)
    (1, "dynamic-typing-basics", "Dynamic Typing Basics"),
    (2, "control-flow-loops", "Control Flow and Loops"),
    (3, "functions-scope", "Functions and Scope"),
    (4, "data-structures-basics", "Data Structures (Lists, Tuples, Dictionaries)"),
    (5, "strings-text-processing", "Strings and Text Processing"),
    (6, "object-oriented-basics", "Object-Oriented Basics"),
    (7, "modules-packages", "Modules and Packages"),
    (8, "error-handling-exceptions", "Error Handling with Exceptions"),
    (9, "file-io-cli-basics", "File I/O and CLI Basics"),
    (10, "automation-scripting-project", "Automation Scripting Project"),

    # Part 2: Math and Autodiff Fundamentals (11-17)
    (11, "numerical-computing-numpy", "Numerical Computing with Python (NumPy Intro)"),
    (12, "manual-differentiation", "Manual Differentiation and Gradients"),
    (13, "backpropagation-from-scratch", "Implementing Backpropagation"),
    (14, "simple-autodiff-engine", "Simple Autodiff Engine"),
    (15, "gradient-verification", "Gradient Verification"),
    (16, "visualizing-loss-landscapes", "Visualizing Loss Landscapes"),
    (17, "exploratory-data-analysis", "Exploratory Data Analysis (EDA)"),

    # Part 3: Supervised ML Fundamentals (18-29)
    (18, "linear-regression-gradient-descent", "Linear Regression (Gradient Descent)"),
    (19, "data-preprocessing-train-test-split", "Data Preprocessing and Train/Test Split"),
    (20, "logistic-regression-binary-classification", "Logistic Regression (Binary Classification)"),
    (21, "multiclass-classification-softmax", "Multiclass Classification with Softmax"),
    (22, "vectorized-neural-network-numpy", "Vectorized Neural Network from Scratch"),
    (23, "training-mlp-pytorch", "Training an MLP with PyTorch"),
    (24, "overfitting-regularization", "Overfitting and Regularization"),
    (25, "batch-normalization", "Batch Normalization"),
    (26, "cnn-basics", "Convolutional Neural Network Basics"),
    (27, "cnn-image-classification-pytorch", "CNN Image Classification with PyTorch"),
    (28, "neural-network-visualization", "Neural Network Visualization"),
    (29, "transfer-learning-pretrained-models", "Transfer Learning with Pretrained Models"),

    # Part 4: Unsupervised Learning (30-32)
    (30, "kmeans-clustering", "K-Means Clustering"),
    (31, "principal-component-analysis-pca", "Principal Component Analysis (PCA)"),
    (32, "autoencoder-dimensionality-reduction", "Autoencoder for Dimensionality Reduction"),

    # Part 5: Sequence Models (33-36)
    (33, "rnn-sequence-classification", "RNN for Sequence Classification"),
    (34, "character-level-text-generation-rnn", "Character-Level Text Generation (Vanilla RNN)"),
    (35, "lstm-improvement", "Long Short-Term Memory (LSTM) Improvement"),
    (36, "seq2seq-attention", "Sequence-to-Sequence and Attention"),

    # Part 6: Word Embeddings and NLP Representation (37-39)
    (37, "word2vec-from-scratch", "Word2Vec from Scratch (Skip-Gram Model)"),
    (38, "using-pretrained-word-embeddings", "Using Pretrained Word Embeddings"),
    (39, "evaluating-visualizing-embeddings", "Evaluating and Visualizing Embeddings"),

    # Part 7: Deep Learning with PyTorch (40-44)
    (40, "custom-autograd-function", "Custom Autograd Function"),
    (41, "building-custom-layers", "Building Custom Layers (nn.Module)"),
    (42, "writing-custom-optimizer", "Writing a Custom Optimizer"),
    (43, "data-pipeline-dataloader", "Data Pipeline and DataLoader"),
    (44, "training-loop-checkpointing", "Training Loop and Checkpointing"),

    # Part 8: GPU Acceleration and Performance (45-51)
    (45, "gpu-basics-speedup", "GPU Basics and Speedup"),
    (46, "vectorization-vs-loops", "Vectorization vs. Loops (Performance on CPU)"),
    (47, "jit-compilation-numba", "JIT Compilation with Numba"),
    (48, "gpu-programming-cuda", "GPU Programming with CUDA (PyCUDA/CuPy)"),
    (49, "custom-gpu-kernels-triton", "Custom GPU Kernels with Triton"),
    (50, "profiling-optimization", "Profiling and Optimization"),
    (51, "multi-gpu-distributed-training", "Multi-GPU and Distributed Training Basics"),

    # Part 9: Transformers and Large Language Models (52-57)
    (52, "implementing-attention-mechanism", "Implementing the Attention Mechanism"),
    (53, "building-transformer-block", "Building a Transformer Block"),
    (54, "gpt-style-language-model", "GPT-Style Language Model"),
    (55, "training-transformer-from-scratch", "Training a Transformer from Scratch"),
    (56, "using-pretrained-transformer", "Using a Pretrained Transformer (GPT/BERT)"),
    (57, "bert-style-masked-lm", "BERT-Style Masked Language Modeling"),

    # Part 10: Tokenization and Text Processing (58-61)
    (58, "tokenization-basics", "Tokenization Basics"),
    (59, "byte-pair-encoding-from-scratch", "Byte-Pair Encoding (BPE) from Scratch"),
    (60, "training-sentencepiece-tokenizer", "Training a SentencePiece Tokenizer"),
    (61, "integrating-tokenizer-with-transformer", "Integrating Tokenizer with the Transformer Model"),

    # Part 11: Training Techniques and Infrastructure (62-68)
    (62, "gradient-checkpointing", "Gradient Checkpointing"),
    (63, "mixed-precision-training", "Mixed Precision Training"),
    (64, "model-quantization-inference", "Model Quantization for Inference"),
    (65, "gradient-accumulation", "Gradient Accumulation for Large Batches"),
    (66, "distributed-training-multi-node", "Distributed Training (Multi-node/Multi-GPU)"),
    (67, "model-pruning-sparsity", "Model Pruning and Sparsity"),
    (68, "knowledge-distillation", "Knowledge Distillation"),

    # Part 12: Model Serving and Deployment (69-74)
    (69, "fastapi-model-serving", "FastAPI Model Serving"),
    (70, "batch-inference-request-batching", "Batch Inference and Request Batching"),
    (71, "streaming-responses-llms", "Streaming Responses for LLMs"),
    (72, "model-optimization-inference", "Model Optimization for Inference (TorchScript/ONNX)"),
    (73, "dockerizing-deploying-service", "Dockerizing and Deploying the Service"),
    (74, "scalable-deployment-monitoring", "Scalable Deployment and Monitoring"),

    # Part 13: RLHF and Alignment (75-78)
    (75, "supervised-fine-tuning-instructions", "Supervised Fine-Tuning for Instructions"),
    (76, "reward-model-training", "Reward Model Training"),
    (77, "ppo-fine-tuning", "Proximal Policy Optimization (PPO) Fine-Tuning"),
    (78, "evaluating-alignment-safety", "Evaluating Alignment and Safety"),

    # Part 14: Scaling Laws and System Design (79-82)
    (79, "scaling-law-experiment", "Scaling Law Experiment"),
    (80, "model-compute-scaling-strategy", "Model and Compute Scaling Strategy"),
    (81, "designing-gpt3-scale-training-system", "Designing a GPT-3 Scale Training System"),
    (82, "designing-deployed-chatgpt-system", "Designing a Deployed ChatGPT System"),

    # Part 15: Advanced Applications and Next Steps (83-85)
    (83, "retrieval-augmented-generation-rag", "Retrieval-Augmented Generation (RAG)"),
    (84, "parameter-efficient-fine-tuning-lora", "Parameter-Efficient Fine-Tuning (LoRA)"),
    (85, "chatgpt-chatbot-capstone", "ChatGPT-style Chatbot (Capstone Application)"),
]


def create_project_structure():
    """Create the directory structure for all 85 projects."""
    base_dir = Path("/home/user/python-edu/Projects")
    base_dir.mkdir(exist_ok=True)

    for num, slug, title in PROJECTS:
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
                f.write(f"This project focuses on {title.lower()}.\n\n")
                f.write(f"## Objectives\n\n")
                f.write(f"- Understand {title.lower()}\n")
                f.write(f"- Implement practical examples\n")
                f.write(f"- Apply concepts to real-world scenarios\n\n")
                f.write(f"## Tasks\n\n")
                f.write(f"1. Complete the implementation in `solution/solution.py`\n")
                f.write(f"2. Run tests with `pytest tests/`\n")
                f.write(f"3. Review `solution_in_words.md` for conceptual understanding\n\n")
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
                f.write(f"[Explanation of the core concepts]\n\n")
                f.write(f"## Approach\n\n")
                f.write(f"[Step-by-step reasoning and approach]\n\n")
                f.write(f"## Key Takeaways\n\n")
                f.write(f"[Important lessons from this project]\n")

        # Create solution.py stub
        solution_file = project_dir / "solution" / "solution.py"
        if not solution_file.exists():
            with open(solution_file, "w") as f:
                f.write(f'"""\n')
                f.write(f"Project {num:02d}: {title}\n")
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
                f.write(f'    """Placeholder test - replace with actual tests."""\n')
                f.write(f"    assert True\n")

        print(f"✓ Created Project {num:02d}: {title}")

    print(f"\n✅ Successfully created all 85 project directories!")
    print(f"📁 Location: {base_dir}")


if __name__ == "__main__":
    create_project_structure()
