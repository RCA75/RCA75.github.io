<template>
  <div>
    
    <div v-if="peleador">
      <h1>¡Peleador encontrado!</h1>
      <p>ID: {{peleador.id}}</p>
      <p>Nombre: {{peleador.nombre}}</p>
      <img :src="peleador.imgSrc" alt="">
    </div>

    <div v-if="!peleador">
      <h1>El peleador que buscas no existe 😓 </h1>
      <h1>Esta página no existe 😕</h1>
    </div>
  </div>
</template>

<script>
export default {
  data: ()=>({
   peleador:""
  }), 
  created() {
    const idPeleador= this.$route.params.id
    fetch("/peleadores.json")
      .then((res) => res.json())
      .then((data) => {
        this.peleador = data.find((item)=> (
          item.id == idPeleador
        ));
      });
  },
}
</script>