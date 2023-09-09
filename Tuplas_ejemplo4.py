#Tuplas_ejemplo4

#Funcion que solicita la carga del dia, mes, año
#se almacena en una tupla que retorna los datos ingresados.

def cargar_fecha():
    dd=int(input("Ingrese numero de dia:"))
    mm=int(input("Ingrese numero de mes:"))
    aa=int(input("Ingrese numero de año:"))
    return (dd,mm,aa)

def imprimir_fecha(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")

#bloque principal

fecha=cargar_fecha()
imprimir_fecha(fecha)

