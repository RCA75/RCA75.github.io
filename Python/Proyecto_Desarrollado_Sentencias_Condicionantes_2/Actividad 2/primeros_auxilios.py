# Autor Reinaldo Carocca

# Definir los pasos a seguir
pasos = {
    "Estimulos": ["Verificar los Estimulos"],
    "Respira": ["Verificar su respiración."],
    "Administrar ventilación y llamar a ambulancia": ["Colocar respiración al paciente y Llamar a la ambulancia"],
    "Verificar Signos de Vida": ["Comprobar regularmente si hay signos de vida"],
    "Reevaluar Espera de ambulancia": ["Validar si llego ambulancia para traslado"],
    "Administrar compresiones": ["Compresiones cada 5 min. y verificar llegada de ambulancia"],
}
#Aplicación primeros auxilios
print("\n Bienvenido a la aplicación de primeros auxilios.")
print("\n Por favor, sigue los siguientes pasos para manejar la situación de emergencia:")

paso_actual = "Estimulos"
while paso_actual in pasos:
    print("\nPasos a seguir:")
    for instruccion in pasos[paso_actual]:
        print("-", instruccion)

    #Manejo de las respuestas del usuario
    if paso_actual == "Estimulos":
        respuesta = input("\n¿Responde a estímulos? (s/n): ")
        if respuesta.lower() == "s":
            print("\nValorar necesidad de ir al hospital, Termina Proceso")
            break
        else:
            paso_actual = "Respira"
            continue
    elif paso_actual == "Respira":
        respuesta = input("\n¿Respira? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPermitir suficiente respiración, Termina Proceso")
            break
        else:
            paso_actual = "Administrar ventilación y llamar a ambulancia"
            continue
    elif paso_actual == "Administrar ventilación y llamar a ambulancia":
        print("\nAdministrar al paciente ventilación y llamar a la ambulancia.")
        paso_actual = "Verificar Signos de Vida"
        continue
    
    elif paso_actual == "Verificar Signos de Vida":
        respuesta = input("\n¿Hay signos de vida? (s/n): ")
        if respuesta.lower() == "s":
            respuesta = input("\n¿Llegó la ambulancia? (s/n): ")
            if respuesta.lower() == "s":
                print("\nTermina Proceso.")
                break
            else:
                print("\nReevaluar regularmente si se espera a la ambulancia.")
                continue
        else:
            paso_actual = "Administrar compresiones"
            continue
    elif paso_actual == "Administrar compresiones":
        
        respuesta = input("\n¿Llegó la ambulancia? (s/n): ")
        if respuesta.lower() == "s":
            print("\nTermina Proceso.")
            break
        else:
            continue
