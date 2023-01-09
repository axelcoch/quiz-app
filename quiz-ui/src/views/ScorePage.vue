<template>

    <div>
        <h1>{{ playerName }} votre score est de : {{score}} / {{totalNumberOfQuestion}}</h1>
    </div>
    
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";

export default {
    name: "ScorePage",
    data(){
        return {
            playerName: null,
            score: 0,
            totalNumberOfQuestion: null
        }
    },
    async created() {
        this.playerName = participationStorageService.getPlayerName();
        this.score = participationStorageService.getParticipationScore();
        const quizInfo = await quizApiService.getQuizInfo();
        this.totalNumberOfQuestion = quizInfo["data"]["size"];
    },

};
</script>