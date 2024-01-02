"""Task 01 ---> To do List """

import tkinter
from tkinter import *
from tkinter import messagebox 

l=[] 
c=1

def entryError():
    if insertField.get() == "":
        messagebox.showerror("Error in input. Please input again")
        return 0
    return 1

def insertTask():
    global c 
    value = entryError()
    if (value == 0):
        return
    var = insertField.get() + "\n"
    l.append(var)
    TextArea.insert('end -1 chars', str(c) + "---> " + var)
    c = c + 1
    del_tf()

def del_nf():
    nf.delete(0.0, END)

def del_tf():
    insertField.delete(0, END)

def delete():
    global c
    if (len(l) == 0):
        messagebox.showerror("There are no tasks")
        return
    number = nf.get(1.0, END)
    if (number == "\n"):
        messagebox.showerror("input error")
        return
    else:
        task_no = int(number)
    del_nf()
    l.pop(task_no - 1)
    c = c - 1
    TextArea.delete(1.0, END)
    for i in range(len(l)):
        TextArea.insert('end -1 chars', str(i + 1) + "---> " + l[i])

if (__name__ == "__main__"):
    window = Tk()
    window.configure(background="purple")
    window.title("My To-Do List")
    window.geometry("800x600")  

    enterTask = Label(window, text="Please enter your task", bg="red", font="Arial 14 bold")  
    insertField = Entry(window, font="Arial 14")

    Submit = Button(window, text="Submit", fg="Black", bg="yellow", command=insertTask, font="Arial 12 bold")  
    TextArea = Text(window, height=8, width=35, font="arial 13")  
    taskNumber = Label(window, text="Specify the task number that you want to remove, below", bg="cyan", font="Arial 14 bold")  

    nf = Text(window, height=1, width=2, font="arial 13")

    delete = Button(window, text="Delete", fg="Black", bg="yellow", command=delete, font="Arial 12 bold")  

    Exit = Button(window, text="Do you want to close?", fg="Black", bg="Red", command=exit, font="Arial 12 bold")  

    enterTask.grid(row=0, column=2, pady=10)  
    insertField.grid(row=1, column=2, ipadx=50, pady=10)
    Submit.grid(row=2, column=2, pady=10)
    TextArea.grid(row=3, column=2, padx=100, sticky=W, pady=10)
    taskNumber.grid(row=4, column=2, pady=10)
    nf.grid(row=5, column=2, pady=10)
    delete.grid(row=6, column=2, pady=10)
    Exit.grid(row=7, column=2, pady=10)

    window.mainloop()
