#listbox

import tkinter as tk

pupils = ['Дерев’янчук Назар', "Лей Максим", 'Невірко Ілля', "Фіц Олександр"]

w = tk.Tk()
w.geometry("700x200")

l = tk.Listbox(w, height=4, width=30, font=("Helvetica", 20))
l.pack()

for i in pupils:
    l.insert(tk.END, i)

w.mainloop()