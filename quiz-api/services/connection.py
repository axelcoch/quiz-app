import sqlite3

def init_db():
    # create a connection
    db = sqlite3.connect("./quizdb.db", timeout=10)
    # set the sqlite connection in "manual transaction mode"
    # (by default, all execute calls are performed in their own transactions, not what we want)
    # db.isolation_level = None
    return db

def build_db():
    db = init_db()
    cur = db.cursor()
    try:
        cur.execute("DROP TABLE IF EXISTS Question")
        cur.execute("DROP TABLE IF EXISTS Reponse")
        cur.execute("DROP TABLE IF EXISTS Participant")

        cur.execute(
            f'CREATE TABLE Question ("id"	INTEGER, "title" TEXT, "text" TEXT, "position" INTEGER, "image"	TEXT COLLATE BINARY, PRIMARY KEY("id"));'
        )
        db.commit()
        cur.execute(
            f'CREATE TABLE Reponse ("id"	INTEGER UNIQUE, "id_question" INTEGER, "text" TEXT, "isCorrect"	INTEGER,FOREIGN KEY("id_question") REFERENCES "Question"("id"), PRIMARY KEY("id"));'
        )
        db.commit()
        cur.execute(
            """CREATE TABLE Participant (
                "id"	INTEGER UNIQUE,
                "playerName"	TEXT NOT NULL,
                "score"	INTEGER,
                "date"	TEXT,
                PRIMARY KEY("id")
            );"""
        )
        db.commit()
    except sqlite3.Error as e:
        # handle the error
        print(f'An error occurred: {e}')
    finally:
        if db:
            cur.close()
            db.close()
            print('SQLite Connection closed')
    return "Ok", 200

# def build_db():
#     db = init_db() 
#     # create cursor
#     cur = db.cursor()
#     # start transaction
#     cur.execute("BEGIN")
#     try:
        
#         cur.execute("DROP TABLE IF EXISTS Question")
#         cur.execute("DROP TABLE IF EXISTS Reponse")
#         cur.execute("DROP TABLE IF EXISTS Participant")
#         # tables_to_drop = ['Question', 'Reponse', 'Participant']
#         # for table in tables_to_drop:
#         #     cur.execute(f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table}'")
#         #     if cur.fetchone()[0] == 1:
#         #         cur.execute(f"DROP TABLE {table}")
#         #         print(f"Table '{table}' has been dropped.")
#         #     else:
#         #         print(f"Table '{table}' does not exist.")

#         # cur.execute(
#         #     """IF EXISTS(SELECT * FROM Question)
#         #     DROP TABLE Question;
#         #     """
#         # )
#         # cur.execute(
#         #     """IF EXISTS(SELECT * FROM Reponse)
#         #     DROP TABLE Reponse;"""
#         # )
#         # cur.execute(
#         #     """IF EXISTS(SELECT * FROM Participant)
#         #     DROP TABLE Participant;"""
#         # )
#         cur.execute(
#             f'CREATE TABLE Question ("id"	INTEGER, "title" TEXT, "text" TEXT, "position" INTEGER, "image"	TEXT COLLATE BINARY, PRIMARY KEY("id"));'
#         )
#         cur.execute(
#             f'CREATE TABLE Reponse ("id"	INTEGER UNIQUE, "id_question" INTEGER, "text" TEXT, "isCorrect"	INTEGER,FOREIGN KEY("id_question") REFERENCES "Question"("id"), PRIMARY KEY("id"));'
#         )
#         cur.execute(
#             """CREATE TABLE Participant (
#                 "id"	INTEGER UNIQUE,
#                 "playerName"	TEXT NOT NULL,
#                 "score"	INTEGER,
#                 "date"	TEXT,
#                 PRIMARY KEY("id")
#             );"""
#         )
#         db.commit()
#     except sqlite3.Error as e:
#         # handle the error
#         print(f'An error occurred: {e}')
#         db.rollback()
#     # cur.execute("commit")
#     finally:
#         cur.execute("COMMIT")
        
#         cur.close()
#         db.close()
#     return "Ok", 200
