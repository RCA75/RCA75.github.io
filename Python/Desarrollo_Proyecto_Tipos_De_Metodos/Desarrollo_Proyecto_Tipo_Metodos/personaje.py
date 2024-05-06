#Autor: Reinaldo Carocca 

import random

#Creación de Clase con su constructor
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    # Definimos los métodos para obtener y actualizar estado personaje
    def get_estado(self):
        return f"{self.nombre}: Nivel {self.nivel}, Experiencia {self.experiencia}"

    def set_estado(self, experiencia):
        self.experiencia += experiencia
        if self.experiencia < 0:
            self.experiencia = 0
        while self.experiencia >= 100:
            self.nivel += 1
            self.experiencia -= 100
            
    # Sobrecargamos los operadores < y > para comparar personajes por nivel.
    def __lt__(self, other):
        return self.nivel < other.nivel

    def __gt__(self, other):
        return self.nivel > other.nivel

    # Método opcional para calcular la probabilidad de ganar contra otro personaje
    def calcular_probabilidad_ganar(self, otro_personaje):
        if self == otro_personaje:
            return 0.5
        elif self < otro_personaje:
            return 0.33
        else:
            return 0.66

    # Método opcional para mostrar el diálogo de enfrentamiento con el orco y obtener la opción del jugador
    def enfrentamiento_orco(self):
        probabilidad_ganar = self.calcular_probabilidad_ganar(Orco())
        print(f"¡Ha aparecido un orco! Probabilidad de ganar: {probabilidad_ganar * 100}%")
        print("Si ganas, obtendrás 50 puntos de experiencia y el orco perderá 30. Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        opcion = input("¿Qué quieres hacer? (1: Atacar, 2: Huir): ")
        return opcion

class Orco(Personaje):
    def __init__(self):
        super().__init__("Orco")
        self.nivel = random.randint(1, 10)  # Nivel aleatorio para el orco

# Etapa prueba de Ingreso personaje
if __name__ == "__main__":
    jugador = Personaje(input("¡Bienvenido! Ingresa el nombre de tu personaje: "))
    print(jugador.get_estado())
    opcion = jugador.enfrentamiento_orco()
    print(opcion)
