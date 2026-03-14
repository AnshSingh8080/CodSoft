import tkinter as tk
from tkinter import scrolledtext
import random
import re
from datetime import datetime


# ============================
# INTENTS
# ============================

INTENTS = [
    {
        "name": "greeting",
        "keywords": ["hello", "hi", "hey"],
        "responses": [
            "Hello! 👋 How can I help you today?",
            "Hi there! What would you like to talk about?",
            "Hey! Nice to see you."
        ]
    },

    {
        "name": "identity",
        "keywords": ["who are you", "your name"],
        "responses": [
            "I'm SmartBot 🤖, a rule-based NLP chatbot built with Python.",
        ]
    },

    {
        "name": "joke",
        "keywords": ["joke", "funny"],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why do Python developers wear glasses? Because they can't C! 😂"
        ]
    },

    {
        "name": "help",
        "keywords": ["help", "what can you do"],
        "responses": [
            "You can ask me about:\n• Time\n• Date\n• Jokes\n• AI\n• Python\n• General chat"
        ]
    }
]


# ============================
# INTENT MATCHER
# ============================

def match_intent(text):

    text = text.lower()

    for intent in INTENTS:
        for keyword in intent["keywords"]:
            if keyword in text:
                return random.choice(intent["responses"])

    # Time query
    if "time" in text:
        return "Current time is " + datetime.now().strftime("%H:%M:%S")

    if "date" in text:
        return "Today's date is " + datetime.now().strftime("%d %B %Y")

    if "python" in text:
        return "Python is a powerful programming language widely used in AI, automation, and data science."

    if "ai" in text:
        return "Artificial Intelligence allows machines to simulate human intelligence."

    return random.choice([
        "Interesting question. Tell me more!",
        "Hmm, I'm not fully sure about that.",
        "Could you explain that differently?"
    ])


# ============================
# ADD MESSAGE
# ============================

def add_message(sender, message):

    time = datetime.now().strftime("%H:%M")

    if sender == "user":
        chat_area.insert(tk.END, f"\nYou ({time})\n", "user")
        chat_area.insert(tk.END, message + "\n", "user_msg")

    else:
        chat_area.insert(tk.END, f"\nBot ({time})\n", "bot")
        chat_area.insert(tk.END, message + "\n", "bot_msg")

    chat_area.yview(tk.END)


# ============================
# SEND MESSAGE
# ============================

def send_message():

    user_text = entry.get()

    if user_text.strip() == "":
        return

    add_message("user", user_text)

    response = match_intent(user_text)

    add_message("bot", response)

    entry.delete(0, tk.END)


# ============================
# GUI
# ============================

root = tk.Tk()
root.title("Smart AI Chatbot")
root.geometry("550x650")
root.configure(bg="#0f172a")


# TITLE
title = tk.Label(
    root,
    text="🤖 Smart AI Chatbot",
    font=("Arial", 18, "bold"),
    bg="#0f172a",
    fg="white"
)
title.pack(pady=10)


# CHAT AREA
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 12),
    bg="#1e293b",
    fg="white",
    height=28
)

chat_area.pack(padx=10, pady=10)


# TAG STYLES
chat_area.tag_config("user", foreground="#38bdf8", font=("Arial", 11, "bold"))
chat_area.tag_config("bot", foreground="#22c55e", font=("Arial", 11, "bold"))

chat_area.tag_config("user_msg", foreground="white")
chat_area.tag_config("bot_msg", foreground="#e2e8f0")


# INPUT FRAME
input_frame = tk.Frame(root, bg="#0f172a")
input_frame.pack(pady=10)


entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    width=35
)
entry.grid(row=0, column=0, padx=10)


send_btn = tk.Button(
    input_frame,
    text="Send",
    command=send_message,
    bg="#22c55e",
    fg="white",
    font=("Arial", 11, "bold"),
    width=10
)

send_btn.grid(row=0, column=1)


# ENTER KEY
root.bind("<Return>", lambda event: send_message())


# START MESSAGE
add_message("bot", "Hello! I'm SmartBot 🤖. Ask me anything.")


root.mainloop()