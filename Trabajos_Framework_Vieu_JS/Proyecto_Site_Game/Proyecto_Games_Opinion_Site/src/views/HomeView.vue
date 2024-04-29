<template>
  <div class="container homeview">
    <CardGame
      v-for="(juego, $index) in juegos"
      :key="$index"
      :index="juego.id"
      :name="juego.name"
      :rating="juego.rating"
      :released="juego.released"
      :updated="juego.updated"
      :background_image="juego.background_image"
    />
  </div>
</template>

<script>
// @ is an alias to /src
import CardGame from '@/components/CardGame.vue'
import { mapState, mapActions } from 'vuex'
export default {
  name: 'HomeView',
  components: { CardGame },
  created() {
    this.obtenerJuegos()
  },
  methods: {
    ...mapActions('juegos', ['obtenerJuegos'])
  },
  computed: {
    ...mapState('juegos', {
      juegos: (state) => state.listado,
      loadingJuegos: (state) => state.loading
    })
  }
}
</script>

<style scoped>
.homeview {
  margin-top: 2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}
</style>