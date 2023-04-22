<template>

  <div class="col text-center">
  <div class="container">
  <h1 class="text-dark">QuizAnime</h1>
  <!-- <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
  {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div> -->
      <br/>
      <button class="btn btn-light">
        <router-link to="/start-new-quiz-page" class="link-dark text-decoration-none">Démarrer le quiz !</router-link>
      </button>
    </div>
    <div class="container">
      <br>
  <ScorePage /></div>
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