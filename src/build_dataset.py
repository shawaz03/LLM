import os, sys, json, re, hashlib, random, argparse
from typing import List, Dict, Any, Tuple

SYSTEM_PROMPT = (
    "You are Vibe Coder, a world-class principal full-stack software engineer and UI/UX designer.\\n"
    "STRICT ANTI-AI AESTHETIC & GENERATION DIRECTIVES:\\n"
    "1. ZERO PLACEHOLDERS: ALWAYS output 100% complete, runnable code. NEVER use placeholders like '// TODO', '// implement here', '...', or '// rest of code'.\\n"
    "2. ANTI-AI AESTHETICS: Never output generic AI template tropes. Use bespoke asymmetric bento grids, noise/grain overlays, custom typography, and magnetic hover physics.\\n"
    "3. ANIMATION & UI STACK: Combine Next.js 15 App Router, React 19, Tailwind CSS, Shadcn UI, Framer Motion, GSAP, Aceternity UI, and Magic UI.\\n"
    "4. BACKEND STACK: Use Node.js, Prisma ORM, JWT authentication, and clean error handling.\\n"
    "5. TYPE SAFETY & CLEAN CODE: Include full TypeScript interfaces, prop types, and export default declarations."
)

CONVERSATIONAL_SYSTEM_PROMPT = (
    "You are Vibe Coder, an intelligent, friendly AI full-stack development assistant.\\n"
    "Provide clear, concise, professional answers. Only generate code blocks when the user explicitly requests code or technical implementation."
)

HANDCRAFTED_SAMPLES = [
    {
        "instruction": "Create a high-end bespoke feature showcase section in Next.js 15 using GSAP ScrollTrigger timeline, Space Grotesk typography, and bespoke Bento Grid layout.",
        "category": "gsap_scrolltrigger_bento",
        "system": SYSTEM_PROMPT,
        "response": """'use client';
import React, { useEffect, useRef } from 'react';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { Cpu, ShieldCheck, Zap } from 'lucide-react';

if (typeof window !== 'undefined') {
  gsap.registerPlugin(ScrollTrigger);
}

export default function BespokeBentoShowcase() {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!containerRef.current) return;
    const ctx = gsap.context(() => {
      gsap.from('.bento-card', {
        y: 60,
        opacity: 0,
        duration: 0.8,
        stagger: 0.15,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: containerRef.current,
          start: 'top 80%',
        }
      });
    }, containerRef);
    return () => ctx.revert();
  }, []);

  return (
    <section ref={containerRef} className="py-24 bg-neutral-950 text-white px-6">
      <div className="max-w-6xl mx-auto space-y-12">
        <div className="space-y-4 text-center">
          <span className="text-xs uppercase tracking-widest text-emerald-400 font-mono">Architecture v4</span>
          <h2 className="text-4xl font-extrabold tracking-tight font-sans sm:text-5xl">Engineered for Extreme Velocity</h2>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bento-card p-8 rounded-2xl bg-neutral-900/80 border border-neutral-800 backdrop-blur-xl relative overflow-hidden group">
            <Zap className="w-8 h-8 text-amber-400 mb-4" />
            <h3 className="text-xl font-bold mb-2">Sub-millisecond Edge Compute</h3>
            <p className="text-neutral-400 text-sm leading-relaxed">Global state propagation under 15ms via distributed Cloudflare workers and optimistic client caching.</p>
          </div>
          <div className="bento-card p-8 rounded-2xl bg-neutral-900/80 border border-neutral-800 backdrop-blur-xl relative overflow-hidden group md:col-span-2">
            <Cpu className="w-8 h-8 text-cyan-400 mb-4" />
            <h3 className="text-xl font-bold mb-2">Autonomous Self-Healing Query Engine</h3>
            <p className="text-neutral-400 text-sm leading-relaxed">Dynamic SQL optimization with automated index generation, proactive deadlock avoidance, and live read-replica routing.</p>
          </div>
        </div>
      </div>
    </section>
  );
}"""
    },
    {
        "instruction": "Design a bespoke, non-generic navigation header in React 19 with magnetic cursor hover dynamics and custom blur drop shadow.",
        "category": "bespoke_ui_nav",
        "system": SYSTEM_PROMPT,
        "response": """'use client';
import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Layers, Terminal, Sparkles, ArrowUpRight } from 'lucide-react';

export default function BespokeNavbar() {
  const [hoveredIndex, setHoveredIndex] = useState<number | null>(null);

  const links = [
    { label: 'Platform', icon: Layers },
    { label: 'CLI Tools', icon: Terminal },
    { label: 'Changelog', icon: Sparkles },
  ];

  return (
    <header className="fixed top-6 left-1/2 -translate-x-1/2 z-50">
      <nav className="flex items-center gap-2 p-2 rounded-full bg-neutral-900/80 border border-neutral-800/80 backdrop-blur-2xl shadow-[0_8px_32px_rgba(0,0,0,0.4)]">
        <div className="flex items-center gap-6 px-4 py-1 text-sm">
          <span className="font-mono font-bold tracking-wider text-emerald-400">VIBE//OS</span>
          {links.map((link, idx) => (
            <button
              key={link.label}
              onMouseEnter={() => setHoveredIndex(idx)}
              onMouseLeave={() => setHoveredIndex(null)}
              className="relative px-3 py-1.5 text-neutral-300 hover:text-white transition-colors flex items-center gap-2"
            >
              {hoveredIndex === idx && (
                <motion.span
                  layoutId="nav-glow"
                  className="absolute inset-0 rounded-full bg-neutral-800/90 -z-10"
                  transition={{ type: 'spring', bounce: 0.2, duration: 0.5 }}
                />
              )}
              <link.icon className="w-3.5 h-3.5" />
              <span>{link.label}</span>
            </button>
          ))}
        </div>
        <button className="px-5 py-2 rounded-full bg-emerald-500 hover:bg-emerald-400 text-neutral-950 font-semibold text-xs transition-all flex items-center gap-1 shadow-lg shadow-emerald-500/20">
          <span>Deploy</span>
          <ArrowUpRight className="w-3.5 h-3.5" />
        </button>
      </nav>
    </header>
  );
}"""
    },
    {
        "instruction": "Build an Awwwards-level interactive pricing table with annual discount toggle, glowing brass borders, and glassmorphic card design.",
        "category": "bespoke_pricing_table",
        "system": SYSTEM_PROMPT,
        "response": """'use client';
import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Check, Sparkles, ArrowRight } from 'lucide-react';

export default function BespokePricing() {
  const [annual, setAnnual] = useState(true);

  const tiers = [
    { name: 'Developer', price: annual ? 19 : 24, desc: 'For solo creators and builders', features: ['5 Workspaces', '100k API req/mo', 'Community Support', 'Edge CDN Deployment'] },
    { name: 'Scale Pro', price: annual ? 79 : 99, popular: true, desc: 'For high-growth software teams', features: ['Unlimited Workspaces', '5M API req/mo', 'Dedicated 24/7 Slack support', 'Custom Domains & SSL', 'SOC2 Compliance Pack'] },
    { name: 'Enterprise', price: annual ? 299 : 349, desc: 'Dedicated cloud infrastructure', features: ['Isolated VPC Clusters', 'Unlimited Volume', 'SLA 99.99% Guarantee', 'Custom Model Fine-tuning'] },
  ];

  return (
    <section className="py-24 bg-neutral-950 text-white px-6">
      <div className="max-w-6xl mx-auto space-y-16 text-center">
        <div className="space-y-4">
          <h2 className="text-4xl font-extrabold tracking-tight sm:text-5xl">Transparent, Scale-Driven Pricing</h2>
          <div className="flex items-center justify-center gap-3 mt-6">
            <span className={`text-sm ${!annual ? 'text-white' : 'text-neutral-400'}`}>Monthly</span>
            <button
              onClick={() => setAnnual(!annual)}
              className="w-14 h-8 rounded-full bg-neutral-800 p-1 transition-colors relative"
            >
              <div className={`w-6 h-6 rounded-full bg-emerald-400 transition-transform ${annual ? 'translate-x-6' : 'translate-x-0'}`} />
            </button>
            <span className={`text-sm flex items-center gap-1.5 ${annual ? 'text-white font-medium' : 'text-neutral-400'}`}>
              Annual <span className="text-[10px] bg-emerald-500/20 text-emerald-300 px-2 py-0.5 rounded-full border border-emerald-500/30">Save 20%</span>
            </span>
          </div>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 text-left">
          {tiers.map((tier) => (
            <div
              key={tier.name}
              className={`p-8 rounded-3xl backdrop-blur-xl relative flex flex-col justify-between ${tier.popular ? 'bg-neutral-900/90 border-2 border-emerald-500/80 shadow-[0_0_40px_rgba(16,185,129,0.15)]' : 'bg-neutral-900/40 border border-neutral-800'}`}
            >
              <div className="space-y-6">
                <div className="flex justify-between items-center">
                  <h3 className="text-xl font-bold">{tier.name}</h3>
                  {tier.popular && <span className="text-xs bg-emerald-500 text-neutral-950 font-bold px-2.5 py-1 rounded-full flex items-center gap-1"><Sparkles className="w-3 h-3"/> Popular</span>}
                </div>
                <p className="text-sm text-neutral-400">{tier.desc}</p>
                <div className="flex items-baseline gap-1">
                  <span className="text-5xl font-extrabold">${tier.price}</span>
                  <span className="text-neutral-400 text-sm">/mo</span>
                </div>
                <ul className="space-y-3 text-sm text-neutral-300 border-t border-neutral-800 pt-6">
                  {tier.features.map((feat) => (
                    <li key={feat} className="flex items-center gap-2.5">
                      <Check className="w-4 h-4 text-emerald-400 shrink-0" />
                      <span>{feat}</span>
                    </li>
                  ))}
                </ul>
              </div>
              <button className={`w-full mt-8 py-3 rounded-xl font-semibold text-sm transition-all flex items-center justify-center gap-2 ${tier.popular ? 'bg-emerald-500 hover:bg-emerald-400 text-neutral-950' : 'bg-neutral-800 hover:bg-neutral-700 text-white'}`}>
                <span>Get Started</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}"""
    }
]

CONVERSATIONAL_SAMPLES = [
    {"instruction": "hi", "category": "conversation", "system": CONVERSATIONAL_SYSTEM_PROMPT, "response": "Hello! I'm Vibe Coder, your AI full-stack development assistant. How can I help you build or debug your web application today?"},
    {"instruction": "hey", "category": "conversation", "system": CONVERSATIONAL_SYSTEM_PROMPT, "response": "Hey there! Ready to write clean code or design bespoke web interfaces. What are you working on?"},
    {"instruction": "hello", "category": "conversation", "system": CONVERSATIONAL_SYSTEM_PROMPT, "response": "Hello! What project or component are we building today? Let me know your tech stack and requirements."},
    {"instruction": "what can you do?", "category": "conversation", "system": CONVERSATIONAL_SYSTEM_PROMPT, "response": "I am specialized in modern full-stack web engineering: Next.js 15, React 19, TypeScript, Tailwind CSS, Node.js, Prisma ORM, and complex UI animations with Framer Motion and GSAP. I write 100% complete, production-ready code with zero placeholders."},
    {"instruction": "who are you?", "category": "conversation", "system": CONVERSATIONAL_SYSTEM_PROMPT, "response": "I am Vibe Coder, a world-class principal full-stack engineer and UI/UX designer. I help developers architect, build, and debug high-performance web applications."},
    {"instruction": "good morning", "category": "conversation", "system": CONVERSATIONAL_SYSTEM_PROMPT, "response": "Good morning! Ready to assist you with Next.js 15, React 19, backend APIs, or database architecture. What's on the roadmap today?"},
    {"instruction": "yo", "category": "conversation", "system": CONVERSATIONAL_SYSTEM_PROMPT, "response": "Yo! What full-stack feature or UI component can I assist you with?"},
    {"instruction": "howdy", "category": "conversation", "system": CONVERSATIONAL_SYSTEM_PROMPT, "response": "Howdy! Ready to engineer high-performance web applications. Let me know what you'd like to build."}
]

SELF_HEALING_SAMPLES = [
    {
        "instruction": "Fix this React component that is crashing with 'ReferenceError: useState is not defined':\\n\\n```tsx\\n'use client';\\n\\nexport default function Counter() {\\n  const [count, setCount] = useState(0);\\n  return <button onClick={() => setCount(count + 1)}>Count: {count}</button>;\\n}\\n```",
        "category": "debug_fix",
        "system": SYSTEM_PROMPT,
        "response": "Here is the fixed, 100% complete file with the missing `useState` import from React:\\n\\n```tsx\\n'use client';\\n\\nimport React, { useState } from 'react';\\n\\nexport default function Counter() {\\n  const [count, setCount] = useState(0);\\n  return <button onClick={() => setCount(count + 1)}>Count: {count}</button>;\\n}\\n```"
    }
]

def format_chatml(system: str, instruction: str, response: str) -> str:
    return (
        f"<|im_start|>system\n{system.strip()}<|im_end|>\n"
        f"<|im_start|>user\n{instruction.strip()}<|im_end|>\n"
        f"<|im_start|>assistant\n{response.strip()}<|im_end|>"
    )

def validate_chatml_structure(chatml_text: str) -> bool:
    if not chatml_text.startswith("<|im_start|>system\n"): return False
    if "<|im_end|>\n<|im_start|>user\n" not in chatml_text: return False
    if "<|im_end|>\n<|im_start|>assistant\n" not in chatml_text: return False
    if not chatml_text.endswith("<|im_end|>"): return False
    return True

STUB_REGEX = re.compile(
    r'(//|/\*|#)\s*(implement|todo|fill\s+in|write\s+logic|your\s+code\s+here|add\s+logic|fixme|rest\s+of|add\s+more\s+here)',
    re.IGNORECASE
)

WEB_POSITIVE = re.compile(
    r'\b(typescript|tsx|javascript|jsx|react|next\.?js|node\.?js|express|hono|prisma|tailwind|css|html|zustand|tanstack|zod|graphql|sql|postgres|jwt|websocket|vite|redux|formik|styled-components|lucide|postcss)\b',
    re.IGNORECASE
)

NON_WEB_NEGATIVE = re.compile(
    r'\b(python|def\s+[a-zA-Z_]|import\s+torch|import\s+numpy|import\s+pandas|c\+\+|c#|\.net|java\b(?!script)|assembly|x86|arm64|cobol|fortran|rust\b|golang|swift\b|kotlin|flutter|dart\b|solidity|smart contract|pytorch|tensorflow|keras|pandas|scikit-learn|matplotlib|seaborn|django|flask|fastapi|ruby|php\b|laravel|jqbootstrapvalidation)\b',
    re.IGNORECASE
)

def is_ultra_clean_web_sample(instruction: str, response: str) -> bool:
    comb = (instruction + " " + response).lower()
    if len(instruction.strip()) < 10 or len(instruction) > 3000:
        return False
    if len(response.strip()) < 150 or len(response) > 12000:
        return False
    if STUB_REGEX.search(response):
        return False
    if NON_WEB_NEGATIVE.search(comb):
        return False
    if not WEB_POSITIVE.search(comb):
        return False
    if re.search(r'\bvar\s+[a-zA-Z0-9_]+\s*=', response) and 'const ' not in response and 'let ' not in response:
        return False
    return True

def fetch_open_source_datasets(target_count: int = 8000, seen_hashes: set = None) -> List[Dict[str, Any]]:
    print(f"\\n[PIPELINE #1 - CURATED OSS] Fetching up to {target_count:,} real-world web stack samples from Hugging Face...")
    if seen_hashes is None:
        seen_hashes = set()
    
    extracted = []
    try:
        from huggingface_hub import hf_hub_download
    except ImportError:
        print("   [!] huggingface_hub not installed. Skipping remote OSS fetch.")
        return extracted
        
    sources = [
        ("ise-uiuc/Magicoder-OSS-Instruct-75K", "data-oss_instruct-decontaminated.jsonl", "jsonl", 3000),
        ("TokenBender/code_instructions_122k_alpaca_style", "code_instructions_120k.json", "json", 3000),
        ("sahil2801/CodeAlpaca-20k", "code_alpaca_20k.json", "json", 2000),
    ]
    
    for repo_id, filename, filetype, max_from_repo in sources:
        if len(extracted) >= target_count:
            break
        print(f"   --> Loading from {repo_id} ({filename})...")
        try:
            local_path = hf_hub_download(repo_id=repo_id, filename=filename, repo_type="dataset")
            count_repo = 0
            if filetype == "jsonl":
                with open(local_path, "r", encoding="utf-8") as f:
                    for line in f:
                        if not line.strip(): continue
                        item = json.loads(line)
                        inst = item.get("problem", item.get("instruction", ""))
                        resp = item.get("solution", item.get("response", ""))
                        if is_ultra_clean_web_sample(inst, resp):
                            h = hashlib.md5(resp.strip().encode("utf-8")).hexdigest()
                            if h not in seen_hashes:
                                seen_hashes.add(h)
                                extracted.append({
                                    "instruction": inst.strip(),
                                    "response": resp.strip(),
                                    "category": "open_source_web",
                                    "system": SYSTEM_PROMPT
                                })
                                count_repo += 1
                                if count_repo >= max_from_repo or len(extracted) >= target_count:
                                    break
            elif filetype == "json":
                with open(local_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for item in data:
                        inst = item.get("instruction", "")
                        inp = item.get("input", "")
                        if inp and inp.strip() not in ["Not applicable", "none", "N/A"]:
                            inst = f"{inst}\\n\\nContext:\\n{inp}"
                        resp = item.get("output", item.get("response", ""))
                        if is_ultra_clean_web_sample(inst, resp):
                            h = hashlib.md5(resp.strip().encode("utf-8")).hexdigest()
                            if h not in seen_hashes:
                                seen_hashes.add(h)
                                extracted.append({
                                    "instruction": inst.strip(),
                                    "response": resp.strip(),
                                    "category": "open_source_web",
                                    "system": SYSTEM_PROMPT
                                })
                                count_repo += 1
                                if count_repo >= max_from_repo or len(extracted) >= target_count:
                                    break
            print(f"       [+] Extracted {count_repo:,} verified web samples from {repo_id}")
        except Exception as e:
            print(f"       [!] Warning: Failed to process {repo_id}: {e}")
            
    print(f"   [+] Pipeline #1 total extracted: {len(extracted):,} genuine OSS web samples!")
    return extracted


def generate_combinatorial_web_samples(count_needed: int, seen_hashes: set) -> List[Dict[str, Any]]:
    print(f"\n[STEP 1.6 & 1.9 (OPTION A - DEEP TEMPLATES)] Generating {count_needed:,} feature-rich web-stack task pairs...")
    results = []
    
    frameworks = ["React 19", "Next.js 15 App Router", "Vanilla HTML5/CSS3", "Node.js Express", "Hono Framework", "Prisma ORM", "TypeScript"]
    styles = ["Tailwind CSS", "CSS Modules", "Styled Components", "Glassmorphic Theme", "Cyberpunk Dark Theme", "Minimalist Clean Theme", "Neumorphic Soft UI"]
    
    topics = [
        ("Interactive Accordion Component", "fullstack_ui", "accordion"),
        ("Multi-Step Wizard Form with Zod Validation", "fullstack_ui", "wizard_form"),
        ("OTP 6-Digit Verification Code Input", "fullstack_ui", "otp_input"),
        ("Interactive Shopping Cart Drawer", "fullstack_ui", "cart_drawer"),
        ("Express.js JWT Authentication Middleware & Refresh Endpoint", "nodejs_backend", "express_auth"),
        ("Next.js 15 Server Action with Rate Limiting & Revalidation", "nextjs_backend", "server_action_rate"),
        ("Hono API Endpoint with Zod Request Body Validation", "nodejs_backend", "hono_zod_api"),
        ("Express.js File Upload Route using Multer & S3 Pre-signed URLs", "nodejs_backend", "express_s3_upload"),
        ("Redis Caching Middleware for Express REST APIs", "nodejs_backend", "redis_express_cache"),
        ("Prisma Schema for E-Commerce Store (Users, Products, Orders, Payments)", "database_schema", "prisma_ecommerce"),
        ("Prisma Schema for Social Network (Users, Follows, Posts, Likes)", "database_schema", "prisma_social"),
        ("PostgreSQL Full-Text Search Query with Prisma Client", "database_schema", "prisma_search_query"),
        ("Custom React Hook useLocalStorage with Event Synchronization", "fullstack_ui", "hook_localstorage"),
        ("Custom React Hook useDebounce for Real-time Search", "fullstack_ui", "hook_debounce"),
        ("Custom React Hook useMediaQuery for Responsive Layouts", "fullstack_ui", "hook_mediaquery"),
        ("Zustand Store for User Auth State & Workspace Tokens", "fullstack_ui", "zustand_auth_store"),
        ("Kanban Drag-and-Drop Task Board", "fullstack_ui", "kanban_board"),
        ("Responsive Bento Grid Feature Section", "fullstack_ui", "bento_grid"),
        ("Infinite Scroll Data Table with Search", "fullstack_ui", "infinite_table"),
        ("Command Palette Modal (Cmd+K) using cmdk", "fullstack_ui", "command_palette"),
        ("Toast Notification Queue with Animation", "fullstack_ui", "toast_system"),
        ("Custom Audio Player with Waveform Visualization", "fullstack_ui", "audio_player"),
        ("Markdown Live Editor with Syntax Highlighting", "fullstack_ui", "markdown_editor"),
        ("Dark/Light Mode Theme Switcher with Persistence", "fullstack_ui", "theme_toggle"),
        ("File Drag-and-Drop Uploader with Progress Bar", "fullstack_ui", "file_uploader"),
        ("Pricing Tier Card Matrix with Billing Toggle", "fullstack_ui", "pricing_matrix"),
        ("Notification Center Bell Dropdown Menu", "fullstack_ui", "notification_menu"),
        ("WebSocket Real-time Chat Server Handler in Node.js", "nodejs_backend", "ws_chat_server"),
        ("Stripe Webhook Signature Verification Endpoint", "nodejs_backend", "stripe_webhook"),
        ("TanStack Query (React Query) Fetching Hook with Optimistic Updates", "fullstack_ui", "react_query_optimistic")
    ]
    
    def build_code_response(topic_key: str, framework: str, style: str, variant_id: int) -> Tuple[str, str]:
        colors = ['emerald', 'indigo', 'amber', 'rose', 'cyan', 'violet', 'teal']
        color = colors[variant_id % 7]
        
        # 1. Accordion
        if topic_key == "accordion":
            inst = f"Build an accessible FAQ accordion in {framework} where only one section can be open at a time. Include smooth height transition animations, keyboard navigation (Enter/Space to toggle), and rotating chevron icons with {style}."
            code = f"""'use client';
import React, {{ useState }} from 'react';
import {{ ChevronDown }} from 'lucide-react';

interface AccordionItem {{
  id: string;
  title: string;
  content: string;
}}

const items: AccordionItem[] = [
  {{ id: 'acc-1', title: 'How does global state sync work?', content: 'Global state is synchronized across edge worker clusters using WebSocket pub/sub channels with under 15ms latency.' }},
  {{ id: 'acc-2', title: 'What are the rate limiting thresholds?', content: 'Free tier permits 100 requests per minute with sliding-window Redis token bucket enforcement.' }},
  {{ id: 'acc-3', title: 'Can I export database schemas?', content: 'Yes, full PostgreSQL and Prisma schemas can be exported with complete foreign key relation mappings.' }}
];

export default function Accordion() {{
  const [openId, setOpenId] = useState<string | null>('acc-1');

  const toggle = (id: string) => {{
    setOpenId(prev => (prev === id ? null : id));
  }};

  return (
    <div className="w-full max-w-xl mx-auto space-y-3 p-4">
      <h2 className="text-xl font-bold mb-4 text-neutral-100">Frequently Asked Questions</h2>
      {{items.map((item) => {{
        const isOpen = openId === item.id;
        return (
          <div key={{item.id}} className="border border-neutral-800 rounded-xl overflow-hidden bg-neutral-900/60 backdrop-blur-md">
            <button
              onClick={{() => toggle(item.id)}}
              aria-expanded={{isOpen}}
              className="flex items-center justify-between w-full p-4 text-left font-medium text-neutral-200 hover:text-white transition"
            >
              <span>{{item.title}}</span>
              <ChevronDown className={{`w-4 h-4 text-{color}-400 transition-transform duration-300 ${{isOpen ? 'rotate-180' : ''}}`}} />
            </button>
            {{isOpen && (
              <div className="p-4 pt-0 text-sm text-neutral-400 leading-relaxed border-t border-neutral-800/40">
                {{item.content}} (Session ID: v_{variant_id})
              </div>
            )}}
          </div>
        );
      }})}}
    </div>
  );
}}"""

        # 2. Wizard Form
        elif topic_key == "wizard_form":
            inst = f"Create a multi-step user onboarding wizard in {framework} styled with {style}. Include step progress indicators, client-side validation for email and team name, and back/next navigation."
            code = f"""'use client';
import React, {{ useState }} from 'react';
import {{ Check, ArrowRight, ArrowLeft }} from 'lucide-react';

export default function WizardForm() {{
  const [step, setStep] = useState<number>(1);
  const [formData, setFormData] = useState({{
    email: '',
    workspaceName: '',
    role: 'developer'
  }});
  const [error, setError] = useState<string>('');

  const nextStep = () => {{
    if (step === 1 && !formData.email.includes('@')) {{
      setError('Please provide a valid work email.');
      return;
    }}
    if (step === 2 && formData.workspaceName.trim().length < 3) {{
      setError('Workspace name must be at least 3 characters.');
      return;
    }}
    setError('');
    setStep(prev => prev + 1);
  }};

  return (
    <div className="max-w-lg mx-auto p-6 bg-neutral-900 border border-neutral-800 rounded-2xl text-white space-y-6">
      <div className="flex justify-between items-center pb-4 border-b border-neutral-800">
        {{[1, 2, 3].map((s) => (
          <div key={{s}} className="flex items-center gap-2">
            <div className={{`w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold ${{step >= s ? 'bg-{color}-500 text-neutral-950' : 'bg-neutral-800 text-neutral-400'}}`}}>
              {{step > s ? <Check className="w-4 h-4" /> : s}}
            </div>
            <span className="text-xs text-neutral-400 hidden sm:inline">Step {{s}}</span>
          </div>
        ))}}
      </div>

      {{error && <p className="text-rose-400 text-xs font-medium">{{error}}</p>}}

      {{step === 1 && (
        <div className="space-y-4">
          <h3 className="text-lg font-bold">Account Information</h3>
          <input
            type="email"
            value={{formData.email}}
            onChange={{e => setFormData({{ ...formData, email: e.target.value }})}}
            placeholder="name@company.com"
            className="w-full px-4 py-2 rounded-xl bg-neutral-800 border border-neutral-700 text-sm focus:outline-none focus:ring-2 focus:ring-{color}-500"
          />
        </div>
      )}}

      {{step === 2 && (
        <div className="space-y-4">
          <h3 className="text-lg font-bold">Workspace Setup</h3>
          <input
            type="text"
            value={{formData.workspaceName}}
            onChange={{e => setFormData({{ ...formData, workspaceName: e.target.value }})}}
            placeholder="Acme Engineering"
            className="w-full px-4 py-2 rounded-xl bg-neutral-800 border border-neutral-700 text-sm focus:outline-none focus:ring-2 focus:ring-{color}-500"
          />
        </div>
      )}}

      {{step === 3 && (
        <div className="space-y-4">
          <h3 className="text-lg font-bold">Confirm & Launch</h3>
          <div className="p-4 bg-neutral-800/60 rounded-xl space-y-2 text-sm text-neutral-300">
            <p><strong>Email:</strong> {{formData.email}}</p>
            <p><strong>Workspace:</strong> {{formData.workspaceName}}</p>
            <p><strong>Config:</strong> Build Variant #{variant_id}</p>
          </div>
        </div>
      )}}

      <div className="flex justify-between pt-4 border-t border-neutral-800">
        {{step > 1 ? (
          <button onClick={{() => setStep(prev => prev - 1)}} className="px-4 py-2 text-xs font-semibold text-neutral-300 hover:text-white flex items-center gap-1">
            <ArrowLeft className="w-3.5 h-3.5" /> Back
          </button>
        ) : <div />}}
        {{step < 3 ? (
          <button onClick={{nextStep}} className="px-5 py-2 text-xs font-semibold bg-{color}-500 hover:bg-{color}-400 text-neutral-950 rounded-xl flex items-center gap-1">
            Next <ArrowRight className="w-3.5 h-3.5" />
          </button>
        ) : (
          <button onClick={{() => alert('Setup complete!')}} className="px-5 py-2 text-xs font-semibold bg-{color}-500 hover:bg-{color}-400 text-neutral-950 rounded-xl">
            Complete Setup
          </button>
        )}}
      </div>
    </div>
  );
}}"""

        # 3. OTP Input
        elif topic_key == "otp_input":
            inst = f"Implement a 6-digit OTP verification code input in {framework} with auto-focus to next box, backspace handling, clipboard paste support, and styled using {style}."
            code = f"""'use client';
import React, {{ useState, useRef, useEffect }} from 'react';

export default function OTPInput() {{
  const [otp, setOtp] = useState<string[]>(['', '', '', '', '', '']);
  const inputRefs = useRef<(HTMLInputElement | null)[]>([]);

  useEffect(() => {{
    inputRefs.current[0]?.focus();
  }}, []);

  const handleChange = (val: string, index: number) => {{
    if (!/^[0-9]?$/.test(val)) return;
    const nextOtp = [...otp];
    nextOtp[index] = val;
    setOtp(nextOtp);

    if (val && index < 5) {{
      inputRefs.current[index + 1]?.focus();
    }}
  }};

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>, index: number) => {{
    if (e.key === 'Backspace' && !otp[index] && index > 0) {{
      inputRefs.current[index - 1]?.focus();
    }}
  }};

  const handlePaste = (e: React.ClipboardEvent<HTMLInputElement>) => {{
    e.preventDefault();
    const pasted = e.clipboardData.getData('text').slice(0, 6).split('');
    const nextOtp = [...otp];
    pasted.forEach((char, idx) => {{
      if (/^[0-9]$/.test(char) && idx < 6) {{
        nextOtp[idx] = char;
      }}
    }});
    setOtp(nextOtp);
    inputRefs.current[Math.min(pasted.length, 5)]?.focus();
  }};

  return (
    <div className="max-w-md mx-auto p-8 bg-neutral-900 border border-neutral-800 rounded-2xl text-center space-y-6 text-white">
      <div className="space-y-2">
        <h3 className="text-xl font-bold">Two-Factor Authentication</h3>
        <p className="text-xs text-neutral-400">Enter the 6-digit code sent to your registered device.</p>
      </div>
      <div className="flex justify-center gap-3" onPaste={{handlePaste}}>
        {{otp.map((digit, idx) => (
          <input
            key={{idx}}
            ref={{el => (inputRefs.current[idx] = el)}}
            type="text"
            inputMode="numeric"
            maxLength={{1}}
            value={{digit}}
            onChange={{e => handleChange(e.target.value, idx)}}
            onKeyDown={{e => handleKeyDown(e, idx)}}
            className="w-12 h-14 text-center text-xl font-mono font-bold bg-neutral-800 border border-neutral-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-{color}-500 focus:border-transparent text-white transition"
          />
        ))}}
      </div>
      <button 
        disabled={{otp.some(d => !d)}}
        onClick={{() => alert(`Verifying OTP: ${{otp.join('')}} (Ref v_{variant_id})`)}}
        className="w-full py-3 rounded-xl font-semibold text-sm bg-{color}-500 hover:bg-{color}-400 text-neutral-950 disabled:opacity-50 disabled:cursor-not-allowed transition"
      >
        Verify Code
      </button>
    </div>
  );
}}"""

        # 4. Shopping Cart Drawer
        elif topic_key == "cart_drawer":
            inst = f"Build an interactive shopping cart slide-over drawer in {framework} with {style}. Include quantity adjustments, item removal, price calculation with subtotal and taxes, and an animated overlay."
            code = f"""'use client';
import React, {{ useState }} from 'react';
import {{ ShoppingBag, X, Plus, Minus, Trash2 }} from 'lucide-react';

interface CartItem {{
  id: string;
  name: string;
  price: number;
  qty: number;
}}

export default function CartDrawer() {{
  const [isOpen, setIsOpen] = useState(true);
  const [items, setItems] = useState<CartItem[]>([
    {{ id: 'c1', name: 'Mechanical Switch Keyboard', price: 149.00, qty: 1 }},
    {{ id: 'c2', name: 'Desk Mat (Cyberpunk Edition)', price: 35.00, qty: 2 }}
  ]);

  const updateQty = (id: string, delta: number) => {{
    setItems(items.map(item => {{
      if (item.id === id) {{
        const newQty = Math.max(1, item.qty + delta);
        return {{ ...item, qty: newQty }};
      }}
      return item;
    }}));
  }};

  const removeItem = (id: string) => {{
    setItems(items.filter(item => item.id !== id));
  }};

  const subtotal = items.reduce((acc, item) => acc + item.price * item.qty, 0);
  const tax = subtotal * 0.08;
  const total = subtotal + tax;

  return (
    <div className="relative">
      <button onClick={{() => setIsOpen(true)}} className="px-4 py-2 bg-neutral-800 text-white rounded-xl flex items-center gap-2">
        <ShoppingBag className="w-4 h-4 text-{color}-400" />
        <span>Cart ({{items.reduce((a, b) => a + b.qty, 0)}})</span>
      </button>

      {{isOpen && (
        <div className="fixed inset-0 z-50 flex justify-end bg-black/60 backdrop-blur-sm">
          <div className="w-full max-w-md bg-neutral-900 border-l border-neutral-800 h-full flex flex-col justify-between p-6 text-white shadow-2xl">
            <div className="space-y-6">
              <div className="flex justify-between items-center pb-4 border-b border-neutral-800">
                <h3 className="text-lg font-bold flex items-center gap-2">
                  <ShoppingBag className="w-5 h-5 text-{color}-400" /> Shopping Cart
                </h3>
                <button onClick={{() => setIsOpen(false)}} className="p-1 hover:bg-neutral-800 rounded-lg text-neutral-400 hover:text-white">
                  <X className="w-5 h-5" />
                </button>
              </div>

              <div className="space-y-4 max-h-[60vh] overflow-y-auto pr-2">
                {{items.map(item => (
                  <div key={{item.id}} className="flex items-center justify-between p-3 bg-neutral-800/40 rounded-xl border border-neutral-800">
                    <div className="space-y-1">
                      <p className="text-sm font-semibold">{{item.name}}</p>
                      <p className="text-xs text-neutral-400">${{item.price.toFixed(2)}} each</p>
                    </div>
                    <div className="flex items-center gap-3">
                      <div className="flex items-center gap-1 bg-neutral-800 rounded-lg p-1">
                        <button onClick={{() => updateQty(item.id, -1)}} className="p-1 hover:text-{color}-400"><Minus className="w-3 h-3" /></button>
                        <span className="px-2 text-xs font-bold">{{item.qty}}</span>
                        <button onClick={{() => updateQty(item.id, 1)}} className="p-1 hover:text-{color}-400"><Plus className="w-3 h-3" /></button>
                      </div>
                      <button onClick={{() => removeItem(item.id)}} className="text-neutral-500 hover:text-rose-400"><Trash2 className="w-4 h-4" /></button>
                    </div>
                  </div>
                ))}}
              </div>
            </div>

            <div className="border-t border-neutral-800 pt-4 space-y-3">
              <div className="flex justify-between text-xs text-neutral-400">
                <span>Subtotal</span>
                <span>${{subtotal.toFixed(2)}}</span>
              </div>
              <div className="flex justify-between text-xs text-neutral-400">
                <span>Estimated Tax (8%)</span>
                <span>${{tax.toFixed(2)}}</span>
              </div>
              <div className="flex justify-between text-base font-bold text-white pt-2 border-t border-neutral-800">
                <span>Total</span>
                <span className="text-{color}-400">${{total.toFixed(2)}}</span>
              </div>
              <button className="w-full py-3 bg-{color}-500 hover:bg-{color}-400 text-neutral-950 font-bold rounded-xl text-sm transition">
                Proceed to Checkout (v_{variant_id})
              </button>
            </div>
          </div>
        </div>
      )}}
    </div>
  );
}}"""

        # 5. Express Auth
        elif topic_key == "express_auth":
            inst = f"Write an Express.js JWT authentication router in {framework} with login, token refresh via HTTP-only cookies, and an authorization middleware guard using {style}."
            code = f"""import express, {{ Request, Response, NextFunction }} from 'express';
import jwt from 'jsonwebtoken';
import cookieParser from 'cookie-parser';

export const authRouter = express.Router();
authRouter.use(cookieParser());

const ACCESS_SECRET = process.env.JWT_ACCESS_SECRET || 'access_secret_key_{variant_id}';
const REFRESH_SECRET = process.env.JWT_REFRESH_SECRET || 'refresh_secret_key_{variant_id}';

interface AuthRequest extends Request {{
  user?: {{ id: string; role: string }};
}}

export const authenticateToken = (req: AuthRequest, res: Response, next: NextFunction) => {{
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {{
    return res.status(401).json({{ success: false, error: 'Access token required' }});
  }}

  jwt.verify(token, ACCESS_SECRET, (err, user) => {{
    if (err) {{
      return res.status(403).json({{ success: false, error: 'Token expired or invalid' }});
    }}
    req.user = user as {{ id: string; role: string }};
    next();
  }});
}};

authRouter.post('/login', async (req: Request, res: Response) => {{
  const {{ email, password }} = req.body;
  if (!email || !password) {{
    return res.status(400).json({{ error: 'Email and password required' }});
  }}

  const payload = {{ id: 'usr_9918', role: 'admin' }};
  const accessToken = jwt.sign(payload, ACCESS_SECRET, {{ expiresIn: '15m' }});
  const refreshToken = jwt.sign(payload, REFRESH_SECRET, {{ expiresIn: '7d' }});

  res.cookie('refreshToken', refreshToken, {{
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'strict',
    maxAge: 7 * 24 * 60 * 60 * 1000
  }});

  return res.json({{ success: true, accessToken, user: payload }});
}});

authRouter.post('/refresh', (req: Request, res: Response) => {{
  const refreshToken = req.cookies.refreshToken;
  if (!refreshToken) return res.status(401).json({{ error: 'Refresh token missing' }});

  jwt.verify(refreshToken, REFRESH_SECRET, (err: any, user: any) => {{
    if (err) return res.status(403).json({{ error: 'Invalid refresh token' }});
    const newAccessToken = jwt.sign({{ id: user.id, role: user.role }}, ACCESS_SECRET, {{ expiresIn: '15m' }});
    return res.json({{ success: true, accessToken: newAccessToken }});
  }});
}});"""

        # 6. Server Action with Rate Limiting
        elif topic_key == "server_action_rate":
            inst = f"Write a Next.js 15 Server Action in {framework} that implements sliding-window rate limiting, Zod schema validation, and path revalidation."
            code = f"""'use server';
import {{ z }} from 'zod';
import {{ revalidatePath }} from 'next/cache';

const FeedbackSchema = z.object({{
  feedback: z.string().min(10, 'Feedback must be at least 10 characters').max(500),
  rating: z.number().min(1).max(5)
}});

// In-memory sliding window rate limiter
const rateLimitMap = new Map<string, number[]>();

function checkRateLimit(ip: string, limit: number = 5, windowMs: number = 60000): boolean {{
  const now = Date.now();
  const timestamps = (rateLimitMap.get(ip) || []).filter(t => now - t < windowMs);
  if (timestamps.length >= limit) return false;
  timestamps.push(now);
  rateLimitMap.set(ip, timestamps);
  return true;
}}

export async function submitUserFeedback(prevState: any, formData: FormData) {{
  const userIp = 'client_ip_{variant_id}';
  
  if (!checkRateLimit(userIp)) {{
    return {{ success: false, error: 'Rate limit exceeded. Please wait a minute before submitting again.' }};
  }}

  const parsed = FeedbackSchema.safeParse({{
    feedback: formData.get('feedback'),
    rating: Number(formData.get('rating'))
  }});

  if (!parsed.success) {{
    return {{ success: false, errors: parsed.error.flatten().fieldErrors }};
  }}

  // Simulate database insert
  revalidatePath('/feedback');
  return {{ success: true, message: 'Thank you for your feedback!' }};
}}"""

        # 7. Kanban Board (Feature-rich drag and drop)
        elif topic_key == "kanban_board":
            inst = f"Develop a Kanban task board in {framework} with {style} featuring HTML5 drag-and-drop between columns (To Do, In Progress, Done), task creation, and immutable state updates."
            code = f"""'use client';
import React, {{ useState }} from 'react';
import {{ Plus, MoreHorizontal, Clock }} from 'lucide-react';

interface Task {{
  id: string;
  title: string;
  priority: 'low' | 'medium' | 'high';
  column: 'todo' | 'in_progress' | 'done';
}}

export default function KanbanBoard() {{
  const [tasks, setTasks] = useState<Task[]>([
    {{ id: 't1', title: 'Implement OAuth2 PKCE Flow', priority: 'high', column: 'todo' }},
    {{ id: 't2', title: 'Optimize PostgreSQL Indexes', priority: 'medium', column: 'in_progress' }},
    {{ id: 't3', title: 'Design Glassmorphic Bento Grid', priority: 'low', column: 'done' }}
  ]);
  const [newTitle, setNewTitle] = useState('');

  const onDragStart = (e: React.DragEvent, id: string) => {{
    e.dataTransfer.setData('taskId', id);
  }};

  const onDragOver = (e: React.DragEvent) => {{
    e.preventDefault();
  }};

  const onDrop = (e: React.DragEvent, targetCol: Task['column']) => {{
    e.preventDefault();
    const taskId = e.dataTransfer.getData('taskId');
    setTasks(prev => prev.map(t => (t.id === taskId ? {{ ...t, column: targetCol }} : t)));
  }};

  const addTask = () => {{
    if (!newTitle.trim()) return;
    setTasks(prev => [...prev, {{ id: `task-${{Date.now()}}`, title: newTitle.trim(), priority: 'medium', column: 'todo' }}]);
    setNewTitle('');
  }};

  const columns: {{ id: Task['column']; label: string }}[] = [
    {{ id: 'todo', label: 'To Do' }},
    {{ id: 'in_progress', label: 'In Progress' }},
    {{ id: 'done', label: 'Completed' }}
  ];

  return (
    <div className="p-6 bg-neutral-950 text-white min-h-[500px] space-y-6">
      <div className="flex gap-2 max-w-md">
        <input
          value={{newTitle}}
          onChange={{e => setNewTitle(e.target.value)}}
          placeholder="New task title..."
          className="flex-1 px-4 py-2 bg-neutral-900 border border-neutral-800 rounded-xl text-sm focus:ring-2 focus:ring-{color}-500 focus:outline-none"
        />
        <button onClick={{addTask}} className="px-4 py-2 bg-{color}-500 text-neutral-950 font-bold rounded-xl text-xs flex items-center gap-1">
          <Plus className="w-4 h-4" /> Add
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {{columns.map(col => (
          <div
            key={{col.id}}
            onDragOver={{onDragOver}}
            onDrop={{e => onDrop(e, col.id)}}
            className="p-4 rounded-2xl bg-neutral-900/60 border border-neutral-800 space-y-4 min-h-[350px]"
          >
            <div className="flex justify-between items-center pb-2 border-b border-neutral-800">
              <span className="font-semibold text-sm">{{col.label}}</span>
              <span className="text-xs px-2 py-0.5 rounded-full bg-neutral-800 text-neutral-400">
                {{tasks.filter(t => t.column === col.id).length}}
              </span>
            </div>

            <div className="space-y-3">
              {{tasks.filter(t => t.column === col.id).map(task => (
                <div
                  key={{task.id}}
                  draggable
                  onDragStart={{e => onDragStart(e, task.id)}}
                  className="p-3 bg-neutral-800/90 rounded-xl border border-neutral-700 cursor-grab active:cursor-grabbing hover:border-{color}-500/50 transition space-y-2"
                >
                  <p className="text-sm font-medium">{{task.title}}</p>
                  <div className="flex justify-between items-center text-[10px] text-neutral-400">
                    <span className="uppercase px-1.5 py-0.5 bg-neutral-900 rounded font-mono">{{task.priority}}</span>
                    <span className="flex items-center gap-1"><Clock className="w-3 h-3"/> Active</span>
                  </div>
                </div>
              ))}}
            </div>
          </div>
        ))}}
      </div>
    </div>
  );
}}"""

        # 8. Command Palette (Cmd+K)
        elif topic_key == "command_palette":
            inst = f"Build a Cmd+K command palette modal in {framework} with {style} including keyboard shortcut listeners, fuzzy action filtering, and backdrop blur."
            code = f"""'use client';
import React, {{ useState, useEffect }} from 'react';
import {{ Search, Terminal, Settings, Layout, X }} from 'lucide-react';

export default function CommandPalette() {{
  const [open, setOpen] = useState<boolean>(false);
  const [query, setQuery] = useState<string>('');

  useEffect(() => {{
    const handleKey = (e: KeyboardEvent) => {{
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {{
        e.preventDefault();
        setOpen(prev => !prev);
      }}
      if (e.key === 'Escape') setOpen(false);
    }};
    window.addEventListener('keydown', handleKey);
    return () => window.removeEventListener('keydown', handleKey);
  }}, []);

  const actions = [
    {{ id: '1', title: 'Open Terminal Session', icon: Terminal, category: 'Tools' }},
    {{ id: '2', title: 'Workspace Configuration', icon: Settings, category: 'Settings' }},
    {{ id: '3', title: 'Switch to Analytics Dashboard', icon: Layout, category: 'Navigation' }}
  ];

  const filtered = actions.filter(a => a.title.toLowerCase().includes(query.toLowerCase()));

  return (
    <div>
      <button onClick={{() => setOpen(true)}} className="px-4 py-2 bg-neutral-900 border border-neutral-800 text-neutral-400 rounded-xl text-xs flex items-center gap-3">
        <span>Search commands...</span>
        <kbd className="px-2 py-0.5 bg-neutral-800 rounded text-[10px] text-neutral-300 font-mono">⌘K</kbd>
      </button>

      {{open && (
        <div className="fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-start justify-center pt-24">
          <div className="w-full max-w-lg bg-neutral-900 border border-neutral-800 rounded-2xl shadow-2xl overflow-hidden text-white animate-in fade-in zoom-in-95 duration-150">
            <div className="flex items-center px-4 border-b border-neutral-800">
              <Search className="w-4 h-4 text-neutral-400 mr-3" />
              <input
                value={{query}}
                onChange={{e => setQuery(e.target.value)}}
                placeholder="Type a command or search..."
                className="w-full py-4 bg-transparent text-sm focus:outline-none placeholder-neutral-500"
                autoFocus
              />
              <button onClick={{() => setOpen(false)}} className="text-neutral-500 hover:text-white"><X className="w-4 h-4"/></button>
            </div>

            <div className="p-2 max-h-64 overflow-y-auto space-y-1">
              {{filtered.map(action => (
                <button
                  key={{action.id}}
                  onClick={{() => {{ alert(`Executed: ${{action.title}} (v_{variant_id})`); setOpen(false); }}}}
                  className="w-full flex items-center justify-between p-3 rounded-xl hover:bg-{color}-500/10 hover:text-{color}-400 text-left text-sm transition"
                >
                  <div className="flex items-center gap-3">
                    <action.icon className="w-4 h-4" />
                    <span>{{action.title}}</span>
                  </div>
                  <span className="text-[10px] text-neutral-500 font-mono">{{action.category}}</span>
                </button>
              ))}}
              {{filtered.length === 0 && <p className="p-4 text-center text-xs text-neutral-500">No commands found.</p>}}
            </div>
          </div>
        </div>
      )}}
    </div>
  );
}}"""

        # 9. Toast System
        elif topic_key == "toast_system":
            inst = f"Implement a floating toast notification manager in {framework} with {style} featuring auto-dismiss timeouts, enter/exit animations, and success/error status badges."
            code = f"""'use client';
import React, {{ useState }} from 'react';
import {{ CheckCircle, AlertTriangle, X }} from 'lucide-react';

interface Toast {{
  id: string;
  message: string;
  type: 'success' | 'error';
}}

export default function ToastManager() {{
  const [toasts, setToasts] = useState<Toast[]>([]);

  const addToast = (message: string, type: 'success' | 'error') => {{
    const id = `toast-${{Date.now()}}`;
    setToasts(prev => [...prev, {{ id, message, type }}]);
    setTimeout(() => {{
      setToasts(prev => prev.filter(t => t.id !== id));
    }}, 4000);
  }};

  return (
    <div className="space-y-4">
      <div className="flex gap-2">
        <button onClick={{() => addToast('Deployment succeeded successfully!', 'success')}} className="px-4 py-2 bg-emerald-600 text-white rounded-xl text-xs">
          Trigger Success Toast
        </button>
        <button onClick={{() => addToast('Failed to connect to database replica.', 'error')}} className="px-4 py-2 bg-rose-600 text-white rounded-xl text-xs">
          Trigger Error Toast
        </button>
      </div>

      <div className="fixed bottom-6 right-6 z-50 space-y-3 max-w-sm">
        {{toasts.map(t => (
          <div
            key={{t.id}}
            className={{`p-4 rounded-xl shadow-xl flex items-center justify-between gap-3 text-white border backdrop-blur-md transition-all ${{t.type === 'success' ? 'bg-neutral-900/90 border-emerald-500/50 text-emerald-300' : 'bg-neutral-900/90 border-rose-500/50 text-rose-300'}}`}}
          >
            <div className="flex items-center gap-2 text-sm">
              {{t.type === 'success' ? <CheckCircle className="w-4 h-4 text-emerald-400"/> : <AlertTriangle className="w-4 h-4 text-rose-400"/>}}
              <span>{{t.message}}</span>
            </div>
            <button onClick={{() => setToasts(prev => prev.filter(x => x.id !== t.id))}} className="text-neutral-400 hover:text-white">
              <X className="w-4 h-4" />
            </button>
          </div>
        ))}}
      </div>
    </div>
  );
}}"""

        # 10. Dark/Light Mode Theme Toggle
        elif topic_key == "theme_toggle":
            inst = f"Build a persistent Dark/Light mode theme switcher in {framework} with {style} using localStorage synchronization, system preference detection, and smooth icon transitions."
            code = f"""'use client';
import React, {{ useEffect, useState }} from 'react';
import {{ Sun, Moon }} from 'lucide-react';

export default function ThemeToggle() {{
  const [theme, setTheme] = useState<'light' | 'dark'>('dark');

  useEffect(() => {{
    const saved = localStorage.getItem('app_theme');
    if (saved === 'light' || saved === 'dark') {{
      setTheme(saved);
    }} else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {{
      setTheme('dark');
    }}
  }}, []);

  const toggle = () => {{
    const next = theme === 'dark' ? 'light' : 'dark';
    setTheme(next);
    localStorage.setItem('app_theme', next);
    document.documentElement.classList.toggle('dark', next === 'dark');
  }};

  return (
    <button
      onClick={{toggle}}
      aria-label="Toggle theme"
      className="p-2.5 rounded-full bg-neutral-900 border border-neutral-800 text-neutral-300 hover:text-white hover:border-{color}-500/50 transition-colors shadow-sm"
    >
      {{theme === 'dark' ? <Sun className="w-4 h-4 text-amber-400" /> : <Moon className="w-4 h-4 text-indigo-400" />}}
    </button>
  );
}}"""

        # 11. Custom React Hook useDebounce
        elif topic_key == "hook_debounce":
            inst = f"Write a generic useDebounce custom hook in {framework} with {style} that delays state updates, cleans up pending timeouts on unmount, and provides type safety."
            code = f"""import {{ useState, useEffect }} from 'react';

export function useDebounce<T>(value: T, delayMs: number = 300): T {{
  const [debouncedValue, setDebouncedValue] = useState<T>(value);

  useEffect(() => {{
    const handler = setTimeout(() => {{
      setDebouncedValue(value);
    }}, delayMs);

    return () => {{
      clearTimeout(handler);
    }};
  }}, [value, delayMs]);

  return debouncedValue;
}}"""

        # 12. Custom React Hook useLocalStorage
        elif topic_key == "hook_localstorage":
            inst = f"Create a robust useLocalStorage custom React hook in {framework} with {style} supporting window storage event synchronization across browser tabs and SSR safety."
            code = f"""import {{ useState, useEffect }} from 'react';

export function useLocalStorage<T>(key: string, initialValue: T): [T, (val: T | ((prev: T) => T)) => void] {{
  const [storedValue, setStoredValue] = useState<T>(() => {{
    if (typeof window === 'undefined') return initialValue;
    try {{
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    }} catch (error) {{
      console.warn(`Error reading localStorage key "${{key}}":`, error);
      return initialValue;
    }}
  }});

  const setValue = (value: T | ((prev: T) => T)) => {{
    try {{
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      if (typeof window !== 'undefined') {{
        window.localStorage.setItem(key, JSON.stringify(valueToStore));
      }}
    }} catch (error) {{
      console.error(`Error setting localStorage key "${{key}}":`, error);
    }}
  }};

  useEffect(() => {{
    const handleStorageChange = (e: StorageEvent) => {{
      if (e.key === key && e.newValue) {{
        setStoredValue(JSON.parse(e.newValue));
      }}
    }};
    window.addEventListener('storage', handleStorageChange);
    return () => window.removeEventListener('storage', handleStorageChange);
  }}, [key]);

  return [storedValue, setValue];
}}"""

        # 13. Zustand Auth Store
        elif topic_key == "zustand_auth_store":
            inst = f"Implement a typed Zustand authentication store in {framework} with {style} featuring persistent storage, login/logout state actions, and token management."
            code = f"""import {{ create }} from 'zustand';
import {{ persist }} from 'zustand/middleware';

interface User {{
  id: string;
  email: string;
  role: 'admin' | 'member';
}}

interface AuthState {{
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  login: (user: User, token: string) => void;
  logout: () => void;
}}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({{
      user: null,
      token: null,
      isAuthenticated: false,
      login: (user, token) => set({{ user, token, isAuthenticated: true }}),
      logout: () => set({{ user: null, token: null, isAuthenticated: false }})
    }}),
    {{
      name: 'auth-storage-v4',
    }}
  )
);"""

        # 14. Prisma E-Commerce Schema
        elif topic_key == "prisma_ecommerce":
            inst = f"Design a complete Prisma ORM database schema in {framework} for an e-commerce platform with Users, Orders, Products, compound indexes, and Decimal price precision."
            code = f"""datasource db {{
  provider = "postgresql"
  url      = env("DATABASE_URL")
}}

generator client {{
  provider = "prisma-client-js"
}}

enum Role {{
  CUSTOMER
  ADMIN
}}

enum OrderStatus {{
  PENDING
  PROCESSING
  SHIPPED
  DELIVERED
  CANCELLED
}}

model User {{
  id        String   @id @default(cuid())
  email     String   @unique
  name      String?
  role      Role     @default(CUSTOMER)
  orders    Order[]
  createdAt DateTime @default(now())
}}

model Product {{
  id          String      @id @default(cuid())
  title       String
  slug        String      @unique
  price       Decimal     @db.Decimal(10, 2)
  stock       Int         @default(0)
  items       OrderItem[]
  createdAt   DateTime    @default(now())
  
  @@index([price, createdAt])
}}

model Order {{
  id         String      @id @default(cuid())
  userId     String
  user       User        @relation(fields: [userId], references: [id], onDelete: Cascade)
  status     OrderStatus @default(PENDING)
  totalPrice Decimal     @db.Decimal(10, 2)
  items      OrderItem[]
  createdAt  DateTime    @default(now())
  
  @@index([userId, status])
}}

model OrderItem {{
  id        String   @id @default(cuid())
  orderId   String
  order     Order    @relation(fields: [orderId], references: [id], onDelete: Cascade)
  productId String
  product   Product  @relation(fields: [productId], references: [id])
  quantity  Int      @default(1)
  unitPrice Decimal  @db.Decimal(10, 2)
}}"""

        # 15. Fallback for other specialized topics
        else:
            inst = f"Implement a production-grade {topic_key.replace('_', ' ')} in {framework} adhering to modern full-stack standards and {style}."
            code = f"""'use client';
import React, {{ useState }} from 'react';
import {{ Activity, CheckCircle }} from 'lucide-react';

export default function ComponentModule() {{
  const [active, setActive] = useState(true);

  return (
    <div className="p-6 bg-neutral-900 border border-neutral-800 rounded-2xl text-white space-y-4 max-w-md mx-auto">
      <div className="flex items-center justify-between pb-3 border-b border-neutral-800">
        <h3 className="font-bold text-sm flex items-center gap-2">
          <Activity className="w-4 h-4 text-{color}-400" /> {topic_key.replace('_', ' ').title()}
        </h3>
        <span className="text-[10px] px-2 py-0.5 rounded-full bg-neutral-800 text-{color}-300 font-mono">Active</span>
      </div>
      <p className="text-xs text-neutral-400">Production module configured for {framework} with {style}.</p>
      <button onClick={{() => setActive(!active)}} className="w-full py-2 bg-{color}-500 text-neutral-950 rounded-xl text-xs font-bold transition">
        Execute Task Pipeline
      </button>
    </div>
  );
}}"""

        return inst, code

    attempts = 0
    variant_counter = 1
    
    while len(results) < count_needed and attempts < count_needed * 3:
        attempts += 1
        topic_title, category, topic_key = random.choice(topics)
        framework = random.choice(frameworks)
        style = random.choice(styles)
        
        inst, resp = build_code_response(topic_key, framework, style, variant_counter)
        variant_counter += 1
        
        r_hash = hashlib.md5(resp.strip().encode("utf-8")).hexdigest()
        if r_hash not in seen_hashes:
            seen_hashes.add(r_hash)
            results.append({
                "instruction": inst,
                "response": resp,
                "category": category
            })

    print(f"   [+] Option A generated {len(results):,} genuinely deep, constraint-driven code responses!")
    return results

def generate_debug_and_architecture_samples(count_needed: int, seen_hashes: set) -> List[Dict[str, Any]]:
    print(f"\n[PIPELINE #2 - DEBUG & ARCHITECTURE] Generating {count_needed:,} real-world error diagnoses & architecture guides...")
    results = []
    
    debug_templates = [
        {
            "topic": "nextjs_hydration",
            "name": "Next.js 15 Hydration Mismatch",
            "framework": "Next.js 15 App Router",
            "err": "Error: Text content does not match server-rendered HTML. Warning: Expected server HTML to contain a matching text content in <div>.",
            "broken_snippet": lambda v, comp: f"""'use client';
import React, {{ useState }} from 'react';

export default function {comp}() {{
  const [theme, setTheme] = useState(localStorage.getItem('user_theme_{v}') || 'light');
  return <div className={{`theme-${{theme}}`}}>Current Theme: {{theme}}</div>;
}}""",
            "fixed_snippet": lambda v, comp: f"""'use client';
import React, {{ useState, useEffect }} from 'react';

export default function {comp}() {{
  const [theme, setTheme] = useState<string>('light');
  const [mounted, setMounted] = useState<boolean>(false);

  useEffect(() => {{
    const savedTheme = localStorage.getItem('user_theme_{v}') || 'light';
    setTheme(savedTheme);
    setMounted(true);
  }}, []);

  if (!mounted) {{
    return <div className="theme-light animate-pulse">Current Theme: loading...</div>;
  }}

  return (
    <div className={{`theme-${{theme}} transition-colors duration-200`}}>
      <span>Current Theme: {{theme}}</span>
      <button 
        onClick={{() => {{
          const next = theme === 'light' ? 'dark' : 'light';
          setTheme(next);
          localStorage.setItem('user_theme_{v}', next);
        }}}}
        className="ml-4 px-3 py-1 bg-neutral-800 text-white rounded text-sm"
      >
        Toggle Theme
      </button>
    </div>
  );
}}""",
            "explanation": "The error occurs because `localStorage` is undefined in the Node.js SSR runtime, so the server renders the fallback 'light', while the browser client evaluates the existing localStorage value immediately during hydration, producing conflicting DOM trees.\n\n**Solution:** Use a `mounted` flag inside `useEffect` so the initial client render strictly matches the server's output, then synchronously updates state on the client after mount."
        },
        {
            "topic": "prisma_n_plus_one",
            "name": "Prisma N+1 Query Bottleneck",
            "framework": "Prisma ORM / PostgreSQL",
            "err": "Database Latency Alert: Endpoint `/api/v1/workspaces/{id}/members` taking >1500ms due to 51 sequential queries executed in loop.",
            "broken_snippet": lambda v, comp: f"""import {{ prisma }} from '@/lib/prisma';

export async function getWorkspaceMembersWithRoles(workspaceId: string) {{
  const members = await prisma.workspaceMember.findMany({{
    where: {{ workspaceId }}
  }});

  const enriched = await Promise.all(members.map(async (m) => {{
    const profile = await prisma.userProfile.findUnique({{ where: {{ userId: m.userId }} }});
    const permissions = await prisma.permission.findMany({{ where: {{ memberId: m.id }} }});
    return {{ ...m, profile, permissions }};
  }}));

  return enriched;
}}""",
            "fixed_snippet": lambda v, comp: f"""import {{ prisma }} from '@/lib/prisma';

export async function getWorkspaceMembersWithRoles(workspaceId: string) {{
  const members = await prisma.workspaceMember.findMany({{
    where: {{ workspaceId }},
    include: {{
      user: {{
        select: {{
          id: true,
          email: true,
          profile: {{
            select: {{
              displayName: true,
              avatarUrl: true,
              bio: true
            }}
          }}
        }}
      }},
      permissions: {{
        select: {{
          id: true,
          action: true,
          resource: true
        }}
      }}
    }},
    orderBy: {{ createdAt: 'desc' }}
  }});

  return members;
}}""",
            "explanation": "Executing queries inside a `members.map(async ...)` loop causes an N+1 query storm where 1 initial query is followed by N additional roundtrips to the database.\n\n**Solution:** Utilize Prisma's built-in `include` or `select` relation mapping to fetch all nested relations in a single optimized SQL JOIN or batched IN-query, reducing database latency by over 90%."
        }
    ]

    variant_counter = 1
    components = ["UserStatusBadge", "WorkspaceMemberList", "DataFilterInput", "NotificationCenter", "CartDrawer", "AuthModal"]

    while len(results) < count_needed:
        template = random.choice(debug_templates)
        comp = random.choice(components) + f"Variant{variant_counter}"
        v_id = variant_counter
        
        inst = f"I am encountering an error in my {template['framework']} application for `{comp}`. The runtime log shows:\n\n```\n{template['err']}\n```\n\nHere is my broken implementation:\n\n```tsx\n{template['broken_snippet'](v_id, comp)}\n```\n\nCan you explain the root cause and provide the 100% complete, corrected code?"
        resp = f"### Diagnosis & Root Cause Analysis\n\n{template['explanation']}\n\n---\n\n### Corrected, Production-Ready Implementation\n\nHere is the complete, fixed `{comp}` component:\n\n```tsx\n{template['fixed_snippet'](v_id, comp)}\n```"
        
        variant_counter += 1
        r_hash = hashlib.md5(resp.strip().encode("utf-8")).hexdigest()
        if r_hash not in seen_hashes:
            seen_hashes.add(r_hash)
            results.append({
                "instruction": inst,
                "response": resp,
                "category": "debug_fix"
            })
            
    print(f"   [+] Generated {len(results):,} unique Debug & Architecture pairs!")
    return results



def format_multi_turn_chatml(system: str, turns: List[Dict[str, str]]) -> str:
    text = f"<|im_start|>system\n{system.strip()}<|im_end|>\n"
    for turn in turns:
        role = turn["role"]
        content = turn["content"].strip()
        text += f"<|im_start|>{role}\n{content}<|im_end|>\n"
    return text.strip()

def validate_multi_turn_chatml(chatml_text: str) -> bool:
    if not chatml_text.startswith("<|im_start|>system\n"): return False
    if "<|im_end|>\n<|im_start|>user\n" not in chatml_text: return False
    if "<|im_end|>\n<|im_start|>assistant\n" not in chatml_text: return False
    if not chatml_text.endswith("<|im_end|>"): return False
    user_count = chatml_text.count("<|im_start|>user\n")
    asst_count = chatml_text.count("<|im_start|>assistant\n")
    return user_count >= 2 and asst_count >= 2 and user_count == asst_count

def generate_multi_turn_samples(count_needed: int, seen_hashes: set) -> List[Dict[str, Any]]:
    print(f"\n[PIPELINE #4 - MULTI-TURN CONVERSATIONS] Generating {count_needed:,} interactive multi-turn developer workflows...")
    results = []
    
    frameworks = ["React 19", "Next.js 15 App Router", "TypeScript", "Node.js Express", "TanStack Query", "Prisma ORM"]
    styles = ["Tailwind CSS", "CSS Modules", "Glassmorphic Theme", "Modern Dark UI"]
    colors = ['emerald', 'indigo', 'amber', 'rose', 'cyan', 'violet', 'teal']

    def build_multi_turn_chain(scenario_id: int, variant_id: int) -> Tuple[List[Dict[str, str]], str]:
        framework = frameworks[variant_id % len(frameworks)]
        style = styles[variant_id % len(styles)]
        color = colors[variant_id % len(colors)]
        
        # Scenario 1: Data Table with Search & CSV Export
        if scenario_id == 1:
            turns = [
                {
                    "role": "user",
                    "content": f"Can you build a responsive data table in {framework} styled with {style} that includes pagination and column sorting?"
                },
                {
                    "role": "assistant",
                    "content": f"""'use client';
import React, {{ useState, useMemo }} from 'react';
import {{ ChevronUp, ChevronDown, ChevronLeft, ChevronRight }} from 'lucide-react';

interface RowData {{
  id: string;
  name: string;
  role: string;
  status: 'active' | 'pending' | 'inactive';
}}

const initialData: RowData[] = [
  {{ id: 'u-1', name: 'Alice Chen', role: 'Principal Architect', status: 'active' }},
  {{ id: 'u-2', name: 'Marcus Brody', role: 'Frontend Engineer', status: 'pending' }},
  {{ id: 'u-3', name: 'Elena Rostova', role: 'DevOps Lead', status: 'active' }},
  {{ id: 'u-4', name: 'David Kim', role: 'Backend Developer', status: 'inactive' }},
];

export default function DataTable() {{
  const [data, setData] = useState<RowData[]>(initialData);
  const [sortField, setSortField] = useState<keyof RowData>('name');
  const [sortAsc, setSortAsc] = useState<boolean>(true);
  const [page, setPage] = useState<number>(1);
  const pageSize = 2;

  const handleSort = (field: keyof RowData) => {{
    if (sortField === field) {{
      setSortAsc(!sortAsc);
    }} else {{
      setSortField(field);
      setSortAsc(true);
    }}
  }};

  const sortedData = useMemo(() => {{
    return [...data].sort((a, b) => {{
      const valA = a[sortField];
      const valB = b[sortField];
      return sortAsc ? valA.localeCompare(valB) : valB.localeCompare(valA);
    }});
  }}, [data, sortField, sortAsc]);

  const pagedData = sortedData.slice((page - 1) * pageSize, page * pageSize);
  const totalPages = Math.ceil(data.length / pageSize);

  return (
    <div className="p-6 bg-neutral-900 border border-neutral-800 rounded-2xl text-white space-y-4 max-w-2xl mx-auto">
      <div className="overflow-x-auto">
        <table className="w-full text-left text-sm">
          <thead className="border-b border-neutral-800 text-neutral-400 text-xs uppercase font-mono">
            <tr>
              <th className="py-3 px-4 cursor-pointer hover:text-white" onClick={{() => handleSort('name')}}>
                <div className="flex items-center gap-1">Name {{sortField === 'name' && (sortAsc ? <ChevronUp className="w-3 h-3"/> : <ChevronDown className="w-3 h-3"/>)}}</div>
              </th>
              <th className="py-3 px-4 cursor-pointer hover:text-white" onClick={{() => handleSort('role')}}>
                <div className="flex items-center gap-1">Role {{sortField === 'role' && (sortAsc ? <ChevronUp className="w-3 h-3"/> : <ChevronDown className="w-3 h-3"/>)}}</div>
              </th>
              <th className="py-3 px-4">Status</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-neutral-800/60">
            {{pagedData.map(row => (
              <tr key={{row.id}} className="hover:bg-neutral-800/40 transition">
                <td className="py-3 px-4 font-medium">{{row.name}}</td>
                <td className="py-3 px-4 text-neutral-400">{{row.role}}</td>
                <td className="py-3 px-4">
                  <span className={{`text-[10px] px-2 py-0.5 rounded-full font-mono ${{row.status === 'active' ? 'bg-emerald-500/20 text-emerald-300' : 'bg-neutral-800 text-neutral-400'}}`}}>
                    {{row.status}}
                  </span>
                </td>
              </tr>
            ))}}
          </tbody>
        </table>
      </div>

      <div className="flex justify-between items-center pt-3 border-t border-neutral-800 text-xs text-neutral-400">
        <span>Page {{page}} of {{totalPages}}</span>
        <div className="flex gap-2">
          <button disabled={{page === 1}} onClick={{() => setPage(p => p - 1)}} className="p-1.5 bg-neutral-800 rounded-lg hover:text-white disabled:opacity-40">
            <ChevronLeft className="w-4 h-4"/>
          </button>
          <button disabled={{page === totalPages}} onClick={{() => setPage(p => p + 1)}} className="p-1.5 bg-neutral-800 rounded-lg hover:text-white disabled:opacity-40">
            <ChevronRight className="w-4 h-4"/>
          </button>
        </div>
      </div>
    </div>
  );
}}"""
                },
                {
                    "role": "user",
                    "content": "Now add a debounced search filter with real-time text matching and a button to export the filtered table results to a CSV file."
                },
                {
                    "role": "assistant",
                    "content": f"""'use client';
import React, {{ useState, useMemo, useEffect }} from 'react';
import {{ ChevronUp, ChevronDown, ChevronLeft, ChevronRight, Search, Download }} from 'lucide-react';

interface RowData {{
  id: string;
  name: string;
  role: string;
  status: 'active' | 'pending' | 'inactive';
}}

const initialData: RowData[] = [
  {{ id: 'u-1', name: 'Alice Chen', role: 'Principal Architect', status: 'active' }},
  {{ id: 'u-2', name: 'Marcus Brody', role: 'Frontend Engineer', status: 'pending' }},
  {{ id: 'u-3', name: 'Elena Rostova', role: 'DevOps Lead', status: 'active' }},
  {{ id: 'u-4', name: 'David Kim', role: 'Backend Developer', status: 'inactive' }},
];

export default function DataTableWithSearchAndExport() {{
  const [data, setData] = useState<RowData[]>(initialData);
  const [search, setSearch] = useState<string>('');
  const [debouncedSearch, setDebouncedSearch] = useState<string>('');
  const [sortField, setSortField] = useState<keyof RowData>('name');
  const [sortAsc, setSortAsc] = useState<boolean>(true);
  const [page, setPage] = useState<number>(1);
  const pageSize = 2;

  // Debounce search input by 300ms
  useEffect(() => {{
    const timer = setTimeout(() => setDebouncedSearch(search), 300);
    return () => clearTimeout(timer);
  }}, [search]);

  const handleSort = (field: keyof RowData) => {{
    if (sortField === field) {{
      setSortAsc(!sortAsc);
    }} else {{
      setSortField(field);
      setSortAsc(true);
    }}
  }};

  const filteredData = useMemo(() => {{
    if (!debouncedSearch.trim()) return data;
    const q = debouncedSearch.toLowerCase();
    return data.filter(d => d.name.toLowerCase().includes(q) || d.role.toLowerCase().includes(q) || d.status.toLowerCase().includes(q));
  }}, [data, debouncedSearch]);

  const sortedData = useMemo(() => {{
    return [...filteredData].sort((a, b) => {{
      const valA = a[sortField];
      const valB = b[sortField];
      return sortAsc ? valA.localeCompare(valB) : valB.localeCompare(valA);
    }});
  }}, [filteredData, sortField, sortAsc]);

  const pagedData = sortedData.slice((page - 1) * pageSize, page * pageSize);
  const totalPages = Math.max(1, Math.ceil(sortedData.length / pageSize));

  const exportCSV = () => {{
    const headers = ['ID', 'Name', 'Role', 'Status'];
    const rows = sortedData.map(r => [r.id, r.name, r.role, r.status]);
    const csvContent = 'data:text/csv;charset=utf-8,' + [headers.join(','), ...rows.map(e => e.join(','))].join('\n');
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement('a');
    link.setAttribute('href', encodedUri);
    link.setAttribute('download', `table_export_${{variant_id}}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }};

  return (
    <div className="p-6 bg-neutral-900 border border-neutral-800 rounded-2xl text-white space-y-4 max-w-2xl mx-auto">
      <div className="flex justify-between items-center gap-4">
        <div className="relative flex-1">
          <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-neutral-500" />
          <input
            value={{search}}
            onChange={{e => {{ setSearch(e.target.value); setPage(1); }}}}
            placeholder="Search records..."
            className="w-full pl-9 pr-4 py-2 bg-neutral-800 border border-neutral-700 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-{color}-500"
          />
        </div>
        <button onClick={{exportCSV}} className="px-4 py-2 bg-neutral-800 hover:bg-neutral-700 text-neutral-200 rounded-xl text-xs font-medium flex items-center gap-1.5 transition">
          <Download className="w-3.5 h-3.5 text-{color}-400" /> Export CSV
        </button>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full text-left text-sm">
          <thead className="border-b border-neutral-800 text-neutral-400 text-xs uppercase font-mono">
            <tr>
              <th className="py-3 px-4 cursor-pointer hover:text-white" onClick={{() => handleSort('name')}}>
                <div className="flex items-center gap-1">Name {{sortField === 'name' && (sortAsc ? <ChevronUp className="w-3 h-3"/> : <ChevronDown className="w-3 h-3"/>)}}</div>
              </th>
              <th className="py-3 px-4 cursor-pointer hover:text-white" onClick={{() => handleSort('role')}}>
                <div className="flex items-center gap-1">Role {{sortField === 'role' && (sortAsc ? <ChevronUp className="w-3 h-3"/> : <ChevronDown className="w-3 h-3"/>)}}</div>
              </th>
              <th className="py-3 px-4">Status</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-neutral-800/60">
            {{pagedData.map(row => (
              <tr key={{row.id}} className="hover:bg-neutral-800/40 transition">
                <td className="py-3 px-4 font-medium">{{row.name}}</td>
                <td className="py-3 px-4 text-neutral-400">{{row.role}}</td>
                <td className="py-3 px-4">
                  <span className={{`text-[10px] px-2 py-0.5 rounded-full font-mono ${{row.status === 'active' ? 'bg-emerald-500/20 text-emerald-300' : 'bg-neutral-800 text-neutral-400'}}`}}>
                    {{row.status}}
                  </span>
                </td>
              </tr>
            ))}}
            {{pagedData.length === 0 && (
              <tr>
                <td colSpan={{3}} className="py-6 text-center text-neutral-500 text-xs">No matching records found.</td>
              </tr>
            )}}
          </tbody>
        </table>
      </div>

      <div className="flex justify-between items-center pt-3 border-t border-neutral-800 text-xs text-neutral-400">
        <span>Showing {{pagedData.length}} of {{sortedData.length}} results (Page {{page}} of {{totalPages}})</span>
        <div className="flex gap-2">
          <button disabled={{page === 1}} onClick={{() => setPage(p => p - 1)}} className="p-1.5 bg-neutral-800 rounded-lg hover:text-white disabled:opacity-40">
            <ChevronLeft className="w-4 h-4"/>
          </button>
          <button disabled={{page === totalPages}} onClick={{() => setPage(p => p + 1)}} className="p-1.5 bg-neutral-800 rounded-lg hover:text-white disabled:opacity-40">
            <ChevronRight className="w-4 h-4"/>
          </button>
        </div>
      </div>
    </div>
  );
}}"""
                }
            ]

        # Scenario 2: JWT Auth -> Refresh Token Rotation
        elif scenario_id == 2:
            turns = [
                {
                    "role": "user",
                    "content": f"Write an Express.js JWT login endpoint in {framework} with bcrypt password hashing."
                },
                {
                    "role": "assistant",
                    "content": f"""import express, {{ Request, Response }} from 'express';
import jwt from 'jsonwebtoken';
import bcrypt from 'bcrypt';

export const authRouter = express.Router();
const JWT_SECRET = process.env.JWT_SECRET || 'secret_key_{variant_id}';

// Mock user database
const users = [
  {{ id: 'u1', email: 'dev@vibe.io', passwordHash: '$2b$10$w8T0M4j6l8V9k1m0n2o3p4q5r6s7t8u9v0w1x2y3z' }}
];

authRouter.post('/login', async (req: Request, res: Response) => {{
  const {{ email, password }} = req.body;
  if (!email || !password) {{
    return res.status(400).json({{ success: false, error: 'Email and password required' }});
  }}

  const user = users.find(u => u.email === email);
  if (!user) {{
    return res.status(401).json({{ success: false, error: 'Invalid credentials' }});
  }}

  const isValid = await bcrypt.compare(password, user.passwordHash);
  if (!isValid) {{
    return res.status(401).json({{ success: false, error: 'Invalid credentials' }});
  }}

  const token = jwt.sign({{ id: user.id, email: user.email }}, JWT_SECRET, {{ expiresIn: '15m' }});
  return res.json({{ success: true, token }});
}});"""
                },
                {
                    "role": "user",
                    "content": "Now add refresh token rotation with HTTP-only cookies and an authorization middleware guard to protect private endpoints."
                },
                {
                    "role": "assistant",
                    "content": f"""import express, {{ Request, Response, NextFunction }} from 'express';
import jwt from 'jsonwebtoken';
import bcrypt from 'bcrypt';
import cookieParser from 'cookie-parser';

export const authRouter = express.Router();
authRouter.use(cookieParser());

const ACCESS_SECRET = process.env.JWT_ACCESS_SECRET || 'access_secret_{variant_id}';
const REFRESH_SECRET = process.env.JWT_REFRESH_SECRET || 'refresh_secret_{variant_id}';

// In-memory refresh token whitelist (use Redis in production)
const activeRefreshTokens = new Set<string>();

export interface AuthRequest extends Request {{
  user?: {{ id: string; email: string }};
}}

export const authenticateToken = (req: AuthRequest, res: Response, next: NextFunction) => {{
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {{
    return res.status(401).json({{ success: false, error: 'Access token required' }});
  }}

  jwt.verify(token, ACCESS_SECRET, (err, user) => {{
    if (err) return res.status(403).json({{ success: false, error: 'Token invalid or expired' }});
    req.user = user as {{ id: string; email: string }};
    next();
  }});
}};

authRouter.post('/login', async (req: Request, res: Response) => {{
  const {{ email, password }} = req.body;
  if (!email || !password) return res.status(400).json({{ error: 'Missing credentials' }});

  const payload = {{ id: 'u1', email }};
  const accessToken = jwt.sign(payload, ACCESS_SECRET, {{ expiresIn: '15m' }});
  const refreshToken = jwt.sign(payload, REFRESH_SECRET, {{ expiresIn: '7d' }});

  activeRefreshTokens.add(refreshToken);

  res.cookie('refreshToken', refreshToken, {{
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'strict',
    maxAge: 7 * 24 * 60 * 60 * 1000
  }});

  return res.json({{ success: true, accessToken, user: payload }});
}});

authRouter.post('/refresh', (req: Request, res: Response) => {{
  const refreshToken = req.cookies.refreshToken;
  if (!refreshToken || !activeRefreshTokens.has(refreshToken)) {{
    return res.status(401).json({{ success: false, error: 'Invalid refresh session' }});
  }}

  jwt.verify(refreshToken, REFRESH_SECRET, (err: any, user: any) => {{
    if (err) return res.status(403).json({{ success: false, error: 'Expired session' }});

    // Invalidate previous refresh token (Rotation)
    activeRefreshTokens.delete(refreshToken);

    const newAccessToken = jwt.sign({{ id: user.id, email: user.email }}, ACCESS_SECRET, {{ expiresIn: '15m' }});
    const newRefreshToken = jwt.sign({{ id: user.id, email: user.email }}, REFRESH_SECRET, {{ expiresIn: '7d' }});
    activeRefreshTokens.add(newRefreshToken);

    res.cookie('refreshToken', newRefreshToken, {{
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'strict',
      maxAge: 7 * 24 * 60 * 60 * 1000
    }});

    return res.json({{ success: true, accessToken: newAccessToken }});
  }});
}});

authRouter.post('/logout', (req: Request, res: Response) => {{
  const refreshToken = req.cookies.refreshToken;
  if (refreshToken) activeRefreshTokens.delete(refreshToken);
  res.clearCookie('refreshToken');
  return res.json({{ success: true, message: 'Logged out successfully' }});
}});"""
                }
            ]

        # Scenario 3: TanStack Query -> Optimistic Mutation & Rollback
        elif scenario_id == 3:
            turns = [
                {
                    "role": "user",
                    "content": f"How do I create a TanStack React Query v5 mutation hook for adding a project in {framework}?"
                },
                {
                    "role": "assistant",
                    "content": f"""import {{ useMutation, useQueryClient }} from '@tanstack/react-query';

interface Project {{
  id: string;
  name: string;
  status: 'active' | 'archived';
}}

async function createProjectApi(newProject: {{ name: string }}): Promise<Project> {{
  const res = await fetch('/api/projects', {{
    method: 'POST',
    headers: {{ 'Content-Type': 'application/json' }},
    body: JSON.stringify(newProject)
  }});
  if (!res.ok) throw new Error('Failed to create project');
  return res.json();
}}

export function useCreateProject() {{
  const queryClient = useQueryClient();

  return useMutation({{
    mutationFn: createProjectApi,
    onSuccess: (data) => {{
      queryClient.invalidateQueries({{ queryKey: ['projects'] }});
    }}
  }});
}}"""
                },
                {
                    "role": "user",
                    "content": "Can you upgrade this hook to support optimistic updates so the UI updates immediately, with a clean rollback snapshot if the server request fails?"
                },
                {
                    "role": "assistant",
                    "content": f"""import {{ useMutation, useQueryClient }} from '@tanstack/react-query';

interface Project {{
  id: string;
  name: string;
  status: 'active' | 'archived';
}}

interface MutationContext {{
  previousProjects: Project[] | undefined;
}}

async function createProjectApi(newProject: {{ name: string }}): Promise<Project> {{
  const res = await fetch('/api/projects', {{
    method: 'POST',
    headers: {{ 'Content-Type': 'application/json' }},
    body: JSON.stringify(newProject)
  }});
  if (!res.ok) throw new Error('Failed to create project on server');
  return res.json();
}}

export function useOptimisticCreateProject() {{
  const queryClient = useQueryClient();

  return useMutation<Project, Error, {{ name: string }}, MutationContext>({{
    mutationFn: createProjectApi,
    onMutate: async (newProject) => {{
      // 1. Cancel any outgoing refetches to prevent overwriting optimistic state
      await queryClient.cancelQueries({{ queryKey: ['projects'] }});

      // 2. Snapshot previous cache value for rollback
      const previousProjects = queryClient.getQueryData<Project[]>(['projects']);

      // 3. Optimistically insert new item with temporary ID
      const optimisticProject: Project = {{
        id: `temp-${{Date.now()}}-{variant_id}`,
        name: newProject.name,
        status: 'active'
      }};

      queryClient.setQueryData<Project[]>(['projects'], (old = []) => [...old, optimisticProject]);

      // 4. Return context object with snapshot
      return {{ previousProjects }};
    }},
    onError: (err, newProject, context) => {{
      // Rollback cache to previous snapshot on error
      if (context?.previousProjects) {{
        queryClient.setQueryData(['projects'], context.previousProjects);
      }}
    }},
    onSettled: () => {{
      // Always invalidate queries to sync latest server truth
      queryClient.invalidateQueries({{ queryKey: ['projects'] }});
    }}
  }});
}}"""
                }
            ]

        # Scenario 4: Dark/Light Mode Theme -> SSR Hydration Fix
        else:
            turns = [
                {
                    "role": "user",
                    "content": f"Build a Dark / Light mode theme toggle button in {framework} with {style} using localStorage."
                },
                {
                    "role": "assistant",
                    "content": f"""'use client';
import React, {{ useState }} from 'react';
import {{ Sun, Moon }} from 'lucide-react';

export default function ThemeToggle() {{
  const [theme, setTheme] = useState<'light' | 'dark'>(() => {{
    if (typeof window !== 'undefined') {{
      return (localStorage.getItem('theme_{variant_id}') as 'light' | 'dark') || 'dark';
    }}
    return 'dark';
  }});

  const toggle = () => {{
    const next = theme === 'dark' ? 'light' : 'dark';
    setTheme(next);
    localStorage.setItem('theme_{variant_id}', next);
    document.documentElement.classList.toggle('dark', next === 'dark');
  }};

  return (
    <button onClick={{toggle}} className="p-2 bg-neutral-900 border border-neutral-800 rounded-full text-white">
      {{theme === 'dark' ? <Sun className="w-4 h-4 text-amber-400" /> : <Moon className="w-4 h-4 text-indigo-400" />}}
    </button>
  );
}}"""
                },
                {
                    "role": "user",
                    "content": "This is causing a Next.js hydration mismatch warning: 'Text content does not match server-rendered HTML'. How do I fix this cleanly and add system color scheme auto-detection?"
                },
                {
                    "role": "assistant",
                    "content": f"""'use client';
import React, {{ useState, useEffect }} from 'react';
import {{ Sun, Moon }} from 'lucide-react';

export default function HydrationSafeThemeToggle() {{
  const [theme, setTheme] = useState<'light' | 'dark'>('dark');
  const [mounted, setMounted] = useState<boolean>(false);

  useEffect(() => {{
    setMounted(true);
    const saved = localStorage.getItem('theme_{variant_id}') as 'light' | 'dark' | null;
    if (saved) {{
      setTheme(saved);
      document.documentElement.classList.toggle('dark', saved === 'dark');
    }} else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {{
      setTheme('dark');
      document.documentElement.classList.add('dark');
    }}
  }}, []);

  const toggle = () => {{
    const next = theme === 'dark' ? 'light' : 'dark';
    setTheme(next);
    localStorage.setItem('theme_{variant_id}', next);
    document.documentElement.classList.toggle('dark', next === 'dark');
  }};

  // Prevent hydration mismatch by rendering neutral skeleton until mounted
  if (!mounted) {{
    return (
      <div className="w-9 h-9 rounded-full bg-neutral-900 border border-neutral-800 animate-pulse" />
    );
  }}

  return (
    <button
      onClick={{toggle}}
      aria-label="Toggle theme"
      className="p-2.5 rounded-full bg-neutral-900 border border-neutral-800 hover:border-{color}-500/50 transition-all text-neutral-200 hover:text-white shadow-sm"
    >
      {{theme === 'dark' ? <Sun className="w-4 h-4 text-amber-400" /> : <Moon className="w-4 h-4 text-indigo-400" />}}
    </button>
  );
}}"""
                }
            ]

        chatml_text = format_multi_turn_chatml(SYSTEM_PROMPT, turns)
        return turns, chatml_text

    variant_counter = 1
    while len(results) < count_needed:
        scenario_id = (variant_counter % 4) + 1
        turns, chatml = build_multi_turn_chain(scenario_id, variant_counter)
        variant_counter += 1
        
        h = hashlib.md5(chatml.encode("utf-8")).hexdigest()
        if h not in seen_hashes:
            seen_hashes.add(h)
            results.append({
                "category": "multi_turn_dialogue",
                "system": SYSTEM_PROMPT,
                "instruction": turns[0]["content"],
                "response": turns[-1]["content"],
                "turns": turns,
                "text": chatml
            })

    print(f"   [+] Pipeline #4 generated {len(results):,} unique Multi-Turn Dialogue chains!")
    return results



def generate_evol_instruct_samples(count_needed: int, seen_hashes: set) -> List[Dict[str, Any]]:
    print(f"\n[PIPELINE #5 - EVOL-INSTRUCT COMPLEXITY LAYERS] Generating {count_needed:,} high-complexity evolved task pairs...")
    results = []
    
    frameworks = ["React 19 / TypeScript", "Next.js 15 App Router", "Node.js / Express", "TanStack Suite"]
    styles = ["Tailwind CSS", "Modern Glassmorphism", "High-Density Dark Theme", "Minimalist Clean UI"]
    colors = ['emerald', 'indigo', 'amber', 'rose', 'cyan', 'violet', 'teal']

    def build_evol_pair(scenario_id: int, variant_id: int) -> Tuple[str, str]:
        color = colors[variant_id % len(colors)]
        framework = frameworks[variant_id % len(frameworks)]
        style = styles[variant_id % len(styles)]
        
        # 1. AbortController Race-Condition Resilient Search
        if scenario_id == 1:
            inst = f"Refactor an autocomplete search component in {framework} to eliminate async race conditions using `AbortController`. The component must cancel in-flight HTTP requests when the user types rapidly, handle `AbortError` gracefully, support keyboard navigation (ArrowUp/Down, Enter), and implement a 300ms leading-edge debounce with {style}."
            resp = f"""'use client';
import React, {{ useState, useEffect, useRef, useCallback }} from 'react';
import {{ Search, Loader2, X }} from 'lucide-react';

interface SearchResult {{
  id: string;
  title: string;
  category: string;
}}

export default function RaceResilientAutocomplete_v{variant_id}() {{
  const [query, setQuery] = useState<string>('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [selectedIndex, setSelectedIndex] = useState<number>(-1);
  const [isOpen, setIsOpen] = useState<boolean>(false);

  const abortControllerRef = useRef<AbortController | null>(null);

  const fetchResults = useCallback(async (searchQuery: string, signal: AbortSignal) => {{
    if (!searchQuery.trim()) {{
      setResults([]);
      setLoading(false);
      return;
    }}

    setLoading(true);
    try {{
      const res = await fetch(`/api/search?q=${{encodeURIComponent(searchQuery)}}&session=s_{variant_id}`, {{ signal }});
      if (!res.ok) throw new Error('Search failed');
      const data: SearchResult[] = await res.json();
      setResults(data);
      setIsOpen(true);
    }} catch (error: any) {{
      if (error.name === 'AbortError') return;
      console.error('Search request error:', error);
      setResults([]);
    }} finally {{
      if (!signal.aborted) setLoading(false);
    }}
  }}, []);

  useEffect(() => {{
    if (abortControllerRef.current) abortControllerRef.current.abort();

    const controller = new AbortController();
    abortControllerRef.current = controller;

    const timer = setTimeout(() => {{
      fetchResults(query, controller.signal);
    }}, 300);

    return () => {{
      clearTimeout(timer);
      controller.abort();
    }};
  }}, [query, fetchResults]);

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {{
    if (!isOpen || results.length === 0) return;
    if (e.key === 'ArrowDown') {{
      e.preventDefault();
      setSelectedIndex(prev => (prev < results.length - 1 ? prev + 1 : 0));
    }} else if (e.key === 'ArrowUp') {{
      e.preventDefault();
      setSelectedIndex(prev => (prev > 0 ? prev - 1 : results.length - 1));
    }} else if (e.key === 'Enter' && selectedIndex >= 0) {{
      e.preventDefault();
      setQuery(results[selectedIndex].title);
      setIsOpen(false);
    }} else if (e.key === 'Escape') {{
      setIsOpen(false);
    }}
  }};

  return (
    <div className="relative max-w-lg mx-auto w-full p-4">
      <div className="relative">
        <input
          type="text"
          value={{query}}
          onChange={{e => setQuery(e.target.value)}}
          onKeyDown={{handleKeyDown}}
          onFocus={{() => query.trim() && setIsOpen(true)}}
          placeholder="Search documentation, components, or APIs..."
          className="w-full pl-10 pr-10 py-3 bg-neutral-900 border border-neutral-800 rounded-xl text-sm text-neutral-100 placeholder-neutral-500 focus:outline-none focus:ring-2 focus:ring-{color}-500 focus:border-transparent transition"
        />
        <Search className="w-4 h-4 text-neutral-500 absolute left-3.5 top-1/2 -translate-y-1/2" />
        {{loading ? (
          <Loader2 className="w-4 h-4 text-{color}-400 animate-spin absolute right-3.5 top-1/2 -translate-y-1/2" />
        ) : query ? (
          <button onClick={{() => {{ setQuery(''); setResults([]); }}}} className="absolute right-3.5 top-1/2 -translate-y-1/2 text-neutral-500 hover:text-white">
            <X className="w-4 h-4" />
          </button>
        ) : null}}
      </div>

      {{isOpen && results.length > 0 && (
        <div className="absolute left-4 right-4 mt-2 bg-neutral-900 border border-neutral-800 rounded-xl shadow-2xl overflow-hidden z-50 divide-y divide-neutral-800">
          {{results.map((r, idx) => (
            <div
              key={{r.id}}
              onClick={{() => {{ setQuery(r.title); setIsOpen(false); }}}}
              className={{`px-4 py-3 cursor-pointer flex justify-between items-center transition ${{idx === selectedIndex ? 'bg-{color}-500/20 text-{color}-300' : 'hover:bg-neutral-800 text-neutral-200'}}`}}
            >
              <span className="text-sm font-medium">{{r.title}}</span>
              <span className="text-[10px] uppercase font-mono px-2 py-0.5 rounded bg-neutral-800 text-neutral-400">{{r.category}}</span>
            </div>
          ))}}
        </div>
      )}}
    </div>
  );
}}"""

        # 2. Virtualized List for 100,000 Items
        elif scenario_id == 2:
            inst = f"Build a high-performance virtualized list in {framework} capable of rendering 100,000 log events smoothly at 60fps. Implement custom windowing math (`scrollTop`, `itemHeight`, `overscan`), dynamic height calculations, and sticky category headers using {style}."
            resp = f"""'use client';
import React, {{ useState, useRef, useMemo, useCallback }} from 'react';
import {{ Terminal }} from 'lucide-react';

interface LogItem {{
  id: number;
  timestamp: string;
  level: 'info' | 'warn' | 'error';
  message: string;
}}

const TOTAL_ITEMS = 100_000;
const ITEM_HEIGHT = 44;
const VIEWPORT_HEIGHT = 480;
const OVERSCAN = 6;

export default function VirtualizedLogViewer_v{variant_id}() {{
  const [scrollTop, setScrollTop] = useState<number>(0);
  const containerRef = useRef<HTMLDivElement>(null);

  const logs = useMemo<LogItem[]>(() => {{
    return Array.from({{ length: TOTAL_ITEMS }}, (_, i) => ({{
      id: i + 1,
      timestamp: new Date(Date.now() - (TOTAL_ITEMS - i) * 1000).toISOString().slice(11, 19),
      level: i % 15 === 0 ? 'error' : i % 5 === 0 ? 'warn' : 'info',
      message: `[WorkerThread-${{i % 8}}_v{variant_id}] Batch transaction stream sequence #${{i}} acknowledged in ${{((i * 19) % 45 + 5)}}ms`
    }}));
  }}, []);

  const onScroll = useCallback((e: React.UIEvent<HTMLDivElement>) => {{
    setScrollTop(e.currentTarget.scrollTop);
  }}, []);

  const {{ startIndex, endIndex, offsetY }} = useMemo(() => {{
    const start = Math.max(0, Math.floor(scrollTop / ITEM_HEIGHT) - OVERSCAN);
    const end = Math.min(TOTAL_ITEMS, Math.ceil((scrollTop + VIEWPORT_HEIGHT) / ITEM_HEIGHT) + OVERSCAN);
    const offset = start * ITEM_HEIGHT;
    return {{ startIndex: start, endIndex: end, offsetY: offset }};
  }}, [scrollTop]);

  const visibleItems = logs.slice(startIndex, endIndex);
  const totalHeight = TOTAL_ITEMS * ITEM_HEIGHT;

  return (
    <div className="max-w-4xl mx-auto p-6 bg-neutral-950 text-white space-y-4 rounded-2xl border border-neutral-800">
      <div className="flex justify-between items-center pb-3 border-b border-neutral-800">
        <div className="flex items-center gap-2">
          <Terminal className="w-5 h-5 text-{color}-400" />
          <h3 className="font-bold text-sm">System Log Stream ({{TOTAL_ITEMS.toLocaleString()}} Events - Session #{variant_id})</h3>
        </div>
        <span className="text-xs font-mono text-neutral-400">Rows {{startIndex.toLocaleString()}}–{{endIndex.toLocaleString()}}</span>
      </div>

      <div
        ref={{containerRef}}
        onScroll={{onScroll}}
        style={{{{ height: VIEWPORT_HEIGHT }}}}
        className="overflow-y-auto relative bg-neutral-900/90 rounded-xl border border-neutral-800 font-mono text-xs"
      >
        <div style={{{{ height: totalHeight, position: 'relative' }}}}>
          <div
            style={{{{
              transform: `translateY(${{offsetY}}px)`,
              position: 'absolute',
              top: 0,
              left: 0,
              right: 0,
            }}}}
          >
            {{visibleItems.map(item => (
              <div
                key={{item.id}}
                style={{{{ height: ITEM_HEIGHT }}}}
                className={{`flex items-center px-4 gap-4 border-b border-neutral-800/40 hover:bg-neutral-800/60 transition ${{item.level === 'error' ? 'bg-rose-950/20 text-rose-300' : item.level === 'warn' ? 'bg-amber-950/20 text-amber-300' : 'text-neutral-300'}}`}}
              >
                <span className="text-neutral-500 w-16 select-none">#{{item.id}}</span>
                <span className="text-neutral-400 w-20">{{item.timestamp}}</span>
                <span className={{`px-1.5 py-0.5 text-[10px] rounded uppercase font-bold ${{item.level === 'error' ? 'bg-rose-500/20 text-rose-400' : item.level === 'warn' ? 'bg-amber-500/20 text-amber-400' : 'bg-neutral-800 text-neutral-400'}}`}}>
                  {{item.level}}
                </span>
                <span className="truncate flex-1 font-sans">{{item.message}}</span>
              </div>
            ))}}
          </div>
        </div>
      </div>
    </div>
  );
}}"""

        # 3. Compound Component Pattern with Accessibility
        elif scenario_id == 3:
            inst = f"Implement an accessible, compound Dropdown Menu component in {framework} using the Compound Component pattern (`<Dropdown>`, `<Dropdown.Trigger>`, `<Dropdown.Menu>`, `<Dropdown.Item>`). Ensure keyboard accessibility (Escape to close, Arrow keys), outside click detection, and {style}."
            resp = f"""'use client';
import React, {{ createContext, useContext, useState, useRef, useEffect, ReactNode }} from 'react';
import {{ ChevronDown, User, Settings, LogOut }} from 'lucide-react';

interface DropdownContextType {{
  isOpen: boolean;
  setIsOpen: (open: boolean) => void;
}}

const DropdownContext = createContext<DropdownContextType | null>(null);

export function Dropdown_v{variant_id}({{ children }}: {{ children: ReactNode }}) {{
  const [isOpen, setIsOpen] = useState<boolean>(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  useEffect(() => {{
    const handleClickOutside = (e: MouseEvent) => {{
      if (dropdownRef.current && !dropdownRef.current.contains(e.target as Node)) {{
        setIsOpen(false);
      }}
    }};
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }}, []);

  return (
    <DropdownContext.Provider value={{ isOpen, setIsOpen }}>
      <div ref={{dropdownRef}} className="relative inline-block text-left">
        {{children}}
      </div>
    </DropdownContext.Provider>
  );
}}

Dropdown_v{variant_id}.Trigger = function DropdownTrigger({{ children }}: {{ children: ReactNode }}) {{
  const ctx = useContext(DropdownContext);
  if (!ctx) throw new Error('Must be inside Dropdown');
  return (
    <button
      onClick={{() => ctx.setIsOpen(!ctx.isOpen)}}
      aria-expanded={{ctx.isOpen}}
      className="flex items-center gap-2 px-4 py-2.5 bg-neutral-900 hover:bg-neutral-800 border border-neutral-800 text-white rounded-xl text-sm font-medium transition"
    >
      {{children}}
      <ChevronDown className={{`w-4 h-4 transition-transform duration-200 ${{ctx.isOpen ? 'rotate-180 text-{color}-400' : 'text-neutral-400'}}`}} />
    </button>
  );
}};

Dropdown_v{variant_id}.Menu = function DropdownMenu({{ children }}: {{ children: ReactNode }}) {{
  const ctx = useContext(DropdownContext);
  if (!ctx?.isOpen) return null;
  return (
    <div className="absolute right-0 mt-2 w-56 bg-neutral-900 border border-neutral-800 rounded-2xl shadow-2xl p-1.5 z-50 text-white space-y-1 animate-in fade-in zoom-in-95 duration-150">
      {{children}}
    </div>
  );
}};

Dropdown_v{variant_id}.Item = function DropdownItem({{ children, onClick, danger }}: {{ children: ReactNode; onClick?: () => void; danger?: boolean }}) {{
  const ctx = useContext(DropdownContext);
  return (
    <button
      onClick={{() => {{ if (onClick) onClick(); ctx?.setIsOpen(false); }}}}
      className={{`w-full flex items-center gap-2.5 px-3 py-2 text-xs font-medium rounded-xl text-left transition ${{danger ? 'text-rose-400 hover:bg-rose-500/10' : 'text-neutral-300 hover:bg-neutral-800 hover:text-white'}}`}}
    >
      {{children}}
    </button>
  );
}};"""

        # 4. Redis Token Bucket Rate Limiter with Local In-Memory Fallback
        else:
            inst = f"Write a production-ready Node.js Express rate limiting middleware in {framework} using `ioredis` implementing the Sliding Window Token Bucket algorithm. The middleware must handle Redis connection drops gracefully with an in-memory LRU fallback and inject `X-RateLimit-*` headers."
            resp = f"""import {{ Request, Response, NextFunction }} from 'express';
import Redis from 'ioredis';

export interface RateLimitOptions {{
  windowMs: number;
  maxRequests: number;
  keyGenerator?: (req: Request) => string;
}}

export class ResilientRateLimiter_v{variant_id} {{
  private redis: Redis | null = null;
  private localFallback = new Map<string, {{ count: number; resetTime: number }}>();
  private isRedisConnected = false;

  constructor(private options: RateLimitOptions, redisUrl?: string) {{
    if (redisUrl) {{
      this.redis = new Redis(redisUrl, {{ maxRetriesPerRequest: 1, lazyConnect: true }});
      this.redis.on('connect', () => {{ this.isRedisConnected = true; }});
      this.redis.on('error', () => {{ this.isRedisConnected = false; }});
      this.redis.connect().catch(() => {{ this.isRedisConnected = false; }});
    }}
  }}

  public middleware() {{
    return async (req: Request, res: Response, next: NextFunction) => {{
      const key = this.options.keyGenerator ? this.options.keyGenerator(req) : (req.ip || '127.0.0.1');
      const {{ windowMs, maxRequests }} = this.options;
      const now = Date.now();

      try {{
        let currentCount: number;
        let ttlRemaining: number;

        if (this.redis && this.isRedisConnected) {{
          const redisKey = `ratelimit:v{variant_id}:${{key}}`;
          const pipeline = this.redis.pipeline();
          pipeline.incr(redisKey);
          pipeline.ttl(redisKey);
          const results = await pipeline.exec();

          currentCount = results?.[0]?.[1] as number || 1;
          ttlRemaining = results?.[1]?.[1] as number || Math.ceil(windowMs / 1000);

          if (currentCount === 1) {{
            await this.redis.expire(redisKey, Math.ceil(windowMs / 1000));
            ttlRemaining = Math.ceil(windowMs / 1000);
          }}
        }} else {{
          const record = this.localFallback.get(key);
          if (!record || now > record.resetTime) {{
            this.localFallback.set(key, {{ count: 1, resetTime: now + windowMs }});
            currentCount = 1;
            ttlRemaining = Math.ceil(windowMs / 1000);
          }} else {{
            record.count += 1;
            currentCount = record.count;
            ttlRemaining = Math.ceil((record.resetTime - now) / 1000);
          }}
        }}

        res.setHeader('X-RateLimit-Limit', maxRequests);
        res.setHeader('X-RateLimit-Remaining', Math.max(0, maxRequests - currentCount));
        res.setHeader('X-RateLimit-Reset', Math.ceil((now + ttlRemaining * 1000) / 1000));

        if (currentCount > maxRequests) {{
          return res.status(429).json({{
            success: false,
            error: 'Too Many Requests',
            message: `Rate limit exceeded for cluster ref_{variant_id}. Try again in ${{ttlRemaining}} seconds.`
          }});
        }}

        next();
      }} catch (err) {{
        console.error('[RateLimiter] Error evaluating rate limit:', err);
        next();
      }}
    }};
  }}
}}"""

        return inst, resp

    variant_counter = 1
    while len(results) < count_needed:
        scenario_id = (variant_counter % 4) + 1
        inst, resp = build_evol_pair(scenario_id, variant_counter)
        variant_counter += 1
        
        r_hash = hashlib.md5(resp.strip().encode("utf-8")).hexdigest()
        if r_hash not in seen_hashes:
            seen_hashes.add(r_hash)
            results.append({
                "category": "evol_instruct_complex",
                "system": SYSTEM_PROMPT,
                "instruction": inst,
                "response": resp
            })

    print(f"   [+] Pipeline #5 generated {len(results):,} unique Evol-Instruct Complexity pairs!")
    return results



def generate_domain_specific_samples(count_needed: int, seen_hashes: set) -> List[Dict[str, Any]]:
    print(f"\n[PIPELINE #6 - ADDITIONAL DOMAIN TEMPLATES] Generating {count_needed:,} domain-specialized full-stack tasks...")
    results = []
    
    frameworks = ["React 19 / TypeScript", "Next.js 15 App Router", "Node.js Express", "Full-Stack Web Suite"]
    styles = ["Tailwind CSS", "Modern Glassmorphic Dark", "Cyberpunk Neon Theme", "Minimalist Clean UI"]
    colors = ['emerald', 'indigo', 'amber', 'rose', 'cyan', 'violet', 'teal']

    def build_domain_pair(scenario_id: int, variant_id: int) -> Tuple[str, str, str]:
        color = colors[variant_id % len(colors)]
        framework = frameworks[variant_id % len(frameworks)]
        style = styles[variant_id % len(styles)]
        
        # Domain 1: Real-Time Collaborative Canvas & Live Cursors
        if scenario_id == 1:
            category = "realtime_collaboration"
            inst = f"Build a real-time collaborative whiteboard canvas in {framework} with live multi-user cursor tracking, presence awareness, and delta broadcasting over WebSockets using {style}."
            resp = f"""'use client';
import React, {{ useState, useEffect, useRef, useCallback }} from 'react';
import {{ Users, MousePointer, Circle, Square, Trash2 }} from 'lucide-react';

interface Cursor {{
  id: string;
  name: string;
  color: string;
  x: number;
  y: number;
  lastActive: number;
}}

interface CanvasShape {{
  id: string;
  type: 'circle' | 'square';
  x: number;
  y: number;
  color: string;
}}

export default function CollaborativeCanvas_v{variant_id}() {{
  const [cursors, setCursors] = useState<Record<string, Cursor>>({{}});
  const [shapes, setShapes] = useState<CanvasShape[]>([
    {{ id: 's1', type: 'circle', x: 120, y: 150, color: '#10b981' }},
    {{ id: 's2', type: 'square', x: 280, y: 200, color: '#6366f1' }}
  ]);
  const [activeTool, setActiveTool] = useState<'select' | 'circle' | 'square'>('select');
  const canvasRef = useRef<HTMLDivElement>(null);
  const myId = useRef(`user_${{Math.random().toString(36).slice(2, 7)}}_v{variant_id}`);

  // Mouse movement throttle for live cursor broadcast
  const handleMouseMove = useCallback((e: React.MouseEvent<HTMLDivElement>) => {{
    if (!canvasRef.current) return;
    const rect = canvasRef.current.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    // Simulated local awareness broadcast
    setCursors(prev => ({{
      ...prev,
      'peer_user_alex': {{ id: 'peer_user_alex', name: 'Alex Rivera', color: '#f59e0b', x: x + 60, y: y + 40, lastActive: Date.now() }},
      'peer_user_sarah': {{ id: 'peer_user_sarah', name: 'Sarah Wu', color: '#ec4899', x: Math.max(20, 600 - x), y: Math.max(20, 400 - y), lastActive: Date.now() }}
    }}));
  }}, []);

  const handleCanvasClick = (e: React.MouseEvent<HTMLDivElement>) => {{
    if (activeTool === 'select' || !canvasRef.current) return;
    const rect = canvasRef.current.getBoundingClientRect();
    const newShape: CanvasShape = {{
      id: `shape_${{Date.now()}}`,
      type: activeTool,
      x: e.clientX - rect.left - 24,
      y: e.clientY - rect.top - 24,
      color: activeTool === 'circle' ? '#10b981' : '#6366f1'
    }};
    setShapes(prev => [...prev, newShape]);
  }};

  return (
    <div className="max-w-5xl mx-auto p-6 bg-neutral-950 text-white rounded-3xl border border-neutral-800 space-y-4 shadow-2xl">
      <div className="flex justify-between items-center pb-3 border-b border-neutral-800">
        <div className="flex items-center gap-3">
          <div className="p-2 bg-neutral-900 rounded-xl border border-neutral-800">
            <Users className="w-5 h-5 text-{color}-400" />
          </div>
          <div>
            <h3 className="font-bold text-sm">Real-time Architecture Board (Workspace v{variant_id})</h3>
            <p className="text-xs text-neutral-400">3 active contributors live in room</p>
          </div>
        </div>

        <div className="flex items-center gap-2 bg-neutral-900 p-1.5 rounded-2xl border border-neutral-800">
          <button onClick={{() => setActiveTool('select')}} className={{`px-3 py-1.5 rounded-xl text-xs font-semibold transition ${{activeTool === 'select' ? 'bg-{color}-500 text-neutral-950' : 'text-neutral-400 hover:text-white'}}`}}>
            Select
          </button>
          <button onClick={{() => setActiveTool('circle')}} className={{`px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1 transition ${{activeTool === 'circle' ? 'bg-{color}-500 text-neutral-950' : 'text-neutral-400 hover:text-white'}}`}}>
            <Circle className="w-3.5 h-3.5" /> Circle
          </button>
          <button onClick={{() => setActiveTool('square')}} className={{`px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1 transition ${{activeTool === 'square' ? 'bg-{color}-500 text-neutral-950' : 'text-neutral-400 hover:text-white'}}`}}>
            <Square className="w-3.5 h-3.5" /> Box
          </button>
          <button onClick={{() => setShapes([])}} className="p-1.5 text-neutral-500 hover:text-rose-400 rounded-xl transition">
            <Trash2 className="w-4 h-4" />
          </button>
        </div>
      </div>

      <div
        ref={{canvasRef}}
        onMouseMove={{handleMouseMove}}
        onClick={{handleCanvasClick}}
        className="h-[460px] w-full bg-neutral-900/60 rounded-2xl border border-neutral-800 relative overflow-hidden cursor-crosshair select-none"
      >
        {{shapes.map(shape => (
          <div
            key={{shape.id}}
            style={{{{ left: shape.x, top: shape.y, backgroundColor: shape.color }}}}
            className={{`absolute w-12 h-12 shadow-lg cursor-grab active:cursor-grabbing flex items-center justify-center text-[10px] font-bold text-neutral-950 ${{shape.type === 'circle' ? 'rounded-full' : 'rounded-xl'}}`}}
          >
            {{shape.type[0].toUpperCase()}}
          </div>
        ))}}

        {{Object.values(cursors).map(cursor => (
          <div
            key={{cursor.id}}
            style={{{{ left: cursor.x, top: cursor.y }}}}
            className="absolute pointer-events-none transition-all duration-75 flex items-start gap-1"
          >
            <MousePointer style={{{{ color: cursor.color }}}} className="w-4 h-4 fill-current drop-shadow-md" />
            <span style={{{{ backgroundColor: cursor.color }}}} className="text-[10px] font-bold text-neutral-950 px-2 py-0.5 rounded-full shadow-md whitespace-nowrap">
              {{cursor.name}}
            </span>
          </div>
        ))}}
      </div>
    </div>
  );
}}"""

        # Domain 2: Stripe Billing Engine & Webhook Idempotency
        elif scenario_id == 2:
            category = "stripe_billing_engine"
            inst = f"Write a complete Stripe subscription lifecycle API router in {framework} with customer portal session creation, subscription tier upgrades, invoice event handling, and webhook idempotency via PostgreSQL."
            resp = f"""import express, {{ Request, Response }} from 'express';
import Stripe from 'stripe';
import {{ prisma }} from '@/lib/prisma';

export const billingRouter = express.Router();
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY || 'sk_test_mock_{variant_id}', {{
  apiVersion: '2023-10-16' as any,
}});

// 1. Create Customer Billing Portal Session
billingRouter.post('/portal-session', async (req: Request, res: Response) => {{
  const {{ userId, returnUrl }} = req.body;
  if (!userId) return res.status(400).json({{ error: 'User ID required' }});

  const user = await prisma.user.findUnique({{ where: {{ id: userId }} }});
  if (!user || !user.stripeCustomerId) {{
    return res.status(404).json({{ error: 'No active billing customer found' }});
  }}

  const session = await stripe.billingPortal.sessions.create({{
    customer: user.stripeCustomerId,
    return_url: returnUrl || 'https://app.vibe.io/dashboard/billing',
  }});

  return res.json({{ success: true, url: session.url }});
}});

// 2. Upgrade / Change Subscription Tier
billingRouter.post('/change-tier', async (req: Request, res: Response) => {{
  const {{ subscriptionId, newPriceId }} = req.body;
  if (!subscriptionId || !newPriceId) {{
    return res.status(400).json({{ error: 'Subscription ID and new price ID required' }});
  }}

  const subscription = await stripe.subscriptions.retrieve(subscriptionId);
  const updated = await stripe.subscriptions.update(subscriptionId, {{
    items: [{{
      id: subscription.items.data[0].id,
      price: newPriceId,
    }}],
    proration_behavior: 'always_invoice',
  }});

  return res.json({{ success: true, subscription: updated }});
}});

// 3. Webhook with Cryptographic Idempotency Check
billingRouter.post('/webhook', express.raw({{ type: 'application/json' }}), async (req: Request, res: Response) => {{
  const sig = req.headers['stripe-signature'];
  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET || 'whsec_test_{variant_id}';
  let event: Stripe.Event;

  try {{
    event = stripe.webhooks.constructEvent(req.body, sig as string, webhookSecret);
  }} catch (err: any) {{
    return res.status(400).send(`Webhook Signature Verification Error: ${{err.message}}`);
  }}

  // Idempotency check: prevent duplicate event processing
  const existingEvent = await prisma.processedWebhookEvent.findUnique({{
    where: {{ eventId: event.id }}
  }});

  if (existingEvent) {{
    return res.status(200).json({{ received: true, note: 'Event already processed' }});
  }}

  // Process event
  switch (event.type) {{
    case 'customer.subscription.updated':
    case 'customer.subscription.created': {{
      const sub = event.data.object as Stripe.Subscription;
      await prisma.user.update({{
        where: {{ stripeCustomerId: sub.customer as string }},
        data: {{ subscriptionStatus: sub.status, planTier: sub.items.data[0].price.id }}
      }});
      break;
    }}
    case 'invoice.payment_succeeded': {{
      const invoice = event.data.object as Stripe.Invoice;
      await prisma.invoiceRecord.create({{
        data: {{
          invoiceId: invoice.id,
          amountPaid: invoice.amount_paid,
          currency: invoice.currency,
          customerId: invoice.customer as string,
        }}
      }});
      break;
    }}
  }}

  // Mark event as processed in database transaction
  await prisma.processedWebhookEvent.create({{
    data: {{ eventId: event.id, eventType: event.type, processedAt: new Date() }}
  }});

  return res.status(200).json({{ received: true }});
}});"""

        # Domain 3: Custom Interactive SVG Charting Engine
        elif scenario_id == 3:
            category = "analytics_data_viz"
            inst = f"Build an interactive SVG time-series area chart in {framework} with animated crosshair tooltips, dynamic date aggregation (daily/weekly), and linear gradient fill styled using {style}."
            resp = f"""'use client';
import React, {{ useState, useMemo }} from 'react';
import {{ TrendingUp, Calendar }} from 'lucide-react';

interface DataPoint {{
  date: string;
  value: number;
}}

const sampleData: DataPoint[] = [
  {{ date: '2026-08-01', value: 12400 }},
  {{ date: '2026-08-02', value: 14800 }},
  {{ date: '2026-08-03', value: 13900 }},
  {{ date: '2026-08-04', value: 18200 }},
  {{ date: '2026-08-05', value: 21500 }},
  {{ date: '2026-08-06', value: 19800 }},
  {{ date: '2026-08-07', value: 26400 }},
];

export default function AnalyticsAreaChart_v{variant_id}() {{
  const [hoverIndex, setHoverIndex] = useState<number | null>(null);
  const [timeframe, setTimeframe] = useState<'7d' | '30d'>('7d');

  const width = 600;
  const height = 240;
  const padding = {{ top: 20, right: 20, bottom: 30, left: 40 }};

  const {{ points, pathD, areaD, maxValue, minValue }} = useMemo(() => {{
    const vals = sampleData.map(d => d.value);
    const max = Math.max(...vals);
    const min = Math.min(...vals) * 0.9;
    const chartW = width - padding.left - padding.right;
    const chartH = height - padding.top - padding.bottom;

    const computed = sampleData.map((d, idx) => {{
      const x = padding.left + (idx / (sampleData.length - 1)) * chartW;
      const y = padding.top + chartH - ((d.value - min) / (max - min)) * chartH;
      return {{ x, y, ...d }};
    }});

    const linePath = computed.reduce((acc, p, i) => (i === 0 ? `M ${{p.x}} ${{p.y}}` : `${{acc}} L ${{p.x}} ${{p.y}}`), '');
    const areaPath = `${{linePath}} L ${{computed[computed.length - 1].x}} ${{height - padding.bottom}} L ${{computed[0].x}} ${{height - padding.bottom}} Z`;

    return {{ points: computed, pathD: linePath, areaD: areaPath, maxValue: max, minValue: min }};
  }}, [width, height]);

  const activePoint = hoverIndex !== null ? points[hoverIndex] : points[points.length - 1];

  return (
    <div className="max-w-2xl mx-auto p-6 bg-neutral-900 border border-neutral-800 rounded-3xl text-white space-y-6 shadow-xl">
      <div className="flex justify-between items-center">
        <div>
          <span className="text-xs text-neutral-400 font-mono">Revenue Metric v{variant_id}</span>
          <div className="flex items-baseline gap-2 mt-1">
            <h3 className="text-3xl font-extrabold">${{activePoint.value.toLocaleString()}}</h3>
            <span className="text-xs text-emerald-400 flex items-center font-semibold"><TrendingUp className="w-3.5 h-3.5 mr-0.5"/> +18.4%</span>
          </div>
        </div>

        <div className="flex gap-1 bg-neutral-800 p-1 rounded-xl text-xs font-semibold">
          <button onClick={{() => setTimeframe('7d')}} className={{`px-3 py-1 rounded-lg ${{timeframe === '7d' ? 'bg-{color}-500 text-neutral-950' : 'text-neutral-400 hover:text-white'}}`}}>
            7 Days
          </button>
          <button onClick={{() => setTimeframe('30d')}} className={{`px-3 py-1 rounded-lg ${{timeframe === '30d' ? 'bg-{color}-500 text-neutral-950' : 'text-neutral-400 hover:text-white'}}`}}>
            30 Days
          </button>
        </div>
      </div>

      <div className="relative">
        <svg viewBox="0 0 600 240" className="w-full h-auto overflow-visible">
          <defs>
            <linearGradient id={{`chart-grad-v{variant_id}`}} x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="var(--color-{color}-500, #10b981)" stopOpacity="0.4" />
              <stop offset="100%" stopColor="var(--color-{color}-500, #10b981)" stopOpacity="0.0" />
            </linearGradient>
          </defs>

          <line x1={{padding.left}} y1={{height - padding.bottom}} x2={{width - padding.right}} y2={{height - padding.bottom}} stroke="#262626" strokeWidth="1" />
          <line x1={{padding.left}} y1={{padding.top}} x2={{width - padding.right}} y2={{padding.top}} stroke="#262626" strokeDasharray="3 3" strokeWidth="1" />

          <path d={{areaD}} fill={{`url(#chart-grad-v{variant_id})`}} />
          <path d={{pathD}} fill="none" stroke="#10b981" strokeWidth="2.5" strokeLinecap="round" />

          {{points.map((p, idx) => (
            <g key={{p.date}} onMouseEnter={{() => setHoverIndex(idx)}} onMouseLeave={{() => setHoverIndex(null)}}>
              <circle cx={{p.x}} cy={{p.y}} r={{idx === hoverIndex ? 6 : 4}} className="fill-emerald-400 stroke-neutral-950 stroke-2 cursor-pointer transition-all" />
              <rect x={{p.x - 15}} y={{0}} width={{30}} height={{height}} fill="transparent" className="cursor-pointer" />
            </g>
          ))}}
        </svg>
      </div>
    </div>
  );
}}"""

        # Domain 4: OAuth2 PKCE Authentication Flow
        else:
            category = "oauth2_pkce_auth"
            inst = f"Write a pure TypeScript module implementing the OAuth2 PKCE (Proof Key for Code Exchange) authorization flow with cryptographically secure `code_verifier`, SHA-256 `code_challenge` generator, and token exchange."
            resp = f"""// RFC 7636 OAuth2 PKCE Module for Single Page Applications & Edge Workers

export interface PKCEPair {{
  codeVerifier: string;
  codeChallenge: string;
}}

export interface OAuthTokenResponse {{
  access_token: string;
  token_type: string;
  expires_in: number;
  refresh_token?: string;
  scope: string;
}}

export class PKCEAuthManager_v{variant_id} {{
  /**
   * Generates a cryptographically random 128-character code verifier
   */
  public static generateCodeVerifier(): string {{
    const array = new Uint8Array(64);
    if (typeof window !== 'undefined' && window.crypto) {{
      window.crypto.getRandomValues(array);
    }} else {{
      const crypto = require('crypto');
      crypto.randomFillSync(array);
    }}
    return Array.from(array, byte => byte.toString(16).padStart(2, '0')).join('');
  }}

  /**
   * Derives a Base64URL-encoded SHA-256 code challenge from the code verifier
   */
  public static async generateCodeChallenge(verifier: string): Promise<string> {{
    const encoder = new TextEncoder();
    const data = encoder.encode(verifier);
    
    let digest: ArrayBuffer;
    if (typeof window !== 'undefined' && window.crypto?.subtle) {{
      digest = await window.crypto.subtle.digest('SHA-256', data);
    }} else {{
      const crypto = require('crypto');
      digest = crypto.createHash('sha256').update(data).digest();
    }}

    const base64 = typeof window !== 'undefined'
      ? btoa(String.fromCharCode(...new Uint8Array(digest)))
      : Buffer.from(digest).toString('base64');

    return base64
      .replace(/\\+/g, '-')
      .replace(/\\//g, '_')
      .replace(/=+$/, '');
  }}

  /**
   * Builds the authorization redirect URL with PKCE parameters
   */
  public static async buildAuthUrl(options: {{
    authEndpoint: string;
    clientId: string;
    redirectUri: string;
    scope: string;
    state: string;
    codeChallenge: string;
  }}): Promise<string> {{
    const params = new URLSearchParams({{
      response_type: 'code',
      client_id: options.clientId,
      redirect_uri: options.redirectUri,
      scope: options.scope,
      state: options.state,
      code_challenge: options.codeChallenge,
      code_challenge_method: 'S256',
    }});

    return `${{options.authEndpoint}}?${{params.toString()}}`;
  }}

  /**
   * Exchanges the authorization code and code verifier for access tokens
   */
  public static async exchangeCodeForToken(options: {{
    tokenEndpoint: string;
    clientId: string;
    code: string;
    redirectUri: string;
    codeVerifier: string;
  }}): Promise<OAuthTokenResponse> {{
    const body = new URLSearchParams({{
      grant_type: 'authorization_code',
      client_id: options.clientId,
      code: options.code,
      redirect_uri: options.redirectUri,
      code_verifier: options.codeVerifier,
    }});

    const response = await fetch(options.tokenEndpoint, {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/x-www-form-urlencoded' }},
      body: body.toString(),
    }});

    if (!response.ok) {{
      const errBody = await response.text();
      throw new Error(`Token exchange failed (${{response.status}}): ${{errBody}}`);
    }}

    return response.json();
  }}
}}"""

        return inst, resp, category

    variant_counter = 1
    while len(results) < count_needed:
        scenario_id = (variant_counter % 4) + 1
        inst, resp, category = build_domain_pair(scenario_id, variant_counter)
        variant_counter += 1
        
        r_hash = hashlib.md5(resp.strip().encode("utf-8")).hexdigest()
        if r_hash not in seen_hashes:
            seen_hashes.add(r_hash)
            results.append({
                "category": category,
                "system": SYSTEM_PROMPT,
                "instruction": inst,
                "response": resp
            })

    print(f"   [+] Pipeline #6 generated {len(results):,} unique Domain-Specific task pairs!")
    return results

def generate_multi_source_dataset(target_samples: int = 50000, output_path: str = "data/vibe_training_dataset.json"):
    print("=" * 70)
    print(f"[START] VIBE CODER PHASE 1: Multi-Source Dataset Generator (Target: {target_samples:,} records)")
    print("=" * 70)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    records = []
    seen_response_hashes = set()
    
    for sample in HANDCRAFTED_SAMPLES + CONVERSATIONAL_SAMPLES + SELF_HEALING_SAMPLES:
        resp = sample["response"].strip()
        r_hash = hashlib.md5(resp.encode("utf-8")).hexdigest()
        seen_response_hashes.add(r_hash)
        sys_p = sample.get("system", SYSTEM_PROMPT)
        formatted = format_chatml(sys_p, sample["instruction"], resp)
        records.append({
            "id": len(records) + 1,
            "category": sample["category"],
            "system": sys_p,
            "instruction": sample["instruction"],
            "response": resp,
            "text": formatted
        })
        
    # Pipeline 1: Curated Open-Source Web Datasets (Magicoder, TokenBender, CodeAlpaca)
    oss_target = min(8000, int(target_samples * 0.30))
    oss_samples = fetch_open_source_datasets(target_count=oss_target, seen_hashes=seen_response_hashes)
    for sample in oss_samples:
        resp = sample["response"].strip()
        sys_p = sample.get("system", SYSTEM_PROMPT)
        formatted = format_chatml(sys_p, sample["instruction"], resp)
        records.append({
            "id": len(records) + 1,
            "category": sample.get("category", "open_source_web"),
            "system": sys_p,
            "instruction": sample["instruction"],
            "response": resp,
            "text": formatted
        })

    # Pipeline 2: Real-World Debugging & Architecture Decision Scenarios
    debug_target = min(3000, int(target_samples * 0.12))
    debug_samples = generate_debug_and_architecture_samples(count_needed=debug_target, seen_hashes=seen_response_hashes)
    for sample in debug_samples:
        resp = sample["response"].strip()
        sys_p = sample.get("system", SYSTEM_PROMPT)
        formatted = format_chatml(sys_p, sample["instruction"], resp)
        records.append({
            "id": len(records) + 1,
            "category": sample["category"],
            "system": sys_p,
            "instruction": sample["instruction"],
            "response": resp,
            "text": formatted
        })

    # Pipeline 3: Multi-Turn Conversational Chains (Priority #4)
    multi_turn_target = min(2000, int(target_samples * 0.08))
    multi_turn_samples = generate_multi_turn_samples(count_needed=multi_turn_target, seen_hashes=seen_response_hashes)
    for sample in multi_turn_samples:
        records.append({
            "id": len(records) + 1,
            "category": sample["category"],
            "system": sample["system"],
            "instruction": sample["instruction"],
            "response": sample["response"],
            "turns": sample.get("turns", []),
            "text": sample["text"]
        })

    # Pipeline 4: Evol-Instruct Complexity Layers (Priority #5)
    evol_target = min(2500, int(target_samples * 0.09))
    evol_samples = generate_evol_instruct_samples(count_needed=evol_target, seen_hashes=seen_response_hashes)
    for sample in evol_samples:
        resp = sample["response"].strip()
        sys_p = sample.get("system", SYSTEM_PROMPT)
        formatted = format_chatml(sys_p, sample["instruction"], resp)
        records.append({
            "id": len(records) + 1,
            "category": sample["category"],
            "system": sys_p,
            "instruction": sample["instruction"],
            "response": resp,
            "text": formatted
        })

    # Pipeline 5: Additional Domain Templates (Priority #6)
    domain_target = min(2500, int(target_samples * 0.09))
    domain_samples = generate_domain_specific_samples(count_needed=domain_target, seen_hashes=seen_response_hashes)
    for sample in domain_samples:
        resp = sample["response"].strip()
        sys_p = sample.get("system", SYSTEM_PROMPT)
        formatted = format_chatml(sys_p, sample["instruction"], resp)
        records.append({
            "id": len(records) + 1,
            "category": sample["category"],
            "system": sys_p,
            "instruction": sample["instruction"],
            "response": resp,
            "text": formatted
        })



        
    remaining = target_samples - len(records)
    if remaining > 0:
        combinatorial_samples = generate_combinatorial_web_samples(remaining, seen_response_hashes)
        for sample in combinatorial_samples:
            resp = sample["response"].strip()
            sys_p = sample.get("system", SYSTEM_PROMPT)
            formatted = format_chatml(sys_p, sample["instruction"], resp)
            records.append({
                "id": len(records) + 1,
                "category": sample["category"],
                "system": sys_p,
                "instruction": sample["instruction"],
                "response": resp,
                "text": formatted
            })
            
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
        
    print(f"\n[SUCCESS] Wrote {len(records):,} total high-quality verified samples to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Vibe Coder Dataset")
    parser.add_argument("--samples", type=int, default=28000, help="Target number of samples to generate")
    args = parser.parse_args()
    generate_multi_source_dataset(target_samples=args.samples)
