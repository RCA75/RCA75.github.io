#Autor: Reinaldo Carocca

#Importo la clase Campaña desde el archivo campaña.py
from campaña import Campaña
#Importo la clase Video desde el archivo anuncio.py
from anuncio import Video  
#Importo las clases de excepciones desde archivo error.py
from error import LargoExcedidoException, SubTipoInvalidoError 
try:
    #Creo una instancia de Video
    video = Video(duracion=30, sub_tipo="instream")

    #Creo una instancia de Campaña con un único anuncio de tipo Video
    campaña = Campaña("Campaña de ejemplo", [video])

    #Solicito al usuario un nuevo nombre para la campaña
    nuevo_nombre = input("Ingrese el nuevo nombre para la campaña: ")

    #Solicito al usuario un nuevo subtipo para el anuncio
    nuevo_subtipo = input("Ingrese el nuevo subtipo para el anuncio: ")

    #Se intenta modificar el nombre de la campaña y el subtipo del anuncio
    campaña.nombre = nuevo_nombre
    campaña.anuncios[0].sub_tipo = nuevo_subtipo

except LargoExcedidoException as e:
    #Para el caso de excepción de LargoExcedidoException, añadir el mensaje al archivo error.log
    with open("error.log", "a") as file:
        file.write(str(e) + "\n")

except SubTipoInvalidoError as e:
    #Para el caso de excepción de SubTipoInvalidoError, añadir el mensaje al archivo error.log
    with open("error.log", "a") as file:
        file.write(str(e) + "\n")

except Exception as e:
    #Para el caso de cualquier otra excepción, añadir el mensaje al archivo error.log
    with open("error.log", "a") as file:
        file.write(str(e) + "\n")