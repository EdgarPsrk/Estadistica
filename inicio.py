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
        return a,b

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

        return e,a

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

        return e,a

    else:
        print('Perdoname solo puedo operarar con  1, 0.1 y 0.01')
        return 0


def condicion(amplitud, intervalo, rango):
    a = amplitud*intervalo
    
    if a > rango:
        print('La condicion se cumple')
    else:
        print('La condicion no se cumple')


def imprimirC(contenedor):
    print(contenedor)
    contenedor.sort()
    print('tus datos ordenados\n', contenedor)
    n = len(contenedor)
    print('tamaño del arreglo: ', n)
    return n


def agrupamientoT(datom, datoM, n, unidad_variacion):
    rango = datoM - datom
    print('Rango: ', rango)

    k = intervalo(n)
    kfinal= redondeo(k)

    opAmplitud = rango / kfinal
    ampFinal = amplitudF(unidad_variacion,opAmplitud)
    #ampFinal me retorna el valor final de la amplitud y la unidada de variacion convertida 
    ampAprobacion = ampFinal[0]
    unidadV = ampFinal[1]

    condicion(ampAprobacion,kfinal,rango)

    return kfinal, ampAprobacion, unidadV






if __name__ == "__main__":
    inicio = input('Para iniciar coloca si\n')

    while inicio != 'no':
        
        unidad_variacion = input( '¿Cual es la unidad de variacion?')

        if unidad_variacion == '1':
            print('digite sus datos: ')
            contenedor = list( map( int, input().split(',') ) )

            muestra = imprimirC(contenedor)

            datom = contenedor[0]
            datoM = contenedor[muestra-1]
            data = agrupamientoT(datom, datoM, muestra,unidad_variacion)
        else:
            print('digite sus datos: ')
            contenedor = list( map( float, input().split(',') ) )

            muestra = imprimirC(contenedor)

            datom = contenedor[0]
            datoM = contenedor[muestra-1]
            data = agrupamientoT(datom, datoM, muestra, unidad_variacion)

        print('Dato menor:', datom)
        print('Dato mayor:', datoM)
        k = data[0]
        inter = k

        amp = data[1]

        unidad_variacion = data[2]
        
        array = []
        array.append(datom)
        lsc = datom + amp - unidad_variacion

        while k > 1:
            datom += amp
            array.append(datom)
            k -= 1
        
        print('limites inferiores de clase\n', array)

        array = []
        array.append(lsc)
        k = inter

        while k > 1:
            lsc += amp
            array.append(lsc)
            k-=1
        
        print('limites superiores de clase\n', array)




        
        
        

        inicio = input('Tienes otro arreglo\n') 

