<template>
  <div id="app">
      <div class="background">
        <router-view/>
      </div>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.background {
  background: url('assets/tenniscourt.jpg') no-repeat center center / cover
}

</style>
