// Creación clases solicitada (punto 2)
class Multimedia{
    constructor(url){
        let _url = url;
        this.getUrl = () => _url;
    } //se protege atributo implementando Closures(punto 2.1)
    get url(){
        return this.getUrl();
    }
    //Método que retorna mensaje definido (punto 2.2)
    setInicio(){
        return 'Este método es para realizar un cambio en la URL del video'
    }
};
// Creación clase solicitada (punto 3)
class Reproductor extends Multimedia{
    constructor(url, id){
        super(url);
        this._id = id;
    };
    //Método que hace el llamado a la funcion IIFE functionPuntoUno
    playMultimedia(){
        functionPuntoUno.funPublic( this.url, this._id )
    };
    //Metodo que agrega un tiempo de inicio a la URL de la etiqueta iframe, utilizando método setAtribute
    setInicio(tiempo){
        this._id.setAttribute('src',`${ this.url }?start=${ tiempo }`)
    };
};

// Implementación Patrón Módulo mediante IIFE, (punto 1)
let functionPuntoUno = (function(){
    
    //Funcion Privada interior (punto 1.1)
    let funPrivada = ( url, id ) => id.setAttribute('src', url);

    //retorno con funcion publica (punto 1.2)
    return {
        funPublic: ( url, id ) => funPrivada( url, id )
    }
})()

//Llamado a Método setInicio con un parámetro tiempo definido (punto 6)
musica.setInicio(50);

//Instanciar clase reproductor hija con argumento URL e id (punto 4)
let musica = new Reproductor('https://www.youtube.com/embed/HdWw9SksiwQ', iframeMusica);
let pelicula = new Reproductor('https://www.youtube.com/embed/cDfHM5VItrk', iframePelicula);
let serie = new Reproductor('https://www.youtube.com/embed/w3PtsCNz7pU', iframeSerie);

//Invocacion Método play Multimedia para cada instancia creada (punto 5)
musica.playMultimedia();
pelicula.playMultimedia();
serie.playMultimedia();
