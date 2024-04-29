<template>
  <div class="bg-dark">
    <nav class="container navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="#">Games Opinion</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/"><i class="fas fa-home"></i> Home </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/opiniones">
              <i class="fas fa-comments"></i> Opiniones
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/administracion">
              <i class="fas fa-users-cog"></i> Administracion
            </router-link>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
export default {}
</script>

<style></style>