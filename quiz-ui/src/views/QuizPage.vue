<template>      
  <div class="container text-center">
    <div
      class="row justify-content-center align-items-center"
      style="height: 70vh"
    >
      <div class="col-md-12">
        <p class="text-dark h2">Saisissez votre nom juste en dessous :</p>
        <div class="form-floating mx-auto w-25">
          <input
            type="text"
            class="form-control"
            v-model="username"
            id="name"
            name="name"
            placeholder="Username"
          />
          <label style="color: white" class="text-dark" for="name"></label>
          <br />
          <button
            class="text-center btn btn-light link-dark text-decoration-none"
            type="button"
            @click="launchNewQuiz()"
          >
            GO!
          </button>
        </div>
      </div>
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
    },
  },
};
</script>
