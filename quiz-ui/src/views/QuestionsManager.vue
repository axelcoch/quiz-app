<template>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
    <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
    <br/>
    <ScorePage/>
</template>

<script>
import ScorePage from "./ScorePage.vue";
import QuestionDisplay from "./QuestionDisplay.vue";
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";

export default {
    name: "QuestionsManager",
    data() {
      return {
        currentQuestion : {},
        currentQuestionPosition : 1,
        totalNumberOfQuestion : null,
        answerSelected : Array()
      };
    },
    components: {
      QuestionDisplay,
      ScorePage
    },

    async created() {
        let quizInfoPromise = quizApiService.getQuizInfo();
        let quizInfoApiResult = await quizInfoPromise;
        this.totalNumberOfQuestion = quizInfoApiResult.data.size
        this.currentQuestion = await this.loadQuestionByPosition();
    },

    methods: {
    async loadQuestionByPosition(){
      let questionPromise = quizApiService.getQuestion(this.currentQuestionPosition);
      let questionApiResult = await questionPromise;
      return questionApiResult.data
    },

    async answerClickedHandler(position){
      this.answerSelected.push(position + 1)
      if (this.currentQuestionPosition == this.totalNumberOfQuestion) {
        this.endQuiz()
      } else {
        this.currentQuestionPosition += 1
        this.currentQuestion = await this.loadQuestionByPosition();
      }
    },

    async endQuiz(){
      let quizSubmitPromise = quizApiService.postParticipation({
        "playerName": participationStorageService.getPlayerName(),
        "answers" : this.answerSelected
      });
      let quizSubmitApiResult = await quizSubmitPromise
      this.$router.push('/');
    },
  }
};
</script>
