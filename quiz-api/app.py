from flask import Flask, request
from flask_cors import CORS

from services.jwt_utils import build_token, decode_token
import services.functions as functions
import services.connection as connection

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return functions.get_quiz_info()

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
    return {"message" : "Aucune position"}, 404

@app.route('/count',methods=['GET'])
def count_question():
    return {"nb_question" : functions.count()}, 200

@app.route('/questions/all', methods=['DELETE'])
def delete_all():
    #Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    try :
        decode_token(token[7:])
    except TypeError:
        return {"message" : "Not authenticated"}, 401
    except Exception as e:
        return e.__dict__ , 401

    return functions.delete_all()

@app.route('/questions/<question_id>', methods=['DELETE'])
def delete_by_id(question_id):
    #Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    try :
        decode_token(token[7:])
    except TypeError:
        return {"message" : "Not authenticated"}, 401
    except Exception as e:
        return e.__dict__ , 401

    return functions.delete_id(question_id)

@app.route('/questions/<question_id>', methods=['PUT'])
def update_question(question_id):
    #Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    try :
        decode_token(token[7:])
    except TypeError:
        return {"message" : "Not authenticated"}, 401
    except Exception as e:
        return e.__dict__ , 401

    questions = request.get_json()
    return functions.update_question(questions, question_id)

@app.route('/participations',methods=['POST'])
def add_participant():

    participant = request.get_json()
    return functions.add_participant(participant)

@app.route('/participations/all', methods=['DELETE'])
def deleteAllPart():
    #Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    try :
        decode_token(token[7:])
    except TypeError:
        return {"message" : "Not authenticated"}, 401
    except Exception as e:
        return e.__dict__ , 401

    return functions.delete_all_part()

@app.route('/rebuild-db', methods=['POST'])
def dbBuild():
    return connection.build_db() 

if __name__ == "__main__":
    app.run(debug=True)