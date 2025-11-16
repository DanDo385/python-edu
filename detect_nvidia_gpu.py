#!/usr/bin/env python3
"""
NVIDIA GPU Detection Script

This script detects NVIDIA GPUs and verifies CUDA availability for PyTorch.
It provides detailed information about your GPU setup and training readiness.

Usage:
    python detect_nvidia_gpu.py
"""

import sys


def detect_nvidia_gpu():
    """Detect NVIDIA GPU and CUDA setup."""
    print("🎮 NVIDIA GPU Detection")
    print("=" * 50)
    print()

    # Check if PyTorch is installed
    try:
        import torch
    except ImportError:
        print("❌ PyTorch is not installed!")
        print("   Install with: pip install torch")
        return False

    print(f"PyTorch Version: {torch.__version__}")

    # Check CUDA availability
    cuda_available = torch.cuda.is_available()
    print(f"CUDA Available: {'✓' if cuda_available else '✗'}")

    if not cuda_available:
        print()
        print("⚠️  CUDA is not available. Possible reasons:")
        print("   1. No NVIDIA GPU detected")
        print("   2. NVIDIA drivers not installed")
        print("   3. PyTorch installed without CUDA support")
        print()
        print("To fix:")
        print("   1. Install NVIDIA drivers: https://www.nvidia.com/Download/index.aspx")
        print("   2. Install CUDA toolkit: https://developer.nvidia.com/cuda-downloads")
        print("   3. Reinstall PyTorch with CUDA:")
        print("      pip install torch --index-url https://download.pytorch.org/whl/cu118")
        return False

    # CUDA version
    cuda_version = torch.version.cuda
    print(f"CUDA Version: {cuda_version}")

    # cuDNN version
    cudnn_version = torch.backends.cudnn.version()
    if cudnn_version:
        print(f"cuDNN Version: {cudnn_version}")

    # Device count
    device_count = torch.cuda.device_count()
    print(f"Number of GPUs: {device_count}")
    print()

    # Details for each GPU
    for i in range(device_count):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")

        # Compute capability
        capability = torch.cuda.get_device_capability(i)
        print(f"  Compute Capability: {capability[0]}.{capability[1]}")

        # Memory
        total_memory = torch.cuda.get_device_properties(i).total_memory / 1024**3
        print(f"  Total Memory: {total_memory:.2f} GB")

        # Multi-processors
        multi_processor_count = torch.cuda.get_device_properties(i).multi_processor_count
        print(f"  Multi-Processors: {multi_processor_count}")

        print()

    # Benchmark
    print("Running quick benchmark...")
    try:
        # Warmup
        device = torch.device("cuda:0")
        a = torch.randn(1000, 1000, device=device)
        b = torch.randn(1000, 1000, device=device)
        c = torch.matmul(a, b)
        torch.cuda.synchronize()

        # Benchmark
        import time

        start = time.time()
        for _ in range(100):
            c = torch.matmul(a, b)
        torch.cuda.synchronize()
        end = time.time()

        time_per_op = (end - start) / 100 * 1000
        print(f"Matrix multiplication (1000x1000): {time_per_op:.2f} ms")
        print()

    except Exception as e:
        print(f"Benchmark failed: {e}")
        print()

    # Summary
    print("✓ Your system is ready for GPU-accelerated training!")
    print()
    print("Next steps:")
    print("  1. Review GPU_GUIDE.md for optimization tips")
    print("  2. Start with Projects/45-gpu-basics-speedup/")
    print("  3. Use device = torch.device('cuda') in your code")

    return True


def main():
    """Main entry point."""
    try:
        success = detect_nvidia_gpu()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
