
// Clase padre Propietario
class Propietario {
    constructor(nombre, direccion, telefono) {
      this.nombrePropietario = nombre;
      this.direccion = direccion;
      this.telefono = telefono;
    }
    datosPropietario() {
      return `El nombre del dueño es: ${this.nombrePropietario}. El domicilio es: ${this.direccion}, y el numero telefonico de contacto: ${this.telefono}`;
    }
}
  
//Clase Hija Animal que hereda de Propietario
class Animal extends Propietario {
    constructor(nombre, direccion, telefono, tipo) {
      super(nombre, direccion, telefono);
      this._tipo = tipo;
    };
    get tipo() {
      return `El tipo de animal es un: ${this._tipo}`;
    }
}
  
// Clase hija Mascota que ereda de Animal
class Mascota extends Animal {
    constructor(nombre, direccion, telefono, tipo, nombreMascota, enfermedad) {
      super(nombre, direccion, telefono, tipo);
      this._nombreMascota = nombreMascota;
      this._enfermedad = enfermedad;
    }
  
    // Getter nombreMascota
    get nombre() {
      return this._nombreMascota;
    }
    // Setter nombreMascota
    set nombreMascota(_setNombreMascota) {
      this._nombreMascota = _setNombreMascota;
    }
    //Getter enfermedad
    get enfermedad() {
      return this._enfermedad;
    }
    //Setter
    set enfermedad(_setEnfermedad) {
      this._enfermedad = _setEnfermedad;
    }
}
  
  // Captura de inputs
let propietario = document.getElementById('propietario');
let telefono = document.getElementById('telefono');
let direccion = document.getElementById('direccion');
let nombreMascota = document.getElementById('nombreMascota');
let selectorTipo = document.getElementById('tipo');
let enfermedad = document.getElementById('enfermedad');
let form = document.querySelector('form');

let btnEnviar = document.getElementById('btnEnviar');
let resultado = document.getElementById('resultado');

//funcion Dato
const nuevoDato = (propietario) => {
    let addli = document.createElement('li');
    let liData = document.createTextNode(`${propietario.datosPropietario()}.`);
    addli.appendChild(liData);
    resultado.appendChild(addli);
}
//Funcion mascota
const nuevoMascota = (animal) => {
    let addli = document.createElement('li');
    let liData = document.createTextNode(`${animal.tipo}, mientras que el nombre de la mascota  es: ${animal.nombre} y la enfermedad es: ${animal.enfermedad}`);
    addli.appendChild(liData);
    resultado.appendChild(addli);
}

btnEnviar.addEventListener('click', (e) =>{
    e.preventDefault();

    if(selectorTipo.value == 'perro'){
        let perro = new Mascota(propietario.value, direccion.value, telefono.value, selectorTipo.value, nombreMascota.value, enfermedad.value);
        nuevoDato(perro);
        nuevoMascota(perro);
    }
    if(selectorTipo.value == 'gato'){
        let gato = new Mascota(propietario.value, direccion.value, telefono.value, selectorTipo.value, nombreMascota.value, enfermedad.value);
        nuevoDato(gato);
        nuevoMascota(gato);
    }
    if(selectorTipo.value == 'conejo'){
        let conejo = new Mascota(propietario.value, direccion.value, telefono.value, selectorTipo.value, nombreMascota.value, enfermedad.value);
        nuevoDato(conejo);
        nuevoMascota(conejo);
    }
    FormData.reset();
})