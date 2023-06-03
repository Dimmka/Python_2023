import tkinter as tk
from tkinter import colorchooser
import PIL.ImageGrab as ImageGrab
from tkinter import filedialog

w = tk.Tk()
w.geometry("1000x600")
w.resizable(False, False)

fill_color = tk.StringVar()
fill_color.set("black")

x_prev = 0
y_prev = 0

figure = "pencil"

def draw(e):
    global x_prev, y_prev, pencil_size, figure
    if e.type == "4":
        x_prev = e.x
        y_prev = e.y
        return
    if not (x_prev == 0 and y_prev == 0) and figure == "pencil":
        c.create_oval(e.x-sc.get()/2, e.y-sc.get()/2, e.x+sc.get()/2, e.y+sc.get()/2, fill=fill_color.get(), width=0)
        c.create_line(x_prev, y_prev, e.x, e.y, width=sc.get(), fill=fill_color.get())
        x_prev = e.x
        y_prev = e.y
    if e.type == "5" and figure == "rectangle":
        c.create_rectangle(x_prev, y_prev, e.x, e.y, fill=fill_color.get(), width=0)
    if e.type == "5" and figure == "oval":
        c.create_oval(x_prev, y_prev, e.x, e.y, fill=fill_color.get(), width=0)
    if e.type == "5" and figure == "triangle":
        if x_prev<=e.x:
            tr = [x_prev + abs(x_prev - e.x)/2, y_prev, e.x, e.y, x_prev, e.y]
        else:
            tr = [x_prev - abs(x_prev - e.x)/2, y_prev, e.x, e.y, x_prev, e.y]
        c.create_polygon(tr, fill=fill_color.get(), width=0)
    if e.type == "5":
        x_prev = 0
        y_prev = 0

def pick_color():
    global fill_color
    fill_color.set(colorchooser.askcolor(title="Виберіть колір")[1])

def set_rect():
    global figure
    figure = "rectangle"

def set_triangle():
    global figure
    figure = "triangle"

def set_oval():
    global figure
    figure = "oval"

def set_pencil():
    global figure
    figure = "pencil"
    fill_color.set("black")

def set_eraser():
    global figure
    figure = "eraser"
    fill_color.set("white")

def clear_canvas():
    c.create_rectangle(0,0, c['width'], c['height'], fill=fill_color.get(), width=0)

def save_picture():
    # TODO: розібратися з розмірами
    x = w.winfo_x()+50
    y = w.winfo_y() + 200
    fileLocation = filedialog.asksaveasfilename(defaultextension="jpg")
    img = ImageGrab.grab(bbox=(x, y, x+1100, y+600))
    img.save(fileLocation)


fr1 = tk.Frame(w, width=1000, height=100, bg="lightgray")
fr1.pack(fill="y")
fr1.pack_propagate(0)
pencil = tk.Button(fr1, text="Олівець", width=13, command=set_pencil)
pencil.pack(side="left", fill="y")
eraser = tk.Button(fr1, text="Гумка", width=13, command=set_eraser)
eraser.pack(side="left", fill="y")
color_picker = tk.Button(fr1, text="Вибір кольору", width=13, command=pick_color)
color_picker.pack(side="left", fill="y")
rectangle = tk.Button(fr1, text="Прямокутник", width=13, command=set_rect)
rectangle.pack(side="left", fill="y")
oval = tk.Button(fr1, text="Овал", width=13, command=set_oval)
oval.pack(side="left", fill="y")
triangle = tk.Button(fr1, text="Трикутник", width=13, command=set_triangle)
triangle.pack(side="left", fill="y")
clear = tk.Button(fr1, text="Очистити", width=13, command=clear_canvas)
clear.pack(side="left", fill="y")
sc = tk.Scale(fr1, from_ = 1, to = 50, length=180, orient="horizontal")
sc.pack(side="left", fill="y")
leave = tk.Button(fr1, text="Вихід", command=exit)
leave.pack(side="right", fill="y")
save = tk.Button(fr1, text="Зберегти", command=save_picture)
save.pack(side="right", fill="y")

fr2 = tk.Frame(w, width=1000, height=500)
fr2.pack()

c = tk.Canvas(fr2, width=1000, height=500, bg="white")
c.bind("<Button-1>", draw)
c.bind("<B1-Motion>", draw)
c.bind("<ButtonRelease-1>", draw)
c.pack()




w.mainloop()