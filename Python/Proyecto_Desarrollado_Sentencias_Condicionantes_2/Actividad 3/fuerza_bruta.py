#Autor Reinaldo Carocca

from string import ascii_lowercase #ascii_lowercase es un string con todas las letras del abecedario

#Solicito al usuario ingresar la contraseña a buscar
password = input("\n Ingrese la contraseña: ")

contar = 0  #Inicio el contador de intentos

#Generación de las combinaciones           
for caracter in password:              #Iteración de la longitudes de combinacion
    for letras in ascii_lowercase:     #Iteración de las letras minúsculas
        contar += 1                    #Aumento del contador de intentos
        if caracter == letras:         #Comprobar si la combinación coincide con parte de la contraseña
            break                      #Salir del programa

print(f'La contraseña fue forzada en {contar} intentos')
