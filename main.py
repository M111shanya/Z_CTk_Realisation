from customtkinter import *
import customtkinter

customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_appearance_mode("dark")

app = CTk()
app.title("Sudoku")
app.geometry("500x500")
app.grid_columnconfigure((0, 3, 6), weight=1)
app.grid_rowconfigure((0, 3, 6), weight=1)

def draw3x3(global_row, global_col):
    frame3x3 = CTkFrame(app, fg_color="#ffffff", corner_radius=0, border_width=0)
    frame3x3.grid(row=global_row, column=global_col, padx=2, pady=2, sticky="ewsn")
    for row in range(3):
        for col in range(3):
            frame = CTkFrame(frame3x3, fg_color="#100404", corner_radius=0, border_width=0)
            frame3x3.grid_columnconfigure((0, 1, 2), weight=1)
            frame3x3.grid_rowconfigure((0, 1, 2), weight=1)
            frame.grid(row=row, column=col, padx=0, pady=0, sticky="ewsn")
            entry = CTkEntry(frame, placeholder_text="5", fg_color="#ffffff", justify="center", corner_radius=0, border_width=0)
            frame.grid_columnconfigure((0), weight=1)
            frame.grid_rowconfigure((0), weight=1)
            entry.grid(padx=1, pady=1, sticky="nswe")
            
def draw9x9():
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            draw3x3(row, col)
            
draw9x9()

app.mainloop()