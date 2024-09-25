import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

def save_tasks():
    tasks = task_listbox.get(0, task_listbox.size())
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

delete_task_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_task_button.pack(pady=5)

save_tasks_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_tasks_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

load_tasks()

root.mainloop()
