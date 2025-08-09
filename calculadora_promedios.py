nombres = []
calificaciones = []


def ingresar_calificaciones():
    """
    Método que permite ingresar datos
    :return: listas creadas
    """
    nombres.append(obtener_materia())
    calificaciones.append(obtener_calificacion())

    if (input("Desea seguir introduciendo materias? (s/n)") == "s"):
        ingresar_calificaciones()

    return nombres, calificaciones


def obtener_materia():
    """
    Método que permite obtener el nombre de la materia controlando que no sea vacío
    :return: materia introducida
    """
    materia = input("Introduce el nombre de la materia")

    if(materia == ""):
        print("El nombre de la materia es incorrecto")
        return obtener_materia()
    else:
        return materia


def obtener_calificacion():
    """
    Permite obtener una calificacion, verifica que sea un número entre 1 y 10
    :return: calificacion introducida
    """
    try:
        calificacion = int(input("Introduce la calificacion"))
        if (calificacion >= 0 and calificacion <= 10):
            return calificacion
        else:
            print("La calificacion debe estar entre 0 y 10")
            return obtener_calificacion()
    except:
        print("La calificacion debe ser un número")
        return obtener_calificacion()


def calcular_promedio(calificaciones):
    """
    Calcula el promedio de las calificaciones recibidas por parámetro
    :param calificaciones: calificaciones de las que se hará el promedio
    :return: promedio de las calificaciones
    """
    suma = 0
    for calificacion in calificaciones:
        suma += calificacion
    return suma / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    """
    Permite calcular el estado de las materias (aprobada o reprobada) en base a un umbral
    :param calificaciones: calificaciones sobre las que se desea verificar si están reprobadas o no
    :param umbral: umbral que determina el aprobado, por defecto será 5
    :return: dos listas, primero aprobadas y después reprobadas
    """
    aprobadas = []
    reprobadas = []
    for indice in range(0, len(calificaciones)):
        if calificaciones[indice] >= umbral:
            aprobadas.append(nombres[indice])
        else:
            reprobadas.append(nombres[indice])

    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    """
    Busca el indice de la mayor y menor nota en la lista proporcionada
    :param calificaciones: calificaciones que se comprobaran
    :return: indice de la nota más baja e indice de la nota más alta
    """
    baja = 10
    indice_baja = None
    alta = 0
    indice_alta = None
    for indice in range(0, len(calificaciones)):
        if calificaciones[indice] >= alta:
            alta = calificaciones[indice]
            indice_alta = indice

        if calificaciones[indice] <= baja:
            baja = calificaciones[indice]
            indice_baja = indice

    return indice_baja, indice_alta

if __name__ == "__main__":
    materias, notas = ingresar_calificaciones()
    print("materias: ", materias)
    print("notas: ", notas)
    print("Promedio: ", calcular_promedio(notas))
    aprobadas, reprobadas = determinar_estado(calificaciones)
    print("aprobadas: ", aprobadas)
    print("reprobadas: ", reprobadas)
    baja, alta = encontrar_extremos(calificaciones)
    print("Extremos: ")
    print("Nota más baja: ", nombres[baja], "(", calificaciones[baja], ")")
    print("Nota más alta: ", nombres[alta], "(", calificaciones[alta], ")")
