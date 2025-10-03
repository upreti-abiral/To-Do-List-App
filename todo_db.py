import sqlite3

class TodoDB:
    def __init__(self, db_name="todo.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pending'
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_task(self, task):
        query = "INSERT INTO tasks (task, status) VALUES (?, 'Pending')"
        self.conn.execute(query, (task,))
        self.conn.commit()

    def get_tasks(self):
        query = "SELECT * FROM tasks"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def mark_done(self, task_id):
        query = "UPDATE tasks SET status='Done' WHERE id=?"
        self.conn.execute(query, (task_id,))
        self.conn.commit()

    def delete_task(self, task_id):
        query = "DELETE FROM tasks WHERE id=?"
        self.conn.execute(query, (task_id,))
        self.conn.commit()
