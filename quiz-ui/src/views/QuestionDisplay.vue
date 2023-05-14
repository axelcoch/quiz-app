<template>   
  <div
    class="d-flex flex-column justify-content-center align-items-center text-dark"
  >
    <div
      class="card d-flex flex-column justify-content-center align-items-center p-2"
      style="opacity: 0.8; width: 60%; max-width: 60rem; min-width: 20rem"
    >
      <h1>{{ question.title }}</h1>
      <h4>{{ question.text }}</h4>
      <img v-if="question.image" :src="question.image" />

      <div
        class="d-flex flex-column justify-content-center text-center my-3 w-50 p-3"
        style="background-color: #eee; opacity: 0.7"
      >
        <a
          class="text-center text-dark link-dark text-decoration-none h-25 rounded"
          style="font-size: 1.2em; cursor: pointer"
          v-for="(answer, index) in question.possibleAnswers"
          @click="$emit('answer-selected', index)"
        >
          {{ answer.text }}
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "QuestionDisplay",
  props: {
    question: {
      type: Object,
    },
    emits: ["answer-selected"],
  },
};
</script>
