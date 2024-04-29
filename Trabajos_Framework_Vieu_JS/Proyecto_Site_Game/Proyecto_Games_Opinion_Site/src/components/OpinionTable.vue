<template>
  <div>
    <div v-if="opiniones.length === 0" class="alert alert-danger" role="alert">
      No existen opiniones por mostrar
    </div>
    <table v-if="opiniones.length >= 1" class="table table-striped">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Persona</th>
          <th scope="col">Juego</th>
          <th scope="col">Opinion</th>
          <th scope="col">Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(opinion, $index) in opiniones" :key="$index">
          <th scope="row">{{ $index }}</th>
          <td>{{ opinion.nombre }}</td>
          <td>{{ opinion.titulo }}</td>
          <td>{{ opinion.opinion }}</td>
          <td>
            <button @click="eliminarOpinion($index)" class="btn btn-danger">Eliminar</button>
            <button @click="redireccionar($index)" class="btn btn-info ml-2">Editar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  computed: {
    ...mapState('opiniones', {
      opiniones: (state) => state.listado
    })
  },
  methods: {
    ...mapActions('opiniones', ['eliminarOpinion']),
    redireccionar($index) {
      this.$router.push(`/administracion/${$index}`)
    }
  }
}
</script>

<style></style>