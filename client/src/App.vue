<template>
  <div id="app">
    <div class="background">
      <div class="container">
        <div class="col-12 mx-auto black-border border-radius-15">
          <navigation></navigation>
        </div>
      </div>
      <router-view/>
    </div>
  </div>
</template>

<script>

import Navigation from './components/Navigation.vue';

export default {
  name: 'App',
  components: {
    Navigation,
  },
};

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#copyright {
  text-align: right;
  color: rgba(0, 0, 0, 0.5);
}

html {
  overflow-y: scroll;
}

.background {
  background: url('assets/tenniscourt.jpg') no-repeat center center / cover
}

.invisible {
  visibility: hidden !important;
}

.black-border {
  background: white;
  border: 2px solid black !important;
}

.border-radius-15 {
  border-radius: 15px !important;
}

.row {
  margin: 10px;
  padding: 10px;
}

.card-text {
  text-align: left;
}

.large {
  font-size: 125%;
  margin: 0px;
  width: 100%;
}

.td-right {
  text-align: right;
}

</style>
