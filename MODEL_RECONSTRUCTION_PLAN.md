# 🏗️ Complete Model Reconstruction Plan — Vibe-Coder LLM

> **Goal**: Build a properly trained, fine-tuned code generation LLM from scratch with a massive dataset, proper training, and real inference serving.

---

## ⚠️ Honest Reality Check First

Before we start, let me be completely transparent about what's achievable:

| Model | Parameters | Training Data | Training Compute | Cost |
|---|---|---|---|---|
| Claude Sonnet 4.6 | ~200B+ (estimated) | Trillions of tokens | Thousands of A100 GPUs for months | $100M+ |
| Gemini 3.1 Flash | ~100B+ (estimated) | Trillions of tokens | Thousands of TPUs for months | $50M+ |
| **What you can build** | **7B-32B** | **50K-200K high-quality samples** | **1 GPU for hours/days** | **$0-$50** |

> [!IMPORTANT]
> You **cannot** match Sonnet or Gemini quality with fine-tuning alone — those are foundation models trained from scratch on trillions of tokens with massive compute. **BUT** — you CAN build a model that is **excellent at your specific domain** (full-stack web development) by fine-tuning a strong open-source base model. A well-fine-tuned 7B model can outperform GPT-4 **on your specific task** if trained on the right data.

**What you'll achieve**: A code generation model that produces **high-quality, complete, runnable** Next.js/React/Node.js code components — better than the base model at your specific coding style.

---

## 🗑️ Phase 0: Cleanup — Remove What's Broken

Before building anything new, we need to clean out the broken pieces.

### Step 0.1: Delete the Wrong Local Model & Dataset

These files are actively hurting your project:

| File | Problem | Action |
|---|---|---|
| [`models/lora_adapter/adapter_config.json`](file:///d:/LLM/models/lora_adapter/adapter_config.json) | Points to `distilgpt2` — a text model that can't generate code | **DELETE** entire `models/lora_adapter/` folder |
| [`data/dataset.json`](file:///d:/LLM/data/dataset.json) | 4,000 **news articles** — wrong data for code generation | **DELETE** |
| [`src/data_loader.py`](file:///d:/LLM/src/data_loader.py) | Scrapes news articles & 20Newsgroups — irrelevant | **DELETE** |
| [`src/train_lora_llm.py`](file:///d:/LLM/src/train_lora_llm.py) | Trains distilgpt2 on news data — completely wrong pipeline | **DELETE** |
| [`data/embeddings.npy`](file:///d:/LLM/data/embeddings.npy) | Embedding vectors for news articles | **DELETE** |
| [`data/clusters.json`](file:///d:/LLM/data/clusters.json) | Cluster data for news articles | **DELETE** |
| [`src/embed_and_cluster.py`](file:///d:/LLM/src/embed_and_cluster.py) | News clustering pipeline — unrelated to code gen | **DELETE** |
| [`src/evaluate_and_summarize.py`](file:///d:/LLM/src/evaluate_and_summarize.py) | News evaluation metrics — unrelated | **DELETE** |

### Step 0.2: Delete the Fake Dataset

> [!CAUTION]
> **This is the biggest problem in your project.** Your [`prepare_vibe_dataset.py`](file:///d:/LLM/src/prepare_vibe_dataset.py) generates 5,000 "samples" but it only contains **2 actual code examples** that are **copied 2,500 times each**:
> ```python
> for i in range(total_samples):  # 5000 iterations
>     sample = high_end_samples[i % len(high_end_samples)]  # Only 2 samples!
> ```
> The model sees the EXACT SAME 2 components over and over. This teaches the model to **memorize** 2 templates, not to **generate** new code. This is why every output looks identical.

| File | Problem | Action |
|---|---|---|
| [`data/vibe_coding_dataset.json`](file:///d:/LLM/data/vibe_coding_dataset.json) | 5,000 entries but only **2 unique examples** repeated | **DELETE** — rebuild from scratch |
| [`src/prepare_vibe_dataset.py`](file:///d:/LLM/src/prepare_vibe_dataset.py) | Generator that copies 2 samples 2500x each | **REWRITE** completely |

### Step 0.3: Keep These Files (They Have Good Bones)

| File | Status | Notes |
|---|---|---|
| [`src/vibe_prompt.py`](file:///d:/LLM/src/vibe_prompt.py) | ✅ Keep & enhance | Good ChatML formatting, needs more prompt types |
| [`src/train_vibe_colab.ipynb`](file:///d:/LLM/src/train_vibe_colab.ipynb) | ✅ Keep & heavily modify | Right base model, but needs proper hyperparameters |
| [`backend/src/services/rag.ts`](file:///d:/LLM/backend/src/services/rag.ts) | ✅ Keep | Good RAG retrieval system |
| [`backend/src/routes/chat.ts`](file:///d:/LLM/backend/src/routes/chat.ts) | ✅ Keep & modify | SSE streaming protocol is correct |

---

## 📊 Phase 1: Build a Massive, Real Dataset (Most Important Phase)

> [!IMPORTANT]
> **Data quality is 80% of model quality.** A mediocre model on great data beats a great model on bad data. This is the most time-consuming but most important phase.

### Step 1.1: Understand the Dataset Format

Every training sample must follow this ChatML structure:
```
<|im_start|>system
{system_prompt}
<|im_end|>
<|im_start|>user
{user_instruction}
<|im_end|>
<|im_start|>assistant
{complete_code_response}
<|im_end|>
```

### Step 1.2: Define the 25 Task Categories

Your dataset needs to cover the **full breadth** of what a full-stack developer asks an LLM:

| # | Category | Example Prompt | Example Response Type |
|---|---|---|---|
| 1 | `react_component` | "Create a responsive navbar with dropdown" | Complete React component |
| 2 | `nextjs_page` | "Build a dashboard page with charts" | Next.js page.tsx |
| 3 | `html_css_vanilla` | "Create a registration form in HTML" | Pure HTML + CSS |
| 4 | `tailwind_ui` | "Design a pricing card with Tailwind" | Tailwind-styled component |
| 5 | `api_route` | "Create a REST API for user CRUD" | Express/Next.js API route |
| 6 | `database_schema` | "Design a schema for an e-commerce app" | Prisma/SQL schema |
| 7 | `authentication` | "Implement JWT login system" | Auth middleware + routes |
| 8 | `form_handling` | "Build a multi-step form with validation" | Form component with state |
| 9 | `animation_gsap` | "Animate a hero section on scroll" | GSAP ScrollTrigger code |
| 10 | `animation_framer` | "Add page transitions with Framer Motion" | Framer Motion component |
| 11 | `data_fetching` | "Fetch and display posts from an API" | useEffect/SWR/React Query |
| 12 | `state_management` | "Create a shopping cart with Zustand" | Zustand store + component |
| 13 | `typescript_types` | "Define types for a blog platform" | TS interfaces and types |
| 14 | `testing` | "Write unit tests for a calculator" | Jest/Vitest test file |
| 15 | `debugging` | "Fix this error: Cannot read property..." | Debugged corrected code |
| 16 | `refactoring` | "Refactor this class component to hooks" | Refactored clean code |
| 17 | `landing_page` | "Build a SaaS landing page" | Full page component |
| 18 | `dashboard` | "Create an admin dashboard layout" | Dashboard with sidebar |
| 19 | `mobile_responsive` | "Make this component mobile responsive" | Responsive CSS/Tailwind |
| 20 | `chat_interface` | "Build a real-time chat UI" | WebSocket chat component |
| 21 | `file_upload` | "Create a drag-and-drop file uploader" | Upload component |
| 22 | `data_visualization` | "Build a bar chart component" | Chart component |
| 23 | `conversation` | "Hi, how are you?" | Friendly conversational reply (NOT code) |
| 24 | `explanation` | "Explain how React hooks work" | Educational explanation |
| 25 | `css_layout` | "Create a masonry grid layout" | Pure CSS grid code |

### Step 1.3: Collect Real Data from Open-Source Sources

You need **50,000+ unique, real** code samples. Here's where to get them:

#### Source A: HuggingFace Datasets (Free, Instant)
```python
# These datasets contain millions of real coding instruction-response pairs
datasets_to_download = [
    "bigcode/the-stack-v2-dedup",          # 619M+ code files from GitHub
    "sahil2801/CodeAlpaca-20k",             # 20K coding instruction pairs
    "TokenBender/code_instructions_122k",   # 122K code instructions
    "iamtarun/python_code_instructions_18k",# 18K Python code samples
    "nickrosh/Evol-Instruct-Code-80k",      # 80K evolved code instructions
    "codeparrot/github-code-clean",         # Clean GitHub code
    "HuggingFaceH4/CodeAlpaca_20K",         # 20K ChatGPT code instructions
    "ajibawa-2023/Code-290k-ShareGPT",      # 290K code conversations
]
```

#### Source B: Generate Synthetic Data Using a Strong Model
Use Claude, GPT-4, or Gemini API to generate high-quality training pairs:
```python
# Prompt a strong model to generate training data
prompt = """Generate a coding task and complete solution:
- Task: A realistic web development request a user would make
- Solution: Complete, runnable code with no placeholders
- Framework: React/Next.js/Express/HTML (vary each time)
- Quality: Production-grade, well-commented code
"""
```

#### Source C: Curate Real GitHub Projects
Extract high-quality components from popular open-source repos:
- Shadcn UI components
- Radix UI examples
- Next.js official examples
- Tailwind UI patterns

### Step 1.4: Build the Dataset Generator Script

Create a new [`src/build_dataset.py`](file:///d:/LLM/src/build_dataset.py) that:

```python
# Pseudocode for the new dataset builder
def build_training_dataset():
    all_samples = []
    
    # 1. Download & filter HuggingFace datasets
    hf_samples = download_and_filter_hf_datasets()      # ~30K samples
    
    # 2. Generate synthetic samples via API
    synthetic_samples = generate_synthetic_samples()      # ~10K samples
    
    # 3. Hand-craft high-quality reference samples
    handcrafted_samples = load_handcrafted_samples()      # ~500 samples
    
    # 4. Add conversational samples (greetings, explanations)
    conversation_samples = create_conversation_samples()  # ~2K samples
    
    # 5. Combine, deduplicate, validate
    all_samples = hf_samples + synthetic_samples + handcrafted_samples + conversation_samples
    all_samples = deduplicate(all_samples)
    all_samples = validate_code_quality(all_samples)
    
    # 6. Format into ChatML
    formatted = [format_to_chatml(s) for s in all_samples]
    
    # 7. Save
    save_dataset(formatted, "data/vibe_training_dataset.json")
```

### Step 1.5: Dataset Quality Rules

Every sample MUST pass these quality checks:

| Rule | Why |
|---|---|
| **Min 200 tokens** response length | Short responses teach lazy generation |
| **Max 4096 tokens** total (prompt + response) | Fits in context window during training |
| **No TODO/placeholder** comments | Model should never learn to output placeholders |
| **Code must be syntactically valid** | Validate with AST parsers |
| **Diverse instructions** — no duplicates | Prevents memorization (your current problem) |
| **Include non-code samples** (5-10%) | Teaches model when NOT to generate code |
| **Include error-fixing samples** (10%) | Teaches debugging capabilities |
| **Balance categories** | ~2000 samples per category minimum |

### Step 1.6: Target Dataset Size

| Dataset Quality Level | Samples | Training Time (T4 GPU) | Expected Quality |
|---|---|---|---|
| Minimum Viable | 10,000 | 2-4 hours | Basic code generation |
| Good | 50,000 | 8-16 hours | Solid full-stack assistant |
| **Recommended** | **100,000** | **24-48 hours** | **Professional quality outputs** |
| Excellent | 200,000+ | 48-96 hours | Near-commercial quality |

---

## 🧠 Phase 2: Choose the Right Base Model

### Step 2.1: Base Model Selection

| Model | Size | Code Ability | VRAM Required | Recommendation |
|---|---|---|---|---|
| ~~distilgpt2~~ | 82M | ❌ None | 0.5 GB | **DELETE — cannot generate code** |
| `Qwen/Qwen2.5-Coder-7B-Instruct` | 7B | ⭐⭐⭐⭐ | 5.5 GB (4-bit) | ✅ **Best for free Colab T4** |
| `Qwen/Qwen2.5-Coder-14B-Instruct` | 14B | ⭐⭐⭐⭐⭐ | 10 GB (4-bit) | ✅ Best if you have Colab Pro |
| `Qwen/Qwen2.5-Coder-32B-Instruct` | 32B | ⭐⭐⭐⭐⭐ | 20 GB (4-bit) | ✅ Best if you have A100 GPU |
| `deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct` | 16B | ⭐⭐⭐⭐⭐ | 12 GB (4-bit) | ✅ Alternative option |
| `codellama/CodeLlama-13b-Instruct-hf` | 13B | ⭐⭐⭐ | 8 GB (4-bit) | Good alternative |

### Step 2.2: Why Qwen2.5-Coder-7B Is the Right Choice

- Already trained on **5.5 trillion tokens** of code (Python, JS, TS, HTML, CSS, etc.)
- Understands **ChatML format** natively (`<|im_start|>` / `<|im_end|>`)
- **Instruction-tuned** — already knows how to follow prompts
- Fits in **free Colab T4 GPU** (15GB VRAM) with 4-bit quantization
- Your existing notebook already targets this model ✅

### Step 2.3: What Fine-Tuning Actually Does

```
Base Qwen2.5-Coder-7B:
├── Knows: Python, JS, TS, HTML, CSS, SQL, general coding
├── Doesn't know: Your specific style, GSAP, Tailwind patterns, Anti-AI aesthetics
└── Fine-tuning adds: Your coding style, framework preferences, output format

After Fine-Tuning:
├── Still knows: Everything from base training (5.5T tokens)
├── NOW knows: Your Vibe Coder style, GSAP, bento grids, specific patterns
└── Behavior: Prioritizes your style while maintaining general ability
```

---

## ⚙️ Phase 3: Training Infrastructure Setup

### Step 3.1: Choose Your Training Platform

| Platform | GPU | VRAM | Cost | Max Model |
|---|---|---|---|---|
| **Google Colab Free** | T4 | 15 GB | Free | 7B (4-bit) |
| **Google Colab Pro** | A100 | 40 GB | $10/mo | 32B (4-bit) |
| **RunPod** | A100 80GB | 80 GB | $1.5/hr | 70B (4-bit) |
| **Vast.ai** | A100 40GB | 40 GB | $0.8/hr | 32B (4-bit) |
| **Lambda Labs** | H100 | 80 GB | $2.5/hr | 70B (4-bit) |
| **Local RTX 4090** | RTX 4090 | 24 GB | One-time | 14B (4-bit) |

**Recommended**: Start with **Colab Free (T4)** for 7B model, upgrade to **Colab Pro (A100)** or **RunPod** for larger models or longer training.

### Step 3.2: Install Dependencies

```bash
# On Colab or cloud GPU
pip install torch transformers peft trl datasets bitsandbytes accelerate \
            huggingface_hub wandb sentencepiece protobuf
```

### Step 3.3: Set Up Weights & Biases (W&B) for Training Monitoring

```python
import wandb
wandb.login()  # Track loss curves, learning rate, GPU utilization in real-time
```

---

## 🔥 Phase 4: Proper Fine-Tuning (The Training)

### Step 4.1: Fixed Training Hyperparameters

Here's what was **wrong** vs what should be **correct**:

| Parameter | ❌ Your Current Value | ✅ Correct Value | Why |
|---|---|---|---|
| `max_steps` | 60 | **Remove** (use `num_train_epochs` instead) | 60 steps only sees 60 samples |
| `num_train_epochs` | Not set | **3-5** | Model needs multiple passes over entire dataset |
| `per_device_train_batch_size` | 1 | **1-2** | Limited by T4 VRAM |
| `gradient_accumulation_steps` | 8 | **16** | Effective batch size = 16-32 |
| `learning_rate` | 2e-4 | **1e-4 to 5e-5** | Lower LR = more stable training |
| `max_seq_length` | 512 | **2048-4096** | Code needs longer context |
| `warmup_ratio` | 5 steps | **0.05** (5% of total steps) | Proportional warmup |
| `lr_scheduler_type` | linear | **cosine** | Better convergence |
| `save_strategy` | "no" | **"steps"** (every 500 steps) | Save checkpoints to resume |
| `eval_strategy` | Not set | **"steps"** (every 500 steps) | Track validation loss |
| `lora_r` | 16 | **32-64** | Higher rank = more capacity |
| `lora_alpha` | 32 | **64-128** (2x rank) | Standard ratio |
| `target_modules` | 7 modules ✅ | Same ✅ | All attention + MLP layers |

### Step 4.2: Complete Training Script

The updated Colab notebook should have these cells:

```python
# ============================================
# CELL 6: PROPER Training Configuration
# ============================================
from trl import SFTTrainer
from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="./checkpoints",
    
    # TRAINING DURATION — Full epochs, not arbitrary step count
    num_train_epochs=3,                    # 3 full passes over ALL data
    
    # BATCH SIZE — Effective batch = 1 × 16 = 16
    per_device_train_batch_size=1,
    gradient_accumulation_steps=16,
    
    # LEARNING RATE — Lower = more stable for fine-tuning
    learning_rate=5e-5,
    lr_scheduler_type="cosine",            # Smooth decay
    warmup_ratio=0.05,                     # 5% warmup
    weight_decay=0.01,
    
    # PRECISION
    fp16=True,                             # Use FP16 on T4
    bf16=False,
    
    # MEMORY OPTIMIZATION
    gradient_checkpointing=True,
    optim="paged_adamw_8bit",
    
    # CHECKPOINTING — Save every 500 steps to resume if disconnected
    save_strategy="steps",
    save_steps=500,
    save_total_limit=3,                    # Keep last 3 checkpoints
    
    # EVALUATION — Track if model is improving
    eval_strategy="steps",
    eval_steps=500,
    
    # LOGGING — Track training curves
    logging_steps=10,
    report_to="wandb",                     # Or "none" if not using W&B
    run_name="vibe-coder-v2-training",
    
    # SEED
    seed=42,
)
```

### Step 4.3: LoRA Configuration (Increased Capacity)

```python
lora_config = LoraConfig(
    r=64,                     # ⬆️ Increased from 16 → 64 (more learning capacity)
    lora_alpha=128,           # ⬆️ 2x rank (standard ratio)
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.CAUSAL_LM,
    target_modules=[
        "q_proj", "k_proj", "v_proj", "o_proj",  # All attention heads
        "gate_proj", "up_proj", "down_proj"        # MLP layers
    ],
)
```

### Step 4.4: Train with Validation Split

```python
# Split dataset: 95% train, 5% validation
split_dataset = dataset.train_test_split(test_size=0.05, seed=42)

trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=split_dataset["train"],
    eval_dataset=split_dataset["test"],      # ← Validation set!
    tokenizer=tokenizer,
    max_seq_length=2048,                      # ⬆️ Increased from 512
    packing=True,                             # Pack short samples together for efficiency
)

trainer.train()
```

### Step 4.5: Training Duration Estimates

| Dataset Size | Epochs | Total Steps (batch=16) | Time on T4 | Time on A100 |
|---|---|---|---|---|
| 10,000 | 3 | ~1,875 | ~3 hours | ~45 min |
| 50,000 | 3 | ~9,375 | ~15 hours | ~4 hours |
| 100,000 | 3 | ~18,750 | ~30 hours | ~8 hours |

> [!TIP]
> **Colab Pro tip**: Use `save_strategy="steps"` with `save_steps=500`. If Colab disconnects, you can resume from the last checkpoint with `trainer.train(resume_from_checkpoint="./checkpoints/checkpoint-500")`.

### Step 4.6: What to Watch During Training

```
✅ GOOD signs:
- Training loss steadily decreasing from ~2.5 → ~0.3-0.5
- Validation loss also decreasing (not just training loss)
- Loss curve is smooth (no wild spikes)

❌ BAD signs:
- Training loss goes down but validation loss goes UP → Overfitting!
- Loss plateaus at high value (~2.0+) → Learning rate too low or bad data
- Loss oscillates wildly → Learning rate too high
- NaN loss → Numerical instability, reduce LR
```

---

## 🖥️ Phase 5: Real Inference Backend (Replace Mock Server)

### Step 5.1: Choose Your Serving Method

Your current [`llm.ts`](file:///d:/LLM/backend/src/services/llm.ts) returns a **hardcoded template** — it's not running any model. You need real inference.

| Method | Setup Effort | Speed | Local? | Cost |
|---|---|---|---|---|
| **Ollama** (Recommended) | ⭐ Easy | Fast | ✅ Yes | Free |
| **vLLM** | ⭐⭐ Medium | Fastest | ✅ Yes | Free |
| **HuggingFace Inference API** | ⭐ Easy | Medium | ❌ Cloud | Free tier available |
| **text-generation-webui** | ⭐⭐ Medium | Fast | ✅ Yes | Free |

### Step 5.2: Ollama Setup (Easiest Path)

```bash
# 1. Install Ollama (https://ollama.ai)
# 2. Create a Modelfile for your fine-tuned model
cat > Modelfile << EOF
FROM qwen2.5-coder:7b
ADAPTER ./vibe_coder_lora           # Your fine-tuned LoRA adapter
PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER num_predict 4096           # Max output tokens
SYSTEM "You are Vibe Coder, a world-class full-stack engineer..."
EOF

# 3. Create the model
ollama create vibe-coder -f Modelfile

# 4. Run it
ollama run vibe-coder
```

### Step 5.3: Update Backend `llm.ts` for Real Inference

Replace the hardcoded template with actual Ollama API calls:

```typescript
// NEW llm.ts — Real inference via Ollama
const OLLAMA_URL = process.env.OLLAMA_URL || 'http://localhost:11434';

export async function streamLLMInference(options: LLMStreamOptions): Promise<void> {
  const { userPrompt, onToken, onComplete, onError } = options;
  
  const { augmentedSystemPrompt } = augmentPromptWithRAG(userPrompt, MASTER_SYSTEM_PROMPT);
  
  const response = await fetch(`${OLLAMA_URL}/api/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      model: 'vibe-coder',
      messages: [
        { role: 'system', content: augmentedSystemPrompt },
        { role: 'user', content: userPrompt }
      ],
      stream: true,
      options: {
        temperature: 0.7,
        top_p: 0.9,
        num_predict: 4096,
      }
    }),
  });
  
  // Stream tokens from Ollama → SSE to frontend
  const reader = response.body.getReader();
  let accumulated = '';
  
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    
    const chunk = JSON.parse(new TextDecoder().decode(value));
    const token = chunk.message?.content || '';
    accumulated += token;
    onToken(token);
  }
  
  onComplete(accumulated);
}
```

---

## 📏 Phase 6: Evaluation & Iteration

### Step 6.1: Benchmark Test Suite

Create a test suite of 50+ prompts across all categories:

```python
test_prompts = [
    # Conversational (should NOT generate code)
    {"prompt": "Hi, how are you?", "expect": "conversation"},
    {"prompt": "What is React?", "expect": "explanation"},
    
    # HTML/CSS (should generate plain HTML, NOT React)
    {"prompt": "Create a registration form in HTML and CSS", "expect": "html"},
    {"prompt": "Build a responsive footer with HTML", "expect": "html"},
    
    # React Components
    {"prompt": "Create a todo list app in React", "expect": "react_component"},
    {"prompt": "Build a dashboard with charts", "expect": "react_component"},
    
    # API/Backend
    {"prompt": "Create a REST API for user authentication", "expect": "api_route"},
    
    # Debugging
    {"prompt": "Fix this error: TypeError: Cannot read property 'map' of undefined", "expect": "debug"},
]
```

### Step 6.2: Quality Metrics to Track

| Metric | How to Measure | Target |
|---|---|---|
| **Code Compilability** | Run generated code through TypeScript/Babel compiler | >90% compile |
| **Intent Accuracy** | Does it generate code when asked for code, chat when greeted? | >95% correct |
| **Completeness** | No TODOs, no `...`, no truncated output | 100% complete |
| **Style Consistency** | Uses your design system (Tailwind, GSAP, etc.) | >80% |
| **Response Length** | Average token count of responses | 200-800 tokens |

### Step 6.3: Iterate

If results aren't good enough:
1. **Add more data** in weak categories
2. **Increase LoRA rank** (64 → 128)
3. **Train for more epochs** (3 → 5)
4. **Upgrade base model** (7B → 14B → 32B)
5. **Use DPO/RLHF** for preference alignment (advanced)

---

## 📋 Summary: Execution Order

| Step | Phase | Action | Time |
|---|---|---|---|
| 1 | 🗑️ Phase 0 | Delete wrong files (distilgpt2, news data, fake adapter) | 10 min |
| 2 | 📊 Phase 1.1-1.2 | Define 25 task categories | 30 min |
| 3 | 📊 Phase 1.3 | Download HuggingFace datasets | 1-2 hours |
| 4 | 📊 Phase 1.4 | Build dataset generator script | 2-4 hours |
| 5 | 📊 Phase 1.5-1.6 | Validate & filter to 50K+ quality samples | 1-2 hours |
| 6 | 🧠 Phase 2 | Confirm base model (Qwen2.5-Coder-7B) | 10 min |
| 7 | ⚙️ Phase 3 | Set up Colab/RunPod training environment | 30 min |
| 8 | 🔥 Phase 4 | Run full QLoRA training (3 epochs) | 15-30 hours |
| 9 | 🖥️ Phase 5 | Install Ollama + deploy model | 1-2 hours |
| 10 | 🖥️ Phase 5 | Update `llm.ts` for real Ollama inference | 1 hour |
| 11 | 📏 Phase 6 | Run benchmark tests & evaluate | 2-3 hours |
| 12 | 📏 Phase 6 | Iterate on weak areas | Ongoing |

> **Total estimated time: 3-5 days** (mostly waiting for training to complete)

---

## 🎯 What You'll Have at the End

- ✅ A **properly fine-tuned** Qwen2.5-Coder-7B model trained on **50K+ real coding samples**
- ✅ A model that **understands intent** — codes when asked to code, chats when greeted
- ✅ **Real inference** via Ollama (not hardcoded templates)
- ✅ Output quality comparable to **specialized coding assistants** for your domain
- ✅ Complete training pipeline you can **re-run and improve** anytime
- ✅ Practical experience with **QLoRA, PEFT, ChatML, model serving** — real ML engineering skills

> [!NOTE]
> Ready to start? Approve this plan and I'll begin with Phase 0 (cleanup) and Phase 1 (dataset building). We'll tackle each phase step by step.
