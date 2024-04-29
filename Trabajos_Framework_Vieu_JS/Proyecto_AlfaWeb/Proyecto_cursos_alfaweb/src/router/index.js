import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import auth from '../authentification'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/cursos',
    name: 'Cursos',
    component: () => import('../views/Cursos.vue'),
    meta: {
      ingresar: true,
    },
  },
  {
    path: '/administracion',
    name: 'Administracion',
    component: () => import('../views/Administracion.vue'),
    meta: {
      ingresar: true,
    },
  },
  {
    path: '/editar/:id',
    name: 'EditarCurso',
    component: () => import('../views/EditarCurso.vue'),
    meta: {
      ingresar: true,
    },
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  let email = auth.currentUser;
  let authRequired = to.matched.some((route) => route.meta.ingresar);
  if (!email && authRequired) {
    next("/");
  } else if (email && !authRequired) {
    next("Cursos");
  } else {
    next();
  }
});

export default router
