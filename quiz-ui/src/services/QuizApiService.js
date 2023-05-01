import axios from "axios";

const instance = axios.create({
	baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  getQuestion(position) {
    return this.call("get", "questions?position="+position);
  },
  login(password) {
    return this.call("post", "login", { password: password });
  },
  postQuestion(question, token) {
    return this.call("post", "questions", question, token);
  },
  postParticipation(player_answers) {
    return this.call("post", "participations", player_answers);
  },
  updateQuestion(question_id, question, token) {
    return this.call("put", "questions/" + question_id, question, token);
  },
  deleteQuestion(question_id, token) {
    return this.call("delete", "questions/" + question_id, null, token);
  },
  deleteAllQuestions(token) {
    return this.call("delete", "questions/all", null, token);
  },
  deleteAllParticipations(token) {
    return this.call("delete", "participations/all", null, token);
  }
};