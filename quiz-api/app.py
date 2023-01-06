from flask import Flask, request
from flask_cors import CORS

from jwt_utils import build_token, decode_token
import functions

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

@app.route('/login', methods=['POST'])
def GetPassword():
    payload = request.get_json()
    password = payload["password"]
    if password == 'flask2023':
        token = build_token()
        return {"token": token}, 200
    else:
        return 'Unauthorized', 401

@app.route('/questions', methods=['POST'])
def AddQuestions():
    #Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    try :
        decode_token(token[7:])
    except TypeError:
        return {"message" : "Not authenticated"}, 401
    except Exception as e:
        return e.__dict__ , 401
        
    #récupèrer un l'objet json envoyé dans le body de la requète
    questions = request.get_json()
    return functions.add_question(questions)

@app.route('/questions/<question_id>', methods=['GET'])
def get_question_by_id(question_id):
    return functions.get_id(question_id)

@app.route('/questions', methods=['GET'])
def get_question_by_position():
    position = request.args.get("position")
    if position :
        return functions.get_pos(position)
    return {"message" : "Pas de position"}, 404

if __name__ == "__main__":
    app.run()