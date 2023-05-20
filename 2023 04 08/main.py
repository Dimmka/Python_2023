from tkinter import *

w = Tk()

w.geometry("500x500")

gender = StringVar()
age = IntVar()

age.set(10)
gender.set("male")

def f1():
    if gender.get() == "female":
        w.config(bg="pink")
    if gender.get() == "male":
        w.config(bg="lightblue")


def f2():
    if age.get() == 10:
        b1['state'] = DISABLED
    if age.get() == 20:
        b1['state'] = NORMAL


l1 = Label(w, text="Оберіть стать:")
l1.pack()

r1 = Radiobutton(w, text="Жіноча", variable=gender, value="female", command=f1)
r2 = Radiobutton(w, text="Чоловіча", variable=gender, value='male', command=f1)

r1.pack()
r2.pack()

l2 = Label(w, text="Оберіть вік:")
l2.pack()

r3 = Radiobutton(w, text="Неповнолітній", variable=age, value=10, command=f2)
r4 = Radiobutton(w, text="Повнолітній", variable=age, value=20, command=f2)

r3.pack()
r4.pack()

b1 = Button(w, text="Зареєструватися", state=DISABLED)
b1.pack()

w.mainloop()