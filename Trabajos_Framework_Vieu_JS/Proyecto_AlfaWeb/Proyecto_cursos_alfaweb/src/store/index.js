import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    cursosDB: [],
    logOutBtn: false,
  },
  mutations: {
    FETCH_CURSOS(state, cursos){
      state.cursosDB = cursos
    },
    LOG_OUT(state, show){
      state.logOutBtn = show
    },
  },
  actions: {
  },
  modules: {
  }
})
