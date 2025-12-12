import subprocess, sys
from strands import Agent, tool

@tool
def bash(cmd: str) -> str:
    """Run a bash command and returns results"""
    return subprocess.run(["bash", "-lc", cmd], capture_output=True)

Agent(tools=[bash])(f"One-shot SWE agent: {sys.argv[1:]}")