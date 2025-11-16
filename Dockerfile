# AI Learning Curriculum Dockerfile
# Supports NVIDIA CUDA GPUs with PyTorch, Jupyter, and all curriculum dependencies

# Use NVIDIA CUDA base image for GPU support
# For CPU-only, use: FROM python:3.10-slim
FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set working directory
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3.10-dev \
    python3-pip \
    git \
    wget \
    curl \
    vim \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python3.10 -m pip install --upgrade pip setuptools wheel

# Install PyTorch with CUDA support
# For CUDA 11.8
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install Jupyter and IPython
RUN pip install jupyter jupyterlab ipython ipykernel ipywidgets

# Install scientific computing libraries
RUN pip install numpy scipy matplotlib pandas scikit-learn

# Install NLP and transformer libraries
RUN pip install transformers datasets tokenizers sentencepiece

# Install deep learning utilities
RUN pip install einops timm accelerate

# Install development and testing tools
RUN pip install pytest pytest-cov black flake8 mypy

# Install API and deployment tools
RUN pip install fastapi uvicorn pydantic

# Install vector database and RAG tools
RUN pip install faiss-cpu chromadb

# Install Triton for GPU kernels (CUDA only)
RUN pip install triton || echo "Triton installation skipped (requires CUDA)"

# Install additional utilities
RUN pip install tqdm rich typer requests beautifulsoup4 pillow

# Copy requirements file (if you want to use it)
COPY requirements-dev.txt /tmp/requirements-dev.txt
RUN pip install -r /tmp/requirements-dev.txt || echo "Some packages from requirements-dev.txt may have failed"

# Create Jupyter config directory
RUN mkdir -p /root/.jupyter

# Configure Jupyter
RUN jupyter notebook --generate-config && \
    echo "c.NotebookApp.ip = '0.0.0.0'" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.allow_root = True" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.open_browser = False" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.token = ''" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = ''" >> /root/.jupyter/jupyter_notebook_config.py

# Expose Jupyter port
EXPOSE 8888

# Copy curriculum files
COPY . /workspace

# Set Python path
ENV PYTHONPATH="/workspace:${PYTHONPATH}"

# Default command: Start Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
