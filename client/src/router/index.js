import Vue from 'vue';
import Router from 'vue-router';
import Match from '../components/Match.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/match',
      name: 'Match',
      component: Match,
    },
  ],
});
