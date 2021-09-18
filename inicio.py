from math import log
def intervalo(muestra):
    a = log(muestra, 10)
    b = 3.322
    c= a*b
    return 1 + c

if __name__ == "__main__":
    inicio = input('para iniciar coloca si\n')

    while inicio != 'no':
        largo_contenedor = int(input('¿Que tamaño tiene n?\n'))
        contenedor = []

        while largo_contenedor != 0:
            dato = int(input('ingresa el numero\n'))
            contenedor.append(dato)
            largo_contenedor -= 1

        print('Estos son tus datos\n', contenedor)
        contenedor.sort()
        print('Lista acomodada', contenedor)
        datom = contenedor[largo_contenedor-1]
        datoM = contenedor[0]

        rango = datoM - datom
        k = intervalo(largo_contenedor)
        amplitud = rango / k

        inicio = input('tienes otro arreglo\n') 

