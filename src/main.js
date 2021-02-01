import Vue from 'vue'
import App from './App.vue'
import router from './router/index'
import store from './store/index'
import vuetify from './plugins/vuetify';
import Vuetify from 'vuetify';
import VueSplit from "vue-split-panel";

Vue.config.productionTip = false

Vue.use(Vuetify);
Vue.use(VueSplit);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
