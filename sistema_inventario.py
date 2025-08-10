class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return "Producto: " + self.nombre + "Precio unitario: " + str(self.precio) + "Cantidad: " + str(self.cantidad)


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

    def calcular_valor_inventario(self):
        return sum(list(map(lambda x: x.calcular_valor_total(), self.productos)))

    def listar_productos(self):
        return list(map(lambda x: str(x), self.productos))


def menu_principal(inventario):
    opt = -1
    while (opt != 0):
        print("Elija una opción:")
        print("1 - Agregar producto")
        print("2 - Buscar producto")
        print("3 - Calcular valor inventario")
        print("4 - Listar productos")
        print("0 - Salir")
        try:
            opt = int(input())
            if opt == 0:
                print("Hasta otra!")
            elif opt == 1:
                print("TODO")
            elif opt == 2:
                print("TODO")
            elif opt == 3:
                print(inventario.calcular_valor_inventario())
            elif opt == 4:
                productos = inventario.listar_productos()
                for producto in productos:
                    print(producto)
            else:
                print("Opcion no valida")
        except:
            print("Opcion no valida")


if __name__ == "__main__":
    menu_principal(Inventario())
