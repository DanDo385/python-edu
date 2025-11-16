"""
Comprehensive tests for Project 23: K-Means Clustering from Scratch

This test suite validates the K-Means implementation including:
- Core algorithm functionality
- Different initialization methods
- Edge cases and error handling
- Convergence behavior
- Inertia calculations
- Helper functions

Run with: pytest tests/test_project_23.py -v
"""

import pytest
import numpy as np
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from solution.solution import (
    KMeans,
    find_optimal_k,
    compare_initializations
)


class TestKMeansBasic:
    """Test basic K-Means functionality."""

    def test_initialization(self):
        """Test KMeans object initialization."""
        kmeans = KMeans(n_clusters=3, max_iters=100, tol=1e-4)
        assert kmeans.n_clusters == 3
        assert kmeans.max_iters == 100
        assert kmeans.tol == 1e-4
        assert kmeans.init == 'kmeans++'
        assert kmeans.cluster_centers_ is None
        assert kmeans.labels_ is None
        assert kmeans.inertia_ is None
        assert kmeans.n_iter_ is None

    def test_fit_simple_data(self):
        """Test fitting on simple 2-cluster data."""
        np.random.seed(42)

        # Create two well-separated clusters
        cluster1 = np.random.randn(50, 2) + np.array([5, 5])
        cluster2 = np.random.randn(50, 2) + np.array([-5, -5])
        X = np.vstack([cluster1, cluster2])

        kmeans = KMeans(n_clusters=2, random_state=42)
        kmeans.fit(X)

        # Check attributes are set
        assert kmeans.cluster_centers_ is not None
        assert kmeans.cluster_centers_.shape == (2, 2)
        assert kmeans.labels_ is not None
        assert len(kmeans.labels_) == 100
        assert kmeans.inertia_ is not None
        assert kmeans.inertia_ > 0
        assert kmeans.n_iter_ is not None
        assert kmeans.n_iter_ > 0

    def test_fit_predict(self):
        """Test fit_predict method."""
        np.random.seed(42)
        X = np.random.randn(100, 2)

        kmeans = KMeans(n_clusters=3, random_state=42)
        labels = kmeans.fit_predict(X)

        assert len(labels) == 100
        assert np.all((labels >= 0) & (labels < 3))
        assert np.array_equal(labels, kmeans.labels_)

    def test_predict(self):
        """Test prediction on new data."""
        np.random.seed(42)

        # Training data
        X_train = np.random.randn(100, 2)
        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans.fit(X_train)

        # New data
        X_test = np.array([[0, 0], [10, 10], [-10, -10]])
        labels = kmeans.predict(X_test)

        assert len(labels) == 3
        assert np.all((labels >= 0) & (labels < 3))

    def test_predict_before_fit_raises_error(self):
        """Test that predict raises error if called before fit."""
        kmeans = KMeans(n_clusters=3)
        X = np.random.randn(10, 2)

        with pytest.raises(ValueError, match="not been fitted"):
            kmeans.predict(X)


class TestKMeansInitialization:
    """Test different initialization methods."""

    def test_random_initialization(self):
        """Test random centroid initialization."""
        np.random.seed(42)
        X = np.random.randn(100, 2)

        kmeans = KMeans(n_clusters=3, init='random', random_state=42)
        kmeans.fit(X)

        assert kmeans.cluster_centers_.shape == (3, 2)
        assert kmeans.labels_ is not None

    def test_kmeans_plus_plus_initialization(self):
        """Test k-means++ initialization."""
        np.random.seed(42)
        X = np.random.randn(100, 2)

        kmeans = KMeans(n_clusters=3, init='kmeans++', random_state=42)
        kmeans.fit(X)

        assert kmeans.cluster_centers_.shape == (3, 2)
        assert kmeans.labels_ is not None

    def test_invalid_initialization_raises_error(self):
        """Test that invalid init parameter raises error."""
        X = np.random.randn(100, 2)
        kmeans = KMeans(n_clusters=3, init='invalid')

        with pytest.raises(ValueError, match="Invalid init method"):
            kmeans.fit(X)

    def test_kmeans_plus_plus_better_than_random(self):
        """Test that k-means++ generally gives better results than random."""
        np.random.seed(42)

        # Create data with clear clusters
        cluster1 = np.random.randn(50, 2) + np.array([5, 5])
        cluster2 = np.random.randn(50, 2) + np.array([-5, -5])
        cluster3 = np.random.randn(50, 2) + np.array([5, -5])
        X = np.vstack([cluster1, cluster2, cluster3])

        # Run multiple times
        random_inertias = []
        kpp_inertias = []

        for i in range(10):
            kmeans_random = KMeans(n_clusters=3, init='random', random_state=i)
            kmeans_random.fit(X)
            random_inertias.append(kmeans_random.inertia_)

            kmeans_kpp = KMeans(n_clusters=3, init='kmeans++', random_state=i)
            kmeans_kpp.fit(X)
            kpp_inertias.append(kmeans_kpp.inertia_)

        # K-means++ should have lower variance and generally better results
        assert np.std(kpp_inertias) <= np.std(random_inertias)


class TestKMeansConvergence:
    """Test convergence behavior."""

    def test_convergence_simple_data(self):
        """Test that algorithm converges on simple data."""
        np.random.seed(42)

        # Well-separated clusters should converge quickly
        cluster1 = np.random.randn(50, 2) + np.array([10, 10])
        cluster2 = np.random.randn(50, 2) + np.array([-10, -10])
        X = np.vstack([cluster1, cluster2])

        kmeans = KMeans(n_clusters=2, max_iters=100, random_state=42)
        kmeans.fit(X)

        # Should converge in fewer than 20 iterations for well-separated data
        assert kmeans.n_iter_ < 20

    def test_max_iterations_respected(self):
        """Test that algorithm stops at max_iters."""
        np.random.seed(42)
        X = np.random.randn(100, 2)

        max_iters = 5
        kmeans = KMeans(n_clusters=3, max_iters=max_iters, random_state=42)
        kmeans.fit(X)

        assert kmeans.n_iter_ <= max_iters

    def test_tolerance_affects_convergence(self):
        """Test that tolerance parameter affects convergence."""
        np.random.seed(42)
        X = np.random.randn(100, 2)

        # Tight tolerance - more iterations
        kmeans_tight = KMeans(n_clusters=3, tol=1e-10, random_state=42)
        kmeans_tight.fit(X)

        # Loose tolerance - fewer iterations
        kmeans_loose = KMeans(n_clusters=3, tol=1e-1, random_state=42)
        kmeans_loose.fit(X)

        assert kmeans_loose.n_iter_ <= kmeans_tight.n_iter_


class TestKMeansInertia:
    """Test inertia calculations."""

    def test_inertia_positive(self):
        """Test that inertia is always positive."""
        np.random.seed(42)
        X = np.random.randn(100, 2)

        for k in [2, 3, 5]:
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(X)
            assert kmeans.inertia_ > 0

    def test_inertia_decreases_with_iterations(self):
        """Test that inertia decreases or stays same with iterations."""
        np.random.seed(42)
        X = np.random.randn(100, 2)

        # We'll manually track inertia by fitting multiple times with increasing max_iters
        inertias = []
        for max_iters in [1, 5, 10, 20]:
            kmeans = KMeans(n_clusters=3, max_iters=max_iters, random_state=42)
            kmeans.fit(X)
            inertias.append(kmeans.inertia_)

        # Inertia should generally decrease or stay the same
        # (It's monotonically non-increasing)
        for i in range(len(inertias) - 1):
            assert inertias[i] >= inertias[i + 1] - 1e-6  # Small tolerance for numerical errors

    def test_inertia_decreases_with_more_clusters(self):
        """Test that inertia decreases as k increases."""
        np.random.seed(42)
        X = np.random.randn(100, 2)

        inertias = []
        for k in [1, 2, 3, 5, 10]:
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(X)
            inertias.append(kmeans.inertia_)

        # More clusters should have lower inertia
        for i in range(len(inertias) - 1):
            assert inertias[i] >= inertias[i + 1]

    def test_inertia_zero_when_k_equals_n(self):
        """Test that inertia is near zero when k equals n_samples."""
        np.random.seed(42)
        X = np.random.randn(10, 2)

        kmeans = KMeans(n_clusters=10, random_state=42)
        kmeans.fit(X)

        # Each point is its own cluster center, so inertia should be very small
        assert kmeans.inertia_ < 1e-10


class TestKMeansEdgeCases:
    """Test edge cases and error handling."""

    def test_k_equals_1(self):
        """Test with single cluster."""
        np.random.seed(42)
        X = np.random.randn(100, 2)

        kmeans = KMeans(n_clusters=1, random_state=42)
        kmeans.fit(X)

        assert kmeans.cluster_centers_.shape == (1, 2)
        assert np.all(kmeans.labels_ == 0)

    def test_k_equals_n_samples(self):
        """Test when k equals number of samples."""
        np.random.seed(42)
        X = np.random.randn(5, 2)

        kmeans = KMeans(n_clusters=5, random_state=42)
        kmeans.fit(X)

        assert kmeans.cluster_centers_.shape == (5, 2)
        assert len(np.unique(kmeans.labels_)) == 5

    def test_k_greater_than_n_samples_raises_error(self):
        """Test that k > n_samples raises error."""
        X = np.random.randn(5, 2)
        kmeans = KMeans(n_clusters=10)

        with pytest.raises(ValueError, match="cannot be larger"):
            kmeans.fit(X)

    def test_1d_data_raises_error(self):
        """Test that 1D data raises error."""
        X = np.random.randn(100)
        kmeans = KMeans(n_clusters=3)

        with pytest.raises(ValueError, match="must be 2D"):
            kmeans.fit(X)

    def test_single_sample(self):
        """Test with single sample."""
        X = np.array([[1, 2]])
        kmeans = KMeans(n_clusters=1, random_state=42)
        kmeans.fit(X)

        assert kmeans.cluster_centers_.shape == (1, 2)
        assert kmeans.labels_[0] == 0
        assert kmeans.inertia_ == 0

    def test_high_dimensional_data(self):
        """Test with high-dimensional data."""
        np.random.seed(42)
        X = np.random.randn(100, 50)  # 50 dimensions

        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans.fit(X)

        assert kmeans.cluster_centers_.shape == (3, 50)
        assert len(kmeans.labels_) == 100


class TestKMeansLabels:
    """Test cluster label assignments."""

    def test_all_labels_assigned(self):
        """Test that all points get a label."""
        np.random.seed(42)
        X = np.random.randn(100, 2)

        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans.fit(X)

        assert len(kmeans.labels_) == 100
        assert not np.any(np.isnan(kmeans.labels_))

    def test_labels_in_valid_range(self):
        """Test that labels are in range [0, k-1]."""
        np.random.seed(42)
        X = np.random.randn(100, 2)

        for k in [2, 3, 5]:
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(X)

            assert np.all(kmeans.labels_ >= 0)
            assert np.all(kmeans.labels_ < k)

    def test_all_clusters_used(self):
        """Test that all clusters have at least one point (for well-distributed data)."""
        np.random.seed(42)

        # Create well-separated clusters
        clusters = [
            np.random.randn(50, 2) + np.array([i * 10, i * 10])
            for i in range(3)
        ]
        X = np.vstack(clusters)

        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans.fit(X)

        # All 3 clusters should be used
        unique_labels = np.unique(kmeans.labels_)
        assert len(unique_labels) == 3


class TestKMeansReproducibility:
    """Test reproducibility with random_state."""

    def test_random_state_reproducibility(self):
        """Test that same random_state gives same results."""
        np.random.seed(42)
        X = np.random.randn(100, 2)

        kmeans1 = KMeans(n_clusters=3, random_state=42)
        kmeans1.fit(X)

        kmeans2 = KMeans(n_clusters=3, random_state=42)
        kmeans2.fit(X)

        # Results should be identical
        np.testing.assert_array_equal(kmeans1.labels_, kmeans2.labels_)
        np.testing.assert_array_almost_equal(
            kmeans1.cluster_centers_,
            kmeans2.cluster_centers_
        )
        assert abs(kmeans1.inertia_ - kmeans2.inertia_) < 1e-10

    def test_different_random_state_different_results(self):
        """Test that different random_state can give different results."""
        np.random.seed(42)
        X = np.random.randn(100, 2)

        kmeans1 = KMeans(n_clusters=3, init='random', random_state=42)
        kmeans1.fit(X)

        kmeans2 = KMeans(n_clusters=3, init='random', random_state=123)
        kmeans2.fit(X)

        # Results might be different (though could be same by chance)
        # Check that at least one of: labels, centers, or inertia differs
        labels_same = np.array_equal(kmeans1.labels_, kmeans2.labels_)
        centers_same = np.allclose(kmeans1.cluster_centers_, kmeans2.cluster_centers_)
        inertia_same = abs(kmeans1.inertia_ - kmeans2.inertia_) < 1e-10

        # At least one should be different for random init
        assert not (labels_same and centers_same and inertia_same)


class TestDistanceCalculations:
    """Test distance computation methods."""

    def test_compute_distances_shape(self):
        """Test that distance matrix has correct shape."""
        np.random.seed(42)
        X = np.random.randn(100, 2)

        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans.fit(X)  # Need to fit first to initialize centroids

        distances = kmeans._compute_distances(X, kmeans.cluster_centers_)
        assert distances.shape == (100, 3)

    def test_compute_distances_positive(self):
        """Test that all distances are non-negative."""
        np.random.seed(42)
        X = np.random.randn(100, 2)
        centroids = np.random.randn(3, 2)

        kmeans = KMeans(n_clusters=3)
        distances = kmeans._compute_distances(X, centroids)

        assert np.all(distances >= 0)

    def test_compute_distances_zero_for_same_point(self):
        """Test that distance from point to itself is zero."""
        X = np.array([[1, 2], [3, 4], [5, 6]])
        centroids = X.copy()

        kmeans = KMeans(n_clusters=3)
        distances = kmeans._compute_distances(X, centroids)

        # Diagonal should be zero (point to itself)
        np.testing.assert_array_almost_equal(np.diag(distances), [0, 0, 0])


class TestHelperFunctions:
    """Test helper functions."""

    def test_find_optimal_k(self):
        """Test find_optimal_k function."""
        np.random.seed(42)
        X = np.random.randn(100, 2)

        inertias, fig = find_optimal_k(X, k_range=range(1, 6), plot=False)

        # Should return list of inertias
        assert len(inertias) == 5

        # Inertias should decrease with k
        for i in range(len(inertias) - 1):
            assert inertias[i] >= inertias[i + 1]

    def test_find_optimal_k_with_plot(self):
        """Test find_optimal_k creates plot when requested."""
        np.random.seed(42)
        X = np.random.randn(100, 2)

        inertias, fig = find_optimal_k(X, k_range=range(1, 6), plot=True)

        assert fig is not None
        assert len(fig.axes) == 1  # Should have one axes

    def test_compare_initializations(self):
        """Test compare_initializations function."""
        np.random.seed(42)
        X = np.random.randn(100, 2)

        results = compare_initializations(
            X,
            n_clusters=3,
            n_runs=5,
            random_state=42
        )

        # Check structure
        assert 'random' in results
        assert 'kmeans++' in results
        assert 'inertias' in results['random']
        assert 'iterations' in results['random']
        assert 'inertias' in results['kmeans++']
        assert 'iterations' in results['kmeans++']

        # Check lengths
        assert len(results['random']['inertias']) == 5
        assert len(results['random']['iterations']) == 5
        assert len(results['kmeans++']['inertias']) == 5
        assert len(results['kmeans++']['iterations']) == 5


class TestRealWorldScenarios:
    """Test on realistic scenarios."""

    def test_iris_like_data(self):
        """Test on Iris-like dataset."""
        np.random.seed(42)

        # Create 3-cluster dataset similar to Iris
        cluster1 = np.random.randn(50, 4) * 0.2 + np.array([5.0, 3.5, 1.5, 0.2])
        cluster2 = np.random.randn(50, 4) * 0.4 + np.array([6.0, 2.8, 4.5, 1.5])
        cluster3 = np.random.randn(50, 4) * 0.5 + np.array([6.5, 3.0, 5.5, 2.0])

        X = np.vstack([cluster1, cluster2, cluster3])

        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans.fit(X)

        # Should identify 3 clusters
        assert len(np.unique(kmeans.labels_)) == 3

        # Most points from same original cluster should be in same predicted cluster
        # (Note: cluster IDs might be permuted)
        labels_cluster1 = kmeans.labels_[:50]
        labels_cluster2 = kmeans.labels_[50:100]
        labels_cluster3 = kmeans.labels_[100:]

        # Within each original cluster, most should have same label
        for labels in [labels_cluster1, labels_cluster2, labels_cluster3]:
            most_common = np.bincount(labels).max()
            assert most_common >= 40  # At least 80% agreement

    def test_image_compression_scenario(self):
        """Test scenario similar to image color quantization."""
        np.random.seed(42)

        # Simulate image pixels as RGB values
        n_pixels = 1000
        pixels = np.random.randint(0, 256, size=(n_pixels, 3)).astype(float)

        # Compress to 16 colors
        kmeans = KMeans(n_clusters=16, random_state=42)
        kmeans.fit(pixels)

        # All pixels should be assigned to one of 16 clusters
        assert len(np.unique(kmeans.labels_)) <= 16

        # Cluster centers should be in valid RGB range
        assert np.all(kmeans.cluster_centers_ >= 0)
        assert np.all(kmeans.cluster_centers_ <= 256)

    def test_customer_segmentation_scenario(self):
        """Test customer segmentation scenario."""
        np.random.seed(42)

        # Simulate customer features: [age, income, purchase_frequency]
        n_customers = 500

        # Segment 1: Young, low income, high frequency
        seg1 = np.random.randn(200, 3) * [5, 10000, 2] + [25, 30000, 10]

        # Segment 2: Middle-aged, high income, medium frequency
        seg2 = np.random.randn(200, 3) * [8, 20000, 3] + [45, 80000, 5]

        # Segment 3: Senior, medium income, low frequency
        seg3 = np.random.randn(100, 3) * [6, 15000, 1] + [65, 50000, 2]

        X = np.vstack([seg1, seg2, seg3])

        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans.fit(X)

        # Should find 3 segments
        assert len(np.unique(kmeans.labels_)) == 3

        # Each segment should have meaningful size
        label_counts = np.bincount(kmeans.labels_)
        assert np.all(label_counts > 50)  # Each cluster has at least 50 customers


class TestNumericalStability:
    """Test numerical stability and edge cases."""

    def test_very_small_values(self):
        """Test with very small values."""
        np.random.seed(42)
        X = np.random.randn(100, 2) * 1e-10

        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans.fit(X)

        assert not np.any(np.isnan(kmeans.cluster_centers_))
        assert not np.any(np.isinf(kmeans.cluster_centers_))
        assert not np.isnan(kmeans.inertia_)

    def test_very_large_values(self):
        """Test with very large values."""
        np.random.seed(42)
        X = np.random.randn(100, 2) * 1e10

        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans.fit(X)

        assert not np.any(np.isnan(kmeans.cluster_centers_))
        assert not np.any(np.isinf(kmeans.cluster_centers_))
        assert not np.isnan(kmeans.inertia_)

    def test_identical_points(self):
        """Test with all identical points."""
        X = np.ones((100, 2)) * 5

        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans.fit(X)

        # All centroids should be at the same location
        for i in range(3):
            np.testing.assert_array_almost_equal(
                kmeans.cluster_centers_[i],
                [5, 5]
            )

        # Inertia should be zero
        assert kmeans.inertia_ < 1e-10


# Performance benchmark (not run by default)
@pytest.mark.skip(reason="Performance benchmark - run manually")
def test_performance_benchmark():
    """Benchmark K-Means performance."""
    import time

    np.random.seed(42)

    sizes = [100, 500, 1000, 5000]
    times = []

    for size in sizes:
        X = np.random.randn(size, 10)

        start = time.time()
        kmeans = KMeans(n_clusters=5, random_state=42)
        kmeans.fit(X)
        elapsed = time.time() - start

        times.append(elapsed)
        print(f"n={size}: {elapsed:.3f}s, iterations={kmeans.n_iter_}")

    # Should scale reasonably
    assert times[-1] < times[0] * 100  # Should not be quadratic


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v", "--tb=short"])
