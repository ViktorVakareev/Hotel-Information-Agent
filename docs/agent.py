"""
agent.py
---------
Hotel Information Agent — client script for the Azure AI Foundry agent.

This mirrors the code Azure AI Foundry generates when you open your agent in
the Playground and select "View Code": it uses the Azure AI Foundry Agents
SDK (azure-ai-projects) rather than raw HTTP calls, and authenticates with
DefaultAzureCredential instead of a hardcoded key.

Replace the placeholders below with your own project connection string and
agent ID before running (see the "Configuration" section). Never commit real
values for PROJECT_CONNECTION_STRING or AGENT_ID-adjacent secrets to a public
repository — keep them in environment variables or a secrets manager.

Install dependencies:
    pip install azure-ai-projects azure-identity
"""

import os
import sys

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
# The project endpoint / connection string is found on the Overview page of
# your Azure AI Foundry project (Project Security / Credentials section).
# Store it as an environment variable rather than typing it here directly.
PROJECT_CONNECTION_STRING = os.environ.get(
    "PROJECT_CONNECTION_STRING",
    "<your-region>.api.azureml.ms;<subscription-id>;<resource-group>;<project-name>",
)

# The agent ID for the deployed Hotel Information Agent (visible in the
# Agents tab in Azure AI Foundry).
AGENT_ID = os.environ.get("AGENT_ID", "<your-agent-id>")


def get_client() -> AIProjectClient:
    """Create an authenticated client for the Azure AI Foundry project.

    DefaultAzureCredential tries several auth methods in order (environment
    variables, managed identity, Azure CLI login, etc.) so the same code
    works locally during development and in production without changes.
    """
    return AIProjectClient.from_connection_string(
        credential=DefaultAzureCredential(),
        conn_str=PROJECT_CONNECTION_STRING,
    )


def ask_agent(question: str) -> str:
    """Send one guest question to the agent and return its text reply.

    This walks the same perception -> reasoning -> action cycle described in
    the course: a thread is created, the guest's question is added to it as
    a "user" message (perception), the agent processes the thread against
    its system prompt and knowledge base (reasoning), and the resulting
    "assistant" message is the action returned to the caller.
    """
    client = get_client()

    # 1. Create a conversation thread for this guest interaction.
    thread = client.agents.create_thread()

    # 2. Perception: hand the guest's question to the agent as a JSON-shaped
    #    message — {"role": "user", "content": question}.
    client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content=question,
    )

    # 3. Reasoning + Action: run the agent against the thread. This is where
    #    the agent applies its system prompt, optionally searches its
    #    knowledge base, and generates a reply.
    run = client.agents.create_and_process_run(
        thread_id=thread.id,
        agent_id=AGENT_ID,
    )

    if run.status != "completed":
        raise RuntimeError(f"Agent run did not complete successfully: {run.status}")

    # 4. Retrieve the conversation, including the agent's reply, and pull out
    #    the most recent assistant message.
    messages = client.agents.list_messages(thread_id=thread.id)
    for message in messages.data:
        if message.role == "assistant":
            return message.content[0].text.value

    raise RuntimeError("No assistant response was found in the thread.")


def main() -> None:
    sample_question = "What time is checkout?"
    try:
        answer = ask_agent(sample_question)
        print(f"Guest asked: {sample_question}")
        print(f"Agent replied: {answer}")
    except Exception as exc:  # noqa: BLE001 - top-level demo error handling
        # A real application should distinguish auth failures (401), rate
        # limiting (429), and transient network errors, and show the guest a
        # graceful fallback message instead of a stack trace.
        print(f"Request failed: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
