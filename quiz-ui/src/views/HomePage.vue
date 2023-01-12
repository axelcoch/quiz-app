<template>
  <div class="quizstart">
  <div class="col text-center">
  <h1 style="color: white">QuizAnime</h1>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
  {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
      <br/>
      <button class="btn btn-light">
        <router-link to="/start-new-quiz-page">Démarrer le quiz !</router-link>
      </button>
  </div>
  </div>

</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registredScores: []
    };
  },
  async created() {
		console.log("Composant Home page 'created'")
    var quizInfoApiResult = await quizApiService.getQuizInfo()
    this.registredScores = quizInfoApiResult.data.scores
  }
};
</script>