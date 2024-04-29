<template>
  <form @submit.prevent="editarOpinionBoton" class="container mt-5">
    <div class="form-group">
      <h2>{{ opiniones[$route.params.id].titulo }}</h2>
      <label>Nombre</label>
      <input
        v-model="nombreOpinion"
        :placeholder="opiniones[$route.params.id].nombre"
        type="text"
        class="form-control"
        required
      />
    </div>
    <div class="form-group">
      <label>Opiniones</label>
      <textarea
        v-model="textoOpinion"
        :placeholder="opiniones[$route.params.id].opinion"
        class="form-control"
        rows="3"
        required
      ></textarea>
    </div>
    <button @click="volver" type="button" class="btn btn-secondary">Volver</button>
    <button type="submit" class="ml-2 btn btn-primary">Editar</button>
  </form>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  data: () => ({
    nombreOpinion: '',
    textoOpinion: ''
  }),
  methods: {
    ...mapActions('opiniones', ['editarOpinion']),
    volver() {
      this.$router.push(`/administracion`)
    },
    editarOpinionBoton() {
      this.editarOpinion([
        { id: this.$route.params.id },
        {
          titulo: this.opiniones[this.$route.params.id].titulo,
          nombre: this.nombreOpinion,
          opinion: this.textoOpinion
        }
      ])
      this.$router.push(`/administracion`)
    }
  },
  computed: {
    ...mapState('opiniones', {
      opiniones: (state) => state.listado
    })
  }
}
</script>

<style></style>