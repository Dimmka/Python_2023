
# my_img = ImageTk.PhotoImage(Image.open("img.jpg"))
#
# l = tk.Button(w, image=my_img, relief="ridge")
# l.pack()
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog

def about():
    messagebox.showinfo(message="Це моя програма")

def save_as():
    file = filedialog.asksaveasfile()
    file.write(my_text.get(1.0,tk.END))
    file.close()

def open_as():
    my_text.delete(1.0, tk.END)
    file_name = filedialog.askopenfilename()
    file = open(file_name, mode='r')
    my_text.insert(1.0, file.read())
    file.close()

def create_file():
    my_text.delete(1.0, tk.END)

font_size = 14
my_font = ["Helvetica", font_size]

def inc_size(font_size):
    my_font[1] = my_font[1] + 2
    my_text.config(font=my_font)
    print(my_text['font'])

def dec_size():
    pass

w = tk.Tk()

my_menu = tk.Menu(w)

file_menu = tk.Menu(my_menu)
file_menu.add_command(label='Новий файл', command=create_file)
file_menu.add_command(label='Відкрити файл', command=open_as)
file_menu.add_command(label='Зберегти файл', command=save_as)
file_menu.add_command(label="Вихід", command=quit)

my_menu.add_cascade(label="Файл", menu=file_menu)

size_menu = tk.Menu(my_menu)
size_menu.add_command(label="Збільшити", command=lambda:inc_size(font_size))
size_menu.add_command(label="Зменшити", command=dec_size)
my_menu.add_cascade(label="Масштаб", menu=size_menu)
my_menu.add_command(label="Про автора", command=about)

my_text = tk.Text(w, width=40, height=10, font=my_font)
my_text.pack(side='left')

my_scroll = tk.Scrollbar(w, command=my_text.yview)
my_text.config(yscrollcommand=my_scroll.set)
my_scroll.pack(side='right', fill='y')

w.config(menu=my_menu)


w.mainloop()