<template>
  <div class="container administracionView">
    <h1 class="text-center">Administrar la Lista de Opiniones</h1>
    <OpinionTable />
  </div>
</template>

<script>
import OpinionTable from '@/components/OpinionTable.vue'
export default {
  name: 'AdministracionView',
  components: { OpinionTable }
}
</script>

<style scoped>
.administracionView {
  margin-top: 2rem;
}
</style>