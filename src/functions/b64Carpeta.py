import os
import base64

def decode64dir():
    import sys
    
    obj = os.listdir('../Entrada/')
    ernot2 = 0
    os.system('cls')
    for entry in obj :
        if entry.endswith(".txt"):
            namefile = entry.split(".")[0]
            try:
                base64.decode(open('../Entrada/'+entry,'rb'),open('../Salida/'+namefile+'.csv','wb'))
                ernot2=1
            except FileNotFoundError:
                print('Archivo '+entry+' no encontrado en carpeta Entrada',file=sys.stderr)
                print()
            
    if len(obj) <1:
        print('No existen archivos txt en carpeta',file=sys.stderr)
        print()
    elif ernot2 == 0:
        print('No existen archivos txt en carpeta',file=sys.stderr)
        print()
    else:
        print('Archivos txt en carpeta ../Entrada/ convertidos con exito',file=sys.stderr)
        print()