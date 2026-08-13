# 🖥️ Free & Cheap GPU Options for Vibe-Coder Model Training

---

## 1️⃣ Can You Get Colab Pro for Free?

**Short answer: No legitimate way to get Colab Pro for free.**

| Option | Verdict |
|---|---|
| Google Colab Pro ($10/mo) | ❌ No free workaround — requires payment |
| Google Research Credits program | ✅ Possible if you're affiliated with a university — apply for Google Cloud Research Credits |
| Google for Startups Cloud Program | ✅ Up to $100K credits if you register as a startup |

**BUT — you don't actually need Colab Pro.** Here's why:

---

## 2️⃣ All Free GPU Options Available RIGHT NOW

Here's every free GPU you can get today, ranked by power:

| # | Platform | GPU | VRAM | Free Limit | Can Train 7B? | Can Train 32B? | Sign Up |
|---|---|---|---|---|---|---|---|
| 1 | **Google Colab Free** | T4 | 15 GB | ~12 hr sessions, ~30 hrs/week | ✅ Yes (4-bit) | ❌ No | [colab.google](https://colab.research.google.com) |
| 2 | **Kaggle Notebooks** | T4 or P100 | 15-16 GB | 30 hrs/week | ✅ Yes (4-bit) | ❌ No | [kaggle.com](https://kaggle.com) |
| 3 | **Lightning AI** | T4 / A10G / A100 | Up to 80 GB | **80 free GPU hours** | ✅ Yes | ⚠️ Maybe (A100) | [lightning.ai](https://lightning.ai) |
| 4 | **Modal** | A100 / H100 | 40-80 GB | **$30 free credits/month** | ✅ Yes | ✅ Yes (A100) | [modal.com](https://modal.com) |
| 5 | **Hugging Face ZeroGPU** | A100 | 40 GB | Limited (inference only) | ❌ Inference only | ❌ No | [huggingface.co](https://huggingface.co) |
| 6 | **NVIDIA Build** | DGX Cloud | - | Free API access (inference) | ❌ Inference only | ❌ No | [build.nvidia.com](https://build.nvidia.com) |

### 🏆 Best Free Options for Your Project:

> **Lightning AI** = Best free option. 80 hours on A100 is enough to train a 7B model on 50K samples for 3 epochs!

> **Modal** = $30/month free = ~20 hours of A100 time. Good supplement.

> **Colab + Kaggle** = Combined 60 hrs/week of T4 time. Use for 7B model training with checkpointing.

---

## 3️⃣ Your AWS $120 Credits — BEST STRATEGY

### What GPUs Can You Get on AWS?

| Instance | GPU | VRAM | $/hour (On-Demand) | $/hour (Spot) | Can Train 32B? |
|---|---|---|---|---|---|
| `g5.xlarge` | A10G × 1 | 24 GB | ~$1.00 | ~$0.40 | ❌ No (too small) |
| `g5.2xlarge` | A10G × 1 | 24 GB | ~$1.21 | ~$0.50 | ❌ No |
| `g5.4xlarge` | A10G × 1 | 24 GB | ~$1.62 | ~$0.65 | ❌ No |
| **`g5.12xlarge`** | **A10G × 4** | **96 GB total** | **~$5.67** | **~$2.00** | **✅ YES** |
| `g6.xlarge` | L4 × 1 | 24 GB | ~$0.80 | ~$0.35 | ❌ No |
| `p4d.24xlarge` | A100 × 8 | 320 GB total | ~$32.77 | ~$10-15 | ✅ Yes (overkill) |

### ⭐ Recommended AWS Strategy with $120 Credits

#### Option A: Train 7B Model (Safe, Maximum Training Time)
```
Instance: g5.xlarge (1× A10G, 24 GB VRAM)
Cost: ~$1.00/hr on-demand, ~$0.40/hr spot
$120 ÷ $0.40 = 300 hours of spot GPU time!

→ Enough for: 3-5 epochs on 100K+ samples with Qwen2.5-Coder-7B (4-bit)
→ This is MORE than enough for an excellent model
```

#### Option B: Train 14B Model (Better Quality, Less Time)
```
Instance: g5.2xlarge (1× A10G, 24 GB VRAM)  
Cost: ~$1.21/hr on-demand, ~$0.50/hr spot
$120 ÷ $0.50 = 240 hours of spot GPU time!

→ Enough for: 3 epochs on 50K samples with Qwen2.5-Coder-14B (4-bit)
→ Better output quality than 7B
```

#### Option C: Train 32B Model (Best Quality, Tight Budget) ⚠️
```
Instance: g5.12xlarge (4× A10G, 96 GB total VRAM)
Cost: ~$5.67/hr on-demand, ~$2.00/hr spot
$120 ÷ $2.00 = 60 hours of spot GPU time

→ Enough for: 1-2 epochs on 50K samples with Qwen2.5-Coder-32B (4-bit)
→ Best output quality but risky — if spot instance gets interrupted you lose progress
→ MUST use aggressive checkpointing (every 200 steps)
```

### 🎯 My Recommendation: Option A or B

> [!IMPORTANT]
> **Go with Option A (7B on g5.xlarge spot)** — it gives you **300 hours** of GPU time. That's enough to train multiple versions, experiment with hyperparameters, and iterate. A well-trained 7B model will outperform a poorly-trained 32B model.
>
> If you want better quality and are confident, **Option B (14B)** gives you 240 hours, which is still plenty.

### AWS Setup Steps

```bash
# Step 1: Log into AWS Console → EC2 → Request quota increase
# Go to: Service Quotas → EC2 → "Running On-Demand G and VT instances"  
# Request increase to at least 4 vCPUs (for g5.xlarge)

# Step 2: Launch a g5.xlarge spot instance
# - AMI: "Deep Learning Base OSS Nvidia Driver GPU AMI (Ubuntu 22.04)"
# - Instance type: g5.xlarge
# - Request type: Spot Instance
# - Storage: 100 GB gp3

# Step 3: SSH in and start training
ssh -i your-key.pem ubuntu@<instance-ip>

# Step 4: Set up environment
pip install torch transformers peft trl datasets bitsandbytes accelerate

# Step 5: Upload your dataset and run training script
# Step 6: Download trained adapter when done
```

> [!CAUTION]
> **SET UP BILLING ALERTS IMMEDIATELY!** Go to AWS Budgets → Create Budget → Set threshold at $100. This prevents accidental charges after credits run out.

---

## 4️⃣ Can You Get Free GPUs from NVIDIA?

| Program | What You Get | Who It's For | Cost |
|---|---|---|---|
| **NVIDIA Developer Program** | Free API access to 100+ models on DGX Cloud | Anyone | Free |
| **NVIDIA Build (build.nvidia.com)** | Free inference API calls | Developers | Free |
| **NVIDIA Inception** | Discounted hardware + partner cloud credits | Startups only | Free to join |
| **NVIDIA DLI (Deep Learning Institute)** | Free courses with GPU lab access | Students | Free |

> [!NOTE]
> **NVIDIA doesn't give free raw GPU compute for training.** Their free tier is for **inference** (using pre-trained models), not training your own. For training, you need cloud providers.

---

## 5️⃣ The Ultimate Free GPU Strategy (Stack Everything)

Here's how to maximize your total free compute:

```
📊 TOTAL FREE GPU HOURS AVAILABLE TO YOU:

┌─────────────────────────┬──────────┬─────────┬──────────────────┐
│ Platform                │ GPU      │ Hours   │ Use For          │
├─────────────────────────┼──────────┼─────────┼──────────────────┤
│ Google Colab Free       │ T4       │ ~120/mo │ Testing & debug  │
│ Kaggle Free             │ T4/P100  │ ~120/mo │ Data prep        │
│ Lightning AI            │ A100     │ 80 hrs  │ Training run #1  │
│ Modal                   │ A100     │ ~20 hrs │ Evaluation       │
│ AWS $120 Credits (Spot) │ A10G     │ 300 hrs │ Main training    │
├─────────────────────────┼──────────┼─────────┼──────────────────┤
│ TOTAL                   │          │ ~640 hrs│                  │
└─────────────────────────┴──────────┴─────────┴──────────────────┘
```

### Recommended Workflow:

```
Phase 1: Dataset Building
├── Use: Local PC (no GPU needed)
├── Time: 1-2 days
└── Cost: $0

Phase 2: Quick Test Training (Small subset, 1000 samples, 1 epoch)
├── Use: Google Colab Free (T4)
├── Time: 30 min
└── Cost: $0

Phase 3: First Real Training Run (50K samples, 3 epochs)
├── Use: Lightning AI Free (80 hrs A100)
├── Time: 8-15 hours
└── Cost: $0

Phase 4: Evaluation & Testing
├── Use: Modal ($30 free) or Colab
├── Time: 2-3 hours
└── Cost: $0

Phase 5: Full Production Training (100K samples, 5 epochs, best hyperparams)
├── Use: AWS $120 Credits (g5.xlarge Spot)
├── Time: 20-40 hours
└── Cost: $0 (covered by credits)

Phase 6: Iteration & Experiments
├── Use: Remaining AWS credits (~260 hours left)
├── Time: As needed
└── Cost: $0
```

---

## 6️⃣ Cost Calculator: How Long Will $120 Last?

### Training Qwen2.5-Coder-7B (4-bit QLoRA)

| Dataset Size | Epochs | Approx Time | AWS Spot Cost | Training Quality |
|---|---|---|---|---|
| 10,000 samples | 3 | ~3 hrs | ~$1.20 | Basic |
| 50,000 samples | 3 | ~15 hrs | ~$6.00 | Good |
| 100,000 samples | 3 | ~30 hrs | ~$12.00 | Very Good |
| 100,000 samples | 5 | ~50 hrs | ~$20.00 | Excellent |

**With $120 on g5.xlarge spot**: You can train a **100K sample, 5-epoch model AND have $100 left** for experiments!

### Training Qwen2.5-Coder-14B (4-bit QLoRA)

| Dataset Size | Epochs | Approx Time | AWS Spot Cost | Training Quality |
|---|---|---|---|---|
| 50,000 samples | 3 | ~25 hrs | ~$12.50 | Good |
| 100,000 samples | 3 | ~50 hrs | ~$25.00 | Very Good |

---

## 7️⃣ Quick Comparison: What Should You Do?

| If you want... | Then use... | Model Size | Cost |
|---|---|---|---|
| **Fastest start, zero cost** | Colab Free + Kaggle | 7B | $0 |
| **Best free A100 training** | Lightning AI (80 free hrs) | 7B-14B | $0 |
| **Maximum training power** | AWS $120 spot credits | 7B-14B | $0 (credits) |
| **32B model quality** | AWS g5.12xlarge spot | 32B | ~$60-120 |
| **Industrial scale** | RunPod / Lambda Labs A100 | 32B-70B | $1.5-3/hr |

---

## ✅ Final Recommendation

> **Start with Lightning AI (free 80 hrs on A100) for your first proper training run, then use AWS $120 credits (g5.xlarge spot at $0.40/hr) for the full production training.** This gives you ~380 hours of GPU time for $0 total cost — more than enough to train an excellent 7B or 14B model.

You do NOT need a 32B model to get great results. A well-trained 7B model with 100K high-quality samples will produce professional-grade code.
