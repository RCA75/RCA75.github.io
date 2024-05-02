# Autor: Reinaldo Carocca
#Solicito al usuario el peso (Kg) y la altura (Cm)
peso = float(input("\n Ingrese el peso en Kg: "))
altura = float(input(" Ingrese la altura en centímetros: "))

#Convierto la altura de centímetros a metros
altura_metros = altura / 100  

#Calculo del indice IMC
imc = peso / (altura_metros ** 2)

#Redondeo el resultado a 2 decimales
imc = round(imc, 2)

#Clasificación del IMC (OMS)
if imc < 18.5:
    clasificacion = "Bajo Peso"
elif 18.5 <= imc < 25:
    clasificacion = "Adecuado"
elif 25 <= imc < 30:
    clasificacion = "Sobrepeso"
elif 30 <= imc < 35:
    clasificacion = "Obesidad Grado I"
elif 35 <= imc < 40:
    clasificacion = "Obesidad Grado II"
else:
    clasificacion = "Obesidad Grado III"

#Entrego el resultado al usuario
print(f"\n Su IMC es: {imc}")
print(f"\n Clasificación de IMC según la OMS: {clasificacion} \n")
