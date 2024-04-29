<template>
  <div>
    <h1>Listado de peleadores</h1>
    <ul>
      <li
        v-for="peleador in peleadores"
        :key="peleador.id"
        @click="findPeleadores(peleador.id)"
      >
        {{ peleador.nombre }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data: () => ({
    peleadores: [],
  }),
  created() {
    fetch("/peleadores.json")
      .then((res) => res.json())
      .then((data) => {
        this.peleadores = data;
      });
  },
  methods: {
    findPeleadores(id) {
      this.$router.push(`/list/${id}`);
    },
  },
};
</script>

<style>
li {
  cursor: pointer;
}
</style>
