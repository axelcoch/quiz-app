<template>

  <div class="container text-center">
    <div class="row justify-content-center align-items-center" style="height: 100vh;">
  <div class="col-md-12">
  <h1 class="text-dark">QuizAnime</h1>
      <br/>
      <button class="btn btn-light btn-lg">
        <router-link to="/start-new-quiz-page" class="link-dark text-decoration-none">Démarrer le quiz !</router-link>
      </button>
    </div>
    <div class="col-md-12">
      <br>
  <ScorePage /></div>
  </div>
</div>


</template>

<script>
import quizApiService from "@/services/QuizApiService";
import ScorePage from "./ScorePage.vue";

export default {
  name: "HomePage",
  data() {
    return {
      registredScores: []
    };
  },
  components: {
      ScorePage
    },
  async created() {
		console.log("Composant Home page 'created'")
    var quizInfoApiResult = await quizApiService.getQuizInfo()
    this.registredScores = quizInfoApiResult.data.scores
  }
};
</script>