# Step 3 — Technical Documentation

Companion documentation for `agent.py`, the client script for the Hotel Information Agent. This covers the three deliverables Step 3 asks for: an architecture diagram, API documentation, and a configuration guide.

## Architecture diagram

![System architecture diagram showing User Input flowing to an API Endpoint, into the Agent, which applies its instructions and temperature/top-p settings, calls the deployed Model, optionally consults the Knowledge Base, and returns a Response Output to the guest](step3-architecture-diagram.png)

*Alt text: User input flows to the API endpoint, into the Agent, which applies its configured instructions and temperature/top-p, calls the Model, optionally consults the Knowledge Base, and returns a Response Output.*

The diagram shows the same request/response path documented for Step 1, at the system level: a guest's input reaches the agent through a single API endpoint, the agent (carrying its own instructions and configuration) calls the underlying model and — when connected — its knowledge base, and the result is returned as the response output.

## API documentation

| Endpoint / operation | Definition | Used by |
|---|---|---|
| **Agent endpoint** (project connection string / base URL, from the Overview page) | The web address where the agent can be reached. All other operations are made through the authenticated client built from this endpoint. | `get_client()` |
| **Create thread** (`agents.create_thread`) | Starts a new conversation thread — a container that holds the message history for one guest interaction. | `ask_agent()`, step 1 |
| **Create message** (`agents.create_message`) | Adds a message to a thread. Used here to add the guest's question as a `"user"`-role message. | `ask_agent()`, step 2 |
| **Create and process run** (`agents.create_and_process_run`) | Triggers the agent to process the thread: apply its instructions, consult its knowledge base if attached, and generate a reply. This is the reasoning + action step. | `ask_agent()`, step 3 |
| **List messages** (`agents.list_messages`) | Retrieves the full thread, including the agent's generated reply, so the calling code can read the answer back out. | `ask_agent()`, step 4 |

### Sample request

The guest's question, as it's structured when added to the thread:

```json
{
  "role": "user",
  "content": "What time is checkout?"
}
```

### Sample response

The agent's reply, retrieved from the thread after the run completes:

```json
{
  "role": "assistant",
  "content": "Check-out is at 11 AM. Would you like to request a late checkout?"
}
```

### Authentication

Requests are authenticated with `DefaultAzureCredential` rather than a hardcoded key — it resolves credentials from the environment (managed identity in production, Azure CLI login locally), so no secret ever needs to appear in source code. The connection string itself (`PROJECT_CONNECTION_STRING`) is read from an environment variable for the same reason.

### Error handling

| Condition | What `agent.py` does |
|---|---|
| Run does not complete (`run.status != "completed"`) | Raises a `RuntimeError` with the run's status, instead of returning a partial or missing answer |
| No assistant message found | Raises a `RuntimeError` rather than returning an empty string |
| Any other exception (auth failure, network error, etc.) | Caught in `main()`, printed to stderr, and exits with a non-zero status — a production caller would instead show the guest a graceful fallback message |

## Configuration guide

These are the agent's configurable parameters, set during agent setup in Azure AI Foundry (not in `agent.py` itself — the client script just calls the already-configured agent):

| Parameter | Plain-language explanation | Notes |
|---|---|---|
| **Temperature** | Controls how creative or conservative the agent's answers are. Lower values (e.g. 0.2–0.3) give more consistent, predictable answers — good for factual questions like check-in times. Higher values give more varied, conversational answers — better suited to open-ended recommendations. | Set to 0.5 as a starting point for the Hotel Information Agent; adjust one parameter at a time when tuning. |
| **Top-p** | Limits how wide a range of possible next words the agent considers. Lower values make responses more focused and predictable; higher values allow more variety. | Also set to 0.5 as a starting point. Change temperature or top-p, not both at once, so you can tell which change caused a difference. |
| **System instructions (prompt)** | The behavioral rules the agent follows on every turn — what it should and shouldn't answer, how to cite sources, when to escalate to staff. | This is where grounding, guardrails, and citation requirements (`[Source: filename]`) are defined. |
| **Knowledge base** | The documents the agent can search before answering (structured data, unstructured documents, or a live/dynamic connection). | Optional — if none is attached, the agent answers from its instructions alone. |
| **Model selection** | Which deployed language model handles the agent's reasoning (lightweight, balanced, or advanced). | Trades off speed, accuracy, and cost; configured under Models + Endpoints. |

## Checklist

- [x] Diagram includes alt text
- [x] Each API operation is defined with an example call/response
- [x] Configuration parameters are listed with short, clear definitions
