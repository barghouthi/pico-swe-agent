import subprocess, sys
from strands import Agent, tool

@tool
def run_bash(cmd: str) -> str:
    """Run a bash command and return a simple, readable result."""
    r = subprocess.run(["bash", "-lc", cmd], capture_output=True)
    return f"exit_code:{r.returncode}\nstdout:\n{r.stdout}\nstderr:\n{r.stderr}"

Agent(tools=[run_bash])(f"You are a SWE agent. {sys.argv[1:]}")