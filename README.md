# Evolyn

> A self-learning AI agent that turns experience into reusable knowledge and measurable improvement.

Evolyn is deliberately built around a **small custom learning loop** and mature open-source infrastructure. The goal is to spend our code on learning, evaluation, and safe improvement—not on rebuilding databases, retrieval engines, LLM gateways, tool protocols, or observability dashboards.

## Architecture

```text
User
  │
  ▼
LibreChat / future UI
  │
  ▼
Evolyn core
  │
  ├── retrieve experience ──► Cognee
  ├── model calls ──────────► LiteLLM
  ├── tools ─────────────────► MCP
  ├── evaluate ──────────────► custom evals + Langfuse
  └── learn ─────────────────► lesson ──► Cognee

Langfuse observes the full run.
```

## Locked stack

- **Python 3.12+** with **uv**
- **Cognee 1.x** for persistent graph/vector knowledge and memory
- **LiteLLM 1.x** for provider-neutral model access and fallbacks
- **MCP Python SDK v2** for standardized tools
- **Langfuse v4** for open-source observability and evaluation
- **LibreChat** for the user-facing agent UI
- **pytest + Ruff** for quality and regression tests

The current Cognee API supports the `remember → recall` memory flow and graph-based retrieval.

Langfuse v4 is the current GA self-hosted line and its current Python SDK is v4.

The official MCP Python SDK v2 is the current stable line.

LiteLLM provides one interface across 100+ LLM providers and supports retries/fallbacks.

## Design rules

1. Prefer mature OSS over custom infrastructure.
2. Keep third-party dependencies behind thin adapters.
3. Never promote a learned behavior without evaluation.
4. Preserve provenance for learned knowledge.
5. Make memory, model, tool, and evaluator implementations replaceable.
6. Measure whether the agent actually improves.

## Current status

**Phase 1 foundation is being built.**

See [`docs/architecture.md`](docs/architecture.md) for the implementation plan.
