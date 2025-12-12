# pico: the tiniest coding agent, just 7 LoC!

7 lines of code that defines an LLM-based coding agent with access to bash. Still it's incredibly powerful!

## Usage

You need [uv](https://docs.astral.sh/uv/getting-started/installation/#installation-methods) and an AWS account configured.

Run the agent by passing your instruction as CLI args, e.g.,:

```bash
uv run python pico.py create a simple website with a calculator
```

## Safety / warning

This agent can execute arbitrary shell commands through `run_bash`. Ideally, run it in a sandbox.