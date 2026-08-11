import sys
import os

from src.data_loader import load_and_prepare_dataset
from src.embed_and_cluster import run_embedding_and_clustering
from src.train_lora_llm import train_lora_llm
from src.evaluate_and_summarize import evaluate_and_summarize_clusters

def main():
    print("\n" + "=" * 70)
    print("      END-TO-END LLM FINE-TUNING & DOCUMENT CLUSTERING PIPELINE")
    print("=" * 70 + "\n")
    
    # Step 1: Data Preparation & Token Formatting
    load_and_prepare_dataset(output_path="data/dataset.json", total_samples=4000)
    
    # Step 2 & 3: Sentence Embeddings (384D) & UMAP + K-Means Clustering
    run_embedding_and_clustering(
        dataset_path="data/dataset.json",
        embeddings_output="data/embeddings.npy",
        clusters_output="data/clusters.json",
        n_clusters=4
    )
    
    # Step 4: Parameter-Efficient LLM LoRA Fine-Tuning
    train_lora_llm(
        data_path="data/dataset.json",
        adapter_output_dir="models/lora_adapter",
        base_model_name="distilgpt2",
        epochs=1,
        batch_size=8
    )
    
    # Step 5 & 6: Evaluation Metrics, Qualitative Inspection & LLM Auto-Labeling
    evaluate_and_summarize_clusters(
        dataset_path="data/dataset.json",
        embeddings_path="data/embeddings.npy",
        clusters_path="data/clusters.json",
        adapter_dir="models/lora_adapter",
        base_model_name="distilgpt2",
        output_dir="outputs"
    )
    
    print("\n" + "=" * 70)
    print("   🎉 COMPLETE PIPELINE EXECUTION FINISHED SUCCESSFULLY! 🎉")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
