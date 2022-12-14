from flask import Flask, request
from flask_cors import CORS

from jwt_utils import build_token, decode_token

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

if __name__ == "__main__":
    app.run()