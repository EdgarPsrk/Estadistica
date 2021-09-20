def frecuencia_absoluta(k, contenedor, inferior, superior):
    contador = 0
    cuenta = 0
    fi = []

    while contador < k:
        for i in contenedor:
            if i <= superior[contador] and i >= inferior[contador]:
                cuenta += 1
                # print('ls', superior[contador])
                # print('li',inferior[contador])
                # print('valor i', i)
                # cuenta += 1
                # print('c:', cuenta )

        fi.append(cuenta)
        contador += 1 
        cuenta = 0 
    #     print('-------------------------------------------')      
    # print(len(contenedor))
    return fi

array = [8, 16, 16, 16, 16, 32, 32, 40, 40, 40, 40, 56, 56, 56, 60, 64, 72, 72, 72, 72, 72, 80, 80, 80, 80, 96, 96, 104, 108, 112, 112, 114, 120, 128, 136, 152, 152, 152, 156, 160, 168, 168, 168, 168, 168, 176, 184, 184, 184, 194, 208, 208, 216, 224, 224, 224, 224, 232, 240, 246, 256, 264, 264, 272, 280, 288, 304, 308, 328, 328, 340, 352, 358, 360, 384, 392, 400, 424, 438, 448, 464, 480, 536, 552, 576, 608, 656, 716]
k = 8
lci = [8,97,186,275,364,453,542, 631]
lcs = [96,185,274,363,452,541,630,719] 

a = frecuencia_absoluta(k, array, lci, lcs)

print(a)


