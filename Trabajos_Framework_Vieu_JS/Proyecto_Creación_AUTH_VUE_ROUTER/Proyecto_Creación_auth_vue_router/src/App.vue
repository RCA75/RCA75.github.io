<template>
  <v-app>
    <ToolBar />
    <router-view />
  </v-app>
</template>

<script>
import ToolBar from "./components/ToolBar.vue";

export default {
  components: { ToolBar },
};
</script>
