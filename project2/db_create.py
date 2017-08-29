#project/db_create.py

from views import db
from models import Task
from datetime import date

#create the database and the db table
db.create_all()

#insert data
db.session.add(Task("Finish this tutorial", date(2017, 8, 28), 10, 1))
db.session.add(Task("Finish course 2", date(2017, 9, 1), 10, 1))

db.session.commit()



    
