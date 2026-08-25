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
- **LiteLLM 1.x** for provider-neutral model access
- **MCP Python SDK v2** for standardized tools
- **Langfuse v4** for open-source observability and evaluation
- **LibreChat** for the user-facing agent UI
- **pytest + Ruff** for quality and regression tests

## Run locally

Windows CMD:

```cmd
git clone https://github.com/RohanSharma-exe/Evolyn-a-self-learning-agent-.git
cd Evolyn-a-self-learning-agent-
uv sync --dev
copy .env.example .env
```

Set `OPENAI_API_KEY`, `LLM_API_KEY`, and `EMBEDDING_API_KEY` in `.env`. For the first local smoke test, the three can use the same OpenAI key.

Then:

```cmd
uv run evolyn "Explain why persistent memory can improve an AI agent."
```

The first Cognee-backed run may take longer because local knowledge infrastructure is initialized and the experience is indexed.

### MCP tool server

```cmd
uv run evolyn-mcp
```

The MCP server currently exposes a small safe calculator tool. Evolyn's MCP client integration will be added in the next phase.

### Tests

```cmd
uv run ruff check .
uv run pytest
```

## Observability

Add Langfuse credentials to `.env` to see the LLM calls and Evolyn agent trace in the Langfuse UI. Without Langfuse credentials, Evolyn still runs locally.

## Design rules

1. Prefer mature OSS over custom infrastructure.
2. Keep third-party dependencies behind thin adapters.
3. Never promote a learned behavior without evaluation.
4. Preserve provenance for learned knowledge.
5. Make memory, model, tool, and evaluator implementations replaceable.
6. Measure whether the agent actually improves.

## Current status

**Phase 1 foundation is runnable in principle; local dependency/runtime verification is the next checkpoint.**

See [`docs/architecture.md`](docs/architecture.md) for the implementation plan.
