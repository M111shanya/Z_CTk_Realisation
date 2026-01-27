# Валидация: https://metanit.com/python/tkinter/2.8.php
# Работа с библиотекой и разметка: 
# https://customtkinter.tomschimansky.com/tutorial/grid-system
# https://customtkinter.tomschimansky.com/tutorial/frames
# https://customtkinter.tomschimansky.com/documentation/

from customtkinter import *
import customtkinter
import sudoku
import random

customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_appearance_mode("dark")

seed = 0

app = CTk()
app.title("Sudoku")
app.geometry("500x500")
app.grid_columnconfigure((0, 3, 6, 10), weight=1)
app.grid_rowconfigure((0, 3, 6), weight=1)

cells = {}

def VelidateNumber(P):
    return (P.isdigit() or P == "") and len(P) < 2

reg = app.register(VelidateNumber)

def generateBoard():
    global seed
    seed = random.randint(1, 10000)
    board =  sudoku.Sudoku(seed=seed).difficulty(0.3).board
    for i, row in enumerate(board):
        for j, el in enumerate(row):
            if el == None:
                board[i][j] = ""
    return board

def generate_solution():
    global seed
    return sudoku.Sudoku(seed=seed).solve().board

def draw3x3(global_row, global_col):
    frame3x3 = CTkFrame(app, fg_color="#ffffff", corner_radius=0, border_width=0)
    frame3x3.grid(row=global_row, column=global_col, padx=2, pady=2, sticky="ewsn")
    for row in range(3):
        for col in range(3):
            frame = CTkFrame(frame3x3, fg_color="#100404", corner_radius=0, border_width=0)
            frame3x3.grid_columnconfigure((0, 1, 2), weight=1)
            frame3x3.grid_rowconfigure((0, 1, 2), weight=1)
            frame.grid(row=row, column=col, padx=0, pady=0, sticky="ewsn")
            entry = CTkEntry(frame, fg_color="#ffffff", font=("Arial", 20, "bold"), text_color="black", justify="center",
                             corner_radius=0, border_width=0, validate="key", validatecommand=(reg, "%P"))
            frame.grid_columnconfigure((0), weight=1)
            frame.grid_rowconfigure((0), weight=1)
            entry.grid(padx=1, pady=1, sticky="nswe")
            cells[(global_row + row), (global_col + col)] = entry
            
def draw9x9():
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            draw3x3(row, col)

def feelBoard():
    board = generateBoard()
    for i in range(9):
        for j in range(9):
            cells[i, j].delete(0, END)
            cells[i, j].configure(fg_color="#ffffff")
            cells[i, j].insert(0, str(board[i][j]))
            if board[i][j] != "":
                cells[i, j].configure("readonli", fg_color="#7A7A7A") # Поменять цвет!
            
def getValues():
    board = []
    for row in range(2, 11):
        rows = []
        for col in range(1, 10):
            val = cells[(row,col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))

        board.append(rows)
    return board

def check_solution():
    pass

def solveBoard():
    solution = generate_solution()
    for i in range(9):
        for j in range(9):
            cells[i, j].delete(0, END)
            cells[i, j].configure(fg_color="#ffffff")
            cells[i, j].insert(0, str(solution[i][j]))
            
draw9x9()
feelBoard()

btn = CTkButton(app, text="Новая игра", command=feelBoard)
btn.grid(row=10, column=0, columnspan=3, sticky="ew")

btn = CTkButton(app, text="Решить", command=solveBoard)
btn.grid(row=10, column=4, columnspan=3, sticky="ew")

app.mainloop()
