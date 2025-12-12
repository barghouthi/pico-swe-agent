## pico: the tiniest coding agent

**The tiniest coding agent in the land: 8 LoC**

This repo is intentionally minimal: a single Python file (`pico.py`) that defines an LLM-based coding agent with access to bash.

### Install

```bash
uv sync
```

### Usage

Run the agent by passing your instruction as CLI args (they’re forwarded into the prompt):

```bash
uv run python pico.py create a simple website with a calculator
```

### Safety / warning

This agent can execute arbitrary shell commands through `run_bash`. Only run it in a sandbox or environment you trust.

