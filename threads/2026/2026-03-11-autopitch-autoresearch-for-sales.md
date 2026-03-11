---
date: 2026-03-11
topic: AutoPitch — applying Karpathy's autoresearch to sales outreach
tags: autoresearch, sales, ai-agents, karpathy, enterprise
mode: builder
tweet_count: 7
---

# AutoPitch — Autoresearch for Sales

**1/**
Karpathy's autoresearch lets AI agents run 700 experiments overnight to optimize neural network training.

I just applied the same pattern to enterprise sales outreach.

**2/**
The idea: a client I'm talking to mentioned he's going back to school for ML. I wanted to build something that connects cutting-edge AI research to his company's actual business.

So I asked: what if sales messaging was the model being optimized?

**3/**
Built "AutoPitch" — mirrors Karpathy's autoresearch structure exactly:

- evaluate.py = fixed scoring rubric (7 dimensions, weighted)
- pitch.py = the file the agent iterates on
- program.md = agent instructions

Same loop. Generate, score, analyze, modify, repeat.

**4/**
The agent generates outreach emails for specific personas (CISOs, compliance officers, procurement leads), scores each one on specificity, pain resonance, hook strength, credibility, CTA clarity, tone, and brevity.

Lower composite score = better. Just like val_bpb.

**5/**
The key insight from Karpathy's tweet: "any metric you care about that is reasonably efficient to evaluate can be autoresearched."

Sales email quality is that metric. The rubric is the eval function. The agent finds what works per industry and persona.

**6/**
Best part: runs on Claude Code Max plan. Same setup Karpathy uses for his autoresearch. Zero additional cost.

Give me a target persona tonight, I'll tell you the best outreach strategy in the morning. Not a guess — proven from the model.

**7/**
The pattern is what matters. Autoresearch isn't just for ML training. Any business process with a measurable output can be optimized this way.

Sales messaging was my first target. It won't be the last.

---

*Session notes: Built the full AutoPitch project scaffolding — evaluate.py (fixed rubric with 7 weighted dimensions), pitch.py (4 email frameworks the agent iterates on), program.md (agent loop instructions mirroring Karpathy's autoresearch), personas.json (5 enterprise TPRM buyer personas), README.md. Project designed to run overnight on Claude Code Max plan. Also drafted a hype text for the sales team leads.*
