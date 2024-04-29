import Vue from 'vue'
import Vuex from 'vuex'

import { juegosModule } from '@/store/modules/juegos'
import { opinionesModule } from '@/store/modules/opiniones'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: {
    juegos: juegosModule,
    opiniones: opinionesModule
  }
})