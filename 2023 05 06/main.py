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

def check_winner():
    for w in win:
        if buttons[w[0][0]][w[0][1]]['text'] == buttons[w[1][0]][w[1][1]]['text'] == buttons[w[2][0]][w[2][1]]['text'] == "X":
            return 1
        if buttons[w[0][0]][w[0][1]]['text'] == buttons[w[1][0]][w[1][1]]['text'] == buttons[w[2][0]][w[2][1]]['text'] == "O":
            return 2
    return False

def left_click(e):
    # #1: хід гравця
    x = e.widget.grid_info()["row"]
    y = e.widget.grid_info()["column"]
    print (buttons[x][y]['text'])
    if not (buttons[x][y]['text'] == ""):
        return
    buttons[x][y].config(text = "X")

    # #2: перевірити чи гравець виграв
    global human_win, comp_win
    if check_winner() == 1:
        messagebox.showinfo(message="Ви виграли!")
        human_win += 1
        result.config(text=f"Рахунок {human_win} : {comp_win}")
        for i in buttons:
            for j in i:
                j['text'] = ""
        return

    draw = True
    for i in buttons:
        for j in i:
            if not (j['text'] == ""):
                draw = False
    if draw:
        messagebox.showerror(message="Нічия!")
        comp_win += 0.5
        human_win += 0.5
        result.config(text=f"Рахунок {human_win} : {comp_win}")
        for i in buttons:
            for j in i:
                j['text'] = ""
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
    if check_winner() == 2:
        messagebox.showwarning(message="Ви програли!")
        comp_win += 1
        result.config(text=f"Рахунок {human_win} : {comp_win}")
        for i in buttons:
            for j in i:
                j['text'] = ""
        return

for i in range(3):
    t = []
    for j in range(3):
        b = tk.Button(w, height=1, width=3, font=my_font, relief="sunken", bd=5)
        b.bind("<Button-1>",left_click)
        t.append(b)
    buttons.append(t)

for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j, padx=2, pady=2)

result = tk.Label(w, text=f"Рахунок {human_win} : {comp_win}")
result.grid(row=3, column=0, columnspan=3)

w.mainloop()