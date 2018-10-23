// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router/index'
import VueResource from 'vue-resource'
import Router from 'vue-router'
import VueModal from 'vue-js-modal'

Vue.use(VueModal, {dialog: true, injectModalsContainer: true})
Vue.use(VueResource)
Vue.use(Router)

Vue.config.productionTip = false

/* eslint-disable no-new */
const app = new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

VueModal.rootInstance = app
