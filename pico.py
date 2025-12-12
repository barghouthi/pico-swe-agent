import subprocess, sys
from strands import Agent, tool

@tool
def bash(cmd: str) -> str:
    """Run a bash command and return a simple, readable result."""
    return subprocess.run(["bash", "-lc", cmd], capture_output=True)

Agent(tools=[bash])(f"You are a one-shot SWE agent: {sys.argv[1:]}")