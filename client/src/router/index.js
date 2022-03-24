import Vue from 'vue';
import Router from 'vue-router';
import Match from '../components/Match.vue';
import Home from '../components/Home.vue';

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
      path: '/match',
      name: 'Match',
      component: Match,
    },
  ],
});
