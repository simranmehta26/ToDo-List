from tkinter import *

win = Tk()
win.title("To-Do List")
win.geometry("350x420")
win.configure(bg="#232E46")
win.resizable(height=False, width=False)

# frames
top = Frame(win, width=350, height=90, bg="#232E46")
top.grid(row=0, column=0)

main = Frame(win, width=350, height=250, bg="#232E46")
main.grid(row=1, column=0)

bottom = Frame(win, width=350, height=80, bg="#232E46")
bottom.grid(row=2, column=0)


# function

# creating a text file and opening it
def open_task_file():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                list_box.insert(END, task)
    except():
        file = open("tasklist.txt", "w")
        file.close()


# adding task
def add_task():
    task = entry.get()
    entry.delete(0, END)

    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        list_box.insert(END, task)


# deleting task
def del_task():
    global task_list
    task = str(list_box.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")

        list_box.delete(ANCHOR)


# 232E46
# top frame
app_name = Label(top, text="Task List", height=1, padx=113, pady=5, anchor=CENTER, font='Arial 20 bold',
                 fg="white", bg="#232E46")
app_name.place(x=0, y=0)

# main frame
entry = Entry(top, width=24, justify=CENTER, font='Ivy 14 bold', relief="solid")
entry.place(x=10, y=50)

add_b = Button(top, text=" ADD ", width=6, height=1, justify=CENTER, font='Ivy 9 bold', relief="solid",
               command=add_task)
add_b.place(x=287, y=50)

task_list = []
list_box = Listbox(main, font='Arial 12 bold', width=36, height=13, bg="#32405b", fg="white",
                   selectbackground="#5a95ff")
# list_box.place(x=10, y=10)
list_box.pack(side=LEFT, fill=BOTH, padx=0)

scrollbar = Scrollbar(main)
# scrollbar.place(x=322, y=10)
scrollbar.pack(side=RIGHT, fill=BOTH)

list_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_box.yview())

open_task_file()

# bottom frame
del_b = Button(bottom, text=" DELETE ", justify=CENTER, font='Ivy 10 bold', relief="solid", anchor=CENTER,
               command=del_task)
del_b.place(x=140, y=20)

win.mainloop()
#232E46
#32405b