import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SearchView from '../views/SearchView.vue'
import ListView from '../views/ListView.vue'
import Results from '../views/Results.vue'
import NotFound from '../views/NotFound.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path:'/search',
    name: 'search',
    component: SearchView
  },
  {
  path: '/list',
  name: 'list',
  component: ListView
  },
  {
    path: '/list/:id',
    name: 'results',
    component: Results
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

// this.$route.params.id
