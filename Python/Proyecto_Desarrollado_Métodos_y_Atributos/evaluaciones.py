#Importo la Clase y Lista de Ingredientes
from pizza import Pizza
from ingredientes import proteicos, vegetales, masas

#Muestro en pantalla los atributos de clase, sin crear instancia en ella (Punto a)
print("Atributos de la clase Pizza:")
print("Ingredientes posibles:", Pizza().ingredientes)
print("Estado de validez:", Pizza().es_valida)
print()

#Verifico si "salsa de tomate" está presente en la lista de ingredientes usando un método de la clase pizza (Punto b)
print("¿La salsa de tomate está presente en la lista?")
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))
print()

#Creo una instancia de la clase (Pizza) y llamo al método (hacer_pedido) para tomar un pedido de pizza (Punto c)
pizza_pedido = Pizza()
pizza_pedido.hacer_pedido()

#Muestro en pantalla ingredientes y masa de la pizza pedida, así como si es válida o no. (Punto d)
print("Ingredientes de la pizza:")
print("Proteico:", pizza_pedido.ingredientes["proteico"])
print("Vegetal 1:", pizza_pedido.ingredientes["vegetal1"])
print("Vegetal 2:", pizza_pedido.ingredientes["vegetal2"])
print("Masa:", pizza_pedido.ingredientes["masa"])
print("¿Es una pizza válida?:", pizza_pedido.es_valida)
print()

#Verifico si la clase (Pizza) es válida sin crear instancia, mostrando el valor del atributo (es_valida). (Punto e)
print("¿La clase Pizza es una pizza válida?")
print(Pizza().es_valida)

