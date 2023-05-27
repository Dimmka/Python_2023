import tkinter as tk

x_prev = 0
y_prev = 0

def draw(e):
    global x_prev, y_prev
    #c.create_oval(e.x-5, e.y-5, e.x+5, e.y+5)
    if not (x_prev == 0 and y_prev == 0):
        c.create_line(x_prev, y_prev, e.x, e.y)
    x_prev = e.x
    y_prev = e.y
    if e.type == "5":
        x_prev = 0
        y_prev = 0

w = tk.Tk()
w.geometry("1000x600")
w.resizable(False, False)

fr1 = tk.Frame(w, width=1000, height=100, bg="lightgray")
fr1.pack()

fr2 = tk.Frame(w, width=1000, height=500)
fr2.pack()

c = tk.Canvas(fr2, width=1000, height=500)
#c.bind("<Button-1>", draw)
c.bind("<B1-Motion>", draw)
c.bind("<ButtonRelease-1>", draw)
c.pack()




w.mainloop()