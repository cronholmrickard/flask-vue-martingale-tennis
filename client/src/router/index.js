import Vue from 'vue';
import Router from 'vue-router';
import Play from '../components/Play.vue';
import Upload from '../components/Upload.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Play',
      component: Play,
    },
    {
      path: '/upload',
      name: 'Upload',
      component: Upload,
    },
  ],
});
