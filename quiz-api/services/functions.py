import sqlite3
from services.model import Question, Answer
from datetime import datetime
from services.connection import init_db, build_db

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
    return {"message": "Aucune question correspondante"}, 404
    
def get_id(id,answer_id=False):
    return select_question(f"SELECT Question.*, group_concat(Reponse.id||'/'||Reponse.text||'/'||Reponse.isCorrect,'nnn') as possibleAnswers "
                            f"FROM Reponse LEFT JOIN Question on Question.id = Reponse.id where Question.id = {id} GROUP BY Question.id",
                            answer_id)

def get_pos(position,answer_id=False):
    return select_question(f"SELECT Question.*, group_concat(Reponse.id||'/'||Reponse.text||'/'||Reponse.isCorrect,'nnn') as possibleAnswers "
                            f"FROM Reponse LEFT JOIN Question on Question.id = Reponse.id where position = {position} GROUP BY Question.id",
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

    id = insert_question.lastrowid
    insert_reponse = ""
    for answer in possible_answers :
       insert_reponse += f"({insert_question.lastrowid!r},{answer.text!r},{answer.isCorrect!r}),"

    cur.execute(
        f"INSERT into Reponse (id,text,isCorrect) values"
        f"{insert_reponse[:-1]}"
    )

    cur.execute('commit')
    cur.close()
    db.close()

    return {"id": id}, 200

def delete_all():
    db = init_db()
    cur = db.cursor()
    cur.execute("begin")

    delete = cur.execute(f"DELETE FROM Question")
    delete

    cur.execute("commit")
    cur.close()
    db.close()
    
    return delete, 204

def delete_id(id):
    db = init_db()
    cur = db.cursor()
    cur.execute("begin")

    question, status = get_id(id)
    if status == 200 :
        cur.execute(f"DELETE FROM Question where id = {id}")
        cur.execute(f"DELETE FROM Answer where id = {id}")
        cur.execute(f"UPDATE Question SET position = position - 1 "
                    f"WHERE position >= {question['position']!r}")
    else:
        return {"message": "Aucune question correspondante"}, 404

    cur.execute('commit')
    cur.close()
    db.close()

    return question, 204

def update_question(new_question,id):
    db = init_db()
    cur = db.cursor()
    cur.execute("begin")

    input_question = Question()
    possible_answers = [Answer() for answer in new_question["possibleAnswers"]]

    for i,answer_json in enumerate(new_question["possibleAnswers"]) :
        possible_answers[i].deserialize(answer_json.copy())

    new_question["possibleAnswers"] = possible_answers
    input_question.deserialize(new_question)
    question_json, status = get_id(int(id),True)
    if status == 200 :
        if int(input_question.position) < question_json["position"] :
            cur.execute(f"UPDATE Question SET position = -1 "
                        f"WHERE id = {int(id)!r}")
            cur.execute(f"UPDATE Question SET position = position + 1 "
                        f"WHERE position >= {input_question.position!r} and position < {question_json['position']!r}")
        elif int(input_question.position) > question_json["position"]:
            cur.execute(f"UPDATE Question SET position = -1 "
                        f"WHERE id = {question_json['id']!r}")
            cur.execute(f"UPDATE Question SET position = position - 1 "
                        f"WHERE position <= {input_question.position!r} and position > {question_json['position']!r}")
    else:
        return {"message":"Question non trouvée"},404
    cur.execute(f"UPDATE Question SET position = {input_question.position!r},"
                f"title = {input_question.title!r},"
                f"text = {input_question.text!r},"
                f"image = {input_question.image!r} WHERE id = {question_json['id']!r}")

    cur.execute(f"DELETE FROM Reponse WHERE id = {question_json['id']!r}")
    insert_reponse = ""
    for answer in possible_answers :
        insert_reponse += f"({question_json['id']!r},{answer.text!r},{answer.isCorrect!r}),"
    cur.execute(f"INSERT into Reponse (id, text, isCorrect) values"
                f"{insert_reponse[:-1]}")

    cur.execute('commit')
    cur.close()
    db.close()

    return question_json, 204