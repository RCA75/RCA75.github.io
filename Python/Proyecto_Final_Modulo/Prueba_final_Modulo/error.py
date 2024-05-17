#Autor: Reinaldo Carocca

#Defini la clase base para las excepciones personalizadas
class Error(Exception): 
    pass 

class SubTipoInvalidoError(Error):
    def __init__(self, mensaje="El subtipo proporcionado no es válido para este tipo de anuncio"):
        #Mensaje de error predeterminado
        self.mensaje = mensaje
        #Llamo al constructor de la clase base con el mensaje de error
        super().__init__(self.mensaje)
        
        
class LargoExcedidoException(Error):
    def __init__(self, mensaje="El Nombre excede el largo permitido (250 caracteres)"):
        #Mensaje de error predeterminado
        self.mensaje = mensaje
        #Llamo al constructor de la clase base con el mensaje de error
        super().__init__(self.mensaje)