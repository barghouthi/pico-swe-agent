# pico: the tiniest coding agent, just 6 LoC!

pico is an AI coding agent that is just 6 lines of Python code. Still, it's incredibly powerful!

## usage

You need [uv](https://docs.astral.sh/uv/getting-started/installation/#installation-methods) installed and an AWS account configured (see [models](#models) below for other providers).

Run the agent as follows:

```bash
uv run python pico.py <YOUR TASK>
```

e.g.,

```bash
uv run python pico.py "create a simple calculator website"
```

> [!WARNING]
> This agent can execute arbitrary shell commands. Ideally, run it in a sandbox.

## models

By default, pico uses Claude via Amazon Bedrock. If you want to use other models, like OpenAI's or local models, modify the `Agent` object following the [strands documentation](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/model-providers/).

## details
pico uses the `strands-agents` library for defining an agent with access to a single tool: bash. This is similar in spirit to the bash-based [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent), which is 100 lines of Python.
