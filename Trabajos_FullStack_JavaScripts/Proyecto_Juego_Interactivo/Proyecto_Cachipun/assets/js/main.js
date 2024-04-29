
const opt = () => Math.floor(Math.random()*3); //Función Math.Floor toma solo valor entero y MathRamdon numero aleatorio
let juegos = 0;
const doc = document;

const validar = (arg) => {      //funcion que valida el argumento 
    return !isNaN(parseFloat(arg)) && isFinite(arg);
}

const verdadero = (n) =>{    //funcion flecha que su resultado se guarda en una constante llamada verdadero
    if(validar(n) && n>=0){
        return true;
    }else{
        return false;
    };
}

const btns = doc.querySelectorAll('.btn-group>button');  //Obtengo los eventos asociados a los botones
const disBtns = (vf) => {
    btns.forEach(e => {
        e.disabled = vf;
    });
}

disBtns(true);
const jugada = () => {   //Funcion flecha que valida el valor registrado en la casilla N° de Juegos con boton Jugar
    juegos = doc.getElementById("juegos").value;
    
    if (verdadero(juegos)) {
        do {
            doc.getElementById('jugada').disabled = true;
            disBtns(false);

        } while (juegos === 0);
            doc.getElementById("juegos").value = '';
            doc.getElementById('jugaras').innerHTML = `Jugarás ${juegos} veces`;
            return (juegos);
    } else {
        doc.getElementById("juegos").value = ''
        return alert("Debes ingresar un número valido para Jugar");
    }
}

const selecciona = (jugador) => {  //Criterios de Ingreso de Cantidad de Juegos
    let jug = jugador;
    let PC = opt();

    if (0<juegos){
        let resultado = resul(jug, PC);
        juegos--;
        doc.getElementById('jugaras').innerHTML = `Jugarás ${juegos} veces`;
        doc.getElementById('resultado').innerHTML = ` <h5> ${resultado} </h5>`
    }
    if (juegos === 0) {
        doc.getElementById('jugada').disabled = false;
        disBtns(true);
        doc.getElementById('jugaras').innerHTML = '';
    }
};

const resul = (jug, c) => {                    //Calculo de la Probabilidad de Ganar el Juego
    const j = ["papel", "tijera", "piedra"];
    const v = ["gana", "empata", "pierde"];

    const r = ((jug - c + 2) % 1.5) * 2;

    //Muestro valor en archivo HTML
    return `<h4> Jugador ${v[r]}: </h4> </br> Jugador eligió ${j[jug]} </br> PC eligió ${j[c]}.`;
}






