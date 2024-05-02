# Autor: Reinaldo Carocca

import requests
import json

#Defino la función que toma la URL y devuelve los datos JSON obtenidos de esa URL
def request_get(url):
    return json.loads(requests.get(url).text)


if __name__ == "__main__":
    #Realizo prueba con un limite en la respuesta a 10 elementos de los 216
    response = request_get("https://aves.ninjas.cl/api/birds")[:10]
    print(response)
