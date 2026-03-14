import tkinter as tk
from tkinter import scrolledtext
import random

# ==============================
# MOVIE DATASET
# ==============================

movies = [
    {"title":"Interstellar","genre":"sci-fi","rating":4.8},
    {"title":"Inception","genre":"sci-fi","rating":4.7},
    {"title":"The Matrix","genre":"sci-fi","rating":4.6},

    {"title":"Avengers Endgame","genre":"action","rating":4.7},
    {"title":"John Wick","genre":"action","rating":4.6},
    {"title":"Mad Max Fury Road","genre":"action","rating":4.5},

    {"title":"The Hangover","genre":"comedy","rating":4.4},
    {"title":"Superbad","genre":"comedy","rating":4.3},
    {"title":"Rush Hour","genre":"comedy","rating":4.2},

    {"title":"Titanic","genre":"romance","rating":4.8},
    {"title":"The Notebook","genre":"romance","rating":4.5},
    {"title":"La La Land","genre":"romance","rating":4.4},

    {"title":"The Conjuring","genre":"horror","rating":4.4},
    {"title":"Insidious","genre":"horror","rating":4.2},
    {"title":"A Quiet Place","genre":"horror","rating":4.5}
]

user_ratings = {}


# ==============================
# RECOMMENDATION ENGINE
# ==============================

def recommend_movies(genre):

    results = []

    for m in movies:
        if m["genre"] == genre:
            score = m["rating"]

            if m["title"] in user_ratings:
                score += user_ratings[m["title"]] * 0.3

            results.append((score,m["title"]))

    results.sort(reverse=True)

    return [r[1] for r in results[:5]]


# ==============================
# MESSAGE DISPLAY
# ==============================

def add_message(sender,message):

    if sender=="user":

        chat.insert(tk.END,"\nYou:\n","user")
        chat.insert(tk.END,message+"\n","user_msg")

    else:

        chat.insert(tk.END,"\nSystem:\n","bot")
        chat.insert(tk.END,message+"\n","bot_msg")

    chat.yview(tk.END)


# ==============================
# PROCESS INPUT
# ==============================

def process():

    text = entry.get().lower()

    if text.strip()=="":
        return

    add_message("user",text)

    # rating command example: rate inception 5
    if text.startswith("rate"):

        parts = text.split()

        if len(parts)>=3:

            movie = " ".join(parts[1:-1]).title()
            rating = int(parts[-1])

            user_ratings[movie] = rating

            add_message("bot",f"Thanks! You rated {movie} {rating}/5 ⭐")

    else:

        for g in ["action","comedy","sci-fi","romance","horror"]:

            if g in text:

                recs = recommend_movies(g)

                msg="Top recommendations:\n"

                for r in recs:
                    msg+="• "+r+"\n"

                add_message("bot",msg)

                break
        else:

            add_message("bot",
            "Try asking:\n• action movies\n• comedy movies\n• sci-fi movies\n\nYou can also rate movies:\nrate inception 5")

    entry.delete(0,tk.END)


# ==============================
# GUI
# ==============================

root = tk.Tk()
root.title("🎬 Smart Movie Recommendation System")
root.geometry("550x650")
root.configure(bg="#0f172a")


title = tk.Label(
    root,
    text="🎬 Smart Recommendation System",
    font=("Arial",18,"bold"),
    bg="#0f172a",
    fg="white"
)

title.pack(pady=10)


chat = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial",12),
    bg="#1e293b",
    fg="white",
    height=28
)

chat.pack(padx=10,pady=10)


chat.tag_config("user",foreground="#38bdf8",font=("Arial",11,"bold"))
chat.tag_config("bot",foreground="#22c55e",font=("Arial",11,"bold"))

chat.tag_config("user_msg",foreground="white")
chat.tag_config("bot_msg",foreground="#e2e8f0")


frame = tk.Frame(root,bg="#0f172a")
frame.pack(pady=10)


entry = tk.Entry(frame,font=("Arial",12),width=32)
entry.grid(row=0,column=0,padx=10)


btn = tk.Button(
    frame,
    text="Recommend",
    font=("Arial",11,"bold"),
    bg="#22c55e",
    fg="white",
    width=12,
    command=process
)

btn.grid(row=0,column=1)


root.bind("<Return>",lambda event:process())


add_message("bot",
"Welcome to Smart Movie Recommender 🎬\n\nAsk for genres like:\n• action movies\n• comedy movies\n• sci-fi movies\n\nYou can also rate movies:\nrate inception 5")


root.mainloop()