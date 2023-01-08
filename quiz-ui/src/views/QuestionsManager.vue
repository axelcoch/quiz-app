<template>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
    <QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
</template>

<script>
import QuestionDisplay from "./QuestionDisplay.vue";
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";

export default {
    name: "QuestionsManager",
    data() {
    return {
      currentQuestion : {},
      currentQuestionPosition : 1,
      totalNumberOfQuestion : 0,
      clickOnAnswer : Array()
    };
    },
    components: {QuestionDisplay},

    async created() {
        let quizInfoPromise = quizApiService.getQuizInfo();
        let quizInfoApiResult = await quizInfoPromise;
        this.totalNumberOfQuestion = quizInfoApiResult.data.size
        this.currentQuestion = await this.loadQuestionByposition();
    },

    methods: {
    async loadQuestionByposition(){
      let questionPromise = quizApiService.getQuestion(this.currentQuestionPosition);
      let questionApiResult = await questionPromise;
      if (!questionApiResult) {
        this.$router.push("/new-quiz-page?error=questionUndefined")
      }
      return questionApiResult.data
    },
    async answerClickedHandler(position){
      // Pour suivre la convention des test Postman
      this.answersSelected.push(position+1)
      if (this.currentQuestionPosition == this.totalNumberOfQuestion) {
        this.endQuiz()
      } else {
        this.currentQuestionPosition += 1
        this.currentQuestion = await this.loadQuestionByposition();
      }
    },
    async endQuiz(){
      let quizSubmitPromise = quizApiService.submitQuiz({
        "playerName": participationStorageService.getPlayerName(),
        "answers" : this.answersSelected
      });
      let quizSubmitApiResult = await quizSubmitPromise
      this.$router.push('/');
    },
  }
};
</script>
