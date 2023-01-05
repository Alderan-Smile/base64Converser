import os
import base64


def encode64dir():
    import sys
    
    obj = os.listdir('../Entrada/')
    ernot = 0
    os.system('cls')
    for entry in obj :
        if entry.endswith(".csv"):
            namefile = entry.split(".")[0]
            try:
                base64.encode(open('../Entrada/'+entry,'rb'),open('../Salida/'+namefile+'.txt','wb'))
                ernot = 1
            except FileNotFoundError:
                print('Archivo '+entry+' no encontrado en carpeta Entrada',file=sys.stderr)
                print()
            
    if len(obj) <1:
        print('No existen archivos csv en carpeta',file=sys.stderr)
        print()
    elif ernot == 0:
        print('No existen archivos csv en carpeta',file=sys.stderr)
        print()
    else:
        print('Archivos csv en carpeta ../Entrada/ convertidos con exito',file=sys.stderr)
        print()