import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import QuizPage from "../views/QuizPage.vue";
import QuestionsManager from "../views/QuestionsManager.vue";
import Administration from "../views/Administration.vue";
       
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage,
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/QuestionDisplay.vue"),
    },
    {
      path: "/start-new-quiz-page",
      name: "QuizPage",
      component: QuizPage,
    },
    {
      path: "/questions",
      name: "QuestionsManager",
      component: QuestionsManager,
    },
    {
      path: "/administration",
      name: "Administration",
      component: Administration,
    },
  ],
});

export default router;
