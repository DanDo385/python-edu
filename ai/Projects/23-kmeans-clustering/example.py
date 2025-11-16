"""
Example usage of K-Means Clustering implementation

This script demonstrates various features of the K-Means implementation:
- Basic clustering on synthetic data
- K-Means++ vs random initialization comparison
- Elbow method for finding optimal k
- Visualization of results

Run: python example.py
"""

import numpy as np
import matplotlib.pyplot as plt
from solution.solution import KMeans, find_optimal_k, compare_initializations


def example_1_basic_clustering():
    """Example 1: Basic K-Means clustering on synthetic data."""
    print("=" * 70)
    print("Example 1: Basic K-Means Clustering")
    print("=" * 70)

    # Generate synthetic data with 3 clear clusters
    np.random.seed(42)
    cluster1 = np.random.randn(100, 2) * 0.5 + np.array([2, 2])
    cluster2 = np.random.randn(100, 2) * 0.5 + np.array([-2, -2])
    cluster3 = np.random.randn(100, 2) * 0.5 + np.array([2, -2])
    X = np.vstack([cluster1, cluster2, cluster3])

    # Fit K-Means
    kmeans = KMeans(n_clusters=3, init='kmeans++', random_state=42)
    kmeans.fit(X)

    print(f"\nDataset: {X.shape[0]} points, {X.shape[1]} features")
    print(f"Converged in {kmeans.n_iter_} iterations")
    print(f"Final inertia: {kmeans.inertia_:.2f}")
    print(f"\nCluster Centers:")
    for i, center in enumerate(kmeans.cluster_centers_):
        print(f"  Cluster {i}: [{center[0]:6.3f}, {center[1]:6.3f}]")

    # Plot results
    fig, ax = plt.subplots(figsize=(10, 6))
    kmeans.plot_clusters(X, ax=ax, title="Example 1: Basic K-Means Clustering")
    plt.tight_layout()
    plt.savefig('example_1_basic_clustering.png', dpi=150)
    print("\nPlot saved as: example_1_basic_clustering.png")


def example_2_elbow_method():
    """Example 2: Using elbow method to find optimal k."""
    print("\n" + "=" * 70)
    print("Example 2: Elbow Method for Optimal k")
    print("=" * 70)

    # Generate data with 4 clusters
    np.random.seed(42)
    clusters = [
        np.random.randn(75, 2) * 0.6 + np.array([i * 4, j * 4])
        for i in [0, 1] for j in [0, 1]
    ]
    X = np.vstack(clusters)

    print(f"\nTesting k from 1 to 10...")

    # Find optimal k
    inertias, fig = find_optimal_k(X, k_range=range(1, 11), plot=True)

    # Print results
    print("\n  k | Inertia")
    print("  " + "-" * 25)
    for k, inertia in enumerate(inertias, start=1):
        marker = "  ← Elbow?" if k == 4 else ""
        print(f"  {k:2d} | {inertia:8.2f}{marker}")

    plt.savefig('example_2_elbow_method.png', dpi=150)
    print("\nPlot saved as: example_2_elbow_method.png")
    print("Optimal k appears to be around 4 (where curve flattens)")


def example_3_initialization_comparison():
    """Example 3: Compare random vs k-means++ initialization."""
    print("\n" + "=" * 70)
    print("Example 3: Initialization Method Comparison")
    print("=" * 70)

    # Generate data
    np.random.seed(42)
    cluster1 = np.random.randn(100, 2) * 0.8 + np.array([5, 5])
    cluster2 = np.random.randn(100, 2) * 0.8 + np.array([-5, -5])
    cluster3 = np.random.randn(100, 2) * 0.8 + np.array([5, -5])
    X = np.vstack([cluster1, cluster2, cluster3])

    print(f"\nRunning 20 trials with each initialization method...")

    # Compare methods
    results = compare_initializations(X, n_clusters=3, n_runs=20, random_state=42)

    # Calculate statistics
    random_inertias = results['random']['inertias']
    kpp_inertias = results['kmeans++']['inertias']

    print("\nRandom Initialization:")
    print(f"  Mean inertia:   {np.mean(random_inertias):8.2f}")
    print(f"  Std deviation:  {np.std(random_inertias):8.2f}")
    print(f"  Min inertia:    {np.min(random_inertias):8.2f}")
    print(f"  Max inertia:    {np.max(random_inertias):8.2f}")

    print("\nK-Means++ Initialization:")
    print(f"  Mean inertia:   {np.mean(kpp_inertias):8.2f}")
    print(f"  Std deviation:  {np.std(kpp_inertias):8.2f}")
    print(f"  Min inertia:    {np.min(kpp_inertias):8.2f}")
    print(f"  Max inertia:    {np.max(kpp_inertias):8.2f}")

    improvement = ((np.mean(random_inertias) - np.mean(kpp_inertias))
                   / np.mean(random_inertias) * 100)
    print(f"\nK-Means++ improvement: {improvement:.1f}% lower average inertia")
    print(f"K-Means++ variance reduction: {np.std(random_inertias) / np.std(kpp_inertias):.1f}x more consistent")

    # Plot comparison
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Box plot
    ax1.boxplot([random_inertias, kpp_inertias],
                labels=['Random', 'K-Means++'],
                showmeans=True)
    ax1.set_ylabel('Inertia')
    ax1.set_title('Inertia Distribution (20 runs each)')
    ax1.grid(True, alpha=0.3)

    # Histogram
    ax2.hist(random_inertias, bins=10, alpha=0.5, label='Random', color='blue')
    ax2.hist(kpp_inertias, bins=10, alpha=0.5, label='K-Means++', color='green')
    ax2.set_xlabel('Inertia')
    ax2.set_ylabel('Frequency')
    ax2.set_title('Inertia Histogram')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('example_3_initialization_comparison.png', dpi=150)
    print("\nPlot saved as: example_3_initialization_comparison.png")


def example_4_predict_new_points():
    """Example 4: Predict cluster for new data points."""
    print("\n" + "=" * 70)
    print("Example 4: Predicting New Points")
    print("=" * 70)

    # Generate training data
    np.random.seed(42)
    cluster1 = np.random.randn(50, 2) + np.array([0, 0])
    cluster2 = np.random.randn(50, 2) + np.array([10, 0])
    cluster3 = np.random.randn(50, 2) + np.array([5, 8])
    X_train = np.vstack([cluster1, cluster2, cluster3])

    # Fit model
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X_train)

    print(f"\nTrained on {X_train.shape[0]} points")
    print(f"Cluster centers:")
    for i, center in enumerate(kmeans.cluster_centers_):
        print(f"  Cluster {i}: [{center[0]:6.2f}, {center[1]:6.2f}]")

    # Predict on new points
    new_points = np.array([
        [0, 0],      # Should be cluster 0
        [10, 0],     # Should be cluster 1
        [5, 8],      # Should be cluster 2
        [-2, 2],     # Close to cluster 0
        [12, -1],    # Close to cluster 1
    ])

    predictions = kmeans.predict(new_points)

    print("\nPredictions for new points:")
    print("  Point         → Cluster")
    print("  " + "-" * 30)
    for point, label in zip(new_points, predictions):
        print(f"  [{point[0]:5.1f}, {point[1]:5.1f}] → Cluster {label}")


def example_5_convergence_analysis():
    """Example 5: Analyze convergence behavior."""
    print("\n" + "=" * 70)
    print("Example 5: Convergence Analysis")
    print("=" * 70)

    # Generate data
    np.random.seed(42)
    X = np.random.randn(200, 2)

    # Track inertia across iterations
    print("\nTracking convergence with different tolerances...")

    tolerances = [1e-1, 1e-3, 1e-5]
    results = []

    for tol in tolerances:
        kmeans = KMeans(n_clusters=3, tol=tol, max_iters=100, random_state=42)
        kmeans.fit(X)
        results.append({
            'tol': tol,
            'iterations': kmeans.n_iter_,
            'inertia': kmeans.inertia_
        })

    print("\n  Tolerance | Iterations | Final Inertia")
    print("  " + "-" * 45)
    for r in results:
        print(f"  {r['tol']:9.0e} | {r['iterations']:10d} | {r['inertia']:13.4f}")

    print("\nObservation: Tighter tolerance requires more iterations but may not")
    print("significantly improve final inertia (diminishing returns).")


def main():
    """Run all examples."""
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 15 + "K-MEANS CLUSTERING EXAMPLES" + " " * 25 + "║")
    print("╚" + "═" * 68 + "╝")
    print()

    try:
        example_1_basic_clustering()
        example_2_elbow_method()
        example_3_initialization_comparison()
        example_4_predict_new_points()
        example_5_convergence_analysis()

        print("\n" + "=" * 70)
        print("All examples completed successfully!")
        print("=" * 70)
        print("\nGenerated plots:")
        print("  - example_1_basic_clustering.png")
        print("  - example_2_elbow_method.png")
        print("  - example_3_initialization_comparison.png")
        print("\nNext steps:")
        print("  - Run tests: pytest tests/test_project_23.py -v")
        print("  - Read solution_in_words.md for detailed explanations")
        print("  - Try your own datasets!")

    except Exception as e:
        print(f"\nError: {e}")
        print("Make sure numpy and matplotlib are installed:")
        print("  pip install numpy matplotlib")


if __name__ == "__main__":
    main()
