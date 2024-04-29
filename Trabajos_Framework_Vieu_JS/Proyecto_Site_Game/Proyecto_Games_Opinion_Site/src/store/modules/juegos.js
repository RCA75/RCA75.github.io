import Axios from 'axios'
export const juegosModule = {
  namespaced: true,
  state: {
    listado: [],
    loading: false
  },
  mutations: {
    SET_LISTADO(state, newListado) {
      state.listado = newListado
    },
    SET_LOADING(state, newLoading) {
      state.loading = newLoading
    }
  },
  actions: {
    async obtenerJuegos(context) {
      context.commit('SET_LOADING', true)
      try {
        const juegos = await Axios.get('/games.json')
        context.commit('SET_LISTADO', juegos.data)
      } catch (error) {
        console.error(error)
      } finally {
        context.commit('SET_LOADING', false)
      }
    }
  }
}