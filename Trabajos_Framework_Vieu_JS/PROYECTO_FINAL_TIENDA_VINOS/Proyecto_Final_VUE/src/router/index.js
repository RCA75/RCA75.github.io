import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/vinos',
    name: 'vinos',
    component: () => import(/* webpackChunkName: "vinos" */ '../views/VinosView.vue')
  },
  {
    path: '/promocion',
    name: 'vinosEnPromocion',
    component: () => import(/* webpackChunkName: "vinosEnPromocion" */ '../views/VinosEnPromocionView.vue')
  },
  {
    path: '/accesorios',
    name: 'accesorios',
    component: () => import(/* webpackChunkName: "accesorios" */ '../views/AccesoriosView.vue')
  },
  {
    path: '/checkout',
    name: 'checkout',
    component: () => import(/* webpackChunkName: "checkout" */ '../views/CheckoutView.vue'),
    children: [{ path: 'confirmed/:orden', name: 'confirmed', props: true, component: () => import(/* webpackChunkName: "confirmed" */ '../views/ConfirmedView.vue'), }]
  },
  {
    path: '*',
    name: 'notFound',
    component: () => import(/* webpackChunkName: "notFound" */ '../views/NotFoundView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
