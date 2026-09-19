import json
import os
from ollama import chat, list as ollama_list

HISTORY_FILE = "history.json"

def choose_model():
    models_info = ollama_list()
    models = [m.model for m in models_info.models]

    if not models:
        print("No models found. Please run 'ollama pull <model>' first.")
        exit()

    print("Available models:")
    for i, m in enumerate(models, start=1):
        print(f"  {i}. {m}")

    while True:
        choice = input(f"Choose a model (1-{len(models)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(models):
            return models[int(choice) - 1]
        print("Invalid choice, try again.")

MODEL = choose_model()

# تحميل المحادثة القديمة لو موجودة
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        messages = json.load(f)
    print(f"📂 Loaded {len(messages)} previous messages.")
else:
    messages = []

def save_history():
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

print(f"\nUsing model: {MODEL}")
print("Local Chatbot — type 'exit' to quit, '/clear' to reset")
print("-" * 40)

while True:
    try:
        user_input = input("You: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
        break

    if user_input.lower() in ("exit", "quit", "/bye"):
        print("Goodbye!")
        break

    if user_input.lower() == "/clear":
        messages = []
        save_history()
        print("🧹 Conversation cleared!\n")
        continue

    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})
    try:
        print("Bot: ", end="", flush=True)
        full_reply = ""
        for chunk in chat(model=MODEL, messages=messages, stream=True):
            piece = chunk["message"]["content"]
            print(piece, end="", flush=True)
            full_reply += piece
        print("\n")
        messages.append({"role": "assistant", "content": full_reply})
        save_history()
    except Exception as e:
        print(f"Error: {e}")
        messages.pop()