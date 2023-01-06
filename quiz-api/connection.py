import sqlite3
from models import Question,Answer
from datetime import datetime

def createCursor():
    # create a connection
    db_connection = sqlite3.connect(path)

    # set the sqlite connection in "manual transaction mode"
    # (by default, all execute calls are performed in their own transactions, not what we want)
    db_connection.isolation_level = None

    # initialise le curseur
    cur = db_connection.cursor()
    # start transaction
    cur.execute("begin")

# save the question to db
insertion_result = cur.execute(
	f"insert into Question (title) values"
	f"('{input_question.title}')")

# send the request
cur.execute("commit")

# in case of exception, rollback the transaction
cur.execute('rollback')