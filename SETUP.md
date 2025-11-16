# Environment Setup Guide

This guide provides detailed instructions for setting up your development environment for the AI Learning Curriculum, covering all major platforms and hardware configurations.

## Table of Contents

- [System Requirements](#system-requirements)
- [Python Installation](#python-installation)
- [Virtual Environment Setup](#virtual-environment-setup)
- [Dependencies Installation](#dependencies-installation)
- [Hardware-Specific Setup](#hardware-specific-setup)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

## System Requirements

### Minimum Requirements
- **OS**: Windows 10/11, macOS 10.15+, Linux (Ubuntu 20.04+, Debian, Fedora, etc.)
- **Python**: 3.10 or higher
- **RAM**: 8GB (16GB+ recommended for Projects 45+)
- **Storage**: 10GB free space (20GB+ recommended)
- **CPU**: Modern multi-core processor (4+ cores recommended)

### Recommended for GPU Acceleration
- **NVIDIA GPU**: GTX 1060 (6GB) or better, with CUDA 11.8+ support
- **Apple Silicon**: M1, M2, M3, or M4 chips with Metal support
- **AMD GPU**: Limited support via ROCm (advanced users)

## Python Installation

### macOS

**Option 1: Using Homebrew (Recommended)**
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.10 or higher
brew install python@3.10

# Verify installation
python3 --version
```

**Option 2: Using pyenv**
```bash
# Install pyenv
brew install pyenv

# Install Python 3.10
pyenv install 3.10.13

# Set as global version
pyenv global 3.10.13
```

**Option 3: Official Installer**
Download from [python.org](https://www.python.org/downloads/macos/) and follow the installation wizard.

### Windows

**Option 1: Official Installer (Recommended)**
1. Download from [python.org](https://www.python.org/downloads/windows/)
2. Run the installer
3. **Important**: Check "Add Python to PATH"
4. Click "Install Now"
5. Verify in Command Prompt: `python --version`

**Option 2: Using winget**
```powershell
# Install Python 3.10
winget install Python.Python.3.10

# Verify installation
python --version
```

**Option 3: Using Chocolatey**
```powershell
# Install Chocolatey first (if needed)
# Then install Python
choco install python310

# Verify installation
python --version
```

### Linux

**Ubuntu/Debian:**
```bash
# Update package list
sudo apt update

# Install Python 3.10+
sudo apt install python3.10 python3.10-venv python3.10-dev

# Install pip
sudo apt install python3-pip

# Verify installation
python3.10 --version
```

**Fedora/RHEL/CentOS:**
```bash
# Install Python 3.10+
sudo dnf install python3.10 python3.10-devel

# Verify installation
python3.10 --version
```

**Arch Linux:**
```bash
# Install Python
sudo pacman -S python python-pip

# Verify installation
python --version
```

## Virtual Environment Setup

Using virtual environments is **strongly recommended** to isolate project dependencies.

### Creating a Virtual Environment

**macOS/Linux:**
```bash
# Navigate to the project directory
cd python-edu

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Your prompt should now show (venv)
```

**Windows (Command Prompt):**
```cmd
# Navigate to the project directory
cd python-edu

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate.bat

# Your prompt should now show (venv)
```

**Windows (PowerShell):**
```powershell
# Navigate to the project directory
cd python-edu

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\Activate.ps1

# If you get an execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Deactivating Virtual Environment

To deactivate the virtual environment:
```bash
deactivate
```

## Dependencies Installation

### Installing All Dependencies

With your virtual environment activated:

```bash
# Upgrade pip to the latest version
pip install --upgrade pip

# Install development dependencies (includes everything)
pip install -r requirements-dev.txt
```

### Phased Installation (Optional)

If you want to install dependencies progressively as you work through the curriculum:

**Phase 1: Python Fundamentals (Projects 1-10)**
```bash
# No external dependencies needed
# Uses Python standard library only
```

**Phase 2: Math & NumPy (Projects 11-17)**
```bash
pip install numpy matplotlib pandas scipy
```

**Phase 3: PyTorch & ML (Projects 18-44)**
```bash
pip install torch torchvision torchaudio
pip install scikit-learn
```

**Phase 4: Advanced (Projects 45-85)**
```bash
pip install transformers datasets tokenizers
pip install sentencepiece
pip install fastapi uvicorn
pip install jupyter ipykernel
pip install pytest pytest-cov
```

### Verifying Installation

```bash
# Check installed packages
pip list

# Verify key packages
python -c "import numpy; print(f'NumPy {numpy.__version__}')"
python -c "import torch; print(f'PyTorch {torch.__version__}')"
python -c "import transformers; print(f'Transformers {transformers.__version__}')"
```

## Hardware-Specific Setup

### NVIDIA GPU Setup (CUDA)

**1. Check GPU Compatibility**
```bash
# On Linux/WSL
nvidia-smi

# Check CUDA version
nvcc --version
```

**2. Install NVIDIA Drivers**
- **Windows**: Download from [NVIDIA Driver Downloads](https://www.nvidia.com/Download/index.aspx)
- **Linux**:
  ```bash
  # Ubuntu
  sudo ubuntu-drivers autoinstall
  sudo reboot
  ```

**3. Install CUDA Toolkit**
- Download from [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
- Follow platform-specific installation instructions
- Recommended version: CUDA 11.8 or 12.1

**4. Install cuDNN**
- Download from [NVIDIA cuDNN](https://developer.nvidia.com/cudnn) (requires free account)
- Extract and copy to CUDA installation directory

**5. Install PyTorch with CUDA Support**
```bash
# For CUDA 11.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# For CUDA 12.1
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Verify CUDA is available
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
python -c "import torch; print(f'CUDA device: {torch.cuda.get_device_name(0)}')"
```

### Apple Silicon Setup (M1/M2/M3/M4)

**1. Ensure macOS is Up-to-Date**
- Minimum: macOS 12.3+ (for Metal support)
- Recommended: Latest macOS version

**2. Install PyTorch with Metal Support**
```bash
# Install PyTorch (includes MPS backend)
pip install torch torchvision torchaudio

# Verify Metal/MPS is available
python -c "import torch; print(f'MPS available: {torch.backends.mps.is_available()}')"
python -c "import torch; print(f'MPS built: {torch.backends.mps.is_built()}')"
```

**3. Test Metal Performance**
```bash
python detect_apple_metal_gpu.py
```

**Note on Apple Silicon:**
- The MPS (Metal Performance Shaders) backend provides GPU acceleration on Apple Silicon
- Not all PyTorch operations are supported on MPS yet; fallback to CPU is automatic
- Some projects may need CPU for compatibility

### CPU-Only Setup

If you don't have a compatible GPU or prefer CPU:

```bash
# Install standard PyTorch (CPU version)
pip install torch torchvision torchaudio

# All projects will work on CPU
# Training will be slower for larger models (Projects 45+)
```

## Verification

### Complete System Check

Run the provided detection scripts:

```bash
# Detect NVIDIA GPU
python detect_nvidia_gpu.py

# Detect Apple Metal GPU
python detect_apple_metal_gpu.py

# Auto-detect best accelerated backend
python detect_accelerated_backend.py
```

### Manual Verification

```bash
# Python version
python --version  # Should be 3.10+

# Pip version
pip --version

# NumPy
python -c "import numpy; numpy.test('full')"

# PyTorch
python -c "import torch; print(torch.__version__)"
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}')"
python -c "import torch; print(f'MPS: {torch.backends.mps.is_available()}')"

# Test basic tensor operation
python -c "import torch; x = torch.randn(5, 5); print(x @ x.T)"

# Run sample tests
pytest Projects/01-dynamic-typing-basics/tests/ -v
```

## Troubleshooting

### Common Issues

**Issue: `python` command not found**
- **Solution**: Use `python3` instead, or create an alias: `alias python=python3`

**Issue: Permission denied when installing packages**
- **Solution**: Ensure virtual environment is activated, or use `pip install --user`

**Issue: CUDA not detected by PyTorch**
- **Solution**:
  1. Verify NVIDIA drivers: `nvidia-smi`
  2. Check CUDA version matches PyTorch installation
  3. Reinstall PyTorch with correct CUDA version

**Issue: MPS not available on Apple Silicon**
- **Solution**:
  1. Update macOS to 12.3+
  2. Update PyTorch to latest version: `pip install --upgrade torch`
  3. Check with: `python -c "import torch; print(torch.backends.mps.is_available())"`

**Issue: Out of memory errors during training**
- **Solution**:
  1. Reduce batch size in training scripts
  2. Use gradient accumulation (covered in Project 65)
  3. Enable gradient checkpointing (covered in Project 62)
  4. Use mixed precision training (covered in Project 63)

**Issue: Slow imports or training**
- **Solution**:
  1. Ensure virtual environment is activated
  2. Check that GPU is being used (not CPU fallback)
  3. Monitor GPU usage: `nvidia-smi` or Activity Monitor (macOS)
  4. Disable debug mode if enabled

**Issue: Module not found errors**
- **Solution**:
  1. Activate virtual environment
  2. Reinstall requirements: `pip install -r requirements-dev.txt`
  3. Check Python path: `python -c "import sys; print(sys.path)"`

### Getting Help

If you encounter issues not covered here:

1. Check [GPU_GUIDE.md](GPU_GUIDE.md) for GPU-specific troubleshooting
2. Check [DOCKER.md](DOCKER.md) for containerized environment option
3. Search existing GitHub issues
4. Open a new issue with:
   - Your OS and Python version
   - Output of `pip list`
   - Full error message and traceback
   - Steps to reproduce

## Next Steps

After completing setup:

1. ✅ Verify installation with detection scripts
2. ✅ Run tests for Project 01: `pytest Projects/01-dynamic-typing-basics/tests/`
3. ✅ Read [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for curriculum overview
4. ✅ Start with [Projects/01-dynamic-typing-basics/README.md](Projects/01-dynamic-typing-basics/README.md)

---

**Happy learning!** 🚀

For GPU-specific setup details, see [GPU_GUIDE.md](GPU_GUIDE.md).
