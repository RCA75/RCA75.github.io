from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def get_nombre(self):
        return self.__nombre

    def get_costo_delivery(self):
        return self.__costo_delivery

    def get_productos(self):
        return self.__productos

    def ingresar_producto(self, producto):
        for p in self.__productos:
            if p.get_nombre() == producto.get_nombre():
                p.set_stock(p.get_stock() + producto.get_stock())
                break
        else:
            self.__productos.append(producto)

    def listar_productos(self):
        lista = ""
        for producto in self.__productos:
            if self.__nombre == "Restaurante" or self.__nombre == "Farmacia":
                lista += f"{producto.get_nombre()}, ${producto.get_precio()}\n"
            else:
                stock = producto.get_stock()
                stock_info = f", Pocos productos disponibles ({stock})" if stock < 10 else ""
                lista += f"{producto.get_nombre()}, ${producto.get_precio()}{stock_info}\n"
        return lista

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.__productos:
            if producto.get_nombre() == nombre_producto:
                if self.__nombre == "Farmacia" and cantidad > 3:
                    print("No se puede vender más de 3 unidades en una venta.")
                    return
                if producto.get_stock() >= cantidad:
                    producto.set_stock(producto.get_stock() - cantidad)
                    print(f"Venta realizada: {cantidad} unidades de {nombre_producto}")
                    return
                else:
                    print("No hay suficiente stock para realizar la venta.")
                    return
        print("Producto no encontrado en la tienda.")
