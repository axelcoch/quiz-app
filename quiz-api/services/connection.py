import sqlite3

def init_db():
    # create a connection
    db = sqlite3.connect("./quizdb.db", timeout=10)
    # set the sqlite connection in "manual transaction mode"
    # (by default, all execute calls are performed in their own transactions, not what we want)
    db.isolation_level = None
    return db

def build_db():
    db = init_db() 
    # create cursor
    cur = db.cursor()
    # start transaction
    cur.execute("begin")
    try:
        cur.execute(

            """CREATE TABLE "Question" (
                "id"	INTEGER,
                "title"	TEXT,
                "text"	TEXT,
                "position"	INTEGER,
                "image"	TEXT COLLATE BINARY,
                PRIMARY KEY("id")
            );"""
        )
        cur.execute(
            """CREATE TABLE "Reponse" (
                "id"	INTEGER UNIQUE,
                "id_question"	INTEGER,
                "text"	TEXT,
                "isCorrect"	INTEGER,
                FOREIGN KEY("id_question") REFERENCES "Question"("id"),
                PRIMARY KEY("id")
            );"""
        )
        cur.execute(
            """CREATE TABLE "Participant" (
                "id"	INTEGER UNIQUE,
                "playerName"	TEXT NOT NULL,
                "score"	INTEGER,
                "date"	TEXT,
                PRIMARY KEY("id")
            );"""
        )
    except sqlite3.Error as e:
        # handle the error
        print(f'An error occurred: {e}')
    cur.execute("commit")
    cur.close()
    db.close()
    return "Ok", 200
