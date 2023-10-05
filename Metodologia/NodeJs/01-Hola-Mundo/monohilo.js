
//vamos a probar mostrar tambien la hora y fecha de la pc

// Importa la biblioteca 'fecha'
const fecha = require('fecha');

// Función para formatear la fecha y hora
function obtenerFechaHoraActual() {
    const fechaActual = new Date();
    return fecha.format(fechaActual, 'YYYY-MM-DD HH:mm:ss');
}


console.log("Hola a toda la cohorte 2022");


var i = 0;
setInterval(function() {
    const formatoFechaHora= obtenerFechaHoraActual();
    console.log('sigo activo --->  '+ formatoFechaHora); 
    i++;
    if( i ===10){
        console.log('llegamos  a un multiplo de 10');
    }
},1000);
console.log("Hola segunda instruccion");