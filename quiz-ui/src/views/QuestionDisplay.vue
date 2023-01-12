<template>
  <div class="d-flex flex-column justify-content-center align-items-center w-80">
    <h1>{{ question.text }}</h1>
    <h5>{{ question.title }}</h5>
    <img v-if="question.image" :src="question.image"/>

    <div class="d-flex flex-column justify-content-center text-center my-5 w-50 p-3" style="background-color: #eee;">
      <a class="text-center h-25" style="font-size: 1.2em; color: white" v-for="(answer, index) in question.possibleAnswers" @click="$emit('answer-selected', index)">
        {{answer.text}}
      </a> 
    </div>
  </div>
</template>

<script>
export default {
  name: "QuestionDisplay",
  props: {
    question: {
      type: Object
    },
    emits: ["answer-selected"]
  },
};
</script>

