print("Primer ejercicio de matrices")

#Cargar la matriz en forma de función
def cargar_matriz(mat):
    #usar recorrido por filas para cargar la matriz
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            #cargar la cantidad vendida
            cant = int(input("Ingrese la cantidad vendida del vendedor " +
                             str(f) + " del artículo " + str(c) + ": "))
            #asignar el cant en la posición f y c de la matriz
            mat[f][c] = cant

#mostrar cantidad por vendedor
def mostrar_vendedor(mat):
    print("Ventas por cada vendedor")
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print("Vendedor " + str(f) + " y del artículo " + str(c) + ": ",mat[f][c])

#mostrar cantidad por artículo
def mostrar_articulo(mat):
    print("Ventas por cada artículo")
    for c in range(len(mat[0])):
        for f in range(len(mat)):
            print("Vendedor " + str(f) + " y del artículo " + str(c) + ": ",mat[f][c])




#programa principal

def test():
    pass
    #pedir las cantidaddes totales de vendedor y artículo
    n = int(input("Ingrese la cantidad de artículos: "))
    m = int(input("Ingrese la cantidad de vendedores: "))

    #crear la matriz
    #usar la creación compacta. primer valor corresponde a la columna y el
    # segundo la fila
    mat = [[0] * n for f in range(m)]
    #cargar matriz
    cargar_matriz(mat)
    #mostrar la matriz
    print("La matriz cargada es:",mat)
    #mostrar por vendedor
    mostrar_vendedor(mat)

    #mostrar por artículo
    mostrar_articulo(mat)



if __name__ == "__main__":
    test()