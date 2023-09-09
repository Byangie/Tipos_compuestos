#Diccionarios_ejemplo1

#En el bloque principal del programa definir un diccionario que almacene
#los nombres de paises como clave y como valor la cantidad de habitantes.
#Implementar una función para nostrar cada clave y cada valor.

def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])
        
#bloque principal
paises={"argentina":40000000, "españa":46000000, "brasil":19000000, "uruguay":3400000}
imprimir(paises)

