#!/usr/bin/env python3
"""
Accelerated Backend Auto-Detection Script

This script automatically detects the best available accelerated backend
(CUDA, MPS, or CPU) for PyTorch training and provides usage examples.

Usage:
    python detect_accelerated_backend.py
"""

import sys
import platform


def detect_best_backend():
    """Detect the best available backend for training."""
    print("🚀 PyTorch Backend Auto-Detection")
    print("=" * 50)
    print()

    # Check if PyTorch is installed
    try:
        import torch
    except ImportError:
        print("❌ PyTorch is not installed!")
        print("   Install with: pip install torch")
        return None

    print(f"PyTorch Version: {torch.__version__}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Platform: {platform.system()} {platform.machine()}")
    print()

    # Detect available backends
    backends = {
        "cuda": False,
        "mps": False,
        "cpu": True,  # Always available
    }

    # Check CUDA
    if torch.cuda.is_available():
        backends["cuda"] = True

    # Check MPS
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        backends["mps"] = True

    # Print detection results
    print("Backend Availability:")
    print(f"  CUDA (NVIDIA GPU): {'✓' if backends['cuda'] else '✗'}")
    print(f"  MPS (Apple Metal): {'✓' if backends['mps'] else '✗'}")
    print(f"  CPU: ✓ (always available)")
    print()

    # Determine best backend
    if backends["cuda"]:
        best_backend = "cuda"
        device_name = torch.cuda.get_device_name(0)
        print(f"🏆 Best Backend: CUDA")
        print(f"   Device: {device_name}")
        print(f"   Memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f} GB")
    elif backends["mps"]:
        best_backend = "mps"
        print(f"🏆 Best Backend: MPS (Apple Metal)")
        print(f"   Device: {get_apple_chip()}")
    else:
        best_backend = "cpu"
        print(f"🏆 Best Backend: CPU")
        print(f"   Note: Projects will run slower without GPU")

    print()

    # Run comparative benchmark
    print("Running comparative benchmark...")
    benchmark_results = run_benchmark(torch, backends)

    # Print benchmark results
    print()
    print("Benchmark Results (1000x1000 matrix multiplication):")
    print("-" * 50)

    cpu_time = benchmark_results.get("cpu", None)
    if cpu_time:
        print(f"  CPU: {cpu_time:.2f} ms")

    cuda_time = benchmark_results.get("cuda", None)
    if cuda_time:
        speedup = cpu_time / cuda_time if cpu_time else 0
        print(f"  CUDA: {cuda_time:.2f} ms ({speedup:.2f}x faster than CPU)")

    mps_time = benchmark_results.get("mps", None)
    if mps_time:
        speedup = cpu_time / mps_time if cpu_time else 0
        print(f"  MPS: {mps_time:.2f} ms ({speedup:.2f}x faster than CPU)")

    print()

    # Usage example
    print("=" * 50)
    print("Usage in Your Code:")
    print("=" * 50)
    print()
    print("```python")
    print("import torch")
    print()
    print("# Auto-detect best device")
    print("def get_device():")
    print("    if torch.cuda.is_available():")
    print("        return torch.device('cuda')")
    print("    elif torch.backends.mps.is_available():")
    print("        return torch.device('mps')")
    print("    else:")
    print("        return torch.device('cpu')")
    print()
    print("device = get_device()")
    print(f"print(f'Using device: {{device}}')  # Will use: {best_backend}")
    print()
    print("# Move tensors and models to device")
    print("x = torch.randn(100, 100).to(device)")
    print("model = MyModel().to(device)")
    print("```")
    print()

    # Project-specific recommendations
    print("=" * 50)
    print("Project Recommendations:")
    print("=" * 50)
    print()

    if backends["cuda"]:
        print("✓ Projects 1-85: All projects fully supported")
        print("✓ Projects 45-51: GPU programming projects will work great")
        print("✓ Projects 52-85: LLM training will be fast")
    elif backends["mps"]:
        print("✓ Projects 1-44: Fully supported")
        print("⚠️ Projects 45-51: CUDA-specific projects need CPU fallback")
        print("✓ Projects 52-85: LLM training supported (some ops may use CPU)")
    else:
        print("✓ Projects 1-44: Fully supported (slower training)")
        print("⚠️ Projects 45-51: Limited functionality (CUDA/Triton unavailable)")
        print("⚠️ Projects 52-85: LLM training will be slow")
        print()
        print("Consider:")
        print("  - Reducing batch sizes")
        print("  - Using smaller models")
        print("  - Cloud GPU instances (AWS, GCP, Colab)")

    print()

    # Next steps
    print("=" * 50)
    print("Next Steps:")
    print("=" * 50)
    print()
    print("1. Review the relevant guide:")
    if backends["cuda"]:
        print("   - GPU_GUIDE.md (NVIDIA CUDA section)")
    elif backends["mps"]:
        print("   - GPU_GUIDE.md (Apple Metal section)")
    else:
        print("   - SETUP.md (CPU optimization tips)")
    print()
    print("2. Start with Projects/01-dynamic-typing-basics/")
    print("3. Use the code example above in your projects")
    print()

    return best_backend


def run_benchmark(torch, backends):
    """Run comparative benchmark across available backends."""
    import time

    results = {}

    # CPU benchmark
    try:
        device_cpu = torch.device("cpu")
        a_cpu = torch.randn(1000, 1000, device=device_cpu)
        b_cpu = torch.randn(1000, 1000, device=device_cpu)

        # Warmup
        for _ in range(10):
            c = torch.matmul(a_cpu, b_cpu)

        # Benchmark
        start = time.time()
        for _ in range(100):
            c = torch.matmul(a_cpu, b_cpu)
        end = time.time()

        results["cpu"] = (end - start) / 100 * 1000
    except Exception as e:
        print(f"CPU benchmark failed: {e}")

    # CUDA benchmark
    if backends["cuda"]:
        try:
            device_cuda = torch.device("cuda")
            a_cuda = torch.randn(1000, 1000, device=device_cuda)
            b_cuda = torch.randn(1000, 1000, device=device_cuda)

            # Warmup
            for _ in range(10):
                c = torch.matmul(a_cuda, b_cuda)
            torch.cuda.synchronize()

            # Benchmark
            start = time.time()
            for _ in range(100):
                c = torch.matmul(a_cuda, b_cuda)
            torch.cuda.synchronize()
            end = time.time()

            results["cuda"] = (end - start) / 100 * 1000
        except Exception as e:
            print(f"CUDA benchmark failed: {e}")

    # MPS benchmark
    if backends["mps"]:
        try:
            device_mps = torch.device("mps")
            a_mps = torch.randn(1000, 1000, device=device_mps)
            b_mps = torch.randn(1000, 1000, device=device_mps)

            # Warmup
            for _ in range(10):
                c = torch.matmul(a_mps, b_mps)

            # Benchmark
            start = time.time()
            for _ in range(100):
                c = torch.matmul(a_mps, b_mps)
            end = time.time()

            results["mps"] = (end - start) / 100 * 1000
        except Exception as e:
            print(f"MPS benchmark failed: {e}")

    return results


def get_apple_chip():
    """Get the Apple chip name (M1, M2, M3, M4)."""
    try:
        import subprocess

        output = subprocess.check_output(
            ["sysctl", "-n", "machdep.cpu.brand_string"], encoding="utf-8"
        )
        return output.strip()
    except Exception:
        return "Apple Silicon"


def main():
    """Main entry point."""
    try:
        backend = detect_best_backend()
        sys.exit(0 if backend else 1)
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
