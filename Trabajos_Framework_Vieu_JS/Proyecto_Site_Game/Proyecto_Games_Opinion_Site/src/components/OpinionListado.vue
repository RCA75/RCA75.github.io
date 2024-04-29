<template>
  <ul class="container mt-3 list-group">
    <li class="list-group-item list-group-item-primary">
      <p>
        <strong>Opinion creada por:</strong> {{ nombre }} <strong>Para el juego:</strong>
        {{ titulo }}
      </p>
    </li>
    <li class="list-group-item">
      <p><strong>Opinion:</strong> {{ opinion }}</p>
    </li>
  </ul>

  <!-- <li class="container opinionListado mt-3 bg-info">
    <div>
      <h3>Opinion creada por: {{ nombre }} para el juego: {{ titulo }}</h3>
    </div>
    <div>
      <p>Opinion: {{ opinion }}</p>
    </div>
  </li> -->
</template>

<script>
export default {
  props: ['nombre', 'titulo', 'opinion']
}
</script>

<style>
.opinionListado {
  padding: 1rem;
  list-style: none;
  border-radius: 1rem;
}

.opinionListado h3 {
  color: blue;
}
</style>