import os
import json
import numpy as np
import umap
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import normalize

def run_embedding_and_clustering(
    dataset_path="data/dataset.json",
    embeddings_output="data/embeddings.npy",
    clusters_output="data/clusters.json",
    n_clusters=4
):
    print("=" * 60)
    print("STEPS 2 & 3: Generating Dense Vector Embeddings & ML Clustering")
    print("=" * 60)
    
    # 1. Load dataset
    with open(dataset_path, "r", encoding="utf-8") as f:
        dataset = json.load(f)
        
    texts = [item["text"] for item in dataset]
    print(f"Loaded {len(texts)} documents for embedding.")
    
    # 2. STEP 2: Generate 384-dimensional dense vector embeddings
    embeddings = None
    
    try:
        print("\n[Step 2] Attempting SentenceTransformer ('all-MiniLM-L6-v2')...")
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        print("Computing 384D dense vector embeddings via Transformer...")
        embeddings = model.encode(texts, show_progress_bar=True, batch_size=64, normalize_embeddings=True)
    except Exception as e:
        print(f"\n[Note] Transformer engine fallback ({e}).")
        print("Using High-Dimensional Dense Semantic Embeddings (TF-IDF + TruncatedSVD 384D)...")
        
        tfidf = TfidfVectorizer(max_features=5000, stop_words='english', ngram_range=(1, 2))
        sparse_matrix = tfidf.fit_transform(texts)
        
        svd = TruncatedSVD(n_components=384, random_state=42)
        dense_svd = svd.fit_transform(sparse_matrix)
        embeddings = normalize(dense_svd, norm='l2')
        print(f"Generated 384D dense semantic embeddings. Explained variance ratio sum: {svd.explained_variance_ratio_.sum():.4f}")

    os.makedirs(os.path.dirname(embeddings_output), exist_ok=True)
    np.save(embeddings_output, embeddings)
    print(f"Saved {embeddings.shape} dense embeddings matrix to '{embeddings_output}'")
    
    # 3. STEP 3: UMAP Reduction & K-Means Clustering
    print("\n[Step 3] Applying UMAP Dimensionality Reduction (384D -> 5D & 2D)...")
    reducer_5d = umap.UMAP(n_components=5, n_neighbors=15, min_dist=0.1, metric='cosine', random_state=42)
    umap_5d = reducer_5d.fit_transform(embeddings)
    
    reducer_2d = umap.UMAP(n_components=2, n_neighbors=15, min_dist=0.1, metric='cosine', random_state=42)
    umap_2d = reducer_2d.fit_transform(embeddings)
    
    print(f"Running K-Means Clustering (K={n_clusters})...")
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(umap_5d)
    
    # 4. Find Top 3 Nearest Documents to Each Cluster Centroid
    centroids_5d = kmeans.cluster_centers_
    cluster_info = {}
    
    for c_id in range(n_clusters):
        cluster_indices = np.where(cluster_labels == c_id)[0]
        cluster_points_5d = umap_5d[cluster_indices]
        
        distances = euclidean_distances(cluster_points_5d, [centroids_5d[c_id]]).flatten()
        sorted_args = np.argsort(distances)
        
        closest_indices = cluster_indices[sorted_args[:3]].tolist()
        closest_docs = [dataset[i]["text"] for i in closest_indices]
        ground_truth_labels = [dataset[i]["label"] for i in cluster_indices]
        
        from collections import Counter
        top_ground_truth = Counter(ground_truth_labels).most_common(1)[0][0]
        
        cluster_info[f"Cluster_{c_id}"] = {
            "cluster_id": c_id,
            "document_count": len(cluster_indices),
            "dominant_ground_truth": top_ground_truth,
            "centroid_doc_indices": closest_indices,
            "centroid_samples": closest_docs
        }
        
    cluster_results = {
        "cluster_labels": cluster_labels.tolist(),
        "umap_2d": umap_2d.tolist(),
        "umap_5d": umap_5d.tolist(),
        "clusters_summary": cluster_info
    }
    
    with open(clusters_output, "w", encoding="utf-8") as f:
        json.dump(cluster_results, f, indent=2)
        
    print(f"\n[SUCCESS] Clustering completed. Results saved to '{clusters_output}'")
    for c_name, c_data in cluster_info.items():
        print(f"  • {c_name}: {c_data['document_count']} docs | Dominant Category: '{c_data['dominant_ground_truth']}'")
        
    return cluster_results

if __name__ == "__main__":
    run_embedding_and_clustering()
