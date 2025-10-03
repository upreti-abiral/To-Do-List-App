import tkinter as tk
from tkinter import messagebox
from todo_db import TodoDB

class TodoApp:
    def __init__(self, root):
        self.db = TodoDB()
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        # Entry box
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        # Add button
        add_btn = tk.Button(root, text="Add Task", command=self.add_task)
        add_btn.pack(pady=5)

        # Task listbox
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Buttons
        done_btn = tk.Button(root, text="Mark Done", command=self.mark_done)
        done_btn.pack(pady=5)

        delete_btn = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_btn.pack(pady=5)

        self.refresh_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.db.add_task(task)
            self.task_entry.delete(0, tk.END)
            self.refresh_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        tasks = self.db.get_tasks()
        for t in tasks:
            display = f"{t[0]}. {t[1]} - [{t[2]}]"
            self.task_listbox.insert(tk.END, display)

    def mark_done(self):
        try:
            selection = self.task_listbox.curselection()[0]
            task_id = int(self.task_listbox.get(selection).split(".")[0])
            self.db.mark_done(task_id)
            self.refresh_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task first!")

    def delete_task(self):
        try:
            selection = self.task_listbox.curselection()[0]
            task_id = int(self.task_listbox.get(selection).split(".")[0])
            self.db.delete_task(task_id)
            self.refresh_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task first!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
