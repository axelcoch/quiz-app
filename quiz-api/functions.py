import sqlite3
from model import Question, Answer
from datetime import datetime
from connection import init_db, build_db

def select_question(query, answer_id = False):
    db = init_db()
    selection = db.execute(query)

    for id, position, title, text, image, answers in selection :
        l_a = answers.split("nnn")
        possible_answers = [Answer() for i in l_a]

        for i,t_a in enumerate(l_a) :
            t_a = t_a.split("/")
            d_a = {"id": t_a[0], "text": t_a[1], "isCorrect": True if t_a[2] == '1' else False}
            possible_answers[i].deserialize(d_a)
        question = Question()
        question.init(id,position,title,text,image,possible_answers)
        db.close()
        return question.serialize(answer_id), 200
    return {"message": "Question non trouvée"}, 404
    
def get_id(id,answer_id=False):
    return select_question(f"SELECT Question.*, group_concat(Reponse.id||'/'||Reponse.text||'/'||Reponse.isCorrect,'nnn') as possibleAnswers "
                            f"FROM Reponse LEFT JOIN Question on Question.id = Reponse.id_question where Question.id = {id} GROUP BY Question.id",
                            answer_id)

def get_pos(position,answer_id=False):
    return select_question(f"SELECT Question.*, group_concat(Reponse.id||'/'||Reponse.text||'/'||Reponse.isCorrect,'nnn') as possibleAnswers "
                            f"FROM Reponse LEFT JOIN Question on Question.id = Reponse.id_question where position = {position} GROUP BY Question.id",
                            answer_id)

def count():
    db = init_db()
    cur = db.cursor()
    cur.execute("begin")
    count = cur.execute(f"SELECT COUNT(DISTINCT position) as count FROM Question")
    nb = count.fetchone()[0]
    return nb

def add_question(questions):
    db = init_db() 
    cur = db.cursor()
    cur.execute("begin")

    input_question = Question()
    possible_answers = [Answer() for i in questions["possibleAnswers"]]

    for i, answer in enumerate(questions["possibleAnswers"]) :
        possible_answers[i].deserialize(answer.copy())

    questions["possibleAnswers"] = possible_answers
    input_question.deserialize(questions)
    question_position, status = get_pos(input_question.position)

    if status == 200 :
        cur.execute(
            f"UPDATE Question SET position = position + 1 "
            f"WHERE position >= {input_question.position!r}")

    insert_question = cur.execute(
        f"INSERT into Question (position,title,text,image) values"
        f"({input_question.position!r},{input_question.title!r},"
        f"{input_question.text!r},{input_question.image!r})"
    )

    id_question = insert_question.lastrowid
    insert_reponse = ""
    for answer in possible_answers :
       insert_reponse += f"({insert_question.lastrowid!r},{answer.text!r},{answer.isCorrect!r}),"

    cur.execute(
        f"INSERT into Reponse (id_question,text,isCorrect) values"
        f"{insert_reponse[:-1]}"
    )

    cur.execute('commit')
    cur.close()
    db.close()

    return {"id": id_question}, 200