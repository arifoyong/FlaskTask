#project/db_create.py

import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()

    #create 'tasks' table
    c.execute(""" CREATE TABLE IF NOT EXISTS tasks(task_id INTEGEr PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL,
         status INTEGER NOT NULL)""" )

    #insert dummy data
    c.execute('''INSERT INTO tasks (name, due_date, priority, status)
       values("Finish this tutorial", "08/27/2017", 10, 1) ''')

    c.execute('''INSERT INTO tasks (name, due_date, priority, status)
       values("Finish course 2", "09/27/2017", 10, 1) ''')
    
