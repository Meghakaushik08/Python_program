'''import tkinter as tk
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

S.mainloop()   '''


import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to connect to the database
def connect_db():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    grade TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Function to add a student
def add_student():
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()

    if name == '' or age == '' or grade == '':
        messagebox.showerror('Error', 'Please fill in all fields')
    else:
        conn = sqlite3.connect('school.db')
        c = conn.cursor()
        c.execute('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', (name, age, grade))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success', 'Student added successfully')

# Function to display students
def display_students():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students')
    rows = c.fetchall()
    conn.close()

    # Clear the text area before displaying
    display_text.delete(1.0, tk.END)

    for row in rows:
        display_text.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}\n")

# Initialize the GUI
root = tk.Tk()
root.title('School Database Management System')

# Create labels and entry fields
tk.Label(root, text='Name:').grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text='Age:').grid(row=1, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

tk.Label(root, text='Grade:').grid(row=2, column=0)
grade_entry = tk.Entry(root)
grade_entry.grid(row=2, column=1)

# Create buttons
add_button = tk.Button(root, text='Add Student', command=add_student)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

display_button = tk.Button(root, text='Display Students', command=display_students)
display_button.grid(row=4, column=0, columnspan=2, pady=10)

# Create text area to display students
display_text = tk.Text(root, height=10, width=40)
display_text.grid(row=5, column=0, columnspan=2)

# Connect to the database
connect_db()

root.mainloop()