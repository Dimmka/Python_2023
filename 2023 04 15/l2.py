#listbox

import tkinter as tk

#pupils = ['Дерев’янчук Назар', "Лей Максим", 'Невірко Ілля', "Фіц Олександр"]

def f(e):
    list.insert(tk.END, entry.get())
    entry.delete(0,tk.END)

def d(e):
    if list.curselection() != ():
        list.delete(list.curselection())

w = tk.Tk()
w.geometry("500x200")
w.title("Список задач")

entry = tk.Entry(w, font=("Helvetica", 20))
entry.pack()
entry.bind("<Return>", f)

list = tk.Listbox(w, height=4, font=("Helvetica", 20))
list.pack(side=tk.LEFT, fill=tk.Y)
list.bind("<Double-Button-1>", d)

scroll = tk.Scrollbar(w)
scroll.pack(side=tk.LEFT, fill=tk.Y)

scroll.config(command=list.yview)
list.config(yscrollcommand=scroll.set)

w.mainloop()