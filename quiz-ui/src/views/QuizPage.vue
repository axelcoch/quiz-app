<template>
    <div>
    


    <p>Saisissez votre nom :</p>
    <div class="form-floating ">
        <input
            type="text"
            class="form-control"
            v-model="username"
            id="name"
            name="name"
            placeholder="Username"
        />
        <label class="text-dark" for="name">Username</label>
    </div>
    <br/>
    <button class="text-center btn btn-light" @click="launchNewQuiz">GO!</button>   
    </div>

    
  
</template>
  
<script>
  import participationStorageService from "@/services/ParticipationStorageService";
  
  export default {
    name: "QuizPage",
    data() {
      return {
        username: "",
      };
    },
    methods: {
        buttonClickHandler() {
            this.username = this.data.username;
        },
    },
    launchNewQuiz() {
        participationStorageService.savePlayerName(this.username.toString());
        const playerName = participationStorageService.getPlayerName();
        console.log("Launch new quiz with " + playerName);
        this.$router.push("/questions");
    },
  };
  </script>