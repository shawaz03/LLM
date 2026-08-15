"""
VIBE CODER - Phase 2: QLoRA Fine-Tuning Pipeline for AWS EC2 (NVIDIA A10G / A100)
Base Model: Qwen/Qwen2.5-Coder-7B-Instruct
Hardware Target: AWS g5.2xlarge (24GB VRAM) or p4d.24xlarge (40GB/80GB A100)
"""

import os
import sys
import gzip
import json
import torch
from datasets import Dataset

def main():
    print("=" * 70)
    print("🚀 VIBE CODER — PHASE 2: AWS EC2 QLoRA FINE-TUNING PIPELINE")
    print("=" * 70)

    # 1. GPU Check
    if not torch.cuda.is_available():
        print("❌ Error: No CUDA GPU detected! Please make sure you are on a GPU instance (e.g. g5.2xlarge).")
        sys.exit(1)

    gpu_name = torch.cuda.get_device_name(0)
    vram_gb = torch.cuda.get_device_properties(0).total_memory / (1024 ** 3)
    print(f"✅ GPU Detected: {gpu_name} ({vram_gb:.2f} GB VRAM)")

    # 2. Import Unsloth
    try:
        from unsloth import FastLanguageModel, is_bfloat16_supported
        from trl import SFTTrainer
        from transformers import TrainingArguments
    except ImportError:
        print("❌ Unsloth not installed! Run:")
        print("pip install --no-cache-dir 'unsloth[cu121-torch240] @ git+https://github.com/unslothai/unsloth.git'")
        sys.exit(1)

    # 3. Model Configuration
    max_seq_length = 2048
    dtype = None # Auto-detect (Float16 or Bfloat16)
    load_in_4bit = True # 4-bit QLoRA quantization

    print(f"\n[1/5] Loading Qwen2.5-Coder-7B-Instruct (4-bit quantized)...")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name="Qwen/Qwen2.5-Coder-7B-Instruct",
        max_seq_length=max_seq_length,
        dtype=dtype,
        load_in_4bit=load_in_4bit,
    )

    # 4. LoRA Configuration
    print("\n[2/5] Configuring LoRA Adapters...")
    model = FastLanguageModel.get_peft_model(
        model,
        r=16,
        target_modules=[
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj",
        ],
        lora_alpha=32,
        lora_dropout=0.0,
        bias="none",
        use_gradient_checkpointing="unsloth",
        random_state=3407,
        use_rslora=False,
        loftq_config=None,
    )

    # 5. Load Dataset
    data_path = "data/vibe_training_dataset.json.gz"
    if not os.path.exists(data_path):
        data_path = "data/vibe_training_dataset.json"

    print(f"\n[3/5] Loading training dataset from {data_path}...")
    if data_path.endswith(".gz"):
        with gzip.open(data_path, "rt", encoding="utf-8") as f:
            raw_data = json.load(f)
    else:
        with open(data_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

    print(f"   [+] Loaded {len(raw_data):,} verified records.")

    # Extract ChatML formatted text strings
    text_data = [{"text": record["text"]} for record in raw_data]
    dataset = Dataset.from_list(text_data)

    # 6. Trainer Setup
    print("\n[4/5] Setting up SFTTrainer with hyperparameters optimized for 24GB VRAM...")
    training_args = TrainingArguments(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        warmup_ratio=0.03,
        num_train_epochs=2,
        learning_rate=2e-4,
        fp16=not is_bfloat16_supported(),
        bf16=is_bfloat16_supported(),
        logging_steps=10,
        optim="adamw_8bit",
        weight_decay=0.01,
        lr_scheduler_type="cosine",
        seed=3407,
        output_dir="models/checkpoints",
        save_strategy="steps",
        save_steps=200,
        save_total_limit=2,
        report_to="none",
    )

    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=dataset,
        dataset_text_field="text",
        max_seq_length=max_seq_length,
        dataset_num_proc=2,
        packing=False,
        args=training_args,
    )

    # 7. Start Training
    print("\n" + "=" * 70)
    print("🔥 STARTING TRAINING RUN — MONITORING LOSS")
    print("=" * 70)
    trainer_stats = trainer.train()
    print(f"\n[SUCCESS] Training complete! Total training runtime: {trainer_stats.metrics['train_runtime']:.2f} seconds.")

    # 8. Save LoRA Adapter
    output_lora_dir = "models/vibe_coder_7b_lora"
    os.makedirs(output_lora_dir, exist_ok=True)
    print(f"\n[5/5] Saving fine-tuned LoRA adapter to {output_lora_dir}...")
    model.save_pretrained(output_lora_dir)
    tokenizer.save_pretrained(output_lora_dir)
    print(f"   [+] LoRA adapter saved successfully.")

    # 9. Optional: Export GGUF for Local Inference (Ollama / llama.cpp)
    try:
        print("\n[BONUS] Exporting quantized GGUF model for local inference...")
        model.save_pretrained_gguf("models/vibe_coder_7b_gguf", tokenizer, quantization_method="q4_k_m")
        print("   [+] GGUF model exported to models/vibe_coder_7b_gguf!")
    except Exception as e:
        print(f"   [!] GGUF export note: {e}")

    print("\n" + "=" * 70)
    print("🎉 ALL DONE! Your fine-tuned Vibe Coder 7B model is ready to deploy.")
    print("=" * 70)

if __name__ == "__main__":
    main()
