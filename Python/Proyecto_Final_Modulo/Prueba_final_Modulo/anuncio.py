#Autor: Reinaldo Carocca

#Importo la clase de excepcion desde error.py
from error import SubTipoInvalidoError

#Defino la Clase Anuncio
class Anuncio:
    formato={}
    #Defino Atributo de clase sub-tipos, dependiendo del tipo de clase hija (video,display, o social)
    SUB_TIPOS=() 
    
    #Defino el constructor de la clase Anuncio
    def __init__(self,ancho: int, alto: int,url_archivo: str,url_click: str,sub_tipo: str) -> None:
        self.__ancho = ancho
        self.__alto  = alto
        self.__url_archivo= url_archivo
        self.__url_click = url_click
        #Defino e utilizo el setter para validar el subtipo al inicializar el objeto
        self.__sub_tipo = sub_tipo 
    
    
    #Defino el método estático para mostrar los formatos de anuncio disponibles
    @staticmethod
    def mostrar_formatos():
        print("Formatos de anuncio disponibles:")
        print("===============================")
        
        #Muestro los formatos y subtipos de Video
        print("Video:")
        print("------")
        for subtipo in Video.SUB_TIPOS:
            print(f"- {subtipo}")
        
        #Muestro los formatos y subtipos de Display
        print("\nDisplay:")
        print("--------")
        for subtipo in Display.SUB_TIPOS:
            print(f"- {subtipo}")
        
        #Muestro los formatos y subtipos de Social
        print("\nSocial:")
        print("-------")
        for subtipo in Social.SUB_TIPOS:
            print(f"- {subtipo}")

      
    #Defino propiedades de ancho y alto con sus correspondientes setters.
    #Con estos métodos permito acceder y modificar los atributos ancho y alto del objeto Anuncio
    @property
    def ancho(self):
        return self.__ancho
        
    @ancho.setter
    def ancho(self,nuevo_ancho):
        if nuevo_ancho > 0 :
            self.__ancho = nuevo_ancho
        else:
            self.__ancho = 1
                
    @property
    def alto(self):
        return self.__alto
        
    @alto.setter
    def alto(self,nuevo_alto: int):
        if nuevo_alto > 0 :
            self.__alto= nuevo_alto
        else:
            self.__alto = 1     
    
    #Defino propiedades url_archivo y url_click con sus respectivos setters
    #Con estos métodos permito acceder y modificar los atributos url_archivo y url_click del objeto Anuncio
    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @property
    def url_click(self):
        return self.__url_click
    
    @url_archivo.setter
    def url_archivo (self, nuevo_url_archivo: str):
        self.__url_archivo = nuevo_url_archivo
        
    @url_click.setter
    def ulr_click(self, nuevo_url_click: str):
        self.__url_click = nuevo_url_click
    
    #Defino propiedades sub_tipo con su setter correspondiente
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    #Con estos métodos permito acceder y modificar el atributo sub_tipo del objeto Anuncio, 
    #asegurando que el valor asignado sea válido
    @sub_tipo.setter
    def sub_tipo(self, nuevo_sub_tipo: str):
        #Verifico si el nuevo subtipo está en la lista de subtipos del anuncio
        if nuevo_sub_tipo in self.SUB_TIPOS: 
            self.__sub_tipo = nuevo_sub_tipo
        else:
            #Lanzo una excepción si el subtipo no es válido
            raise SubTipoInvalidoError() 

#Defino la clase video, que hereda de la clase base Anuncio       
class Video(Anuncio):
    #Defino formato del anuncio
    FORMATO = "Video"
    #Defino subtipos disponibles para el anuncio de video
    SUB_TIPOS=("instream","outstream") 

    #Defino el constructor __init__ de la clase Video, que inicializa los atributos del objeto Video
    def __init__(self, duracion: int, sub_tipo: str) -> None:
        super().__init__(ancho=1, alto=1, url_archivo="", url_click="", sub_tipo=sub_tipo)
        #Inicializo el atributo duración del video
        self.duracion = duracion 

    #Defino las propiedades duracion con su setter correspondiente
    @property
    def duracion(self):
        return self._duracion

    #Con estos métodos permito acceder y modificar el atributo duracion del objeto Video, 
    #asegurando que el valor asignado sea positivo
    @duracion.setter
    def duracion(self, nueva_duracion):
        if nueva_duracion > 0:
            self._duracion = nueva_duracion
        else:
            #Defino si la duración es negativa o cero,se asigna un valor predeterminado de 5 segundos
            self._duracion = 5 

    #Defino métodos específicos de la clase Video, comprimir_anuncio() y redimensionar_anuncio()
    #No están aun implementadas
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")
    
    #Redefino las propiedades ancho y alto con sus setters correspondientes  
    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, nuevo_ancho):
        #Aqui el setter no hace nada,ignorando cualquier intento de cambiar el valor
        pass  

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, nuevo_alto):
        #Aqui el setter no hace nada,ignorando cualquier intento de cambiar el valor
        pass  
        
        
#Defino la clase Display        
class Display(Anuncio):
    #Defino Formato del Display
    FORMATO = "Display"
    #Defino subtipos disponibles para tradicional y native
    SUB_TIPOS = ("tradicional", "native")
    
    ##Defino métodos específicos de la clase Display, comprimir_anuncio() y redimensionar_anuncio()
    #No están aun implementadas
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")
   
#Defino la clase Social        
class Social(Anuncio):
    #Defino formato de Social
    FORMATO = "Social"
    #Defino subtipos disponibles para facebook y linkedin
    SUB_TIPOS = ("facebook","linkedin")
    
    ##Defino métodos específicos de la clase Social, comprimir_anuncio() y redimensionar_anuncio()
    #No están aun implementadas
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")
        
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
        

        
      
