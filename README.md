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
| adk-tutorial.step_<1-6>  | multi-agent system for a Weather Bot agent team | https://adk.dev/tutorials/agent-team/  |


## Options for running the agents

`adk web --port 8000` - run agent with web UI interface (dev/debugging only, not prod)

`adk run <agent name>` - run a specific agent in terminal


## Notes of what I learnt

- uv is a combined python, virtual env and deps manager all in one. It's quicker than pip and written in Rust.
- `adk create <agent name>` - create new agent.
- each folder -> different agent. You can switch between then in the header dropdown on the web interface.
- litellm currently needs at most python 3.13 to run. SO cannot use latest version 3.14.
- [Key Concept: Docstrings are Crucial!](https://adk.dev/tutorials/agent-team/#:~:text=Key%20Concept:%20Docstrings%20are%20Crucial!) Best Practice: Write clear, descriptive, and accurate docstrings for your tools. This is essential for the LLM to use the tool correctly. The agent's LLM relies heavily on the function's docstring to understand:
    - What the tool does.
    - When to use it.
    - What arguments it requires (city: str).
    - What information it returns.
- Params for an Agent (orchestrator of user, LLM and tool interactions):
    - **name**: Unique id for the agent. Be descriptive. This appears in the graph view of the web UI (the name in the app selection dropdown is determined by the directory path name(s))
    - **model**: Which LLM to use e.g. "gemini-3.1-flash-lite".
    - **description**: What other agents use to determine what this agent does (key for delegation of tasks). It should be a short summary of the agent's purpose.
    - **instruction**: How the agent should behave. It's persona, goals and *how* & *when* to use it's tools. Use clear and specific prompts. More detailed on role and how to use the tools the better. Be explicit about error handling if needed. 
    - **tools**: List of functions that the agent is allowed to use.
- agent names (including directory paths to agents) can't have dashes or spaces. Example error: `'adk-tutorial.step_1'. Agent names must be valid Python identifiers or paths separated by dots (letters, digits, underscores, and dots).
- LiteLlm is only needed when you want to route through non-Gemini providers (Anthropic, OpenAI, etc.) via LiteLLM's unified API. No need if just using Gemini.
- For LiteLlm, in the .env files the XXX_API_KEY vars are not referenced in the files. They are instead pre-expected names that LiteLLM uses to pair the model provider to the correct key e.g.  GOOGLE_API_KEY -> gemini/<model>. See the [example .env](<./adk_tutorial/.env example>) for reference