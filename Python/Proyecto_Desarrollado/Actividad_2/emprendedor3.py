
#Aqui Solicito el ingreso de los datos de entrada
print("\nIngrese valores numéricos positivos, sino debera ejecutar de nuevo el programa \n")
Precio = float(input("Ingrese el precio (P) de suscripción: "))
Usuarios = int(input("Ingrese el número (U) de usuarios: "))
Gasto_Total = float(input("Ingrese el gasto total (GT): "))
U_anterior = float(input("Ingrese las utilidades (Ua) del año anterior: "))

#Aqui Calculo las utilidades actuales
utilidades = (Precio*Usuarios) - Gasto_Total

#Aqui Calculo la razón entre las utilidades actuales y las del año anterior
razon_utilidades = (utilidades/U_anterior)

#Aqui Entrego la respuesta de las utilidades y la razón de utilidades al usuario
print("Las utilidades del proyecto son: $", "{:.0f}".format(utilidades))
print("La razón entre las utilidades actuales y las del año anterior es: $", "{:.2f}".format(razon_utilidades))
        