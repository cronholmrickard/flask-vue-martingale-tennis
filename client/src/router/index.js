import Vue from 'vue';
import Router from 'vue-router';
import Home from '../components/Home.vue';
import Upload from '../components/Upload.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/upload',
      name: 'Upload',
      component: Upload,
    },
  ],
});
