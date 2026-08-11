# 🚀 End-to-End LLM Fine-Tuning & Document Clustering System

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-orange.svg)](https://pytorch.org/)
[![HuggingFace PEFT](https://img.shields.io/badge/HuggingFace-PEFT%2FLoRA-yellow.svg)](https://huggingface.co/)
[![UMAP](https://img.shields.io/badge/UMAP-Dimensionality%20Reduction-green.svg)](https://umap-learn.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

An end-to-end Machine Learning, Deep Learning, Artificial Neural Network (ANN), and Large Language Model (LLM) pipeline that combines **dense vector embeddings**, **unsupervised UMAP + K-Means clustering**, and **parameter-efficient LoRA LLM fine-tuning** to automatically cluster, evaluate, and topic-label document corpora.

---

## 📌 System Architecture

```
[ Raw Text Corpus (4,000 Articles across 4 Domains) ]
                         │
                         ▼
[ 384-Dimensional Dense Vector Embedding Space ] ◄── Bi-Encoder / Dense Embeddings
                         │
                         ▼
[ UMAP Dimensionality Reduction: 384D ──► 5D / 2D ]
                         │
                         ▼
[ Unsupervised K-Means Clustering (K=4) & Centroid Extraction ]
                         │
                         ▼
[ Parameter-Efficient LoRA LLM (q_proj, v_proj Adapters) ] ◄── Fine-Tuned LLM
                         │
                         ▼
[ Empirical Metric Evaluation & 2D Cluster Visualization Plot ]
```

---

## 🛠️ Step-by-Step Pipeline

| Step | Script File | Description | Primary Domain |
| :--- | :--- | :--- | :--- |
| **Step 1** | `src/data_loader.py` | Downloads & prepares 4,000 documents + instruction prompt pairs + web scraper utility. | Data Prep & AI |
| **Step 2** | `src/embed_and_cluster.py` | Generates 384D dense semantic vector embeddings. | DL / ANN Vectors |
| **Step 3** | `src/embed_and_cluster.py` | Performs UMAP reduction (384D $\rightarrow$ 5D/2D) and K-Means ($K=4$) clustering. | Unsupervised ML |
| **Step 4** | `src/train_lora_llm.py` | Parameter-efficient fine-tuning (LoRA) of Causal LLM (`distilgpt2` / `Qwen2.5-0.5B`). | DL / ANN / LLM |
| **Step 5** | `src/evaluate_and_summarize.py` | Computes Silhouette Score, Calinski-Harabasz Index, and extracts centroid document samples. | ML Evaluation |
| **Step 6** | `main.py` | Auto-labels cluster topics with fine-tuned LLM and exports 2D UMAP scatter plot (`outputs/cluster_visualization.png`). | Full AI System |

---

## 📊 Empirical Results & Metrics

* **Silhouette Score (Compactness & Separation)**: `0.7823` (High cluster separation in vector space)
* **Calinski-Harabasz Index**: `2819.32`

### Cluster Inspection & Auto-Generated Topic Labels:

- **Cluster 0** (3,527 Docs): `Topic: Technology` (Dominant Ground Truth: *Technology*)
- **Cluster 1** (126 Docs): `Topic: Sports` (Dominant Ground Truth: *Sports*)
- **Cluster 2** (221 Docs): `Topic: Science` (Dominant Ground Truth: *Science*)
- **Cluster 3** (126 Docs): `Topic: Politics/World` (Dominant Ground Truth: *Politics/World*)

---

## 🚀 Quickstart Guide

### 1. Clone Repository & Install Dependencies
```bash
git clone https://github.com/shawaz03/LLM.git
cd LLM
python -m pip install -r requirements.txt
```

### 2. Run Complete Pipeline
```bash
python main.py
```

### 3. Individual Step Execution
```bash
# Step 1: Prepare Dataset
python src/data_loader.py

# Steps 2 & 3: Embeddings & Clustering
python src/embed_and_cluster.py

# Step 4: LoRA Fine-Tuning
python src/train_lora_llm.py

# Steps 5 & 6: Evaluation & Plot Generation
python src/evaluate_and_summarize.py
```

---

## 📁 Repository Structure

```
.
├── NIPS-2017-attention-is-all-you-need-Paper.pdf  # Foundational Transformer paper
├── requirements.txt                                # Python dependencies
├── data/
│   ├── dataset.json                                # 4,000 document dataset & instruction prompts
│   ├── embeddings.npy                              # (4000, 384) dense vector matrix
│   └── clusters.json                               # UMAP projections & cluster centroids
├── models/
│   └── lora_adapter/                               # LoRA fine-tuned adapter config & weights
├── outputs/
│   ├── cluster_evaluation.json                     # Empirical evaluation report
│   └── cluster_visualization.png                   # 2D UMAP cluster scatter plot
├── src/
│   ├── __init__.py
│   ├── data_loader.py                              # Data fetcher & web scraper
│   ├── embed_and_cluster.py                        # Dense vector generator & UMAP clustering
│   ├── train_lora_llm.py                           # LoRA fine-tuning script
│   └── evaluate_and_summarize.py                   # Cluster evaluation & plot generator
└── main.py                                         # End-to-end pipeline orchestrator
```

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
