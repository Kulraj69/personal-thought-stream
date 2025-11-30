# Personal Thoughts Summary AI Agent

This repository contains an AI agent that automatically generates reflective journal entries based on your life context.

## How it works

1.  **Context**: The `life_context.md` file holds information about your current goals, focus, and life situation.
2.  **Agent**: The `agent.py` script reads this context and uses the Llama 3.1 model (via Hugging Face's OpenAI-compatible API) to generate a new journal entry.
3.  **Automation**: A GitHub Action runs this script twice daily (9:00 AM and 9:00 PM UTC).
4.  **Journal**: The generated entry is appended to `journal.md` and committed back to the repository.

## Setup

1.  **Clone the repository**.
2.  **Update `life_context.md`**: Add your own personal context.
3.  **Get a Hugging Face Token**:
    *   Go to [Hugging Face Settings > Tokens](https://huggingface.co/settings/tokens).
    *   Create a new token with `read` access (or `write` if you plan to do more).
4.  **Add Secret to GitHub**:
    *   Go to your repository's **Settings > Secrets and variables > Actions**.
    *   Click **New repository secret**.
    *   Name: `HF_TOKEN`
    *   Value: Your Hugging Face token.
5.  **Push to GitHub**: The action will run automatically on the schedule. You can also trigger it manually from the "Actions" tab.

## Local Usage

To run the agent locally:

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Set the environment variable:
    ```bash
    export HF_TOKEN=your_token_here
    ```
3.  Run the script:
    ```bash
    python agent.py
    ```
