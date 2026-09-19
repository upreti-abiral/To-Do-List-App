# To-Do List App

A desktop To-Do List application built with Python, Tkinter, and SQLite.

## Overview

This project is a simple desktop application for creating and managing tasks.

Tasks are stored in a local SQLite database. Each task has a unique ID and can be marked as either Pending or Done.

The project was built to practise GUI development, database operations, and basic application structure in Python.

## Features

- Add new tasks
- View saved tasks
- Mark tasks as Done
- Mark tasks as Pending
- Delete tasks
- Select multiple tasks
- Store tasks locally using SQLite
- Prevent empty tasks from being added

## How It Works

When a task is added, it is stored in the SQLite database with a unique ID and a Pending status.

The application displays the saved tasks in a table.

Users can:

1. Add a task
2. View saved tasks
3. Select one or more tasks
4. Change their status
5. Delete selected tasks
6. Refresh the task list

The GUI handles user interaction, while the database class handles storing and modifying task data.

## Project Structure

todo-list-app/
├── todo_app.py
├── todo_db.py
├── todo.db
└── README.md

## Files

`todo_app.py`  
Handles the graphical interface, user input, task selection, and application logic.

`todo_db.py`  
Handles SQLite database creation, storing tasks, retrieving tasks, updating task status, and deleting tasks.

`todo.db`  
Local SQLite database created automatically when the application runs.

`README.md`  
Project documentation.

## Technologies Used

- Python
- Tkinter
- ttk
- SQLite
- sqlite3

## Requirements

- Python 3.8 or newer
- Tkinter
- SQLite3

Tkinter and SQLite3 are included with most standard Python installations.

## How to Run

Open the project folder in a terminal:

    cd todo-list-app

Run the application:

    python todo_app.py

The `todo.db` database will be created automatically if it does not already exist.

## Database

The application uses a single `tasks` table.

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Unique task ID |
| `task` | TEXT | Task description |
| `status` | TEXT | `Pending` or `Done` |

Parameterized SQL queries are used when inserting, updating, and deleting data.

## What I Practised

- Building a desktop GUI with Tkinter
- Using ttk widgets
- Handling button commands and keyboard events
- Working with SQLite databases
- Creating and modifying database records
- Separating GUI and database logic
- Handling user input and selections
- Working with multiple selected items
- Managing a database connection

## Possible Improvements

- Edit existing tasks
- Add due dates
- Add task priorities
- Add categories
- Search and filter tasks
- Sort tasks
- Add completion statistics

These features are not currently implemented.

## Author

Abiral Upreti

A Python project focused on learning GUI development, database management, and application design.
