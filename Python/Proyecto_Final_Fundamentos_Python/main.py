# Autor: Reinaldo Carocca

from modulos import html_template as ht
from modulos import request as rq
from modulos import export as go

#Petición a la API
response = rq.request_get('https://aves.ninjas.cl/api/birds')

#Almaceno la respuesta de la solicitud HTTP a la URL especificada
payload_card = ""

#Itero sobre cada elemento en la respuesta
for d in response :
    #Uso la plantilla HTML ht.card para generar una tarjeta HTML
    payload_card = payload_card + ht.card.substitute(
        name_es = d['name']['spanish'],
        name_en = d['name']['english'],
        img_large = d['images']['full']
    )
#Utilizo la plantilla HTML ht.index para crear la página de inicio 
payload_index = ht.index.substitute(card = payload_card)

#Exporto la pagina index.html generada
go.export(payload_index)
