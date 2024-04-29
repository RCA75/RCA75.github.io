<template>
  <nav class="navbar navbar-light bg-light">
    <div class="logo">
      <a class="navbar-brand" href="#">
        <img
          src="https://www.weplay.cl/pub/media/logo/stores/1/logo_weplay_2.png"
          width="200"
          class="d-inline-block align-top"
          alt=""
        />
      </a>
    </div>
    <div class="navbar-collapse" id="navbarNav">
      <ul class="navbarnav">
        <li class="nav-item item">
          <router-link class="nav-link" to="/">
            <i class="fa fa-home" aria-hidden="true"></i>
          </router-link>
        </li>
        <li class="nav-item item">
          <router-link class="nav-link" to="/juegos">
            <i class="fa fa-gamepad" aria-hidden="true"></i>
          </router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {}
</script>

<style>
.navbarnav {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  list-style: none;
  font-size: 40px;
}
.logo {
  width: 100%;
  display: flex;
  justify-content: center;
}
</style> 
