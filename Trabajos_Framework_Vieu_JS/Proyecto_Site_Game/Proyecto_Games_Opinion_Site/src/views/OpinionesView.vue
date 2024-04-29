<template>
  <div class="container opinionesView">
    <h1 class="text-center">Lista de opiniones</h1>
    <div v-if="opiniones.length === 0" class="alert alert-danger" role="alert">
      No existen opiniones por mostrar
    </div>
    <ul>
      <OpinionListado
        v-for="(opinion, $index) in opiniones"
        :key="$index"
        :nombre="opinion.nombre"
        :titulo="opinion.titulo"
        :opinion="opinion.opinion"
      />
    </ul>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import OpinionListado from '@/components/OpinionListado.vue'
export default {
  name: 'OpinionesView',
  components: { OpinionListado },
  computed: {
    ...mapState('opiniones', {
      opiniones: (state) => state.listado
    })
  }
}
</script>

<style scoped>
.opinionesView {
  margin-top: 2rem;
}
</style>