# todo_app.py
import tkinter as tk
from tkinter import ttk, messagebox
from todo_db import TodoDB

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List App")
        self.geometry("600x400")

        self.db = TodoDB()
        self._create_widgets()
        self.refresh_tasks()

    def _create_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(pady=10, padx=10, fill="x")

        # Input box
        self.task_var = tk.StringVar()
        task_entry = ttk.Entry(frame, textvariable=self.task_var, width=40)
        task_entry.pack(side="left", padx=(0, 10))
        
        # Add button
        add_btn = ttk.Button(frame, text="Add Task", command=self.add_task)
        add_btn.pack(side="left")

        # Task list
        cols = ("ID", "Task", "Status")
        self.tree = ttk.Treeview(self, columns=cols, show="headings", height=12)
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=5)

        done_btn = ttk.Button(btn_frame, text="Mark as Done", command=self.mark_done)
        done_btn.grid(row=0, column=0, padx=5)

        pending_btn = ttk.Button(btn_frame, text="Mark as Pending", command=self.mark_pending)
        pending_btn.grid(row=0, column=1, padx=5)

        delete_btn = ttk.Button(btn_frame, text="Delete Task", command=self.delete_task)
        delete_btn.grid(row=0, column=2, padx=5)

        refresh_btn = ttk.Button(btn_frame, text="Refresh", command=self.refresh_tasks)
        refresh_btn.grid(row=0, column=3, padx=5)

    def add_task(self):
        task = self.task_var.get().strip()
        if not task:
            messagebox.showerror("Error", "Task cannot be empty!")
            return
        self.db.add_task(task)
        self.task_var.set("")
        self.refresh_tasks()

    def refresh_tasks(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        rows = self.db.view_tasks()
        for r in rows:
            self.tree.insert("", "end", values=(r["id"], r["task"], r["status"]))

    def mark_done(self):
        self._update_selected_task("Done")

    def mark_pending(self):
        self._update_selected_task("Pending")

    def _update_selected_task(self, status):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Info", "Select a task first.")
            return
        for item in sel:
            task_id = self.tree.item(item, "values")[0]
            self.db.update_task(task_id, status)
        self.refresh_tasks()

    def delete_task(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Info", "Select a task to delete.")
            return
        confirm = messagebox.askyesno("Confirm", "Delete selected task(s)?")
        if not confirm:
            return
        for item in sel:
            task_id = self.tree.item(item, "values")[0]
            self.db.delete_task(task_id)
        self.refresh_tasks()

    def on_close(self):
        self.db.close()
        self.destroy()


if __name__ == "__main__":
    app = TodoApp()
    app.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()
