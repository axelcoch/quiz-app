
<template>

    <div class="container">
        <table class="table text-reset  caption-top table-striped table-hover text-center" style="background-color: #eee; opacity: 0.70;">
      <thead>
        <tr>
          <th>Position</th>
          <th>Username</th>
          <th>Score</th>
          <!-- <th>Date</th> -->
        </tr>
      </thead>
      <tbody>
        <tr v-for="(scoreEntry,index) in score">
          <td>{{ index }}</td>
          <td>{{ scoreEntry.playerName }} </td>
          <td>{{ scoreEntry.score }}</td>
          <!-- <td>{{ scoreEntry.date }}</td> -->
        </tr>
      </tbody>
    </table>
        <!-- <h1 style="color: white">{{ playerName }} votre score est de : {{score}} / {{totalNumberOfQuestion}}</h1> -->
    </div>
    
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";

export default {
    name: "ScorePage",
    data(){
        return {
            score : [],
            // playerName: null,
            // score: 0,
            totalNumberOfQuestion: 0
        }
    },
    async created() {
        // this.playerName = participationStorageService.getPlayerName();
        let quizInfo = await quizApiService.getQuizInfo();
        this.score = quizInfo.data.scores;
        this.totalNumberOfQuestion = quizInfo.data.size;
    // this.registeredScores = quizInfoApiResult.data.scores;
    // this.numberQuestion = quizInfoApiResult.data.size;
    },

};
</script>