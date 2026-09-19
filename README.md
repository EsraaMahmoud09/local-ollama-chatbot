# local-ollama-chatbot

# Local AI Chatbot with Ollama

A terminal-based chatbot that runs entirely offline using a local LLM served by [Ollama](https://ollama.com).

The chatbot communicates with a locally running Ollama instance through the official Ollama Python library. It supports interactive conversations, persistent history, model selection, streamed responses, and basic error handling.

> **Note:** Inference runs locally — no cloud API is needed for chatting. An internet connection is only required initially, to install Ollama and download a model.

---

## Features

* 💬 Interactive terminal chat with a locally running LLM
* 💾 Conversation history saved automatically to `history.json` and reloaded on startup
* 🧹 `/clear` command to reset the conversation
* 🔀 Choose which installed Ollama model to use at startup
* ⚡ Streamed responses (text appears progressively, like ChatGPT)
* 🛡️ Basic error handling for runtime/Ollama errors

---

## Requirements

* [Ollama](https://ollama.com) installed
* Python 3.10.9
* At least one model pulled locally:

bash

```bash
  ollama pull llama3.2:3b
```

---

## Setup

1. Create and activate a virtual environment (inside the project folder):

bash

```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
```

2. Install the required package:

bash

```bash
   pip install ollama
```

> If you're getting this project from GitHub instead of building it locally, clone it first with `git clone <repo-url>`, then follow the steps above.


---

## Usage

bash

```bash
python chatbot.py
```

You'll be asked to pick one of your installed models, then you can start chatting.

**Example (with** **`llama3.2:3b`** **as the only model installed):**

text

```text
Available models:
  1. llama3.2:3b
Choose a model (1-1): 1

Using model: llama3.2:3b
You: how are you?
Bot:I'm just a computer program, so I don't have feelings or emotions
like humans. I'm always "on" and ready to help, 24/7!
I don't have good or bad days, but I'm always here to assist
and chat with users like you, Esraa.
```

The model selector supports multiple installed models, but this project was built and tested with a single model, `llama3.2:3b`.

### Commands

| CommandDescription     |                                                              |
| ---------------------- | ------------------------------------------------------------ |
| `exit`, `quit`, `/bye` | End the chat                                                 |
| `/clear`               | Clear conversation history (in memory and in `history.json`) |

---

## Project Structure

text

```text
chatbot_project/
├── chatbot.py        # Main chatbot script
├── history.json      # Auto-generated conversation history (not tracked in git)
├── requirements.txt  # Python dependencies
└── README.md
```

---

## How It Works

text

```text
User → Python chatbot → Ollama Python library → Ollama local API → Local LLM → Streamed response
```

The full conversation history is sent with each request so the model keeps context. Each exchange is appended to `history.json`, which is reloaded automatically the next time the chatbot starts.
