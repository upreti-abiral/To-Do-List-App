# todo_db.py
import sqlite3

class TodoDB:
    def __init__(self, db_name="todo.db"):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row  # return rows as dict-like objects
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status TEXT NOT NULL
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_task(self, task):
        query = "INSERT INTO tasks (task, status) VALUES (?, ?);"
        self.conn.execute(query, (task, "Pending"))
        self.conn.commit()

    def view_tasks(self):
        query = "SELECT * FROM tasks;"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def update_task(self, task_id, status):
        query = "UPDATE tasks SET status=? WHERE id=?;"
        self.conn.execute(query, (status, task_id))
        self.conn.commit()

    def delete_task(self, task_id):
        query = "DELETE FROM tasks WHERE id=?;"
        self.conn.execute(query, (task_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
