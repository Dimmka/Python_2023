from tkinter import *


def convert():
    grn = float(e_grn.get())
    dol = grn / course.get()
    e_dol.delete(0, len(e_dol.get()))
    e_dol.insert(0,round(dol,2))

def convert2():
    dol = float(e_dol.get())
    grn = dol * course.get()
    e_grn.delete(0, len(e_grn.get()))
    e_grn.insert(0,round(grn,2))


w = Tk()
w.geometry("900x500")
w.title("Конвертор валют")
fnt = ("Arial", 18)

l_grn = Label(w, text="Гривні", font=fnt)
l_grn.grid(row=0, column=0, pady=10, padx=20)

l_dol = Label(w, text="Валюта:", font=fnt)
l_dol.grid(row=0, column=2, pady=10, padx=20)

e_grn = Entry(w, font=fnt)
e_grn.grid(row=1, column=0, rowspan=2, pady=10, padx=20)
e_grn.insert(0, 10)

e_dol = Entry(w, font=fnt)
e_dol.grid(row=1, column=2, rowspan=2, pady=10, padx=20)

b_convert = Button(text="Конвертувати ->", font=fnt, command=convert)
b_convert.grid(row=1, column=1, pady=10, padx=20)

b_convert2 = Button(text="<- Конвертувати", font=fnt, command=convert2)
b_convert2.grid(row=2, column=1, pady=10, padx=20)

l_usd = Label(font=fnt)
l_usd.grid(row=1, column=2, pady=10, padx=20)

#s = Scale(w, from_=0, to=10000, resolution=10, orient=HORIZONTAL, length=300)
#s.grid(row=2, column=0)
#s.bind("<ButtonRelease-1>", get_grn)

l_course = Label(w, text="Оберіть валюту: ", font=fnt)
l_course.grid(row=3, column=0)

course = DoubleVar()
course.set(37)
r_euro = Radiobutton(w, text="Євро, курс = 41", variable=course, value=41)
r_usd = Radiobutton(w, text="Долар, курс = 37", variable=course, value=37)
r_zloty = Radiobutton(w, text="Злотий, курс = 8,7", variable=course, value=8.7)

r_euro.grid(row=4, column=0)
r_usd.grid(row=5, column=0)
r_zloty.grid(row=6, column=0)

w.mainloop()
