# How Requests Travel Through the Hotel Information Agent

This document explains what happens between a guest asking a question and the Hotel Information Agent answering it, based on the generated code visible via **Agents → Try in Playground → View Code** in Azure AI Foundry. It covers the four things Step 1 of the activity asks for: the API endpoint, the JSON message flow, the perception–reasoning–action cycle, and authentication/credentials management.

![Diagram of the request flow through the Hotel Information Agent, from guest input through the API endpoint, the agent's perception, reasoning, and action steps, and back](agent-architecture-diagram.png)

*Six steps, left to right: the guest's question is packaged into JSON by the application, sent over the API endpoint with an auth token, read by the agent (perception), processed against the system prompt and knowledge base (reasoning), turned into an answer (action), and returned as JSON through the same endpoint for the application to display.*

## 1. API endpoint

Every request to the agent goes to a single project-specific URL — the **agent endpoint** — shown on the Overview page in Azure AI Foundry. This is distinct from a *model endpoint*, which talks to the underlying language model directly rather than to the configured agent (with its instructions and knowledge base attached). An external application never needs to know anything about the model underneath; it only needs this one URL to reach the agent.

## 2. JSON message flow

Requests and responses are both structured as JSON so that the application and the agent can reliably exchange information. Each message is an object with two fields:

```json
{
  "role": "user",
  "content": "What time is checkout?"
}
```

`role` identifies who is speaking (`user` for the guest, `assistant` for the agent's reply), and `content` holds the actual text. When the application sends the guest's question, it POSTs a payload containing this JSON in the request body. The agent's reply comes back in the same shape, with `role` set to `assistant`:

```json
{
  "role": "assistant",
  "content": "Check-out is at 11 AM. Would you like to request a late checkout?"
}
```

This consistent structure is what lets the conversation history be tracked accurately — the log always shows who said what.

## 3. Perception → reasoning → action cycle

Once a request reaches the agent, it goes through three stages:

- **Perception** — the agent reads the incoming message and identifies the role (`user`) and the content (the guest's question).
- **Reasoning** — the agent applies its system prompt (the instructions set during configuration) to decide how to behave, then evaluates the guest's question against those instructions. If the agent has a knowledge base attached, this is also where it searches the uploaded documents for relevant information (e.g. the hotel's policy document for a checkout-time question).
- **Action** — the agent turns its reasoning into a response, following whatever citation or formatting rules were set in its instructions, and packages that response back into the `assistant`-role JSON described above.

This cycle runs on every single turn of the conversation — the agent doesn't retain reasoning from a previous turn beyond what's included in the conversation history sent with the request.

## 4. Authentication and credentials management

Every request must prove it's coming from an authorized source. This is done with an **API key**, found in the Project's Security/Credentials section, sent in the request's `Authorization` header (typically `Authorization: Bearer <API_KEY>`). A request with a missing or incorrect key gets rejected with a `401 Unauthorized` status before the agent ever processes it.

The key security practice: the API key is never hardcoded into application source code, especially code that might be pushed to a public repository. Instead, it's stored using environment variables or a secrets manager (in Azure, this typically means `DefaultAzureCredential` paired with Azure Key Vault) and read into the application at runtime. This keeps the key out of version control and limits who can retrieve it.

## Status codes and error handling

A well-behaved application checks the response status code before trusting the response body:

| Status | Meaning | What the application should do |
|---|---|---|
| `200` | Success | Read `content` from the response JSON and display it |
| `401` | Unauthorized (bad/missing API key) | Show an error, don't attempt to parse a response body |
| Other (e.g. timeout, `400`) | Request failed | Show a fallback message rather than crashing |

Checking the status code first — rather than assuming every request succeeds — is what separates a demo script from something dependable enough to put in front of real guests.
