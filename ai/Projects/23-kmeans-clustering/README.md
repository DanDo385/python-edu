# Project 23: K-Means Clustering from Scratch

## Overview

Implement the K-Means clustering algorithm from scratch using NumPy. This project covers one of the most fundamental unsupervised learning algorithms, teaching you how to discover patterns and group similar data points without labeled training data.

## Theory

### What is K-Means Clustering?

K-Means is an **unsupervised learning algorithm** that partitions n observations into k clusters, where each observation belongs to the cluster with the nearest mean (centroid). It's one of the simplest and most widely used clustering algorithms.

**Key Concepts:**

1. **Unsupervised Learning**: Learning patterns from unlabeled data
2. **Centroid**: The center point of a cluster (mean of all points in the cluster)
3. **Inertia (WCSS)**: Within-Cluster Sum of Squares - measures cluster compactness
4. **Convergence**: When centroids no longer move significantly between iterations

### The K-Means Algorithm

The algorithm follows an iterative two-step process:

```
1. Initialize: Randomly select k points as initial centroids
2. Repeat until convergence:
   a. Assignment Step: Assign each point to nearest centroid
   b. Update Step: Recalculate centroids as mean of assigned points
3. Return final clusters and centroids
```

**Mathematical Formulation:**

Given dataset X = {x₁, x₂, ..., xₙ} and k clusters:

- **Distance**: d(xᵢ, μⱼ) = ||xᵢ - μⱼ||² (Euclidean distance)
- **Assignment**: cᵢ = argmin_j ||xᵢ - μⱼ||²
- **Update**: μⱼ = (1/|Cⱼ|) Σ(xᵢ ∈ Cⱼ) xᵢ
- **Inertia**: J = Σⱼ Σ(xᵢ ∈ Cⱼ) ||xᵢ - μⱼ||²

### Initialization Strategies

1. **Random Initialization**: Randomly select k data points as initial centroids
   - Simple but may lead to poor convergence
   - Sensitive to outliers

2. **K-Means++**: Smart initialization that spreads out initial centroids
   - First centroid chosen uniformly at random
   - Subsequent centroids chosen with probability proportional to D(x)²
   - D(x) = distance to nearest already-chosen centroid
   - Provides O(log k) approximation guarantee

### Choosing K: The Elbow Method

The **elbow method** helps determine the optimal number of clusters:

1. Run K-Means for different values of k (e.g., k = 1 to 10)
2. Plot k vs. inertia (WCSS)
3. Look for the "elbow" - point where inertia decrease slows
4. The elbow point suggests optimal k

```
Inertia
   │
   │●
   │  ●
   │    ●
   │      ●──●──●──●  ← Elbow at k=4
   └────────────────── k
```

### Advantages and Limitations

**Advantages:**
- Simple and intuitive
- Fast and efficient: O(n·k·i·d) where i = iterations, d = dimensions
- Works well on spherical clusters
- Scales to large datasets

**Limitations:**
- Requires specifying k in advance
- Sensitive to initial centroid placement
- Assumes clusters are spherical and similar size
- Sensitive to outliers
- May converge to local optima
- Doesn't work well on non-convex clusters

### Distance Metrics

While Euclidean distance is standard, other metrics can be used:
- **Manhattan Distance**: L₁ norm, sum of absolute differences
- **Cosine Distance**: For high-dimensional sparse data (text)
- **Mahalanobis Distance**: Accounts for correlation between features

## Problems

### Problem 1: Core K-Means Implementation

Implement a `KMeans` class with the following functionality:

```python
class KMeans:
    """
    K-Means clustering algorithm implementation.

    Parameters
    ----------
    n_clusters : int, default=3
        Number of clusters to form
    max_iters : int, default=100
        Maximum number of iterations
    tol : float, default=1e-4
        Tolerance for convergence (centroid movement threshold)
    init : str, default='kmeans++'
        Initialization method: 'random' or 'kmeans++'
    random_state : int, optional
        Random seed for reproducibility
    """

    def fit(self, X):
        """
        Compute k-means clustering.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            Training data

        Returns
        -------
        self
        """

    def predict(self, X):
        """
        Predict cluster labels for samples.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            Data to predict

        Returns
        -------
        labels : array, shape (n_samples,)
            Cluster labels
        """

    def fit_predict(self, X):
        """Fit and predict in one step."""
```

**Requirements:**
- Store cluster centers in `self.cluster_centers_`
- Store labels in `self.labels_`
- Store inertia in `self.inertia_`
- Track number of iterations in `self.n_iter_`

### Problem 2: Distance Calculation

Implement efficient distance computation:

```python
def _compute_distances(self, X, centroids):
    """
    Compute Euclidean distances between all samples and centroids.

    Parameters
    ----------
    X : array, shape (n_samples, n_features)
    centroids : array, shape (n_clusters, n_features)

    Returns
    -------
    distances : array, shape (n_samples, n_clusters)
        Distance from each sample to each centroid
    """
```

**Hint**: Use vectorized NumPy operations for efficiency:
- ||x - c||² = ||x||² + ||c||² - 2x·c

### Problem 3: Initialization Methods

Implement both initialization strategies:

```python
def _init_centroids_random(self, X):
    """Randomly select k samples as initial centroids."""

def _init_centroids_kmeans_plus_plus(self, X):
    """
    Initialize centroids using k-means++ algorithm.

    Algorithm:
    1. Choose first centroid uniformly at random
    2. For each remaining centroid:
       a. Compute D(x)² for each point (distance to nearest centroid)
       b. Choose next centroid with probability ∝ D(x)²
    """
```

### Problem 4: Elbow Method Analysis

Implement a helper function to find optimal k:

```python
def find_optimal_k(X, k_range=range(1, 11), plot=True):
    """
    Find optimal number of clusters using elbow method.

    Parameters
    ----------
    X : array, shape (n_samples, n_features)
        Training data
    k_range : range or list
        Range of k values to test
    plot : bool
        Whether to plot the elbow curve

    Returns
    -------
    inertias : list
        Inertia values for each k
    """
```

### Problem 5: Cluster Quality Metrics

Implement inertia calculation:

```python
def _compute_inertia(self, X, labels, centroids):
    """
    Compute within-cluster sum of squares (inertia).

    Inertia = Σᵢ ||xᵢ - μ_{c(i)}||²

    Parameters
    ----------
    X : array, shape (n_samples, n_features)
    labels : array, shape (n_samples,)
    centroids : array, shape (n_clusters, n_features)

    Returns
    -------
    inertia : float
    """
```

## Applications and Use Cases

### 1. Customer Segmentation
**Problem**: Group customers by purchasing behavior
**Solution**: Cluster based on features like purchase frequency, average order value, product categories
**Impact**: Targeted marketing, personalized recommendations

### 2. Image Compression
**Problem**: Reduce image file size
**Solution**: Cluster similar colors, replace each pixel with nearest cluster center
**Impact**: Can compress 24-bit color (16M colors) to 8-bit (256 colors)

Example:
```python
# Flatten image to (n_pixels, 3) for RGB
pixels = image.reshape(-1, 3)
# Cluster into 16 colors
kmeans = KMeans(n_clusters=16)
kmeans.fit(pixels)
# Reconstruct with cluster colors
compressed = kmeans.cluster_centers_[kmeans.labels_]
compressed_image = compressed.reshape(image.shape)
```

### 3. Document Clustering
**Problem**: Organize large document collections
**Solution**: Cluster documents by TF-IDF or embedding vectors
**Impact**: Automatic topic discovery, document organization

### 4. Anomaly Detection
**Problem**: Identify unusual patterns
**Solution**: Points far from all cluster centers are anomalies
**Metric**: Use distance to nearest centroid as anomaly score

### 5. Feature Engineering
**Problem**: Create new features from existing data
**Solution**: Use cluster assignments as categorical features
**Impact**: Can improve supervised learning performance

### 6. Recommendation Systems
**Problem**: Group similar items or users
**Solution**: Cluster items by features, recommend within-cluster items
**Impact**: "Customers who liked this also liked..."

### 7. Genomics
**Problem**: Identify gene expression patterns
**Solution**: Cluster genes with similar expression profiles
**Impact**: Discover gene functions, disease subtypes

### 8. Network Security
**Problem**: Detect malicious traffic patterns
**Solution**: Cluster network behavior, flag unusual clusters
**Impact**: Intrusion detection, threat identification

## Real-World Example: Color Quantization

```python
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image
image = np.array(Image.open('photo.jpg'))
h, w, c = image.shape
pixels = image.reshape(-1, 3) / 255.0  # Normalize

# Cluster colors
kmeans = KMeans(n_clusters=16, init='kmeans++', random_state=42)
kmeans.fit(pixels)

# Reconstruct image with cluster colors
compressed_pixels = kmeans.cluster_centers_[kmeans.labels_]
compressed_image = (compressed_pixels * 255).astype(np.uint8).reshape(h, w, c)

# Compare
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.imshow(image)
ax1.set_title(f'Original ({image.nbytes / 1024:.1f} KB)')
ax2.imshow(compressed_image)
ax2.set_title(f'Compressed to {kmeans.n_clusters} colors')
plt.show()
```

## Tasks

1. **Implement Core Algorithm**
   - Complete the `KMeans` class in `solution/solution.py`
   - Implement random and k-means++ initialization
   - Add convergence detection
   - Calculate inertia

2. **Optimize Performance**
   - Use vectorized NumPy operations (no Python loops for distance calculations)
   - Implement efficient centroid updates
   - Add early stopping when converged

3. **Add Visualization**
   - Plot cluster assignments
   - Visualize centroid movement during iterations
   - Create elbow curve plots

4. **Test Thoroughly**
   - Run all tests in `tests/test_project_23.py`
   - Test edge cases (k=1, k=n_samples, empty clusters)
   - Verify convergence on different datasets

5. **Experiment**
   - Try different initialization methods
   - Compare random vs k-means++ performance
   - Test on real datasets (Iris, synthetic blobs)

## Testing

```bash
# Run all tests
pytest tests/test_project_23.py -v

# Run specific test
pytest tests/test_project_23.py::test_kmeans_basic -v

# Run with coverage
pytest tests/test_project_23.py --cov=solution --cov-report=html
```

## Hints

1. **Distance Computation**: Use `np.linalg.norm` or broadcasting for efficiency
2. **Cluster Assignment**: Use `np.argmin` to find nearest centroid
3. **Centroid Update**: Use `np.mean` with boolean indexing
4. **Empty Clusters**: Reinitialize empty cluster centroids
5. **Convergence**: Check if `np.allclose(old_centroids, new_centroids, atol=tol)`

## Expected Behavior

```python
# Example usage
from solution.solution import KMeans
import numpy as np

# Generate sample data
np.random.seed(42)
X = np.vstack([
    np.random.randn(100, 2) + [2, 2],
    np.random.randn(100, 2) + [-2, -2],
    np.random.randn(100, 2) + [2, -2]
])

# Fit K-Means
kmeans = KMeans(n_clusters=3, init='kmeans++', random_state=42)
kmeans.fit(X)

print(f"Converged in {kmeans.n_iter_} iterations")
print(f"Inertia: {kmeans.inertia_:.2f}")
print(f"Cluster centers:\n{kmeans.cluster_centers_}")

# Predict new points
new_points = np.array([[2, 2], [-2, -2]])
labels = kmeans.predict(new_points)
print(f"Predicted labels: {labels}")
```

## Further Reading

- [K-Means Clustering: Algorithm, Applications, Evaluation Methods](https://stanford.edu/~cpiech/cs221/handouts/kmeans.html)
- [Scikit-learn K-Means Documentation](https://scikit-learn.org/stable/modules/clustering.html#k-means)
- [The K-Means++ Paper (Arthur & Vassilvitskii, 2007)](http://ilpubs.stanford.edu:8090/778/1/2006-13.pdf)
- [An Introduction to Statistical Learning - Chapter 10](https://www.statlearning.com/)

## Extensions

Once you've mastered basic K-Means, try:

1. **Mini-Batch K-Means**: Use random subsets for faster training
2. **K-Medoids (PAM)**: Use actual data points as centers (robust to outliers)
3. **Silhouette Analysis**: Better cluster quality metric
4. **Fuzzy C-Means**: Soft cluster assignments with probabilities
5. **DBSCAN Comparison**: Density-based clustering for non-spherical clusters

---

**Status**: 🚀 Ready for implementation

**Difficulty**: ⭐⭐⭐ Intermediate

**Prerequisites**: NumPy basics, linear algebra fundamentals

**Time Estimate**: 4-6 hours
