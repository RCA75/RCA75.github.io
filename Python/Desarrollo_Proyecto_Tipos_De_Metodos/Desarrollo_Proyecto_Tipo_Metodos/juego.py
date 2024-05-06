#Autor: Reinaldo Carocca

#Importación de la Clase Personaje y Orco
import random
from personaje import Personaje, Orco

#Creación de la Clase Juego con su metodo __init__ para inicializar el juego 
class Juego:
    def __init__(self):
        self.jugador = None

    #Creación metodo jugar para iniciar el juego
    def jugar(self):
        print("¡Bienvenido a Gran Fantasía!")
        nombre_jugador = input("Ingresa el nombre de tu personaje: ")
        self.jugador = Personaje(nombre_jugador) #Creación personaje Jugador
        print(self.jugador.get_estado())

        #Se llama al método enfrentamiento Orco (Opcional) para dicidir atacar o huir
        opcion = self.jugador.enfrentamiento_orco()

        #Si la opción es atacar (1) se llama al método atacar_orco
        while opcion == "1":
            resultado = self.atacar_orco()
            print(resultado)
            print(self.jugador.get_estado())
            print("Estado del Orco:", Orco().get_estado())

            opcion = self.jugador.enfrentamiento_orco()

        #si la opción es (2) se escapa del orco y termina juego
        if opcion == "2":
            print("Escapaste del orco. ¡Hasta la próxima!")

    #Defino el método de atacar_orco
    def atacar_orco(self):
        probabilidad_ganar = self.jugador.calcular_probabilidad_ganar(Orco())
        resultado = "Pierdes"
        if random.uniform(0, 1) <= probabilidad_ganar:
            self.jugador.set_estado(50)
            resultado = "Ganas"
        else:
            self.jugador.set_estado(-30)
        return f"Resultado del ataque: {resultado}"

# Etapa de Prueba Juego
if __name__ == "__main__":
    juego = Juego()
    juego.jugar()


