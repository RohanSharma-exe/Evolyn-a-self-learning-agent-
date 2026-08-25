# Evolyn implementation plan

## Phase 1 — Foundation
- Keep the agent core small and backend-agnostic.
- Use Cognee for persistent graph/vector knowledge memory.
- Use LiteLLM for provider-neutral model calls.
- Use MCP for tools.
- Use Langfuse for traces and evaluation.
- Keep LibreChat as the external interaction UI.

## Phase 2 — Learning loop
1. Retrieve relevant prior experience.
2. Plan and act.
3. Observe the outcome.
4. Evaluate the outcome.
5. Extract a reusable lesson.
6. Store the lesson with provenance and scope.
7. Reuse it on later tasks.

## Phase 3 — Safe improvement
- Separate candidate lessons from trusted knowledge.
- Add regression evaluations before promoting a learned behavior.
- Add temporal metadata and rollback support.
- Add procedural skills only after the learning loop is measurable.

## Phase 4 — Visible agent
- LibreChat for interaction.
- Langfuse for execution traces.
- Cognee visualization for knowledge-graph inspection.
- Add a small Evolyn run/event view only if existing OSS UIs do not provide enough visibility.

## Success criteria
- The agent can remember an experience across runs.
- The agent can retrieve relevant prior experience.
- A failure can produce a reusable lesson.
- A later run can use that lesson.
- Evaluation demonstrates improvement rather than merely storing more data.
