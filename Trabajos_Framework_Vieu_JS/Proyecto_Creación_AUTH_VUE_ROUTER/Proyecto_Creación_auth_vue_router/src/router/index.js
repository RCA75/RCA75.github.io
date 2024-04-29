import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import SignUpView from "../views/SignUpView.vue";
import SuccessfulLoginView from "../views/SuccessfulLoginView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "homeview",
    component: HomeView,
  },
  {
    path: "/signup",
    name: "signup",
    component: SignUpView,
  },
  {
    path: "/success",
    name: "success",
    component: SuccessfulLoginView,
    meta: { login: true },
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

import { getAuth } from "firebase/auth";
router.beforeEach((to, from, next) => {
  const auth = getAuth();
  const user = auth.currentUser;
  const authRequired = to.meta.login;
  if (!user && authRequired) {
    next("/");
  } else {
    next();
  }
});
export default router;
