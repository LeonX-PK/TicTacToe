import tkinter as tk
from tkinter import messagebox
import random

# Setup root window
root = tk.Tk()
root.title("Tic Tac Toe – Player vs Bot 🤖")
root.geometry("400x500")
root.config(bg="#1e1e2f")

# Initial values
board = [""] * 9
buttons = []
player = "X"
bot = "O"
current_player = player

# Score tracking
score_x = 0
score_o = 0
score_draw = 0

# Update the scoreboard
def update_scoreboard():
    score_label.config(text=f"You (X): {score_x}   Bot (O): {score_o}   Draws: {score_draw}")

# Check for win/draw
def check_winner():
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

# Bot makes a random move
def ai_move():
    empty = [i for i in range(9) if board[i] == ""]
    if empty:
        move = random.choice(empty)
        board[move] = bot
        buttons[move].config(text=bot, fg="blue")
        winner = check_winner()
        handle_result(winner)

# Handle result popup and score
def handle_result(winner):
    global score_x, score_o, score_draw
    if winner:
        if winner == "Draw":
            score_draw += 1
            messagebox.showinfo("Result", "🤝 It's a draw!")
        elif winner == player:
            score_x += 1
            messagebox.showinfo("Result", "🎉 You win!")
        else:
            score_o += 1
            messagebox.showinfo("Result", "🤖 Bot wins!")
        update_scoreboard()
        reset_board(clear_scores=False)

# On player click
def on_click(i):
    if board[i] == "":
        board[i] = player
        buttons[i].config(text=player, fg="red")
        winner = check_winner()
        if winner:
            handle_result(winner)
        else:
            root.after(500, ai_move)

# Reset board, optionally clear score
def reset_board(clear_scores=False):
    global board, score_x, score_o, score_draw
    board = [""] * 9
    for btn in buttons:
        btn.config(text="")
    if clear_scores:
        score_x = 0
        score_o = 0
        score_draw = 0
    update_scoreboard()

# UI Layout
label = tk.Label(root, text="You vs Bot (X vs O)", font=("Helvetica", 16), bg="#1e1e2f", fg="white")
label.pack(pady=10)

score_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#1e1e2f", fg="#cccccc")
score_label.pack(pady=5)

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack()

for i in range(9):
    btn = tk.Button(frame, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

reset_btn = tk.Button(root, text="🔁 Reset Board", font=("Helvetica", 12), bg="#444", fg="white",
                      command=lambda: reset_board(clear_scores=False))
reset_btn.pack(pady=10)

clear_btn = tk.Button(root, text="🧹 Clear Scores", font=("Helvetica", 12), bg="#222", fg="white",
                      command=lambda: reset_board(clear_scores=True))
clear_btn.pack(pady=5)

# Init scoreboard
update_scoreboard()
root.mainloop()
