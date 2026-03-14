import tkinter as tk
from tkinter import messagebox
import math

# ===============================
# GAME LOGIC
# ===============================

board = [""] * 9
human = "X"
ai = "O"


def check_winner(b):

    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for condition in win_conditions:
        a,b1,c = condition
        if b[a] == b[b1] == b[c] and b[a] != "":
            return b[a]

    if "" not in b:
        return "Draw"

    return None


# ===============================
# MINIMAX ALGORITHM
# ===============================

def minimax(new_board, is_maximizing):

    result = check_winner(new_board)

    if result == ai:
        return 1
    elif result == human:
        return -1
    elif result == "Draw":
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(9):
            if new_board[i] == "":
                new_board[i] = ai
                score = minimax(new_board, False)
                new_board[i] = ""
                best_score = max(score, best_score)

        return best_score

    else:

        best_score = math.inf

        for i in range(9):
            if new_board[i] == "":
                new_board[i] = human
                score = minimax(new_board, True)
                new_board[i] = ""
                best_score = min(score, best_score)

        return best_score


def best_move():

    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == "":
            board[i] = ai
            score = minimax(board, False)
            board[i] = ""

            if score > best_score:
                best_score = score
                move = i

    return move


# ===============================
# BUTTON CLICK
# ===============================

def player_move(i):

    if board[i] != "":
        return

    board[i] = human
    buttons[i]["text"] = human

    winner = check_winner(board)

    if winner:
        end_game(winner)
        return

    ai_move()


def ai_move():

    move = best_move()

    if move is not None:
        board[move] = ai
        buttons[move]["text"] = ai

    winner = check_winner(board)

    if winner:
        end_game(winner)


# ===============================
# END GAME
# ===============================

def end_game(winner):

    if winner == "Draw":
        messagebox.showinfo("Game Over", "It's a Draw!")
    else:
        messagebox.showinfo("Game Over", f"{winner} Wins!")

    reset_game()


def reset_game():

    global board
    board = [""] * 9

    for b in buttons:
        b["text"] = ""


# ===============================
# GUI
# ===============================

root = tk.Tk()
root.title("🤖 Tic Tac Toe AI")
root.geometry("350x420")
root.configure(bg="#0f172a")


title = tk.Label(
    root,
    text="🤖 Tic Tac Toe AI",
    font=("Arial",18,"bold"),
    bg="#0f172a",
    fg="white"
)

title.pack(pady=15)


frame = tk.Frame(root,bg="#0f172a")
frame.pack()

buttons = []

for i in range(9):

    btn = tk.Button(
        frame,
        text="",
        font=("Arial",22,"bold"),
        width=5,
        height=2,
        bg="#1e293b",
        fg="white",
        command=lambda i=i: player_move(i)
    )

    btn.grid(row=i//3,column=i%3,padx=5,pady=5)

    buttons.append(btn)


reset_btn = tk.Button(
    root,
    text="Restart Game",
    font=("Arial",12,"bold"),
    bg="#22c55e",
    fg="white",
    command=reset_game
)

reset_btn.pack(pady=20)


root.mainloop()