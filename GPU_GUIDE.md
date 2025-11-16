# GPU Acceleration Guide

This guide covers GPU setup and optimization for the AI Learning Curriculum, supporting both NVIDIA CUDA and Apple Metal Performance Shaders backends.

## Table of Contents

- [Overview](#overview)
- [NVIDIA GPU Setup (CUDA)](#nvidia-gpu-setup-cuda)
- [Apple Silicon Setup (Metal)](#apple-silicon-setup-metal)
- [Backend Selection](#backend-selection)
- [Performance Optimization](#performance-optimization)
- [Troubleshooting](#troubleshooting)

## Overview

GPU acceleration dramatically speeds up deep learning training and inference. This curriculum supports:

- **NVIDIA GPUs** (CUDA): Best support, recommended for Projects 45+
- **Apple Silicon** (Metal/MPS): Good support on M1/M2/M3/M4 Macs
- **CPU**: Fallback option, works for all projects (slower for large models)

### When Do You Need a GPU?

| Project Range | GPU Requirement | Reason |
|--------------|----------------|---------|
| 1-17 | Optional | Small-scale NumPy operations, CPU sufficient |
| 18-29 | Recommended | CNNs train faster on GPU, but manageable on CPU |
| 30-44 | Recommended | RNNs and larger models benefit from GPU |
| 45-51 | Required* | GPU programming projects (CUDA, Triton) |
| 52-85 | Highly Recommended | Transformers and LLMs need GPU for practical training |

\* *Projects 47-49 specifically teach GPU programming concepts*

## NVIDIA GPU Setup (CUDA)

### Prerequisites

1. **Compatible NVIDIA GPU**
   - Compute Capability 3.5+ (GTX 600 series or newer)
   - Recommended: RTX 20/30/40 series, or datacenter GPUs (V100, A100)
   - Check compatibility: [NVIDIA CUDA GPUs](https://developer.nvidia.com/cuda-gpus)

2. **Supported Operating Systems**
   - Linux (Ubuntu 20.04+, CentOS 7+, RHEL 7+)
   - Windows 10/11
   - WSL2 on Windows (recommended for Windows users)

### Step 1: Install NVIDIA Drivers

**Linux (Ubuntu):**
```bash
# Check if NVIDIA GPU is detected
lspci | grep -i nvidia

# Install drivers via ubuntu-drivers
sudo ubuntu-drivers autoinstall

# Or install specific driver version
sudo apt install nvidia-driver-535

# Reboot
sudo reboot

# Verify driver installation
nvidia-smi
```

**Windows:**
1. Download from [NVIDIA Driver Downloads](https://www.nvidia.com/Download/index.aspx)
2. Select your GPU model and Windows version
3. Run the installer (choose "Express Installation")
4. Reboot
5. Verify: Open PowerShell and run `nvidia-smi`

**WSL2 on Windows:**
```bash
# Install Windows driver first (see above)
# In WSL2, NVIDIA driver is automatically available

# Verify in WSL2
nvidia-smi
```

### Step 2: Install CUDA Toolkit

**Linux (Ubuntu 22.04):**
```bash
# Download CUDA 12.1 (or latest)
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda-repo-ubuntu2204-12-1-local_12.1.0-530.30.02-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2204-12-1-local_12.1.0-530.30.02-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2204-12-1-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda

# Add to PATH (add to ~/.bashrc for persistence)
export PATH=/usr/local/cuda-12.1/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-12.1/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

# Verify installation
nvcc --version
```

**Windows:**
1. Download from [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
2. Select Windows, x86_64, version, and installer type
3. Run installer (choose "Express Installation")
4. Verify: Open PowerShell and run `nvcc --version`

**Alternative: Use conda (easier, recommended for beginners):**
```bash
# CUDA toolkit via conda
conda install cudatoolkit=11.8 -c conda-forge
```

### Step 3: Install cuDNN (Optional but Recommended)

cuDNN accelerates common deep learning operations.

1. Register for free at [NVIDIA Developer](https://developer.nvidia.com/)
2. Download cuDNN from [NVIDIA cuDNN](https://developer.nvidia.com/cudnn)
3. Extract and copy files to CUDA directory:

**Linux:**
```bash
# Extract cuDNN
tar -xzvf cudnn-linux-x86_64-8.x.x.x_cudaX.Y-archive.tar.xz

# Copy files to CUDA directory
sudo cp cuda/include/cudnn*.h /usr/local/cuda/include
sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*
```

**Windows:**
1. Extract the cuDNN archive
2. Copy files to CUDA installation directory (typically `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\`)

### Step 4: Install PyTorch with CUDA Support

```bash
# For CUDA 11.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# For CUDA 12.1
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Verify CUDA is available
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
python -c "import torch; print(f'CUDA version: {torch.version.cuda}')"
python -c "import torch; print(f'Device count: {torch.cuda.device_count()}')"
python -c "import torch; print(f'Device name: {torch.cuda.get_device_name(0)}')"
```

### Step 5: Run Detection Script

```bash
python detect_nvidia_gpu.py
```

Expected output:
```
🎮 NVIDIA GPU Detection
========================

CUDA Available: ✓
CUDA Version: 12.1
PyTorch Version: 2.1.0
cuDNN Version: 8.9.0

GPU 0: NVIDIA GeForce RTX 3080
  - Compute Capability: 8.6
  - Total Memory: 10.00 GB
  - Multi-Processors: 68

✓ Your system is ready for GPU-accelerated training!
```

## Apple Silicon Setup (Metal)

### Prerequisites

1. **Apple Silicon Mac**
   - M1, M1 Pro, M1 Max, M1 Ultra
   - M2, M2 Pro, M2 Max, M2 Ultra
   - M3, M3 Pro, M3 Max
   - M4, M4 Pro, M4 Max

2. **macOS Version**
   - Minimum: macOS 12.3 (Monterey)
   - Recommended: Latest macOS version for best performance

### Step 1: Update macOS

```bash
# Check macOS version
sw_vers

# Update via System Preferences if needed
# System Preferences → Software Update
```

### Step 2: Install PyTorch with MPS Support

PyTorch automatically includes Metal Performance Shaders (MPS) backend on supported systems.

```bash
# Install PyTorch (includes MPS support)
pip install torch torchvision torchaudio

# Verify MPS is available
python -c "import torch; print(f'MPS available: {torch.backends.mps.is_available()}')"
python -c "import torch; print(f'MPS built: {torch.backends.mps.is_built()}')"
```

### Step 3: Run Detection Script

```bash
python detect_apple_metal_gpu.py
```

Expected output:
```
🍎 Apple Metal GPU Detection
============================

MPS Available: ✓
MPS Built: ✓
PyTorch Version: 2.1.0

Device: Apple M4
  - Architecture: arm64
  - Total Memory: 16.00 GB (unified)

✓ Your system is ready for GPU-accelerated training via Metal!
```

### Using MPS in Code

```python
import torch

# Auto-detect device
if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

# Move tensors and models to device
x = torch.randn(1000, 1000).to(device)
model = MyModel().to(device)

# Training loop
for batch in dataloader:
    inputs = batch['input'].to(device)
    outputs = model(inputs)
```

### MPS Limitations

Some operations are not yet supported on MPS:
- Sparse tensors
- Some advanced indexing operations
- Certain custom CUDA kernels

When an unsupported operation is encountered, PyTorch will automatically fall back to CPU. This is normal and expected.

## Backend Selection

### Auto-Detection (Recommended)

Use the auto-detection script to find the best available backend:

```bash
python detect_accelerated_backend.py
```

This will output:
- Detected backend (CUDA, MPS, or CPU)
- Device to use in your code
- Performance estimate

### Manual Selection in Code

```python
import torch

def get_device():
    """Get the best available device for training."""
    if torch.cuda.is_available():
        return torch.device("cuda")
    elif torch.backends.mps.is_available():
        return torch.device("mps")
    else:
        return torch.device("cpu")

device = get_device()
print(f"Using device: {device}")
```

### Force Specific Backend

```python
# Force CUDA
device = torch.device("cuda:0")  # Use GPU 0

# Force MPS
device = torch.device("mps")

# Force CPU
device = torch.device("cpu")
```

### Multi-GPU Selection

For systems with multiple NVIDIA GPUs:

```python
# Use specific GPU
device = torch.device("cuda:1")  # Use GPU 1

# Use multiple GPUs with DataParallel
model = nn.DataParallel(model, device_ids=[0, 1, 2])

# Use multiple GPUs with DistributedDataParallel (better)
# See Project 66 for details
```

## Performance Optimization

### Benchmarking Your Setup

```python
import torch
import time

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Matrix multiplication benchmark
size = 8192
a = torch.randn(size, size).to(device)
b = torch.randn(size, size).to(device)

# Warmup
for _ in range(10):
    c = a @ b

# Benchmark
torch.cuda.synchronize() if device.type == "cuda" else None
start = time.time()
for _ in range(100):
    c = a @ b
torch.cuda.synchronize() if device.type == "cuda" else None
end = time.time()

print(f"Time: {(end - start) / 100 * 1000:.2f} ms per iteration")
print(f"TFLOPS: {2 * size**3 / ((end - start) / 100) / 1e12:.2f}")
```

### Best Practices

1. **Move data to GPU once**
   ```python
   # Good
   data = data.to(device)
   for epoch in range(epochs):
       output = model(data)

   # Bad (slow)
   for epoch in range(epochs):
       output = model(data.to(device))
   ```

2. **Use pinned memory for DataLoader**
   ```python
   dataloader = DataLoader(
       dataset,
       batch_size=32,
       pin_memory=True,  # Faster CPU-to-GPU transfer
       num_workers=4
   )
   ```

3. **Enable cuDNN autotuner**
   ```python
   torch.backends.cudnn.benchmark = True  # Auto-tune convolution algorithms
   ```

4. **Use mixed precision (AMP)**
   ```python
   from torch.cuda.amp import autocast, GradScaler

   scaler = GradScaler()

   for batch in dataloader:
       with autocast():
           output = model(batch)
           loss = criterion(output, target)

       scaler.scale(loss).backward()
       scaler.step(optimizer)
       scaler.update()
   ```

5. **Monitor GPU utilization**
   ```bash
   # NVIDIA
   watch -n 1 nvidia-smi

   # Apple Silicon
   # Use Activity Monitor → GPU History
   ```

## Troubleshooting

### NVIDIA GPU Issues

**Issue: `nvidia-smi` not found**
- **Solution**: Reinstall NVIDIA drivers

**Issue: CUDA out of memory**
```
RuntimeError: CUDA out of memory. Tried to allocate X.XX GiB
```
- **Solutions**:
  1. Reduce batch size
  2. Use gradient checkpointing (Project 62)
  3. Use gradient accumulation (Project 65)
  4. Enable mixed precision (Project 63)
  5. Clear cache: `torch.cuda.empty_cache()`

**Issue: PyTorch not detecting GPU**
```python
>>> torch.cuda.is_available()
False
```
- **Solutions**:
  1. Check CUDA version: `nvcc --version`
  2. Reinstall PyTorch with matching CUDA version
  3. Check driver: `nvidia-smi`

**Issue: Slow training despite GPU**
- **Solutions**:
  1. Increase batch size to utilize GPU better
  2. Check data loading isn't bottleneck (use `num_workers > 0`)
  3. Enable `torch.backends.cudnn.benchmark = True`
  4. Profile with `torch.profiler`

### Apple Metal Issues

**Issue: MPS not available**
```python
>>> torch.backends.mps.is_available()
False
```
- **Solutions**:
  1. Update macOS to 12.3+
  2. Update PyTorch: `pip install --upgrade torch`
  3. Check chip: `sysctl -n machdep.cpu.brand_string`

**Issue: MPS operation not supported**
```
NotImplementedError: The operator 'aten::foo' is not currently implemented for the MPS device
```
- **Solutions**:
  1. Use CPU fallback for that operation:
     ```python
     x = x.cpu()
     y = some_op(x)
     y = y.to("mps")
     ```
  2. Update PyTorch to latest version
  3. Check PyTorch MPS roadmap for planned support

**Issue: Slower than expected on Apple Silicon**
- **Solutions**:
  1. Ensure MPS is actually being used: `print(tensor.device)`
  2. Increase batch size
  3. Some operations are faster on CPU for small tensors
  4. Check Activity Monitor for GPU utilization

### General GPU Issues

**Issue: Device-side assertion errors**
- **Solution**: Run on CPU to get better error messages, then fix and move back to GPU

**Issue: Inconsistent results between CPU and GPU**
- **Solutions**:
  1. Set seed for all devices:
     ```python
     torch.manual_seed(42)
     torch.cuda.manual_seed(42)
     torch.backends.cudnn.deterministic = True
     ```
  2. Check for numerical precision issues (use double instead of float)

## Additional Resources

- [PyTorch CUDA Semantics](https://pytorch.org/docs/stable/notes/cuda.html)
- [PyTorch MPS Backend](https://pytorch.org/docs/stable/notes/mps.html)
- [NVIDIA CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)
- [Apple Metal Performance Shaders](https://developer.apple.com/documentation/metalperformanceshaders)

---

**Ready to accelerate your training!** ⚡

See [SETUP.md](SETUP.md) for general environment setup.
