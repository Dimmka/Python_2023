import tkinter as tk

fruits = ['кокоси', 'мандарини', 'банани', 'авокадо', 'ківі']

w = tk.Tk()
w.geometry("400x400")

def move_right():
    list2.insert(tk.END, list1.get(list1.curselection()))
    list1.delete(list1.curselection())

def move_left():
    list1.insert(tk.END, list2.get(list2.curselection()))
    list2.delete(list2.curselection())

list1 = tk.Listbox(w, width=10, font=("Helvetica", 20))
list1.grid(row=0, column=0, rowspan=2)

b1 = tk.Button(w, text=">>>", font=("Helvetica", 20), command=move_right)
b1.grid(row=0, column=1)

b2 = tk.Button(w, text="<<<", font=("Helvetica", 20), command=move_left)
b2.grid(row=1, column=1)

list2 = tk.Listbox(w,  width=10, font=("Helvetica", 20))
list2.grid(row=0, column=2, rowspan=2)

for i in fruits:
    list1.insert(tk.END, i)

w.mainloop()