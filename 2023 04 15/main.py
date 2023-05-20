#Програма для тестувань

import tkinter as tk
import tkinter.messagebox

w = tk.Tk()
w.geometry("700x200")
w.title("Хто хоче стати мільйонером?")
w.iconbitmap("question-mark-6-32.ico")

fnt = ("Arial", 18)

def f():
    if answer.get() == 3:
        tkinter.messagebox.showinfo(message="Правильно")
    else:
        tkinter.messagebox.showwarning(message="НЕ правильно")
    w.quit()

question = tk.Label(w, text="Яке завтра свято?", font=fnt)
question.grid(row=0, column=1)

answer = tk.IntVar()
r1 = tk.Radiobutton(w, variable=answer, text="Новий Рік", value=1, font=fnt)
r1.grid(row=1, column=0)

r2 = tk.Radiobutton(w, variable=answer, text="День Валентина", value=2, font=fnt)
r2.grid(row=2, column=0)

r3 = tk.Radiobutton(w, variable=answer, text="Великдень", value=3, font=fnt)
r3.grid(row=1, column=2)

r4 = tk.Radiobutton(w, variable=answer, text="День Незалежності", value=4, font=fnt)
r4.grid(row=2, column=2)

b = tk.Button(w, text="Перевірити", command=f, font=fnt)
b.grid(row=3, column=1)

w.mainloop()