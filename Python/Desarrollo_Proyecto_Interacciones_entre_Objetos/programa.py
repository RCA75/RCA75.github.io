from tienda import Tienda
from producto import Producto

def main():
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))

    tienda = Tienda(nombre_tienda, costo_delivery)

    while True:
        print("\n1. Ingresar producto")
        print("2. Listar productos")
        print("3. Realizar venta")
        print("4. Salir")

        opcion = input("\nIngrese la opción deseada: ")

        if opcion == "1":
            nombre_producto = input("Nombre del producto: ")
            precio_producto = float(input("Precio del producto: "))
            stock_producto = int(input("Stock del producto (opcional): ") or 0)

            producto = Producto(nombre_producto, precio_producto, stock_producto)
            tienda.ingresar_producto(producto)
            print("Producto ingresado correctamente.")

        elif opcion == "2":
            print("\nProductos en la tienda:")
            print(tienda.listar_productos())

        elif opcion == "3":
            nombre_producto = input("Nombre del producto a vender: ")
            cantidad = int(input("Cantidad a vender: "))

            tienda.realizar_venta(nombre_producto, cantidad)

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
 