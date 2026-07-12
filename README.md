# Goofing around with Google ADK

Learning about ADK using Google's https://adk.dev/ docs

## Quickstart

```zsh
uv venv
source .venv/bin/activate
uv sync
adk web --port 8000
```

## Agents
| Agent    | purpose | tutorial link |
| -------- | ------- | ------- |
| my_agent  | returns the time for a given city. Set to 10:30AM for all cities    | https://adk.dev/get-started/python/  |
| multi_tool_agent  | returns time and weather for a given city. Set to only work for Edinburgh (and London for time only) | https://adk.dev/tutorials/multi-tool-agent/  |
| adk-tutorial/step_<1-6>  | multi-agent system for a Weather Bot agent team | https://adk.dev/tutorials/agent-team/  |


## Options for running the agents

`adk web --port 8000` - run agent with web UI interface (dev/debugging only, not prod)

`adk run <agent name>` - run a specific agent in terminal


## Notes of what I learnt

- uv is a combined python, virtual env and deps manager all in one. It's quicker than pip and written in Rust.
- `adk create <agent name>` - create new agent.
- each folder -> different agent. You can switch between then in the header dropdown on the web interface.
- litellm currently needs at most python 3.13 to run. SO cannot use latest version 3.14.
