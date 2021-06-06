import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    alertMessage: null,
    modal: null
  },
  getters: {
    alertMessage: state => state.alertMessage,
    isVisible: state => state.isVisible
  },
  mutations: {
    UPDATE_ALERT_MESSAGE: (state, payload) =>{
      state.alertMessage = payload
    }
  },
  actions: {},
  modules: {},
});
