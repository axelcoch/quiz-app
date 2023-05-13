<template>
  <form>
    <div class="p-1" style="background-color: #eee; opacity: 0.7">
      <div class="row m-2">
        <div class="form-group col col-md-10">
          <label style="color: white" class="text-dark" for="Titre"
            >Titre de la question :</label
          >
          <br />
          <input
            type="text"
            class="form-control"
            id="Titre"
            placeholder="Titre"
            v-model="question.title"
          />
        </div>
        <div class="form-group col col-md-2">
          <label style="color: white" class="text-dark" for="Num"
            >Numéro de la question :</label
          >
          <br />
          <select class="form-control" id="Num" v-model="question.position">
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
            <option>6</option>
            <option>7</option>
            <option>8</option>
            <option>9</option>
            <option>10</option>
            <option>11</option>
            <option>12</option>
            <option>13</option>
            <option>14</option>
            <option>15</option>
            <option>16</option>
            <option>17</option>
            <option>18</option>
            <option>19</option>
            <option>20</option>
            <option>21</option>
            <option>22</option>
            <option>23</option>
            <option>24</option>
            <option>25</option>
          </select>
        </div>
      </div>
      <div class="form-group m-2">
        <label style="color: white" class="text-dark" for="Enonce"
          >Enoncé de la question :</label
        >
        <br />
        <textarea
          type="text"
          class="form-control"
          id="Enonce"
          placeholder="Enoncé"
          v-model="question.text"
        ></textarea>
      </div>
      <div class="form-group m-2">
        <label style="color: white" class="text-dark" for="Img"
          >Image en Base64 :</label
        >
        <br />
        <textarea
          type="text"
          class="form-control"
          id="Enonce"
          placeholder="Img"
          v-model="question.image"
        ></textarea>
      </div>

      <div class="row m-2">
        <div class="col">
          <div class="row">
            <div class="col col-md-8">
              <label style="color: white" class="text-dark" for="Aw1"
                >Réponse 1 :</label
              >
              <br />
              <input
                type="text"
                class="form-control"
                id="Aw1"
                v-model="this.firstAnswer.text"
              />
            </div>
            <div class="col my-4">
              <div class="form-check form-check-inline">
                <input
                  class="form-check-input"
                  type="radio"
                  id="true"
                  name="contact"
                  value="true"
                  v-model="this.firstAnswer.isCorrect"
                />
                <label class="form-check-label" for="true">Bonne réponse</label>
              </div>
            </div>
          </div>
        </div>

        <div class="col">
          <div class="row">
            <div class="col col-md-8">
              <label style="color: white" class="text-dark" for="Aw2"
                >Réponse 2 :</label
              >
              <br />
              <input
                type="text"
                class="form-control"
                id="Aw2"
                v-model="this.secondAnswer.text"
              />
            </div>
            <div class="col my-4">
              <div class="form-check form-check-inline">
                <input
                  class="form-check-input"
                  type="radio"
                  id="true"
                  name="contact"
                  value="true"
                  v-model="this.secondAnswer.isCorrect"
                />
                <label class="form-check-label" for="true">Bonne réponse</label>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="row m-2">
        <div class="col">
          <div class="row">
            <div class="col col-md-8">
              <label style="color: white" class="text-dark" for="Aw3"
                >Réponse 3 :</label
              >
              <br />
              <input
                type="text"
                class="form-control"
                id="Aw3"
                v-model="this.thirdAnswer.text"
              />
            </div>
            <div class="col my-4">
              <div class="form-check form-check-inline">
                <input
                  class="form-check-input"
                  type="radio"
                  id="true"
                  name="contact"
                  value="true"
                  v-model="this.thirdAnswer.isCorrect"
                />
                <label class="form-check-label" for="true">Bonne réponse</label>
              </div>
            </div>
          </div>
        </div>

        <div class="col">
          <div class="row">
            <div class="col col-md-8">
              <label style="color: white" class="text-dark" for="Aw4"
                >Réponse 4 :</label
              >
              <br />
              <input
                type="text"
                class="form-control"
                id="Aw4"
                v-model="this.fourthAnswer.text"
              />
            </div>
            <div class="col my-4">
              <div class="form-check form-check-inline">
                <input
                  class="form-check-input"
                  type="radio"
                  id="true"
                  name="contact"
                  value="true"
                  v-model="this.fourthAnswer.isCorrect"
                />
                <label class="form-check-label" for="true">Bonne réponse</label>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="col-md-12">
        <label style="color: white" class="text-dark" for="name"></label>
        <br />
        <button
          class="text-center btn btn-light link-dark text-decoration-none"
          type="button"
          @click="submit"
        >
          Envoyer
        </button>
        <div><br /></div>
      </div>
    </div>
  </form>
</template>

<script>

export default {
  name: "QuestionEdit",
  props: {
    question: {
      type: Object,
    },
    emits: ["update:question"],
  },
  data() {
    return {
      image: this.question.image,
      firstAnswer: {
        text: null,
        isCorrect: null,
      },
      secondAnswer: {
        text: null,
        isCorrect: null,
      },
      thirdAnswer: {
        text: null,
        isCorrect: null,
      },
      fourthAnswer: {
        text: null,
        isCorrect: null,
      },
    };
  },
  mounted() {
    if (this.question.possibleAnswers) {
      const [firstAnswer, secondAnswer, thirdAnswer, fourthAnswer] =
        this.question.possibleAnswers;
      this.firstAnswer = firstAnswer
        ? firstAnswer
        : { text: null, isCorrect: null };
      this.secondAnswer = secondAnswer
        ? secondAnswer
        : { text: null, isCorrect: null };
      this.thirdAnswer = thirdAnswer
        ? thirdAnswer
        : { text: null, isCorrect: null };
      this.fourthAnswer = fourthAnswer
        ? fourthAnswer
        : { text: null, isCorrect: null };
    }
  },
  emits: ["update:question"],
  methods: {
    submit() {
      let possibleAnswersArray = Array();
      if (this.firstAnswer.text) {
        possibleAnswersArray.push({
          text: this.firstAnswer.text,
          isCorrect: this.firstAnswer.isCorrect === "true" ? true : false,
        });
      }
      if (this.secondAnswer.text) {
        possibleAnswersArray.push({
          text: this.secondAnswer.text,
          isCorrect: this.secondAnswer.isCorrect === "true" ? true : false,
        });
      }
      if (this.thirdAnswer.text) {
        possibleAnswersArray.push({
          text: this.thirdAnswer.text,
          isCorrect: this.thirdAnswer.isCorrect === "true" ? true : false,
        });
      }
      if (this.fourthAnswer.text) {
        possibleAnswersArray.push({
          text: this.fourthAnswer.text,
          isCorrect: this.fourthAnswer.isCorrect === "true" ? true : false,
        });
      }
      this.$emit("update:question", {
        title: this.question.title,
        text: this.question.text,
        image: this.image,
        position: this.question.position,
        possibleAnswers: possibleAnswersArray,
      });
    },
  },
};
</script>
