import subprocess, sys
from strands import Agent, tool
from strands.models.openai import OpenAIModel

@tool
def bash(cmd: str) -> str:
    """Run a bash command and return a simple, readable result."""
    return subprocess.run(["bash", "-lc", cmd], capture_output=True)

model = OpenAIModel(model_id="gpt-5.2")

Agent(tools=[bash], model=model)(f"You are a one-shot SWE agent: {sys.argv[1:]}")