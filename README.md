# Goofing around with Google ADK

Following the getting started guide from Google: https://adk.dev/get-started/python/

## Setup

```zsh
uv venv
source .venv/bin/activate
uv sync
adk web --port 8000
```

## Options for running the agent


`adk web --port 8000` - run agent with web UI interface (dev/debugging only, not prod)
`adk run my_agent` - run agent in terminal