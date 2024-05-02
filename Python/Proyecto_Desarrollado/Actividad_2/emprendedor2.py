
#Aqui Solicito el ingreso de los datos de entrada
print("\nIngrese valores numéricos positivos, sino debera ejecutar de nuevo el programa \n")
Precio = float(input("Ingrese el precio (P) de suscripción: "))
U_normal = int(input("Ingrese el número (Un) de usuarios normales: "))
U_premium = int(input("Ingrese el número (Up) de usuarios premium: "))
Gasto_Total = float(input("Ingrese el gasto total (GT): "))

#Calculo de utilidades considerando los dos tipos de usuarios
utilidades = (((Precio*U_normal) + 1.5)*(Precio*U_premium)) - Gasto_Total

#Aqui Entrego la respuesta de las utilidades al usuario
print("Las utilidades del proyecto son: $" , "{:.0f}".format(utilidades))
