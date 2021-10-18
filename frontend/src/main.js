import Vue from 'vue'
import App from './App.vue'

import ApiUrls from './config/api'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false

// Global API URLs
Vue.prototype.ApiUrls = ApiUrls

Vue.use(ElementUI);
Vue.use(VueAxios, axios)

new Vue({
  render: h => h(App),
}).$mount('#app')
