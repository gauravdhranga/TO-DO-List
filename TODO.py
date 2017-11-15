# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 18:04:02 2017

@author: Divyansh Shukla
"""

import tkinter
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()

root = tkinter.Tk()

root.configure(bg="white")

root.title("To Do List")

root.geometry("380x280")

tasks = []

def data_entry(task):
    c.execute("INSERT INTO Tasks1 VALUES(?)",(task,))
    conn.commit()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Tasks2(Fin_task TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS Tasks1(Unfin_task TEXT)")
    conn.commit()

def update_listbox():
    c.execute('SELECT * FROM Tasks1')
    data = c.fetchall()
    print(data)
    clear_listbox()
    for A in data:
        lb_tasks.insert("end", A)
    update_listbox2()

def update_listbox2():
    c.execute('SELECT * FROM Tasks2')
    data2 = c.fetchall()
    for B in data2:
        lb_tasks_d.insert("end", B)
    conn.commit()

def clear_listbox():
    lb_tasks.delete(0, "end")
    lb_tasks_d.delete(0, "end")

def add_task():
    create_table()
    task = txt_input.get()
    if task != "":
        tasks.append(task)
        data_entry(task)
        update_listbox()
    else:
        tkinter.messagebox.showwarning("Warning", "You need to enter a task.")
    txt_input.delete(0, "end")

def del_all():
    confirmed = tkinter.messagebox.askyesno("Please Confirm", "Do you really want to delete all?")
    if confirmed == True:
        c.execute("DELETE FROM Tasks1")
        c.execute("DELETE FROM Tasks2")
        update_listbox()
        conn.commit()

def del_one():
    task = lb_tasks.get("active")
    c.execute("Delete from Tasks1 where Unfin_task = ?",(task))
    update_listbox()
    conn.commit()

def del_two():
    task = lb_tasks_d.get("active")
    c.execute("Delete from Tasks2 where Fin_task = ?",(task))
    update_listbox()
    conn.commit()

def move_done():
    task = lb_tasks.get("active")
    c.execute("Delete from Tasks1 where Unfin_task = ?", (task))
    c.execute("INSERT INTO Tasks2 VALUES(?)", (task))
    update_listbox()
    conn.commit()

def endProgam():
    root.destroy()


create_table()

lbl_title = tkinter.Label(root, text="To-Do-List", bg="white")
lbl_title.grid(row=0, column=0)

lbl_display = tkinter.Label(root, text="", bg="white")
lbl_display.grid(row=0, column=1)

txt_input = tkinter.Entry(root, width=15)
txt_input.grid(row=1, column=1)

btn_add_task = tkinter.Button(root, text="Add task", fg="green", bg="white", command=add_task)
btn_add_task.grid(row=1, column=0)

btn_del_all = tkinter.Button(root, text="Delete All", fg="green", bg="white", command=del_all)
btn_del_all.grid(row=2, column=0)

btn_del_one = tkinter.Button(root, text="Delete", fg="green", bg="white", command=del_one)
btn_del_one.grid(row=3, column=0)

btn_number_of_tasks = tkinter.Button(root, text="Move to done", fg="green", bg="white", command=move_done)
btn_number_of_tasks.grid(row=4, column=0)

btn_exit = tkinter.Button(root, text="Delete Done", fg="green", bg="white", command=del_two)
btn_exit.grid(row=5, column=0)

btn_exit = tkinter.Button(root, text="Exit", fg="green", bg="white", command=endProgam)
btn_exit.grid(row=7, column=0)

lbl_done_tasks = tkinter.Label(root, text="Done tasks", bg="white")
lbl_done_tasks.grid(row=1, column=2)

btn_exit = tkinter.Button(root, text="Show", fg="green", bg="white", command=update_listbox)
btn_exit.grid(row=6, column=0)

lb_tasks = tkinter.Listbox(root, bg="white")
lb_tasks.grid(row=2, column=1, rowspan=10)
lb_tasks_d = tkinter.Listbox(root, bg="black", fg="white")
lb_tasks_d.grid(row=2, column=2, rowspan=10)
update_listbox()

root.mainloop()