import sqlite3
     
def init_db():
# create a connection
    db = sqlite3.connect("./quizdb.db", timeout=10)
    return db

def build_db():
    with init_db() as db:
        cur = db.cursor()
        try:
            cur.execute("DROP TABLE IF EXISTS Question")
            cur.execute("DROP TABLE IF EXISTS Reponse")
            cur.execute("DROP TABLE IF EXISTS Participant")
            cur.execute(
                'CREATE TABLE Question ("id" INTEGER, "title" TEXT, "text" TEXT, "position" INTEGER, "image" TEXT COLLATE BINARY, PRIMARY KEY("id"));'
            )
            db.commit()
            cur.execute(
                'CREATE TABLE Reponse ("id" INTEGER UNIQUE, "id_question" INTEGER, "text" TEXT, "isCorrect" INTEGER,FOREIGN KEY("id_question") REFERENCES "Question"("id"), PRIMARY KEY("id"));'
            )
            db.commit()
            cur.execute(
                """CREATE TABLE Participant (
                    "id" INTEGER UNIQUE,
                    "playerName" TEXT NOT NULL,
                    "score" INTEGER,
                    "date" TEXT,
                    PRIMARY KEY("id")
                );"""
            )
            db.commit()
        except sqlite3.Error as e:
            # handle the error
            print(f'An error occurred: {e}')
    return "Ok", 200
