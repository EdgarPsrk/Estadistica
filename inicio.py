from math import log

def intervalo(muestra):
    a = 3.322 * log(muestra, 10)
    return 1 + a


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
    print('Estos son tus datos\n', contenedor)
    contenedor.sort()
    print('---------------------------------------------------')
    print('Tus datos ordenados\n', contenedor)
    n = len(contenedor)
    print('Tamaño del arreglo: ', n)
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


def limitesC(k,amp,datom):
    array = []
    array.append(datom)

    while k > 1:
        datom += amp
        array.append(datom)
        k -= 1
        
    return array


def marcaC(lci,lcs,k, uniV):
    contador = 0
    array = []

    if uniV == 1: 

        while contador < k:
            marca =  int( ( lci[contador] + lcs[contador] ) / 2 )
            array.append(marca)
            contador += 1
    else:
        while contador < k:
            marca =  ( lci[contador] + lcs[contador] ) / 2 
            array.append(marca)
            contador += 1

    
    return array


def frecuencia_absoluta(k, contenedor, inferior, superior):
    contador = 0
    cuenta = 0
    fi = []

    while contador < k:
        for i in contenedor:
            if i <= superior[contador] and i >= inferior[contador]: 
                cuenta += 1

        fi.append(cuenta)
        contador += 1 
        cuenta = 0 
    return fi


def fRelativa(k, array, n):
    contador = 0
    fr = []

    while contador < k:
        data = ( array[contador] / n ) * 100
        data = round(data, 3)
        contador += 1
        fr.append(data)
    return fr


def fAcumulada (k, array):
    contador = 1
    a = array[0]
    fa = [a]

    while contador < k:
        a += array[contador] 
        fa.append(a)
        contador += 1
    return fa


def fComplementaria(muestra, array, k):
    contador = 0
    fc =[muestra]
    a = muestra

    while contador < k:
        a -= array[contador]
        fc.append(a)
        contador  += 1

    return fc


def frecuenciaCR(array, n, k):
    fcr = []
    contador = 0

    while contador < k:
        a = round(100*array[contador]/n, 2)
        fcr.append(a)
        contador += 1

    return fcr





def render(inferior, superior,k,titulo):
    print('-------------------------------------------------------------------')
    contador = 0
    print(titulo)
    while contador < k:
        print(f"""
        {inferior[contador]} - {superior[contador]}
        """, end = '')
        contador += 1


def render1(dato, k, titulo):
    print('-------------------------------------------------------------------')
    contador = 0 
    print(titulo)

    while contador < k:
        print(f"""
        {dato[contador]}
        """, end = '')
        contador += 1





if __name__ == "__main__":
    inicio = input('Para iniciar coloca si\n')

    while inicio != 'no':
        
        unidad_variacion = input( '¿Cual es la unidad de variacion?\n')

        if unidad_variacion == '1':
            print('Digite sus datos: ')
            contenedor = list( map( int, input().split(',') ) )

            muestra = imprimirC(contenedor)

            datom = contenedor[0]
            datoM = contenedor[muestra-1]
            data = agrupamientoT(datom, datoM, muestra,unidad_variacion)
        else:
            print('Digite sus datos: ')
            contenedor = list( map( float, input().split(',') ) )

            muestra = imprimirC(contenedor)

            datom = contenedor[0]
            datoM = contenedor[muestra-1]
            data = agrupamientoT(datom, datoM, muestra, unidad_variacion)

        print('Dato menor:', datom)
        print('Dato mayor:', datoM)

        k = data[0]
        amp = data[1]
        unidad_variacion = data[2]
        n = len(contenedor)

        title1 = 'Limites de clases'
        lsc1 = datom + amp - unidad_variacion
        limCi= limitesC(k,amp, datom)
        limCs = limitesC(data[0], data[1], lsc1)

        title2 = 'Limites Reales de Clase'
        lrci = limCi[0] - (unidad_variacion/2)
        lrcs = limCs[0] + (unidad_variacion/2)
        limRCS = limitesC(k,amp,lrcs)
        limRCi = limitesC(k,amp,lrci)

        title3 = 'Marcas de clase'
        xi = marcaC(limCi,limCs,k, unidad_variacion)

        title4 = 'Frecuencia absoluta'
        fi = frecuencia_absoluta(k,contenedor,limCi,limCs)

        title5 = 'frecuencia relativa en %'
        fr = fRelativa(k, fi, n)

        title6 = 'Frecuencia acumulada'
        fa = fAcumulada(k, fi)

        title7 = 'Frecuencia acumulada relativa en %'
        far = fAcumulada(k,fr)

        title8 = 'Frecuencia complementaria'
        fc = fComplementaria(n, fi, k)

        title9 = 'Frecuencia complementaria relativa en %'
        fcr = frecuenciaCR(fc, n, k)



        render(limCi, limCs,k, title1)
        render(limRCi,limRCS,k,title2)
        render1(xi,k,title3)
        render1(fi,k,title4)
        render1(fr,k,title5)
        render1(fa,k,title6)
        render1(far,k,title7)
        render1(fc, k, title8)
        render1(fcr, k, title9)




        print('')
        inicio = input('Tienes otro arreglo\n') 

