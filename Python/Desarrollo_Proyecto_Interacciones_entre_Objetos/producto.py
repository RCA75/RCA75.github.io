class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    def set_stock(self, cantidad):
        self.__stock = max(0, cantidad)  # No permite stock negativo

    def __str__(self):
        return f"Nombre: {self.__nombre}, Precio: ${self.__precio}, Stock: {self.__stock}"
