function soyAsincrona (nombre, miCallback) {
    setTimeout(function(){
        console.log('Hola, soy '+ nombre); 
        miCallback();
    },2000);
  
}

function adios(nombre, otroCallback){
    setTimeout(function(){
        console.log('Adios '+ nombre);
        otroCallback();
},2000);
}




console.log('iniciando el proceso ...'); 

soyAsincrona('carlos', function(){
        adios('carlos', function(){
            console.log('terminado el proceso... '); 
        });
   
});
