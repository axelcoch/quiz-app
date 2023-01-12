<template>
    <div class="text-center fs-4">
    <p style="color: white">Saisissez votre nom dans l'encadré noir juste en dessous:</p>
    <div class="form-floating mx-auto">
        <input
            type="text"
            class="form-control"
            v-model="username"
            id="name"
            name="name"
            placeholder="Username"
        >
        <label style="color: white" class="text-dark" for="name" ></label>
        <br/>
        <button class="text-center btn btn-light" type="button" @click="launchNewQuiz()">GO!</button>
 
    </div>
    </div>
</template>
  
<script>
  import participationStorageService from "@/services/ParticipationStorageService";
  import quizApiService from "@/services/QuizApiService";
  
  export default {
    name: "QuizPage",
    data() {
      return {
        username: "",
      };
    },
    async created() {
	    let quizInfoPromise = quizApiService.getQuizInfo();
	    let quizInfoApiResult = await quizInfoPromise;
        this.numberQuestion = quizInfoApiResult.data.size;
    },
    methods: {
        buttonClickHandler() {
            this.username = this.data.username;
        },
    
        launchNewQuiz() {
            participationStorageService.savePlayerName(this.username.toString());
            const playerName = participationStorageService.getPlayerName();
            console.log("Launch new quiz with " + playerName);
            this.$router.push("/questions");
        }
  },
  };
</script>