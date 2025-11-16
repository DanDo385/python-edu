#!/usr/bin/env python3
"""
Apple Metal GPU Detection Script

This script detects Apple Silicon GPUs and verifies Metal Performance Shaders (MPS)
availability for PyTorch on M1/M2/M3/M4 Macs.

Usage:
    python detect_apple_metal_gpu.py
"""

import sys
import platform


def detect_apple_metal_gpu():
    """Detect Apple Metal GPU and MPS setup."""
    print("🍎 Apple Metal GPU Detection")
    print("=" * 50)
    print()

    # Check platform
    system = platform.system()
    if system != "Darwin":
        print(f"❌ This script is for macOS only (detected: {system})")
        print("   For NVIDIA GPUs, use: python detect_nvidia_gpu.py")
        return False

    machine = platform.machine()
    print(f"System: macOS {platform.mac_ver()[0]}")
    print(f"Architecture: {machine}")
    print()

    # Check if Apple Silicon
    if machine != "arm64":
        print(f"⚠️  Not Apple Silicon (detected: {machine})")
        print("   Metal GPU acceleration requires M1/M2/M3/M4 chip")
        print("   You can still use CPU for all projects")
        return False

    # Check if PyTorch is installed
    try:
        import torch
    except ImportError:
        print("❌ PyTorch is not installed!")
        print("   Install with: pip install torch torchvision torchaudio")
        return False

    print(f"PyTorch Version: {torch.__version__}")

    # Check MPS availability
    mps_available = torch.backends.mps.is_available()
    mps_built = torch.backends.mps.is_built()

    print(f"MPS Available: {'✓' if mps_available else '✗'}")
    print(f"MPS Built: {'✓' if mps_built else '✗'}")
    print()

    if not mps_built:
        print("⚠️  MPS backend not built into this PyTorch installation")
        print("   Reinstall PyTorch: pip install --upgrade torch torchvision torchaudio")
        return False

    if not mps_available:
        print("⚠️  MPS is not available. Possible reasons:")
        print("   1. macOS version too old (need 12.3+)")
        print("   2. PyTorch version too old")
        print()
        print("To fix:")
        print("   1. Update macOS to 12.3 or higher")
        print("   2. Update PyTorch: pip install --upgrade torch")
        return False

    # Get device info
    print("Device Information:")
    print(f"  Chip: {get_chip_name()}")

    # Get memory info
    try:
        import subprocess

        memory_output = subprocess.check_output(
            ["sysctl", "hw.memsize"], encoding="utf-8"
        )
        memory_bytes = int(memory_output.split(":")[1].strip())
        memory_gb = memory_bytes / (1024**3)
        print(f"  Total Memory: {memory_gb:.2f} GB (unified)")
    except Exception:
        print("  Total Memory: Unable to detect")

    print()

    # Benchmark
    print("Running quick benchmark...")
    try:
        # Test MPS device
        device = torch.device("mps")

        # Warmup
        a = torch.randn(1000, 1000, device=device)
        b = torch.randn(1000, 1000, device=device)
        c = torch.matmul(a, b)

        # Benchmark
        import time

        start = time.time()
        for _ in range(100):
            c = torch.matmul(a, b)
        end = time.time()

        time_per_op = (end - start) / 100 * 1000
        print(f"Matrix multiplication (1000x1000): {time_per_op:.2f} ms")
        print()

        # Compare with CPU
        device_cpu = torch.device("cpu")
        a_cpu = a.cpu()
        b_cpu = b.cpu()

        start = time.time()
        for _ in range(100):
            c_cpu = torch.matmul(a_cpu, b_cpu)
        end = time.time()

        time_per_op_cpu = (end - start) / 100 * 1000
        speedup = time_per_op_cpu / time_per_op
        print(f"CPU time: {time_per_op_cpu:.2f} ms")
        print(f"GPU speedup: {speedup:.2f}x")
        print()

    except Exception as e:
        print(f"Benchmark failed: {e}")
        print("This may indicate MPS compatibility issues")
        print()

    # Summary
    print("✓ Your system is ready for GPU-accelerated training via Metal!")
    print()
    print("Next steps:")
    print("  1. Review GPU_GUIDE.md for Apple Silicon tips")
    print("  2. Start with Projects/45-gpu-basics-speedup/")
    print("  3. Use device = torch.device('mps') in your code")
    print()
    print("Note: Some operations may fall back to CPU (this is normal)")

    return True


def get_chip_name():
    """Get the Apple chip name (M1, M2, M3, M4)."""
    try:
        import subprocess

        output = subprocess.check_output(
            ["sysctl", "-n", "machdep.cpu.brand_string"], encoding="utf-8"
        )
        return output.strip()
    except Exception:
        return "Apple Silicon (unknown model)"


def main():
    """Main entry point."""
    try:
        success = detect_apple_metal_gpu()
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
