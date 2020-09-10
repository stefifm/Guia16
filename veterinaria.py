print("Veterinaria")

class Practica:
    def __init__(self, pra, suc, monto):
        self.practica = pra
        self.sucursal = suc
        self.monto = monto


def to_string(practica):
    res = " "
    res += "Tipo de práctica: " + str(practica.practica)
    res += "- Sucursal:" + str(practica.sucursal)
    res += "- Monto: " + str(practica.monto)
    return res

def validar(inf, mensaje, sup = None):
    n = inf -1
    while n < inf or sup != None and n > sup:
        n = int(input(mensaje))
        if n < inf or sup != None and n > sup:
            print("Valor incorrecto")
    return n

def cargar_vector(n, practica):
    for i in range(n):
        p = validar(0, "Ingrese código de práctica [0-9]: ", 9)
        s = validar(0, "Ingrese código de sucursal [0-5]: ", 5)
        m = validar(0, "Ingrese el monto en $: ")
        practica.append(Practica(p, s, m))

def monto_sucursal(practicas):
    acu_vec = [0] * 6
    for i in range(len(practicas)):
        acu_vec[practicas[i].sucursal] += practicas[i].monto
    return acu_vec


def practias_mas_frecuentes(practicas):
    v_cont = [0] * 10
    for i in range(len(practicas)):
        v_cont[practicas[i].practica] += 1
    mayor = v_cont[0]
    indice_mayor = 0
    for i in range(len(v_cont)):
        if v_cont[i] > mayor:
            mayor = v_cont[i]
            indice_mayor = i
    return indice_mayor, mayor

def cant_suc_tipo(practicas):
    matriz = [[0] * 10 for i in range(6)]
    for i in range(len(practicas)):
        fila = practicas[i].sucursal
        columna = practicas[i].practica
        matriz[fila][columna] += 1
    return matriz


def mostrar(v):
    for i in range(len(v)):
        print(to_string(v))

def principal():
    n = validar(0, "Ingrese la cantidad de prácticas a registrar: ")
    #practicas = [None] * n  #para cargar
    practicas = []
    cargar_vector(n, practicas)

    #punto 1
    acu_monto = monto_sucursal(practicas)
    print("Montos acumulados por sucursal:")
    for i in range(len(acu_monto)):
        print("Sucursal:",i,"Monto acumulado:",acu_monto[i])

    #Punto 2
    p, frec = practias_mas_frecuentes(practicas)
    print("La práctica más fecuente es:",p,"con una frecuencia de:",frec)

    #Punto 3
    matriz = cant_suc_tipo(practicas)
    for f in range(6):
        for c in range(10):
            if matriz[f][c] != 0:
                print("Práctica:",c,"Sucursal:",f,"Cantidad:",matriz[f][c])



if __name__ == "__main__":
    principal()