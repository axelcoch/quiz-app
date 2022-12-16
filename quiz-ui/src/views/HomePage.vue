<template>
  <h1>Home page</h1>
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
    this.registredScores.push(quizInfoApiResult.data.scores)

  }
};
</script>