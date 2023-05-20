import tkinter as tk

w = tk.Tk()

c = tk.Canvas(w, width=200, height=200)
c.pack()

c.create_oval(5,5,200,200, fill='lightgreen', outline="green", width=3, dash=(10, 2))


w.mainloop()