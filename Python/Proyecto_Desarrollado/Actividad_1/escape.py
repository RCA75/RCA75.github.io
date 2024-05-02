import math

# Ingreso de los Datos Solicitados
radio = float(input('Ingrese el radio (r) en km : '))
gravedad = float(input('Ingrese la Gravedad (g) : '))
	
#Calculo Velocidad de Escape
r_metros = (radio * 1000)       # Aqui Convertierto el radio de kilómetros a metros
Ve = math.sqrt(2 * gravedad * r_metros)

#Entrega de Respuesta
print(f'La velocidad de Escape es {Ve:.1f} [m/s]')
	


