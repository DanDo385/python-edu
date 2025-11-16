# Docker Guide

This guide explains how to use Docker to run the AI Learning Curriculum in a containerized environment with consistent dependencies across all platforms.

## Table of Contents

- [Why Use Docker?](#why-use-docker)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)
- [GPU Support](#gpu-support)
- [Troubleshooting](#troubleshooting)

## Why Use Docker?

Docker provides a consistent, reproducible environment that:

✅ **Eliminates "works on my machine" issues**
✅ **Bundles all dependencies (Python, PyTorch, Jupyter, etc.)**
✅ **Supports both NVIDIA CUDA and Apple Metal (via host)**
✅ **Simplifies setup across Windows, macOS, and Linux**
✅ **Isolates the environment from your system**

**When to use Docker:**
- You want a quick setup without manual configuration
- You're on different machines (laptop, server, cloud)
- You need reproducibility for experiments
- You prefer containers over virtual environments

**When NOT to use Docker:**
- You already have a working local environment
- You want maximum GPU performance (native install is slightly faster)
- You're learning system administration basics

## Prerequisites

### Install Docker

**macOS:**
```bash
# Download Docker Desktop from:
# https://www.docker.com/products/docker-desktop

# Or via Homebrew
brew install --cask docker
```

**Windows:**
```powershell
# Download Docker Desktop from:
# https://www.docker.com/products/docker-desktop

# Requires WSL2 (Windows Subsystem for Linux)
# Follow Docker Desktop installation wizard
```

**Linux (Ubuntu):**
```bash
# Update package index
sudo apt-get update

# Install prerequisites
sudo apt-get install ca-certificates curl gnupg lsb-release

# Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Set up repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Add user to docker group (avoid sudo)
sudo usermod -aG docker $USER
newgrp docker

# Verify installation
docker --version
docker compose version
```

### Install NVIDIA Container Toolkit (Optional, for GPU)

If you have an NVIDIA GPU and want to use it in Docker:

**Linux:**
```bash
# Add NVIDIA package repositories
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

# Install nvidia-docker2
sudo apt-get update
sudo apt-get install -y nvidia-docker2

# Restart Docker daemon
sudo systemctl restart docker

# Test GPU access
docker run --rm --gpus all nvidia/cuda:11.8.0-base-ubuntu22.04 nvidia-smi
```

**Windows (WSL2):**
CUDA in Docker is supported via WSL2. Ensure:
1. WSL2 is installed and updated
2. NVIDIA drivers are installed on Windows (not in WSL)
3. Docker Desktop has WSL2 backend enabled

**macOS:**
Docker on macOS doesn't support direct GPU passthrough. For Apple Silicon, use native installation instead (see [SETUP.md](SETUP.md)).

## Quick Start

### Build and Run

```bash
# Navigate to repository
cd python-edu

# Build the Docker image
docker compose build

# Start the container
docker compose up -d

# View Jupyter logs to get the access token
docker compose logs

# Open Jupyter in your browser
# Navigate to: http://localhost:8888
# Use the token from the logs
```

### Access Jupyter Notebook

1. The container starts Jupyter Notebook on port 8888
2. Check logs for access token:
   ```bash
   docker compose logs python-edu | grep token
   ```
3. Open browser: `http://localhost:8888/?token=<your-token>`

### Run Tests

```bash
# Run all tests
docker compose exec python-edu pytest Projects/ -v

# Run specific project tests
docker compose exec python-edu pytest Projects/01-dynamic-typing-basics/tests/ -v

# Run with coverage
docker compose exec python-edu pytest Projects/ --cov=. --cov-report=html
```

### Access Shell

```bash
# Open interactive shell in container
docker compose exec python-edu /bin/bash

# Now you're inside the container
(container)$ python --version
(container)$ nvidia-smi  # If GPU enabled
(container)$ cd Projects/01-dynamic-typing-basics
(container)$ pytest tests/
```

### Stop and Clean Up

```bash
# Stop container
docker compose down

# Stop and remove volumes
docker compose down -v

# Remove image
docker rmi python-edu:latest
```

## Configuration

### Dockerfile

The `Dockerfile` defines the container image:

```dockerfile
# See Dockerfile for full configuration
# Key features:
# - Python 3.10 base image
# - PyTorch with CUDA support
# - Jupyter Notebook
# - All curriculum dependencies
# - Triton for GPU kernels
```

### docker-compose.yml

The `docker-compose.yml` orchestrates services:

```yaml
# See docker-compose.yml for full configuration
# Key features:
# - Mounts local directory for persistence
# - Exposes Jupyter on port 8888
# - GPU support (when available)
# - Environment variables for configuration
```

### Environment Variables

Configure the container via environment variables:

```bash
# In docker-compose.yml or .env file

# Jupyter token (set for security)
JUPYTER_TOKEN=your-secret-token

# CUDA device (for multi-GPU systems)
CUDA_VISIBLE_DEVICES=0

# Number of workers for PyTorch DataLoader
NUM_WORKERS=4
```

## Usage Examples

### Example 1: Run a Single Project

```bash
# Start container
docker compose up -d

# Run project 01 tests
docker compose exec python-edu pytest Projects/01-dynamic-typing-basics/tests/ -v

# Run project 01 solution
docker compose exec python-edu python Projects/01-dynamic-typing-basics/solution/solution.py
```

### Example 2: Interactive Development

```bash
# Start container
docker compose up -d

# Access Jupyter at http://localhost:8888
# Create new notebook or edit existing ones
# All changes are persisted to your local directory
```

### Example 3: Training with GPU

```bash
# Start container with GPU
docker compose up -d

# Verify GPU is accessible
docker compose exec python-edu python -c "import torch; print(torch.cuda.is_available())"

# Run a GPU-intensive project
docker compose exec python-edu python Projects/45-gpu-basics-speedup/solution/solution.py
```

### Example 4: Batch Testing

```bash
# Run all Part 1 tests
docker compose exec python-edu pytest Projects/0[1-9]-*/tests/ Projects/10-*/tests/ -v

# Run all NumPy projects
docker compose exec python-edu pytest Projects/1[1-7]-*/tests/ -v

# Run all PyTorch projects
docker compose exec python-edu pytest Projects/[2-3][0-9]-*/tests/ Projects/4[0-4]-*/tests/ -v
```

## GPU Support

### NVIDIA GPU

The Dockerfile and docker-compose.yml are configured for NVIDIA GPU support:

**docker-compose.yml:**
```yaml
services:
  python-edu:
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
```

**Verify GPU in container:**
```bash
docker compose exec python-edu nvidia-smi
docker compose exec python-edu python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
```

### Apple Silicon

Docker on macOS doesn't support GPU passthrough for Metal. Instead:

1. **Use native installation** (recommended for Apple Silicon)
   - See [SETUP.md](SETUP.md) for Apple Metal setup
   - Direct Metal access provides better performance

2. **Use Docker for CPU-only workloads**
   - Docker on macOS runs in a Linux VM
   - Suitable for Projects 1-44 (CPU sufficient)
   - Projects 45+ may be slow without GPU

### CPU-Only

If you don't have a GPU or want CPU-only:

```bash
# Build CPU-only image
docker compose build --build-arg PYTORCH_VERSION=cpu

# Or modify docker-compose.yml to remove GPU reservation
```

## Troubleshooting

### Issue: Port 8888 already in use

**Solution:**
```bash
# Change port in docker-compose.yml
ports:
  - "8889:8888"  # Use 8889 on host

# Or stop conflicting service
lsof -ti:8888 | xargs kill
```

### Issue: Permission denied

**Solution:**
```bash
# Add user to docker group (Linux)
sudo usermod -aG docker $USER
newgrp docker

# Or run with sudo (not recommended)
sudo docker compose up -d
```

### Issue: GPU not detected in container

**Solution:**
```bash
# Verify NVIDIA Container Toolkit is installed
nvidia-ctk --version

# Check nvidia-smi on host
nvidia-smi

# Rebuild image
docker compose down
docker compose build --no-cache
docker compose up -d

# Verify GPU in container
docker compose exec python-edu nvidia-smi
```

### Issue: Out of memory

**Solution:**
```bash
# Increase Docker memory limit
# Docker Desktop → Settings → Resources → Memory
# Set to at least 8GB (16GB recommended)

# Or reduce batch sizes in training scripts
```

### Issue: Container exits immediately

**Solution:**
```bash
# Check logs
docker compose logs python-edu

# Common causes:
# 1. Port conflict
# 2. Invalid environment variable
# 3. Missing dependency

# Rebuild image
docker compose build --no-cache
```

### Issue: Changes not persisted

**Solution:**
```bash
# Verify volume mount in docker-compose.yml
volumes:
  - .:/workspace

# Check that you're editing files in the mounted directory
docker compose exec python-edu pwd  # Should show /workspace
```

### Issue: Slow build time

**Solution:**
```bash
# Use BuildKit for faster builds
export DOCKER_BUILDKIT=1
docker compose build

# Or cache layers
docker compose build --build-arg BUILDKIT_INLINE_CACHE=1
```

## Advanced Usage

### Custom Jupyter Configuration

Create `jupyter_notebook_config.py` in the repository:

```python
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.allow_root = True
c.NotebookApp.open_browser = False
c.NotebookApp.token = 'your-secret-token'
c.NotebookApp.password = ''  # Or set password hash
```

Mount it in docker-compose.yml:
```yaml
volumes:
  - ./jupyter_notebook_config.py:/root/.jupyter/jupyter_notebook_config.py
```

### Multi-GPU Setup

```yaml
# docker-compose.yml
services:
  python-edu:
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              device_ids: ['0', '1']  # Specific GPUs
              capabilities: [gpu]
```

### Cloud Deployment

Deploy the container to cloud providers:

**AWS EC2 (with GPU):**
```bash
# Launch p3.2xlarge instance (V100 GPU)
# Install Docker and NVIDIA Container Toolkit
# Clone repo and run:
docker compose up -d

# Access via public IP: http://<public-ip>:8888
```

**Google Cloud (with GPU):**
```bash
# Launch n1-standard-4 with T4 GPU
# Install Docker and NVIDIA Container Toolkit
# Clone repo and run:
docker compose up -d
```

## Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-docker)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [PyTorch Docker Images](https://hub.docker.com/r/pytorch/pytorch)

---

**Containerize your learning environment!** 🐳

See [SETUP.md](SETUP.md) for native installation or [GPU_GUIDE.md](GPU_GUIDE.md) for GPU-specific setup.
