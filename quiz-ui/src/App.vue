<script setup>
import { RouterView } from "vue-router";
import Headers from "./views/Header.vue";
</script>

<template>
  <Headers />
  <div class="bg-image my-auto">
    <RouterView />
  </div>
</template>
     