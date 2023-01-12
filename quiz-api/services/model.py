class Answer():
    def __init__(self, text: str, isCorrect: bool, id = None) :
        self.text = text
        self.isCorrect = isCorrect
        self.id_question = None
        self.id = None

    def serialize(self, answer_id = False):
        reponse_json = dict()
        for key, value in self.__dict__.items():
            if value is not None and key != "id": 
                reponse_json[key] = value
        if answer_id:
            reponse_json["id"] = self.id
        return reponse_json

    def deserialize(self, reponse_json):
        for k,v in reponse_json.items() :
            setattr(self,k,v)

class Question():
    def __init__(self, title: str, text: str, position: int, image: str, possibleAnswers=list[Answer], id=None):
        self.id = id
        self.title = title
        self.text = text
        self.position = position
        self.image = image
        self.possibleAnswers = possibleAnswers        

    def serialize(self, answer_id=False):
        question_json = dict()
        for key, value in self.__dict__.items():
            if value is not None and key != "possibleAnswers":
                question_json[key] = value
        question_json["possibleAnswers"] = [answer.serialize(answer_id) for answer in self.possibleAnswers]
    
        
        return question_json

    def deserialize(self,question_json):
        for k,v in question_json.items():
            setattr(self,k,v)
