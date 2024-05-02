#Autor: Reinaldo Carocca

class Pizza:
    #Método Especial que se ejecuta automáticamente al crear un objeto de la clase pizza
    def __init__(self):
        self.ingredientes = {"proteico": "", "vegetal1": "", "vegetal2": "", "masa": ""}
        self.es_valida = False

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        return elemento in valores_posibles

    #Defino el método para hacer el pedido
    def hacer_pedido(self):
        print("¡Bienvenido a la pizzería! Vamos a tomar tu pedido.")
        proteico = input("Ingresa el ingrediente proteico (pollo, vacuno, carne vegetal): ")
        vegetal1 = input("Ingresa el primer ingrediente vegetal (tomate, aceitunas, champiñones): ")
        vegetal2 = input("Ingresa el segundo ingrediente vegetal (tomate, aceitunas, champiñones): ")
        masa = input("Ingresa el tipo de masa (tradicional, delgada): ")
        
        #Asigno los ingredientes y la masa a los atributos de la instancia.
        self.ingredientes["proteico"] = proteico
        self.ingredientes["vegetal1"] = vegetal1
        self.ingredientes["vegetal2"] = vegetal2
        self.ingredientes["masa"] = masa

        #Defino las listas de ingredientes y masas posibles.
        proteicos = ["pollo", "vacuno", "carne vegetal"]
        vegetales = ["tomate", "aceitunas", "champiñones"]
        masas = ["tradicional", "delgada"]

        #Verifico si los ingredientes y la masa son válidos utilizando un método llamado validar.elemento()
        if self.validar_elemento(proteico, proteicos) and \
            self.validar_elemento(vegetal1, vegetales) and \
            self.validar_elemento(vegetal2, vegetales) and \
            self.validar_elemento(masa, masas):
            self.es_valida = True
        else:
            self.es_valida = False


