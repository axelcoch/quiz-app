
# def update_question(updated_question,id_question):
#     db = init_db()
#     cur = db.cursor()
#     cur.execute("begin")
#     # Set current position to the last to work on the gap
#     # Given one position, if position modified check difference between old and new position based on question id
#     # If position lower, increase position of all after and equal questions by 1
#     # Else, decrease by 1
#     # Update new position in the filling gap
#     # remove old answers data 
#     # re insert new values
#     id_question = int(id_question)
#     input_question = Question()
#     # print("possible answers",updated_question['possibleAnswers'])
#     possible_answers = [Answer() for answer in updated_question["possibleAnswers"]]

#     for i,answer_json in enumerate(updated_question["possibleAnswers"]) :
#         possible_answers[i].deserialize(answer_json.copy())
#     # print("input answers",possible_answers)
#     updated_question["possibleAnswers"] = possible_answers
#     input_question.deserialize(updated_question)
#     question_json,status = get_id(id_question,True)
#     if status == 200 :

#         if int(input_question.position) < question_json["position"] :
#             print('smaller')
#             cur.execute(
#             f"UPDATE Question SET position = -1 "
#             f"WHERE id = {id_question!r}"
#             )
#             cur.execute(
#                 f"UPDATE Question SET position = position + 1 "
#                 f"WHERE position >= {input_question.position!r} and position < {question_json['position']!r}"
#                 )
#         elif int(input_question.position) > question_json["position"]:
#             cur.execute(
#             f"UPDATE Question SET position = -1 "
#             f"WHERE id = {question_json['id']!r}"
#             )
#             cur.execute(
#                 f"UPDATE Question SET position = position - 1 "
#                 f"WHERE position <= {input_question.position!r} and position > {question_json['position']!r}"
#             )
#     else:
#         return {"message":"Question non trouvée"},404

#     cur.execute(
#         f"UPDATE Question SET position = {input_question.position!r},"
#         f"title = {input_question.title!r},"
#         f"text = {input_question.text!r},"
#         f"image = {input_question.image!r} WHERE id = {question_json['id']!r}"
#     )


#     cur.execute(f"DELETE FROM Answer WHERE id_question = {question_json['id']!r}")
#     insert_reponse = ""
#     for answer in possible_answers :
#         insert_reponse += f"({question_json['id']!r},{answer.text!r},{answer.isCorrect!r}),"

#     cur.execute(
#         f"INSERT into Answer (id_question,text,isCorrect) values"
#         f"{insert_reponse[:-1]}"
#         )

#     cur.execute('commit')
#     cur.close()
#     db.close()

#     return question_json, 204

# def delete_all_questions():
#     db = init_db()
#     cur = db.cursor()
#     cur.execute("begin")
#     delete_question= cur.execute(f"DELETE FROM Question")

#     cur.execute(f"DELETE FROM Answer")

#     cur.execute("commit")
#     cur.close()
#     db.close()
    
#     return delete_question,204

# def delete_question_by_id(id):
#     db = init_db()
#     cur = db.cursor()
#     cur.execute("begin")
#     question,status = get_id(id)
#     print(question)
#     if status == 200 :
#         cur.execute(f"DELETE FROM Question where id = {id}")
#         cur.execute(f"DELETE FROM Answer where id_question = {id}")
#         cur.execute(
#             f"UPDATE Question SET position = position - 1 "
#                 f"WHERE position >= {question['position']!r}"
#         )
        
#     else:
#         return {"message":"Question non trouvée"},404
#     cur.execute('commit')
#     cur.close()
#     db.close()
#     print('delete done')
#     return question,204

# def get_quiz_info():
#     db = init_db()
#     cur = db.cursor()
#     cur.execute("begin")
#     try : 
#         nb_question = cur.execute(f"SELECT COUNT(*) FROM Question")
#         total_question = nb_question.fetchone()[0]
#     except sqlite3.Error as e:
#         # handle the error
#         print(f'An error occurred: {e}')
#     try:
#         participation_info = cur.execute(f"SELECT playerName,score,date FROM Attempts ORDER BY score DESC LIMIT 10")
#     except sqlite3.Error as e:
#         # handle the error
#         print(f'An error occurred: {e}')
#     participations_details = []

#     for participation in participation_info :
#         participations_details.append({"playerName":participation[0],"score":participation[1],"date":participation[2]})
#     cur.close()
#     db.close()
#     return {"size":total_question,"scores":participations_details},200

# def post_participation(player_answers):
#     quiz_info =get_quiz_info()
#     if quiz_info[1] != 200 :
#         return {"error":"Problème de récupération des informations du quiz"},500  
#     print(player_answers)
#     total_question = quiz_info[0]["size"]

#     playerName = player_answers['playerName']

#     if len(player_answers['answers']) < total_question :
#         return {"ERROR":"Answers missing from start to finish"},400

#     if len(player_answers['answers']) > total_question :
#         return {"ERROR":"Too many answers"},400
#     score = 0

#     l_a = []

#     for index,answer_chosen in enumerate(player_answers["answers"]) :
#         question,status = get_pos(index+1)
#         if status!= 200 :
#             return {"ERROR":"Search Question Error"},500
#         possibleAnswers = question["possibleAnswers"]

#         for index_sql,answer_choice in enumerate(possibleAnswers) :
#             if answer_choice['isCorrect'] == True :
#                 correct_text = answer_choice['text']
#                 isCorrect = False
#                 if index_sql == int(answer_chosen)-1 :
#                     score+=1
#                     isCorrect = True
#                 l_a.append((question['text'],possibleAnswers[answer_chosen-1]['text'],isCorrect,correct_text))
#     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(playerName)
#     print(score)
#     print(now)
#     attempt_query = f"({str(playerName)!r},{int(score)!r},{str(now)!r}),"
#     print(attempt_query[:-1])

#     db = init_db()
#     cur = db.cursor()
#     cur.execute("begin") 
#     try:
#         cur.execute(f"INSERT INTO Attempts (playerName,score,date) values {attempt_query[:-1]}")
#     except sqlite3.Error as e:
#         # handle the error
#         print(f'An error occurred: {e}')
#     cur.execute('commit')
#     cur.close()
#     db.close()

#     return {"l_a":l_a,"score":score, "playerName":playerName,"date_attempt":now},200

# def delete_all_participations():
#     db = init_db()
#     cur = db.cursor()
#     cur.execute("begin")
#     try:
#         cur.execute(f"DELETE FROM Participation")
#     except sqlite3.Error as e:
#         # handle the error
#         print(f'An error occurred: {e}')
#     cur.execute('commit')
#     cur.close()
#     db.close()
#     return {},204