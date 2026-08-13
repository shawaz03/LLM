# 🧠 VIBE-CODER LLM — Master Context & Decisions Log
# ===================================================
# This file preserves all critical decisions and context for the project.
# Read this file at the start of every session to restore full context.
# Last updated: 2026-08-14

## PROJECT LOCATION
- Workspace: d:\LLM
- Frontend: d:\LLM\frontend (Next.js 15 + React 19 + Tailwind + Zustand)
- Backend: d:\LLM\backend (Express.js + TypeScript + Prisma + SQLite)
- Training: d:\LLM\src (Python training scripts)
- Data: d:\LLM\data
- Models: d:\LLM\models

## CONFIRMED DECISIONS
1. Base Model: Qwen/Qwen2.5-Coder-7B-Instruct (7B parameters, 4-bit QLoRA)
2. Training Method: QLoRA (4-bit quantization + LoRA adapters)
3. Target Dataset Size: 100,000 unique real coding samples (Verified: 99,992 ChatML records with 0 response hash duplicates)
4. Training Duration: 3-5 full epochs (NOT arbitrary 60-step count)
5. Max Sequence Length: 2048-4096 tokens
6. LoRA Config: r=16 (Colab default) / r=64 (AWS/Lightning AI production), alpha=32/128, dropout=0.05
7. Serving Method: Ollama / HuggingFace Inference API
8. HuggingFace Repo: shawaz03/vibe-coder-7b

## GPU & COMPUTE STRATEGY
- Primary Training: AWS $120 free credits -> g5.xlarge Spot Instance (A10G, 24GB, ~$0.40/hr = ~300 hours)
- Secondary Training: Lightning AI -> 80 free hours on A100
- Testing/Debug: Google Colab Free (T4) + Kaggle Free (T4/P100)
- Total Available: ~380+ hours of GPU time for $0

## PHASE EXECUTION PROGRESS

### Phase 0: Cleanup — ✅ COMPLETE (Audited & Verified)
- Deleted obsolete news dataset, distilgpt2 adapters, and fake loop files.
- Preserved `vibe_prompt.py`, `train_vibe_colab.ipynb`, `rag.ts`, `chat.ts`.

### Phase 1: Build Massive Real Dataset — ✅ COMPLETE (Audited & Verified)
- Step 1.1: Created automated multi-source dataset builder (`src/build_dataset.py`).
- Step 1.2 & 1.3: Integrated open-source coding datasets with strict Web-Stack filtering (React, Next.js, HTML/CSS, Node.js, Express, Prisma, TypeScript).
- Step 1.4: Injected conversational intent calibration samples (greeting & identity handling).
- Step 1.5: Injected self-healing error-fixing debug samples.
- Step 1.6: Hand-crafted high-end Vibe UI bento showcase, magnetic navbar, and pricing matrix components.
- Step 1.7: Formatted all 99,992 records into strict ChatML `<|im_start|>` / `<|im_end|>` tokens.
- Step 1.8: Automated quality validation (length check, syntax check, greeting preservation).
- Step 1.9: Response-hash deduplication (`MD5`) verified **100% unique code responses (0 duplicates)**.
- Compressed file generated: `data/vibe_training_dataset.json.gz` (17 MB compressed).

### Phase 2: Base Model Confirmation — Qwen/Qwen2.5-Coder-7B-Instruct ✅ READY

### Phase 3: Training Infrastructure Setup — ⏳ NEXT
- Set up AWS billing alerts ($100 threshold) / g5.xlarge Spot instance or Lightning AI environment.

### Phase 4: Fine-Tuning Execution — ⏳ PENDING
- Execute 4-bit QLoRA fine-tuning on GPU cloud host.

### Phase 5: Real Inference Backend — ⏳ PENDING
- Replace mock `llm.ts` with real model API client.

### Phase 6: Evaluation & Frontend Polish — ⏳ PENDING
- Benchmark evaluation and live iframe preview audit.
