"""
Project 23: K-Means Clustering from Scratch

This module implements the K-Means clustering algorithm from scratch using NumPy.
K-Means is an unsupervised learning algorithm that partitions data into k clusters
by iteratively assigning points to the nearest centroid and updating centroids.

Key Concepts:
- Unsupervised learning: Finding patterns without labeled data
- Centroid: The mean position of all points in a cluster
- Inertia: Within-cluster sum of squares (WCSS) - measures cluster compactness
- K-Means++: Smart initialization for better convergence

Author: Python-Edu AI Curriculum
Date: 2025-11-16
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Literal, Optional, Tuple


class KMeans:
    """
    K-Means clustering algorithm implementation from scratch.

    K-Means partitions n observations into k clusters by minimizing the
    within-cluster sum of squares (inertia). The algorithm iterates between:
    1. Assignment step: Assign each point to nearest centroid
    2. Update step: Recalculate centroids as mean of assigned points

    Parameters
    ----------
    n_clusters : int, default=3
        The number of clusters to form (k in K-Means)

    max_iters : int, default=100
        Maximum number of iterations of the k-means algorithm

    tol : float, default=1e-4
        Relative tolerance with regards to Frobenius norm of the difference
        in the cluster centers to declare convergence

    init : {'random', 'kmeans++'}, default='kmeans++'
        Method for initialization:
        - 'random': Choose k random observations as initial centroids
        - 'kmeans++': Select centroids using k-means++ algorithm

    random_state : int, optional
        Random seed for reproducibility

    Attributes
    ----------
    cluster_centers_ : ndarray of shape (n_clusters, n_features)
        Coordinates of cluster centers

    labels_ : ndarray of shape (n_samples,)
        Labels of each point (cluster assignment)

    inertia_ : float
        Sum of squared distances of samples to their closest cluster center

    n_iter_ : int
        Number of iterations run

    Examples
    --------
    >>> import numpy as np
    >>> from solution.solution import KMeans
    >>> X = np.array([[1, 2], [1, 4], [1, 0],
    ...               [10, 2], [10, 4], [10, 0]])
    >>> kmeans = KMeans(n_clusters=2, random_state=42)
    >>> kmeans.fit(X)
    >>> kmeans.labels_
    array([0, 0, 0, 1, 1, 1])
    >>> kmeans.predict([[0, 0], [12, 3]])
    array([0, 1])
    >>> kmeans.cluster_centers_
    array([[ 1.,  2.],
           [10.,  2.]])

    Notes
    -----
    The K-Means algorithm aims to minimize the inertia (within-cluster sum-of-squares):

    .. math::
        \\sum_{i=0}^{n} \\min_{\\mu_j \\in C}(||x_i - \\mu_j||^2)

    where C is the set of cluster centers.

    K-Means++ initialization (Arthur & Vassilvitskii, 2007) provides better
    convergence guarantees than random initialization.
    """

    def __init__(
        self,
        n_clusters: int = 3,
        max_iters: int = 100,
        tol: float = 1e-4,
        init: Literal['random', 'kmeans++'] = 'kmeans++',
        random_state: Optional[int] = None
    ):
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.tol = tol
        self.init = init
        self.random_state = random_state

        # Attributes set during fitting
        self.cluster_centers_ = None
        self.labels_ = None
        self.inertia_ = None
        self.n_iter_ = None

    def fit(self, X: np.ndarray) -> 'KMeans':
        """
        Compute k-means clustering.

        Algorithm:
        1. Initialize k centroids using specified method
        2. Repeat until convergence or max iterations:
           a. Assign each point to nearest centroid
           b. Update centroids as mean of assigned points
           c. Check for convergence
        3. Compute final inertia

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training instances to cluster

        Returns
        -------
        self : KMeans
            Fitted estimator
        """
        # Set random seed for reproducibility
        if self.random_state is not None:
            np.random.seed(self.random_state)

        # Convert to numpy array and validate
        X = np.asarray(X)
        if X.ndim != 2:
            raise ValueError(f"X must be 2D array, got {X.ndim}D")

        n_samples, n_features = X.shape

        # Validate n_clusters
        if self.n_clusters > n_samples:
            raise ValueError(
                f"n_clusters ({self.n_clusters}) cannot be larger than "
                f"n_samples ({n_samples})"
            )

        # Initialize centroids
        if self.init == 'random':
            self.cluster_centers_ = self._init_centroids_random(X)
        elif self.init == 'kmeans++':
            self.cluster_centers_ = self._init_centroids_kmeans_plus_plus(X)
        else:
            raise ValueError(f"Invalid init method: {self.init}")

        # Main K-Means loop
        for iteration in range(self.max_iters):
            # Store old centroids for convergence check
            old_centroids = self.cluster_centers_.copy()

            # Assignment step: Assign each point to nearest centroid
            self.labels_ = self._assign_clusters(X, self.cluster_centers_)

            # Update step: Recalculate centroids
            self.cluster_centers_ = self._update_centroids(X, self.labels_)

            # Check for convergence
            centroid_shift = np.linalg.norm(
                self.cluster_centers_ - old_centroids,
                ord='fro'  # Frobenius norm
            )

            if centroid_shift < self.tol:
                self.n_iter_ = iteration + 1
                break
        else:
            # Max iterations reached
            self.n_iter_ = self.max_iters

        # Compute final inertia
        self.inertia_ = self._compute_inertia(X, self.labels_, self.cluster_centers_)

        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict the closest cluster each sample in X belongs to.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            New data to predict

        Returns
        -------
        labels : ndarray of shape (n_samples,)
            Index of the cluster each sample belongs to
        """
        if self.cluster_centers_ is None:
            raise ValueError("Model has not been fitted yet. Call fit() first.")

        X = np.asarray(X)
        return self._assign_clusters(X, self.cluster_centers_)

    def fit_predict(self, X: np.ndarray) -> np.ndarray:
        """
        Compute cluster centers and predict cluster index for each sample.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training instances to cluster

        Returns
        -------
        labels : ndarray of shape (n_samples,)
            Index of the cluster each sample belongs to
        """
        self.fit(X)
        return self.labels_

    def _init_centroids_random(self, X: np.ndarray) -> np.ndarray:
        """
        Initialize centroids by randomly selecting k samples from X.

        This is the simplest initialization method but can lead to poor
        convergence if unlucky with the random selection.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            Training data

        Returns
        -------
        centroids : ndarray of shape (n_clusters, n_features)
            Initial centroid positions
        """
        n_samples = X.shape[0]
        # Randomly choose k samples without replacement
        indices = np.random.choice(n_samples, size=self.n_clusters, replace=False)
        return X[indices].copy()

    def _init_centroids_kmeans_plus_plus(self, X: np.ndarray) -> np.ndarray:
        """
        Initialize centroids using k-means++ algorithm.

        K-Means++ (Arthur & Vassilvitskii, 2007) carefully seeds the initial
        centroids to be far apart, leading to better and more consistent results.

        Algorithm:
        1. Choose first centroid uniformly at random from X
        2. For each remaining centroid:
           a. Compute D(x)² for each point x (distance to nearest centroid)
           b. Choose next centroid with probability proportional to D(x)²

        This ensures centroids are spread out, providing O(log k) approximation
        guarantee to optimal clustering.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            Training data

        Returns
        -------
        centroids : ndarray of shape (n_clusters, n_features)
            Initial centroid positions
        """
        n_samples, n_features = X.shape
        centroids = np.zeros((self.n_clusters, n_features))

        # Step 1: Choose first centroid uniformly at random
        first_idx = np.random.randint(n_samples)
        centroids[0] = X[first_idx]

        # Step 2: Choose remaining centroids
        for k in range(1, self.n_clusters):
            # Compute distance from each point to nearest existing centroid
            distances = self._compute_distances(X, centroids[:k])
            min_distances = np.min(distances, axis=1)

            # Square the distances (D(x)²)
            squared_distances = min_distances ** 2

            # Choose next centroid with probability proportional to D(x)²
            probabilities = squared_distances / squared_distances.sum()
            next_idx = np.random.choice(n_samples, p=probabilities)
            centroids[k] = X[next_idx]

        return centroids

    def _compute_distances(
        self,
        X: np.ndarray,
        centroids: np.ndarray
    ) -> np.ndarray:
        """
        Compute Euclidean distances between all samples and centroids.

        Uses the efficient formula: ||x - c||² = ||x||² + ||c||² - 2x·c
        This avoids explicit computation of all pairwise differences.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            Data points
        centroids : ndarray of shape (n_centroids, n_features)
            Centroid positions

        Returns
        -------
        distances : ndarray of shape (n_samples, n_centroids)
            Euclidean distance from each sample to each centroid
        """
        # Compute ||x||² for each sample (n_samples,)
        x_squared = np.sum(X ** 2, axis=1, keepdims=True)

        # Compute ||c||² for each centroid (n_centroids,)
        c_squared = np.sum(centroids ** 2, axis=1, keepdims=True).T

        # Compute -2x·c (n_samples, n_centroids)
        cross_term = -2 * np.dot(X, centroids.T)

        # Combine: ||x - c||² = ||x||² + ||c||² - 2x·c
        distances_squared = x_squared + c_squared + cross_term

        # Handle numerical errors (tiny negative values)
        distances_squared = np.maximum(distances_squared, 0)

        return np.sqrt(distances_squared)

    def _assign_clusters(
        self,
        X: np.ndarray,
        centroids: np.ndarray
    ) -> np.ndarray:
        """
        Assign each sample to the nearest centroid.

        This is the "assignment step" in the K-Means algorithm.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            Data points
        centroids : ndarray of shape (n_clusters, n_features)
            Current centroid positions

        Returns
        -------
        labels : ndarray of shape (n_samples,)
            Cluster assignment for each sample (0 to n_clusters-1)
        """
        # Compute distances to all centroids
        distances = self._compute_distances(X, centroids)

        # Assign to nearest centroid
        return np.argmin(distances, axis=1)

    def _update_centroids(
        self,
        X: np.ndarray,
        labels: np.ndarray
    ) -> np.ndarray:
        """
        Update centroids as the mean of all points assigned to each cluster.

        This is the "update step" in the K-Means algorithm.

        If a cluster becomes empty, we reinitialize its centroid to a random
        point from X to avoid numerical issues.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            Data points
        labels : ndarray of shape (n_samples,)
            Current cluster assignments

        Returns
        -------
        new_centroids : ndarray of shape (n_clusters, n_features)
            Updated centroid positions
        """
        n_features = X.shape[1]
        new_centroids = np.zeros((self.n_clusters, n_features))

        for k in range(self.n_clusters):
            # Find all points assigned to cluster k
            cluster_mask = (labels == k)

            if np.any(cluster_mask):
                # Compute mean of all points in cluster
                new_centroids[k] = np.mean(X[cluster_mask], axis=0)
            else:
                # Empty cluster: reinitialize to random point
                # This can happen with poor initialization or outliers
                random_idx = np.random.randint(X.shape[0])
                new_centroids[k] = X[random_idx]

        return new_centroids

    def _compute_inertia(
        self,
        X: np.ndarray,
        labels: np.ndarray,
        centroids: np.ndarray
    ) -> float:
        """
        Compute within-cluster sum of squares (inertia/WCSS).

        Inertia measures how tight the clusters are. Lower is better.

        Formula: Σᵢ ||xᵢ - μ_{c(i)}||²

        where c(i) is the cluster assignment for point i.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            Data points
        labels : ndarray of shape (n_samples,)
            Cluster assignments
        centroids : ndarray of shape (n_clusters, n_features)
            Cluster centers

        Returns
        -------
        inertia : float
            Sum of squared distances to nearest centroid
        """
        inertia = 0.0

        for k in range(self.n_clusters):
            # Get all points in cluster k
            cluster_mask = (labels == k)
            cluster_points = X[cluster_mask]

            if len(cluster_points) > 0:
                # Compute squared distances to centroid
                diff = cluster_points - centroids[k]
                squared_distances = np.sum(diff ** 2, axis=1)
                inertia += np.sum(squared_distances)

        return inertia

    def plot_clusters(
        self,
        X: np.ndarray,
        ax: Optional[plt.Axes] = None,
        show_centroids: bool = True,
        title: str = "K-Means Clustering"
    ) -> plt.Axes:
        """
        Visualize clustering results (for 2D data only).

        Parameters
        ----------
        X : ndarray of shape (n_samples, 2)
            Data points (must be 2D)
        ax : matplotlib Axes, optional
            Axes to plot on. If None, creates new figure
        show_centroids : bool, default=True
            Whether to show centroid positions
        title : str
            Plot title

        Returns
        -------
        ax : matplotlib Axes
            The axes with the plot
        """
        if X.shape[1] != 2:
            raise ValueError("Can only plot 2D data")

        if self.labels_ is None:
            raise ValueError("Model must be fitted before plotting")

        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 6))

        # Plot each cluster with different color
        scatter = ax.scatter(
            X[:, 0],
            X[:, 1],
            c=self.labels_,
            cmap='viridis',
            alpha=0.6,
            edgecolors='black',
            linewidth=0.5
        )

        if show_centroids:
            # Plot centroids as red X's
            ax.scatter(
                self.cluster_centers_[:, 0],
                self.cluster_centers_[:, 1],
                c='red',
                marker='X',
                s=200,
                edgecolors='black',
                linewidth=2,
                label='Centroids'
            )
            ax.legend()

        ax.set_title(f"{title}\n(Inertia: {self.inertia_:.2f}, Iterations: {self.n_iter_})")
        ax.set_xlabel("Feature 1")
        ax.set_ylabel("Feature 2")
        plt.colorbar(scatter, ax=ax, label='Cluster')

        return ax


def find_optimal_k(
    X: np.ndarray,
    k_range: range = range(1, 11),
    init: str = 'kmeans++',
    random_state: Optional[int] = None,
    plot: bool = True
) -> Tuple[list, Optional[plt.Figure]]:
    """
    Find optimal number of clusters using the elbow method.

    The elbow method plots inertia vs. number of clusters. The "elbow" point
    where inertia decrease slows indicates a good choice for k.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        Training data
    k_range : range or list, default=range(1, 11)
        Range of k values to test
    init : str, default='kmeans++'
        Initialization method
    random_state : int, optional
        Random seed for reproducibility
    plot : bool, default=True
        Whether to create elbow plot

    Returns
    -------
    inertias : list
        Inertia values for each k
    fig : matplotlib Figure or None
        Figure object if plot=True, else None

    Examples
    --------
    >>> X = np.random.randn(300, 2)
    >>> inertias, fig = find_optimal_k(X, k_range=range(1, 10))
    >>> # Look for elbow in the plot
    """
    inertias = []

    for k in k_range:
        kmeans = KMeans(
            n_clusters=k,
            init=init,
            random_state=random_state
        )
        kmeans.fit(X)
        inertias.append(kmeans.inertia_)

    fig = None
    if plot:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(list(k_range), inertias, 'bo-', linewidth=2, markersize=8)
        ax.set_xlabel('Number of Clusters (k)', fontsize=12)
        ax.set_ylabel('Inertia (Within-Cluster Sum of Squares)', fontsize=12)
        ax.set_title('Elbow Method for Optimal k', fontsize=14)
        ax.grid(True, alpha=0.3)

        # Annotate each point
        for k, inertia in zip(k_range, inertias):
            ax.annotate(
                f'{inertia:.1f}',
                xy=(k, inertia),
                xytext=(5, 5),
                textcoords='offset points',
                fontsize=9
            )

        plt.tight_layout()

    return inertias, fig


def compare_initializations(
    X: np.ndarray,
    n_clusters: int = 3,
    n_runs: int = 10,
    random_state: Optional[int] = None
) -> dict:
    """
    Compare random vs k-means++ initialization.

    Runs K-Means multiple times with each initialization method and
    compares convergence speed and final inertia.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        Training data
    n_clusters : int, default=3
        Number of clusters
    n_runs : int, default=10
        Number of runs for each method
    random_state : int, optional
        Base random seed

    Returns
    -------
    results : dict
        Dictionary with statistics for each method:
        - 'random': {'inertias': [...], 'iterations': [...]}
        - 'kmeans++': {'inertias': [...], 'iterations': [...]}

    Examples
    --------
    >>> X = np.random.randn(300, 2)
    >>> results = compare_initializations(X, n_clusters=3, n_runs=5)
    >>> print(f"Random avg inertia: {np.mean(results['random']['inertias']):.2f}")
    >>> print(f"K-Means++ avg inertia: {np.mean(results['kmeans++']['inertias']):.2f}")
    """
    results = {
        'random': {'inertias': [], 'iterations': []},
        'kmeans++': {'inertias': [], 'iterations': []}
    }

    for i in range(n_runs):
        seed = random_state + i if random_state is not None else None

        # Random initialization
        kmeans_random = KMeans(
            n_clusters=n_clusters,
            init='random',
            random_state=seed
        )
        kmeans_random.fit(X)
        results['random']['inertias'].append(kmeans_random.inertia_)
        results['random']['iterations'].append(kmeans_random.n_iter_)

        # K-Means++ initialization
        kmeans_pp = KMeans(
            n_clusters=n_clusters,
            init='kmeans++',
            random_state=seed
        )
        kmeans_pp.fit(X)
        results['kmeans++']['inertias'].append(kmeans_pp.inertia_)
        results['kmeans++']['iterations'].append(kmeans_pp.n_iter_)

    return results


# Example usage and demonstrations
if __name__ == "__main__":
    # Set random seed for reproducibility
    np.random.seed(42)

    print("=" * 70)
    print("K-Means Clustering from Scratch - Demonstration")
    print("=" * 70)

    # Generate synthetic data: 3 well-separated clusters
    print("\n1. Generating synthetic data (3 clusters)...")
    n_samples_per_cluster = 100

    cluster_1 = np.random.randn(n_samples_per_cluster, 2) + np.array([2, 2])
    cluster_2 = np.random.randn(n_samples_per_cluster, 2) + np.array([-2, -2])
    cluster_3 = np.random.randn(n_samples_per_cluster, 2) + np.array([2, -2])

    X = np.vstack([cluster_1, cluster_2, cluster_3])
    print(f"Generated {X.shape[0]} points with {X.shape[1]} features")

    # Fit K-Means with k-means++ initialization
    print("\n2. Fitting K-Means (k=3, k-means++ initialization)...")
    kmeans = KMeans(n_clusters=3, init='kmeans++', random_state=42)
    kmeans.fit(X)

    print(f"   Converged in {kmeans.n_iter_} iterations")
    print(f"   Final inertia: {kmeans.inertia_:.2f}")
    print(f"\n   Cluster centers:")
    for i, center in enumerate(kmeans.cluster_centers_):
        print(f"   Cluster {i}: [{center[0]:.3f}, {center[1]:.3f}]")

    # Predict on new points
    print("\n3. Predicting cluster for new points...")
    new_points = np.array([[2, 2], [-2, -2], [2, -2], [0, 0]])
    predictions = kmeans.predict(new_points)
    print("   Points → Predicted Clusters:")
    for point, label in zip(new_points, predictions):
        print(f"   {point} → Cluster {label}")

    # Elbow method
    print("\n4. Finding optimal k using elbow method...")
    inertias, _ = find_optimal_k(X, k_range=range(1, 8), plot=False)
    print("   k | Inertia")
    print("   " + "-" * 20)
    for k, inertia in enumerate(inertias, start=1):
        print(f"   {k} | {inertia:7.2f}")

    # Compare initializations
    print("\n5. Comparing initialization methods (10 runs each)...")
    results = compare_initializations(X, n_clusters=3, n_runs=10, random_state=42)

    random_avg_inertia = np.mean(results['random']['inertias'])
    random_avg_iters = np.mean(results['random']['iterations'])
    kpp_avg_inertia = np.mean(results['kmeans++']['inertias'])
    kpp_avg_iters = np.mean(results['kmeans++']['iterations'])

    print(f"\n   Random Initialization:")
    print(f"   - Average inertia: {random_avg_inertia:.2f}")
    print(f"   - Average iterations: {random_avg_iters:.1f}")
    print(f"   - Std inertia: {np.std(results['random']['inertias']):.2f}")

    print(f"\n   K-Means++ Initialization:")
    print(f"   - Average inertia: {kpp_avg_inertia:.2f}")
    print(f"   - Average iterations: {kpp_avg_iters:.1f}")
    print(f"   - Std inertia: {np.std(results['kmeans++']['inertias']):.2f}")

    improvement = ((random_avg_inertia - kpp_avg_inertia) / random_avg_inertia) * 100
    print(f"\n   K-Means++ improvement: {improvement:.1f}% lower inertia")

    print("\n" + "=" * 70)
    print("Demonstration complete!")
    print("=" * 70)
