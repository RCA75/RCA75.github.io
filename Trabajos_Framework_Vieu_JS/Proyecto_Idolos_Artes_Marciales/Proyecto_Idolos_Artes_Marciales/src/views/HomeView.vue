<template>
      <section class="bienvenida">
        <Welcome />
    </section>
</template>

<script>
import Welcome from '@/components/Welcome.vue'
export default {
  name: "home",
  components: {Welcome}
};
</script>

<style>
.bienvenida {
  display: flex;
  justify-content: center;
  vertical-align: middle;
  text-align: center;
  margin-top: 10%;
}
</style>
