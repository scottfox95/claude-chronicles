---
date: 2026-04-01
topic: Eliminating a hidden LLM relay tax that added 15s to every response
tags: ai, latency, vercel, streaming, architecture
mode: tactical
tweet_count: 6
---

# The Sonnet Relay Tax

**1/**
Found a bug in my app's architecture that was adding 15 seconds to every response — and costing money to make things slower.

The fix was deleting an LLM call, not adding one.

**2/**
Context: I built a CBA rules engine for an NBA front office exec. Web chat backed by a local AI agent with a full knowledge base.

The agent returns a complete answer in ~20s. Great. But the user was waiting 35-40s. Why?

**3/**
The API route was taking the agent's finished answer and feeding it through a SECOND Claude call as a "text relay" — just to format it as a stream the frontend could render.

10-20 extra seconds. $0.01/query. For literally copying text.

**4/**
The fix: Vercel AI SDK has createUIMessageStream. You can construct the exact same streaming format the frontend expects — no LLM required.

Chunk the text by word boundaries, write text-delta events with 15ms delays. Progressive rendering in ~600ms.

**5/**
Same session: ripped out an unreliable iMessage bridge, added timing breakdowns to the broker (prefetch_ms, agent_ms, total_ms), and warmed a static QMD cache on startup.

Now I can see exactly where every millisecond goes.

**6/**
The lesson: if your AI app feels slow, check whether you're burning inference cycles on plumbing instead of thinking.

Sometimes the fastest optimization is removing a model call entirely.

---

*Session notes: Eliminated Sonnet relay in CBA Brain /api/chat route using createUIMessageStream, removed Sendblue/iMessage support, added broker observability with request_id and timing breakdowns, warmed eligibility cache on startup. Also ran /simplify earlier — removed hardcoded token, deleted stale duplicate knowledge file, hoisted regex, added QMD error logging.*
