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
3. Target Dataset Size: 50,000-100,000 unique real coding samples across 25 categories
4. Training Duration: 3-5 full epochs (NOT arbitrary step count)
5. Max Sequence Length: 2048-4096 tokens
6. LoRA Config: r=64, alpha=128, dropout=0.05, all attention + MLP modules
7. Serving Method: Ollama (local inference after training)
8. HuggingFace Repo: shawaz03/vibe-coder-7b

## GPU & COMPUTE STRATEGY
- Primary Training: AWS $120 free credits -> g5.xlarge Spot Instance (A10G, 24GB, ~$0.40/hr = ~300 hours)
- Secondary Training: Lightning AI -> 80 free hours on A100
- Testing/Debug: Google Colab Free (T4) + Kaggle Free (T4/P100)
- Total Available: ~380+ hours of GPU time for $0

## PHASE EXECUTION PLAN

### Phase 0: Cleanup - DELETE these broken files:
- models/lora_adapter/ (entire folder - distilgpt2 adapter)
- data/dataset.json (4,000 news articles - wrong data)
- data/vibe_coding_dataset.json (5,000 entries but only 2 unique samples copied 2500x each)
- data/embeddings.npy (news article embeddings)
- data/clusters.json (news article clusters)
- src/data_loader.py (news scraper - irrelevant)
- src/train_lora_llm.py (trains distilgpt2 on news - completely wrong)
- src/embed_and_cluster.py (news clustering - unrelated)
- src/evaluate_and_summarize.py (news evaluation - unrelated)

### Phase 0: Cleanup - KEEP these files:
- src/vibe_prompt.py (good ChatML formatting - enhance later)
- src/train_vibe_colab.ipynb (right base model - heavily modify hyperparams)
- backend/src/services/rag.ts (good RAG system)
- backend/src/routes/chat.ts (SSE streaming protocol is correct)

### Phase 1: Build Massive Real Dataset
- Step 1.1: Create new src/build_dataset.py
- Step 1.2: Download HuggingFace coding datasets
- Step 1.3: Filter and clean to web development focus
- Step 1.4: Add conversational samples
- Step 1.5: Add debugging/error-fixing samples
- Step 1.6: Hand-craft 200-500 high-quality Vibe Coder style samples
- Step 1.7: Format all into ChatML tokens
- Step 1.8: Validate quality
- Step 1.9: Deduplicate and save

### Phase 2: Base Model Confirmation - Qwen/Qwen2.5-Coder-7B-Instruct

### Phase 3: Training Infrastructure
- Set up AWS billing alerts ($100 threshold)
- Request g5.xlarge quota increase
- OR set up Lightning AI account
- Install dependencies

### Phase 4: Fine-Tuning
- Update train_vibe_colab.ipynb with correct hyperparameters
- Quick test run (1000 samples, 1 epoch) on Colab Free
- Full training (50K+ samples, 3-5 epochs) on Lightning AI or AWS
- Monitor loss curves, save best checkpoint

### Phase 5: Real Inference Backend
- Install Ollama, create Modelfile
- Replace mock llm.ts with real Ollama API calls
- Test streaming inference end-to-end

### Phase 6: Evaluation & Frontend Fixes
- Run benchmark tests
- Fix live preview iframe bugs
- Fix frontend layout issues
- Iterate

## KEY PROBLEMS DISCOVERED
1. Dataset had only 2 unique code samples repeated 2500x each
2. Local model was distilgpt2 (82M params) - cannot generate code
3. Backend llm.ts returns hardcoded template - NOT real inference
4. Colab training only ran 60 steps (saw 1.2% of data)
5. Training data was news articles, not code
6. Live preview iframe breaks on multi-line imports, missing icons, TS annotations
7. Frontend layout has grid sizing issues and empty gaps
