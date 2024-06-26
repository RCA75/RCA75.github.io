
//Función estará disponible una vez que carguen todos los elementos del DOM
$(document).ready(function()
{

// Evento del botón que una vez apretado el click() 
// ejecutará la aplicación
$('#btnBuscar').on('click',function(event){

    // Previene el comportamiento por defecto del formulario
    // de recargar la página
    event.preventDefault();

    // Variable para obtener el número que entrega el usuario
    let idHero = $('#numeroHero').val();
        

// Función que ejecuta el programa a través de validaciones con condicionales IF - ELSE
function EjecutarPrograma(){

    // Expresión regular para digitos del 0 al 9
    let regexp = /^[0-9-\s]+$/i;

    // IF-ELSE para validar que el valor ingresado sea un número
    if(regexp.test(idHero) == true){
        // IF-ELSE anidado para validar que el valor ingresado sea 
        // un número entre cero y 732
        // De ser un número válido se llama a la función Buscar()
        if((idHero > 0) && (idHero < 732)){
            Buscar();
        } else {
            alert('Debe ser un número mayor que cero y menor que 732');
        }
    } else {
        alert('Debe ingresar un número.');
    }
}


// Función que hace la petición GET a la API de https://superheroapi.com para conseguir los datos necesarios
function Buscar(){
        // Método AJAX para solicitar los datos
        $.ajax({
            type:"GET",
            url:`https://www.superheroapi.com/api.php/10222364085623839/${idHero}`, //URL con access-token
            dataType:"json",
            success: function(data) {
                console.log(data); //validado que se recibe como data de forma correcta

                // En cada llamada se resetea el renderizador para
                // limpiar los resultados
                $('#containerResultados').empty();
                $("#chartContainer").empty();

                // Se crean y se adjuntan a la vista los datos de la Card
                $('#containerResultados').append(`<div class="card d-flex flex-row me-5" style="width: 100%">
                                                    <div style="width:40%;">
                                                        <img src="${data.image.url}" class="card-img-top" alt="imagen-hero" style="object-fit: cover;width: 100%;height:100%;">
                                                    </div>
                                                    <div style="width:60%;">
                                                        <div class="card-body">
                                                            <h3 class="card-title"><strong>Nombre:</strong> ${data.name}</h3>
                                                        </div>
                                                        <ul class="list-group list-group-flush">
                                                            <li class="list-group-item"><strong>Conexiones:</strong> ${data.connections['group-affiliation']}</li>
                                                            <li class="list-group-item"><strong>Ocupación:</strong> ${data.work.occupation}</li>
                                                            <li class="list-group-item"><strong>Primera Aparición:</strong> ${data.biography['first-appearance']}</li>
                                                            <li class="list-group-item"><strong>Altura:</strong> ${data.appearance.height}</li>
                                                            <li class="list-group-item"><strong>Peso:</strong> ${data.appearance.weight}</li>
                                                            <li class="list-group-item"><strong>Alias:</strong> ${data.biography.aliases}</li>
                                                        </ul>
                                                    </div>
                                                </div>
                 `);


            // Se configuran los datos necesarios para el gráfico de torta                
                let options = new CanvasJS.Chart("chartContainer", {
                    theme: "light",
                    exportEnabled: true,
                    animationEnabled: true,
                    title:{
                        text: `Estadísticas de Poder para ${data.name}`
                    },
                    data: [{
                        type: "pie",
                        toolTipContent: "{name}: <strong>{y}%</strong>",
                        showInLegend: true,
                        indexLabel: "{name} - {y}",
                        dataPoints: [
                            { y: data.powerstats.intelligence, name: "intelligence" },
                            { y: data.powerstats.strength, name: "strength" },
                            { y: data.powerstats.speed, name: "speed" },
                            { y: data.powerstats.durability, name: "durability" },
                            { y: data.powerstats.power, name: "power" },
                            { y: data.powerstats.combat, name: "combat" }
                        ]
                    }]
                });   //Condición de la Validación de Datos de Inteligencia, Fuerza, Velocidad, Durabilidad, Poder y Combate para Reandarizr Grafica requerida. 
                    if(  ((data.powerstats.intelligence) || (data.powerstats.strength) || (data.powerstats.speed) || (data.powerstats.durability) || (data.powerstats.power) || (data.powerstats.combat)) != "null" ) {
                        options.render();
                    }else{
                        document.getElementById('chartContainer').innerHTML='INFORMACION: NO EXISTEN DATOS ESTADISTICOS PARA GENERAR GRAFICA.';
                    }
                 }              
        });
    }
    // Finalmente se llama a la función EjecutarPrograma() para lanzar la aplicación y renderizar la información requerida
    EjecutarPrograma();

    });
});