class Producto:
    """Clase que encapsula la informacion de un producto"""
    def __init__(self, nombre, precio, cantidad):
        """Constructor de la clase Producto

        Argumentos:
        nommbre: Nombre del producto
        precio: Precio del producto
        cantidad: Cantidad del producto
        """
        if (not isinstance(nombre, str) or nombre == ""):
            raise TypeError("Nombre inválido")
        if ((not isinstance(precio, float) and not isinstance(precio, int)) or precio < 0):
            raise TypeError("Precio inválido")
        if (not isinstance(cantidad, int) or cantidad < 0):
            raise TypeError("Cantidad inválida")

        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        """Actualiza la precio del producto si este es positivo"""
        if (nuevo_precio >= 0):
            self.precio = nuevo_precio
        else:
            raise TypeError("Precio inválido")

    def actualizar_cantidad(self, nueva_cantidad):
        """Actualiza la cantidad del producto si es positiva"""
        if (nueva_cantidad >= 0):
            self.cantidad = nueva_cantidad
        else:
            raise TypeError("Cantidad inválida")

    def calcular_valor_total(self):
        """Calcula el valor total del producto teniendo en cuenta su cantidad"""
        return self.precio * self.cantidad

    def __str__(self):
        """Retorna el string del producto"""
        return "Producto: " + self.nombre + " Precio unitario: " + str(self.precio) + " Cantidad: " + str(self.cantidad)


class Inventario:
    """Clase que encapsula la informacion de un inventario"""

    def __init__(self):
        """Constructor de la clase Inventario

        Genera una lista vacía de productos
        """
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un producto"""
        if(isinstance(producto, Producto)):
            self.productos.append(producto)
        else:
            raise TypeError("Se ha proporcionado un objeto que no es un producto")

    def buscar_producto(self, nombre):
        """Busca un producto"""
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def calcular_valor_inventario(self):
        """Calcula el valor total del inventario"""
        return sum(list(map(lambda x: x.calcular_valor_total(), self.productos)))

    def listar_productos(self):
        """Lista todos los productos"""
        return list(map(lambda x: str(x), self.productos))


def menu_principal(inventario):
    """Metodo principal que inicializa el menu"""
    opt = -1
    while (opt != 0):
        opt = levantar_menu(["Agregar producto", "Buscar producto", "Calcular valor inventario", "Listar productos"])
        if opt == 0:
            print("Hasta otra!")
        elif opt == 1:
            inventario.agregar_producto(crear_producto())
        elif opt == 2:
            nombre = input("Nombre del producto: ")
            if (nombre == ""):
                print("Debe introducir un nombre")
            else:
                producto = inventario.buscar_producto(nombre)
                if(producto == None):
                    print("No existe el producto")
                else:
                    print(producto)
                    subopt = -1
                    while (subopt != 0):
                        subopt = levantar_menu(["Actualizar precio", "Actualizar cantidad"])
                        if subopt == 1:
                            producto.actualizar_precio(introducir_precio())
                        if subopt == 2:
                            producto.actualizar_cantidad(introducir_cantidad())


        elif opt == 3:
            print(inventario.calcular_valor_inventario())
        elif opt == 4:
            productos = inventario.listar_productos()
            if(productos):
                for producto in productos:
                    print(producto)
            else:
                print("El inventario está vacío")
        else:
            print("Opcion no válida")


def crear_producto():
    print("Insertar datos de producto")

    nombre = ""
    while (nombre == ""):
        nombre = input("Ingrese nombre: ")
        if (nombre == ""):
            print("Nombre inválido")

    precio = introducir_precio()

    cantidad = introducir_cantidad()

    return Producto(nombre, precio, cantidad)

def introducir_precio():
    precio = -0.1
    while (precio < 0.0):
        try:
            precio = float(input("Ingrese precio: "))

            if (precio >= 0.0):
                return precio

            print("Precio inválido")
        except ValueError:
            print("Debe introducir un número")
            precio = -0.1

def introducir_cantidad():
    cantidad = -1
    while (cantidad < 0):
        try:
            cantidad = int(input("Ingrese cantidad: "))

            if (cantidad >= 0):
                return cantidad

            print("Debe introducir un número")
        except ValueError:
            print("Entrada invalida")
            cantidad = -1
    return cantidad

def levantar_menu(opciones):
    """Metodo levanta el menu con las opciones proporcionadas, la opción 0 siempre será para abandonar el menú"""

    opt = -1
    while (opt != 0):
        for indice, valor in enumerate(opciones):
            print(str(indice+1) + ": " + valor)
        print("0 - Salir")
        try:
            opt = int(input())
            if opt < len(opciones) + 1:
                return opt
            else:
                print("Opcion no válida")
        except ValueError:
            print("Opcion no válida")
        except TypeError:
            print("Entrada inválida")

if __name__ == "__main__":
    menu_principal(Inventario())
