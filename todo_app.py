import tkinter as tk
from tkinter import ttk, messagebox
from todo_db import TodoDB


class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("To-Do List App")
        self.geometry("600x400")

        self.db = TodoDB()

        self.create_widgets()
        self.refresh_tasks()

    def create_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(pady=10, padx=10, fill="x")

        self.task_var = tk.StringVar()

        task_entry = ttk.Entry(
            frame,
            textvariable=self.task_var,
            width=40
        )
        task_entry.pack(side="left", padx=(0, 10))

        add_button = ttk.Button(
            frame,
            text="Add Task",
            command=self.add_task
        )
        add_button.pack(side="left")

        columns = ("ID", "Task", "Status")

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            selectmode="extended",
            height=12
        )

        self.tree.heading("ID", text="ID")
        self.tree.heading("Task", text="Task")
        self.tree.heading("Status", text="Status")

        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Task", width=350)
        self.tree.column("Status", width=100, anchor="center")

        self.tree.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=5)

        done_button = ttk.Button(
            button_frame,
            text="Mark as Done",
            command=self.mark_done
        )
        done_button.grid(row=0, column=0, padx=5)

        pending_button = ttk.Button(
            button_frame,
            text="Mark as Pending",
            command=self.mark_pending
        )
        pending_button.grid(row=0, column=1, padx=5)

        delete_button = ttk.Button(
            button_frame,
            text="Delete Task",
            command=self.delete_task
        )
        delete_button.grid(row=0, column=2, padx=5)

        refresh_button = ttk.Button(
            button_frame,
            text="Refresh",
            command=self.refresh_tasks
        )
        refresh_button.grid(row=0, column=3, padx=5)

        self.bind("<Return>", lambda event: self.add_task())

    def add_task(self):
        task = self.task_var.get().strip()

        if not task:
            messagebox.showwarning(
                "Empty Task",
                "Please enter a task."
            )
            return

        self.db.add_task(task)
        self.task_var.set("")
        self.refresh_tasks()

    def refresh_tasks(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        tasks = self.db.view_tasks()

        for task in tasks:
            self.tree.insert(
                "",
                "end",
                values=(task["id"], task["task"], task["status"])
            )

    def mark_done(self):
        self.update_selected_tasks("Done")

    def mark_pending(self):
        self.update_selected_tasks("Pending")

    def update_selected_tasks(self, status):
        selected = self.tree.selection()

        if not selected:
            messagebox.showinfo(
                "No Selection",
                "Select a task first."
            )
            return

        for item in selected:
            task_id = self.tree.item(item, "values")[0]
            self.db.update_task(task_id, status)

        self.refresh_tasks()

    def delete_task(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showinfo(
                "No Selection",
                "Select a task to delete."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Delete the selected task(s)?"
        )

        if not confirm:
            return

        for item in selected:
            task_id = self.tree.item(item, "values")[0]
            self.db.delete_task(task_id)

        self.refresh_tasks()

    def close_app(self):
        self.db.close()
        self.destroy()


if __name__ == "__main__":
    app = TodoApp()
    app.protocol("WM_DELETE_WINDOW", app.close_app)
    app.mainloop()
