import random
import tkinter as tk
from tkinter import messagebox

w = tk.Tk()
my_font = ["Helvetica", 40]

buttons = []
human_win = 0
comp_win = 0
win = [
    [[0, 0], [0, 1], [0, 2]],
    [[1, 0], [1, 1], [1, 2]],
    [[2, 0], [2, 1], [2, 2]],
    [[0, 0], [1, 0], [2, 0]],
    [[0, 1], [1, 1], [2, 1]],
    [[0, 2], [1, 2], [2, 2]],
    [[0, 0], [1, 1], [2, 2]],
    [[0, 2], [1, 1], [2, 0]],
]

turn = "p1"

def new_game():
    global human_win, comp_win, turn
    turn = "p1"
    r1["state"] = "normal"
    r2["state"] = "normal"
    result.config(text=f"Рахунок {human_win} : {comp_win}")
    for i in buttons:
        for j in i:
            j['text'] = ""

def check_draw():
    global human_win, comp_win
    draw = True
    for i in buttons:
        for j in i:
            if not j['text']:
                draw = False
    if draw:
        messagebox.showerror(message="Нічия!")
        comp_win += 0.5
        human_win += 0.5
        new_game()
    return draw

def check_winner():
    global human_win, comp_win
    for w in win:
        if buttons[w[0][0]][w[0][1]]['text'] == buttons[w[1][0]][w[1][1]]['text'] == buttons[w[2][0]][w[2][1]]['text'] == "X":
            messagebox.showinfo(message="Гравець 1 виграв!")
            human_win += 1
            new_game()
            return 1
        if buttons[w[0][0]][w[0][1]]['text'] == buttons[w[1][0]][w[1][1]]['text'] == buttons[w[2][0]][w[2][1]]['text'] == "O":
            if game_mode.get() == 1:
                messagebox.showinfo(message="PC виграв!")
            if game_mode.get() == 2:
                messagebox.showinfo(message="Гравець 2 виграв!")
            comp_win += 1
            new_game()
            return 2
    return False

def left_click(e):
    x = e.widget.grid_info()["row"]
    y = e.widget.grid_info()["column"]
    r1["state"] = "disabled"
    r2["state"] = "disabled"
    global turn, human_win, comp_win

    if game_mode.get() == 1:
        # #1: хід гравця
        if not (buttons[x][y]['text'] == ""):
            return
        buttons[x][y].config(text = "X")

        # #2: перевірити чи гравець виграв
        if check_winner():
            return

        if check_draw():
            return

        # #3: хід ПК
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if not (buttons[x][y]['text'] == ""):
                continue
            else:
                buttons[x][y].config(text = "O")
                break

        # #4: перевірити чи ПК виграв
        if check_winner():
            return

    if game_mode.get() == 2 and turn == "p1":
        # 1 хід гравця
        turn = "p2"
        if not (buttons[x][y]['text'] == ""):
            return
        buttons[x][y].config(text = "X")

        # #2: перевірити чи гравець виграв
        if check_winner():
            return

        if check_draw():
            return

def right_click(e):
    global turn, human_win, comp_win
    if game_mode.get() == 2 and turn == "p2":
        turn = "p1"
        x = e.widget.grid_info()["row"]
        y = e.widget.grid_info()["column"]
        r1["state"] = "disabled"
        r2["state"] = "disabled"

        # 1 хід гравця №2
        if not (buttons[x][y]['text'] == ""):
            return
        buttons[x][y].config(text="O")

        # #2: перевірити чи гравець №2 виграв
        if check_winner():
            return

        if check_draw():
            return

for i in range(3):
    t = []
    for j in range(3):
        b = tk.Button(w, height=1, width=3, font=my_font, relief="sunken", bd=5)
        b.bind("<Button-1>",left_click)
        b.bind("<Button-3>",right_click)
        t.append(b)
    buttons.append(t)

for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j, padx=2, pady=2)

result = tk.Label(w, text=f"Рахунок {human_win} : {comp_win}")
result.grid(row=3, column=0, columnspan=3)
game_mode = tk.IntVar()
game_mode.set(1)
r1 = tk.Radiobutton(w, text="Гра з PC", variable=game_mode, value=1)
r2 = tk.Radiobutton(w, text="Гра з другом", variable=game_mode, value=2)
r1.grid(row=4, column=0)
r2.grid(row=4, column=2)

w.mainloop()