import Vue from 'vue'
import VueRouter from 'vue-router'

import HomeView from '../views/HomeView.vue'
import AdministracionView from '../views/AdministracionView.vue'
import OpinionesView from '../views/OpinionesView.vue'
import NotFoundView from '../views/NotFoudView.vue'
import EditarOpinionView from '../views/EditarOpinionView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/opiniones',
    name: 'opiniones',
    component: OpinionesView
  },
  {
    path: '/administracion',
    name: 'administracion',
    component: AdministracionView
  },
  {
    path: '/administracion/:id',
    name: 'EditarOpinion',
    component: EditarOpinionView
  },
  {
    path: '*',
    name: 'NotFound',
    component: NotFoundView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router