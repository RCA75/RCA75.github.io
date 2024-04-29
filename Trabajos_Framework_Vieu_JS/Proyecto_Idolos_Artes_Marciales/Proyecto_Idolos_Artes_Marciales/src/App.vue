<template>
  <div id="app">
 <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <router-link :to="{name:'home'}" class="navbar-brand">Home</router-link>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <router-link :to="{name:'search'}" class="nav-link">Buscador</router-link>
      </li>
      <li class="nav-item active">
        <router-link :to="{name:'list'}" class="nav-link">Lista de peleadores</router-link>
      </li>
    </ul>
  </div>
</nav>
    <router-view/>
  
  </div>
</template>
<script>

export default {
  name: "App",
};
</script>
<style>
</style>