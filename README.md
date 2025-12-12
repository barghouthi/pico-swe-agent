# pico: the tiniest coding agent, just 7 LoC!

7 lines of code that defines an LLM-based coding agent. Still, it's incredibly powerful!

## Usage

You need [uv](https://docs.astral.sh/uv/getting-started/installation/#installation-methods) installed and an AWS account configured (see [Models](#models) below for other providers).

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

## Models

By default, uses Claude via Amazon Bedrock. If you want to use other models, like OpenAI's, modify the `Agent` object following the [strands documentation](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/model-providers/).



## Inspiration

Similar in spirit to [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent), which is 100 lines of Python.

