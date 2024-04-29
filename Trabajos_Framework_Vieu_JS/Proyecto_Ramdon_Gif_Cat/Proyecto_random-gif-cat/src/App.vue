<template>
  <div id="app" class="container text-center">
    <div class="row">
      <div class="col bg-title p-5">
        <h1>Desafio Evaluado Random Gif Cat</h1>
      </div>
    </div>
    <div class="row bg-form p-5">
      <div class="col">
        <form>
          <div class="input-group m-2">
            <label class="input-group-text">Titulo: </label>
            <input type="text" class="form-control" v-model="title"/>
          </div>
          <div class="input-group m-2">
            <label for="" class="input-group-text">Filtro</label>
            <select class="form-select" v-model="filter">
              <option value="blur">blur</option>
              <option value="mono">mono</option>
              <option value="sepia">sepia</option>
              <option value="negative">negative</option>
              <option value="paint">paint</option>
              <option value="pixel">pixel</option>
            </select>
          </div>
          <div>
            <div class="col-8 input-group m-2">
            <label class="input-group-text">Color</label>
            <select class="form-select" v-model="color">
              <option value="red">rojo</option>
              <option value="blue">azul</option>
              <option value="green">verde</option>
              <option value="yellow">amarillo</option>
              <option value="black">negro</option>
              <option value="white">blanco</option>
            </select>
            <div class="circle-color col-4" :style="{backgroundColor: color}"></div>
            </div>
          </div>
          <div class="input-group m-2">
            <label class="input-group-text">Tamaño</label>
            <input type="number" class="form-control" v-model.number="size" step="100" min="100" max="500"/>
          </div>
        </form>
      </div>
    </div>
    <div class="row bg-title">
      <div class="col-12 p-3">
        <button class="btn btn-primary" @click="gatosData">Obtener mi gatito</button>
      </div>
      <div class="col-12 p-5">
        <img :src="gatosGif" alt="">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  data: () => ({
    title: "",
    filter: "",
    color: "",
    size: "",
    gatosGif: ""
  }),
  methods: {
    gatosData() {
      this.gatosGif = `https://cataas.com/cat/gif/says/${this.title}?filter=${this.filter}&color=${this.color}&size=${this.size}&type=or`
    }
  },
};
</script>

<style>
.bg-title {
  background-color: lightblue;
}
.bg-form {
  background-color: lightcoral;
}
.circle-color {
  background-color: red;
  width: 50px;
  height: 50px;
  border-radius: 50% !important;
  margin-left: 1rem !important;
}
</style>