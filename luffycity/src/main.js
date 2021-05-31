// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import settings from "./settings";
import '../static/css/reset.css' /* 引入全局css文件 */
import '../static/js/gt.js' /* 引入全局js文件 */

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from "axios";

// 注册并使用vue-video插件
import 'video.js/dist/video-js.css';
// require('video.js/dist/video-js.css'); 与上一句等同。
import 'vue-video-player/src/custom-theme.css';
// require('vue-video-player/src/custom-theme.css'); 与上一句等同。
import VideoPlayer from 'vue-video-player';


Vue.use(VideoPlayer);
Vue.use(ElementUI);
Vue.config.productionTip = false;
Vue.prototype.$axios = axios; /* 封装axios */
Vue.prototype.$settings = settings; /* 封装settings */


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
