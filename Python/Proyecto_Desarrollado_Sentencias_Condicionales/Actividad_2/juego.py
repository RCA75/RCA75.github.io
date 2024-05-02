#Autor: Reinado Carocca

import random

#Usuario debe elegir una opción
opcion_usuario = input("\n Elige piedra, papel o tijera: ")

#Verificar si opción ingresa es válida
opciones_validas = ['piedra', 'papel', 'tijera']

if opcion_usuario.lower() not in opciones_validas:
    print("\n Opción inválida. Debe ser piedra, papel o tijera. \n")
else:
    #Genero elección aleatoriamente del computador
    opcion_computador = random.choice(opciones_validas)
    
    #Muestro Opción seleccionada del computador
    print(f"\n El computador elige: {opcion_computador} \n")

    #Desarrollo del juego
    if opcion_usuario == opcion_computador:
        resultado = "Empate"
    elif (opcion_usuario == 'piedra' and opcion_computador == 'tijera') or \
         (opcion_usuario == 'papel' and opcion_computador == 'piedra') or \
         (opcion_usuario == 'tijera' and opcion_computador == 'papel'):
        resultado = "Ganaste...!!!!!"
    else:
        resultado = "El computador gana \n"

    #Entrego resultado final
    print(f"Resultado: {resultado} \n")
