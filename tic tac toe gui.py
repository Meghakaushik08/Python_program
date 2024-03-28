import tkinter as tk
from tkinter import messagebox

S = tk.Tk()
S.title("Tic Tac Toe")
S.resizable(0,0)

player_x = "x"
player_o = "O"
current_player = player_x
game_board = [["" for _ in range(3)] for _ in range(3)]
game_over = False

def on_click(row, col):
    global current_player, game_over
    if game_board[row][col] == "" and not game_over:
        game_board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_winner():
            messagebox.showinfo("Winner", f"Player {current_player} wins!")
            game_over = True
        elif check_draw():
            messagebox.showinfo("Draw", "It's a draw!")
            game_over = True
        else:
            current_player = player_o if current_player == player_x else player_x

def check_winner():
    for i in range(3):
        if game_board[i][0] == game_board[i][1] == game_board[i][2] != "":
            return True
        if game_board[0][i] == game_board[1][i] == game_board[2][i] != "":
            return True
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != "":
        return True
    if game_board[0][2] == game_board[1][1] == game_board[2][0] != "":
        return True
    return False

def check_draw():
    for row in game_board:
        for cell in row:
            if cell == "":
                return False
    return True

buttons = [[None, None, None] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(S, text="", font=('Cambria', 24), width=5, height=2,
                                   command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

S.mainloop()   