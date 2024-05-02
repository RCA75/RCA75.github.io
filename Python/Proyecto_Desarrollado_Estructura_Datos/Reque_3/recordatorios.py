#Autor: Reinaldo Carocca
#Lista entregada de Datos para Requerimiento
recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
                 ['2021-05-01', "15:00", "No trabajar"],
                 ['2021-07-15', "13:00", "No hacer nada es feriado"],
                 ['2021-09-18', "16:00", "Ramadas"],
                 ['2021-12-25', "00:00", "Navidad"]]

#Agrego un evento el dia 2 de Febrero de 2021 a las 6 AM para “Empezar el Año”
recordatorios.append(['2021-02-02', '06:00', 'Empezar el año'])

#Corrigo el evento del 15 de Julio para que sea el 16 de Julio
for evento in recordatorios:
    if evento[0] == '2021-07-15':
        evento[0] = '2021-07-16'

#Elimino el evento del día del trabajo
for evento in recordatorios:
    if evento[0] == '2021-05-01' and evento[2] == 'No trabajar':
        recordatorios.remove(evento)

#Agrego la cena de Navidad y Cena Año Nuevo cuando corresponda, en horario de 22 hrs.
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

#Ordeno por fecha y hora la lista de recordatorios
recordatorios.sort()

#Imprimo la lista
print(recordatorios)

