import Vue from "vue";
import App from "./App.vue";
import router from "./router";

import vuetify from "./plugins/vuetify";
import { initializeApp } from "firebase/app";
const firebaseConfig = {
  apiKey: "AIzaSyAFVxeWdb60A3Zouf9TsiG7B4RnGVUATIc",
  authDomain: "autentificacion-vue-router.firebaseapp.com",
  projectId: "autentificacion-vue-router",
  storageBucket: "autentificacion-vue-router.appspot.com",
  messagingSenderId: "701615589841",
  appId: "1:701615589841:web:54bfef8e05653d833278f0",
};

const app = initializeApp(firebaseConfig);
app;

Vue.config.productionTip = false;

new Vue({
  router,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
