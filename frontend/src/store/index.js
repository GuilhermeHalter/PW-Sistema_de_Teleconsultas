import { createStore } from "vuex"

export default createStore({

  state: {
    usuario: null
  },

  mutations: {
    SET_USUARIO(state, usuario) {
      state.usuario = usuario
    }
  },

  actions: {
    setUsuario({ commit }, usuario) {
      commit("SET_USUARIO", usuario)
    }
  },

  getters: {
    getUsuario: (state) => state.usuario
  }

})