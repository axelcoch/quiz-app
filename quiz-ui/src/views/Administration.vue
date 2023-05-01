<template>
    <div v-if="token" class="container text-center">
      <div class="row justify-content-center align-items-center">
        <label style="color: white" class="text-dark" for="name" ></label>
            <br/>
            <button class="text-center btn btn-light link-dark text-decoration-none" type="button" @click="logout()">déconnexion</button>

        <div class="col-md-12">
          <div class="mx-auto w-25">
            <label style="color: white" class="text-dark" for="name" ></label>
            <br/>
            <button class="text-center btn btn-light link-dark text-decoration-none" type="button" @click="deleteAllQuestions()">Supprimer toutes les questions</button>
            <label style="color: white" class="text-dark" for="name" ></label>
            <br/>
            <button class="text-center btn btn-light link-dark text-decoration-none" type="button" @click="deleteAllParticipations()">Supprimer tous les participants</button>
          </div>
        </div>
      </div>

    </div>
    <div v-else class="container text-center">
        <div class="row justify-content-center align-items-center" style="height: 70vh;">
      <div class="col-md-12">
      <p class="text-dark h2">Saisissez votre mot de passe en dessous :</p>
      <div class="form-floating mx-auto w-25">
        <input
            type="text"
            class="form-control"
            v-model="password"
            id="password"
            name="password"
            placeholder="mot de passe"
        >
    </div>
      <label style="color: white" class="text-dark" for="name" ></label>
      <br/>
      <button class="text-center btn btn-light link-dark text-decoration-none" type="button" @click="login()">Connexion</button>
      <br/><br/>
      <div class="text-center text-dark h4" v-if="!password && wrong" style="background-color: #eee; opacity: 0.70;"> 
        Ce n'est pas le bon mot de passe, un mail a été envoyé aux autorités compétentes...
      </div>
    </div>
    </div>
    </div>
  </template>
  <script>



  import QuestionDisplay from './QuestionDisplay.vue';
  import participationStorageService from "@/services/ParticipationStorageService";
  import quizApiService from "@/services/QuizApiService";
  
  export default {
  name: "Administration",
  data() {
    return {
      password : '',
      wrong: false,
      token : null,
    };
  },
  components: {
    QuestionDisplay
  },
  async created() {
    this.token = participationStorageService.getToken();
  },
  methods: {
    async login(){
      let loginPromise = quizApiService.login(this.password);
      let loginApiResult = await loginPromise;
      if (loginApiResult) {
        participationStorageService.saveToken(loginApiResult.data.token)
        this.token = loginApiResult.data.token
      }
      else {
        this.wrong = true;
        return;
      }
    },
    async logout() {
      this.token = null;
      participationStorageService.deleteToken();
    },
    async deleteAllParticipations(){
      await quizApiService.deleteAllParticipations(this.token)
      this.token = participationStorageService.getToken()
    },
    async deleteAllQuestions(){
      await quizApiService.deleteAllQuestions(this.token)
      this.token = participationStorageService.getToken()
    }
  }
}
</script>
  