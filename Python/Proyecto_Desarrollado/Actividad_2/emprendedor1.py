
#Aqui Solicito el ingreso de los datos de entrada
print("\nIngrese valores numéricos positivos, sino debera ejecutar de nuevo el programa \n")
Precio = float(input("Ingrese el precio (P) de suscripción: "))
Usuarios = int(input("Ingrese el número (U) de usuarios: "))
Gasto_Total = float(input("Ingrese el gasto total (GT): "))

#Calculo de las utilidades
utilidades = (Precio*Usuarios) - Gasto_Total

#Aqui Entrego la respuesta de las utilidades al usuario
print("Las utilidades del proyecto son: $", "{:.0f}".format(utilidades))
            
