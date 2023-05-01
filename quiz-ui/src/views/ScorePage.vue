
<template>

    <div class="container">
        <table class="table text-reset  caption-top table-striped table-hover text-center" style="background-color: #eee; opacity: 0.70;" v-if="score.length">
      <thead>
        <tr>
          <th>Position</th>
          <th>Username</th>
          <th>Score</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(scoreEntry,index) in score">
          <td>{{ index }}</td>
          <td>{{ scoreEntry.playerName }} </td>
          <td>{{ scoreEntry.score }}</td>
        </tr>
      </tbody>
    </table>
    <div v-else>
    </div>
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
            totalNumberOfQuestion: 0
        }
    },
    async created() {
        let quizInfo = await quizApiService.getQuizInfo();
        this.score = quizInfo.data.scores;
        this.totalNumberOfQuestion = quizInfo.data.size;
    },

};
</script>