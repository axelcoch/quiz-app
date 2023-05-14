<template>      
  <div class="container text-center">
    <div v-if="token" class="row justify-content-center align-items-center">
      <label style="color: white" class="text-dark" for="name"></label>
      <br />
      <button
        class="text-center btn btn-light link-dark text-decoration-none"
        type="button"
        @click="logout()"
      >
        déconnexion
      </button>
      <br /><br />
      <div class="col-md-12">
        <div class="mx-auto w-75">
          <div class="btn-group">
            <label style="color: white" class="text-dark" for="name"></label>
            <br />
            <button
              class="text-center btn btn-light link-dark text-decoration-none"
              type="button"
              @click="deleteAllQuestions()"
            >
              Supprimer toutes les questions
            </button>
            <label style="color: white" class="text-dark" for="name"></label>
            <br />
            <button
              class="text-center btn btn-light link-dark text-decoration-none"
              type="button"
              @click="deleteAllParticipations()"
            >
              Supprimer tous les participants
            </button>
            <label style="color: white" class="text-dark" for="name"></label>
            <br />
            <button
              class="text-center btn btn-light link-dark text-decoration-none"
              @click="listQuestionHandling"
            >
              Afficher la liste des questions
            </button>
            <label style="color: white" class="text-dark" for="name"></label>
            <br />
            <button
              class="text-center btn btn-light link-dark text-decoration-none"
              @click="addQuestionHandling"
            >
              Ajouter une nouvelle question
            </button>
          </div>
        </div>
      </div>
      <div class="col-md-12">
        <br />
        <QuestionList
          v-if="admin_mode === 'list'"
          :question_list="question_list"
          @question-detail="detailQuestionHandling"
          @question-edit="editQuestionHandling"
          @question-delete="deleteQuestionHandling"
        />
        <QuestionDisplay
          v-else-if="admin_mode === 'detailQuestion'"
          :question="question"
        />
        <QuestionEdit
          v-else-if="admin_mode === 'newQuestion'"
          :question="emptyQuestion"
          @update:question="postQuestion"
        />
        <QuestionEdit
          v-else-if="admin_mode === 'editQuestion'"
          :question="question"
          @update:question="updateQuestion"
        />
      </div>
    </div>
    <div v-else class="container text-center">
      <div
        class="row justify-content-center align-items-center"
        style="height: 70vh"
      >
        <div class="col-md-12">
          <p class="text-dark h2">Saisissez votre mot de passe en dessous :</p>
          <div class="form-floating mx-auto w-25">
            <input
              type="password"
              class="form-control"
              v-model="password"
              id="password"
              name="password"
              placeholder="mot de passe"
            />
          </div>
          <label style="color: white" class="text-dark" for="name"></label>
          <br />
          <button
            class="text-center btn btn-light link-dark text-decoration-none"
            type="button"
            @click="login()"
          >
            Connexion
          </button>
          <br /><br />
          <div
            class="text-center text-dark h4"
            v-if="!password && wrong"
            style="background-color: #eee; opacity: 0.7"
          >
            Ce n'est pas le bon mot de passe, un mail a été envoyé aux autorités
            compétentes...
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import QuestionDisplay from "./QuestionDisplay.vue";
import QuestionList from "./QuestionList.vue";
import QuestionEdit from "./QuestionEdit.vue";
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";

export default {
  name: "Administration",
  data() {
    return {
      password: "",
      wrong: false,
      token: null,
      admin_mode: "",
      question: null,
      question_list: Array(),
      emptyQuestion: {
        text: null,
        title: null,
        image: null,
        position: null,
        possibleAnswers: null,
      },
    };
  },
  components: {
    QuestionDisplay,
    QuestionList,
    QuestionEdit,
  },
  async created() {
    this.token = participationStorageService.getToken();
    this.updateQuestionList();
  },
  methods: {
    async login() {
      let loginPromise = quizApiService.login(this.password);
      let loginApiResult = await loginPromise;
      if (loginApiResult) {
        participationStorageService.saveToken(loginApiResult.data.token);
        this.token = loginApiResult.data.token;
      } else {
        this.wrong = true;
        return;
      }
    },
    async logout() {
      this.token = null;
      participationStorageService.deleteToken();
    },
    async deleteAllParticipations() {
      await quizApiService.deleteAllParticipations(this.token);
      this.token = participationStorageService.getToken();
    },
    async deleteAllQuestions() {
      await quizApiService.deleteAllQuestions(this.token);
      this.token = participationStorageService.getToken();
      this.updateQuestionList();
      this.admin_mode = "";
    },
    async deleteQuestionHandling(position) {
      let questionPromise = quizApiService.getQuestion(position);
      let questionApiResult = await questionPromise;
      console.log(questionApiResult);
      await quizApiService.deleteQuestion(
        questionApiResult.data.id,
        this.token
      );
      this.updateQuestionList();
      this.admin_mode = "";
    },
    addQuestionHandling() {
      this.admin_mode = "newQuestion";
    },
    listQuestionHandling() {
      this.admin_mode = "list";
    },
    async editQuestionHandling(position) {
      let questionPromise = quizApiService.getQuestion(position);
      let questionApiResult = await questionPromise;
      this.admin_mode = "editQuestion";
      this.question = questionApiResult.data;
    },
    async detailQuestionHandling(position) {
      let questionPromise = quizApiService.getQuestion(position);
      let questionApiResult = await questionPromise;
      this.admin_mode = "detailQuestion";
      this.question = questionApiResult.data;
    },
    async updateQuestionList() {
      this.question_list = Array();
      let quizInfo = quizApiService.getQuizInfo();
      let quizInfoResult = await quizInfo;
      for (let i = 1; i <= quizInfoResult.data.size; i++) {
        try {
          let questionPromise = quizApiService.getQuestion(i);
          let questionApiResult = await questionPromise;
          this.question_list.push(questionApiResult.data);
        } catch (error) {
          console.log(error);
        }
      }
    },
    async updateQuestion(new_question) {
      await quizApiService.updateQuestion(
        this.question.id,
        new_question,
        this.token
      );
      this.token = participationStorageService.getToken();
      this.updateQuestionList();
      this.admin_mode = "list";
    },
    async postQuestion(new_question) {
      console.log(new_question);
      await quizApiService.postQuestion(new_question, this.token);
      this.token = participationStorageService.getToken();
      this.updateQuestionList();
      this.admin_mode = "list";
    },
  },
};
</script>
