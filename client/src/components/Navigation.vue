<template>

<div id="nav">
  <nav class="container navbar navbar-expand-lg navbar-light">
      <a class="navbar-brand" href="https://github.com/cronholmrickard/flask-vue-martingale-tennis"><i class="bi bi-github"></i></a>
      <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <div class="navbar-nav mr-auto">
          <router-link to="/" class="nav-item nav-link">
              Home
          </router-link>
          <router-link to="/Upload" class="nav-item nav-link">
              Upload tournament
          </router-link>
          </div>
      </div>
      <span id="copyright">Rickard Cronholm, 2022</span>
      </nav>
  </div>

</template>

<script>

export default {
  name: 'Navigation',
};

</script>
