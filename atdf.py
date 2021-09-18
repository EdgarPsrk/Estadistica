from math import log

def intervalo(muestra):
    a = log(muestra, 10)
    b = 3.322
    c = a*b
    return 1 + c


def redondeo(k):

    if type(k) == float:
        a = int(k)
        a += 1 
        print('Tu intervalo final es: ', a)
        return a

    else:
        print('Tu intervalo es: ', k)
        return k


def amplitudF(uniV, amplitud):
    if uniV == '1':
        a = int(amplitud)
        a += 1
        b = int(uniV)
        print('Esta seria tu amplitud final: ', a)
        return a

    elif uniV == '0.1':
        a = float(uniV)
        b = round(amplitud, 2)
        c = int(amplitud)
        d = c - b

        if d < 0.5:
            e = round(amplitud,1)
            e += a
            print('Esta es tu amplitud: ', e)
        else:
            e = round(amplitud, 1)
            print('Tu amplitud es: ', e)

        return e

    elif uniV == '0.01':
        a = float(uniV)
        b = round(amplitud, 3)
        c = int(amplitud)
        d = c - b
        
        if d < 0.5:
            e = round(amplitud,2)
            e += a
            print('Esta es tu amplitud: ', e)
        else:
            e = round(amplitud, 2)
            print('Tu amplitud es: ', e)

        return e

    else:
        print('Perdoname solo puedo operarar con  1, 0.1 y 0.01')
        return 0


def condicion(amplitud, intervalo, rango):
    a = amplitud*intervalo
    
    if a > rango:
        print('La condicion se cumple')
    else:
        print('La condicion no se cumple')






if __name__ == "__main__":
    inicio = input('Para iniciar coloca si\n')

    while inicio != 'no':
        largo_contenedor = int(input('¿Que tamaño tiene n?\n'))
        n = largo_contenedor
        contenedor = []

        while largo_contenedor != 0:
            dato = int(input('Ingresa los datos\n'))
            contenedor.append(dato)
            largo_contenedor -= 1

        print('Estos son tus datos\n', contenedor)
        contenedor.sort()
        print('Lista acomodada', contenedor)

        unidad_variacion = input( '¿Cual es la unidad de variacion?')

        datoM = contenedor[largo_contenedor-1]
        datom = contenedor[0]

        rango = datoM - datom
        k = intervalo(n)
        opAmplitud = rango / k
        kfinal= redondeo(k)
        ampFinal = amplitudF(unidad_variacion,opAmplitud)

        print('Rango: ', rango)
        aprobacion = condicion(ampFinal,kfinal,rango)
        

        inicio = input('Tienes otro arreglo\n') 