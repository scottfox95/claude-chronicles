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

I just applied the same pattern to sales outreach.

**2/**
A client I'm working with mentioned he's going back to school for ML. Got me thinking — what if I could connect what's happening in AI research to something his company would actually use?

What if sales messaging was the thing being optimized?

**3/**
Built "AutoPitch" — same structure as Karpathy's autoresearch:

- evaluate.py = scoring rubric (7 dimensions, weighted)
- pitch.py = the file the agent iterates on
- program.md = agent instructions

Generate, score, analyze, modify, repeat.

**4/**
It writes outreach emails for specific personas — CISOs, compliance officers, procurement leads — then scores each one on specificity, pain resonance, hook strength, credibility, CTA clarity, tone, brevity.

Lower composite score = better. Just like val_bpb.

**5/**
Karpathy said it best: "any metric you care about that is reasonably efficient to evaluate can be autoresearched."

Sales email quality is that metric. The rubric is the eval. The agent figures out what works per industry and persona.

**6/**
Runs on Claude Code Max plan. Same setup Karpathy uses for his autoresearch. Zero additional cost.

Give me a target persona tonight, I'll have the best outreach strategy by morning. Not a guess — tested by the model.

**7/**
Autoresearch isn't just for ML training. Any business process with a measurable output can be optimized this way.

Sales messaging was my first target. Won't be the last.

---

*Session notes: Built the full AutoPitch project scaffolding — evaluate.py (fixed rubric with 7 weighted dimensions), pitch.py (4 email frameworks the agent iterates on), program.md (agent loop instructions mirroring Karpathy's autoresearch), personas.json (5 enterprise TPRM buyer personas), README.md. Project designed to run overnight on Claude Code Max plan.*
