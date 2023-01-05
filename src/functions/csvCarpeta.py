import os
import base64

obj = os.listdir('../Entrada/')

def encode64dir():
    import sys
    os.system('cls')
    for entry in obj :
        if entry.endswith(".csv"):
            namefile = entry.split(".")[0]
            try:
                base64.encode(open('../Entrada/'+entry,'rb'),open('../Salida/'+namefile+'.txt','wb'))
            except FileNotFoundError:
                print('Archivo '+entry+' no encontrado en carpeta Entrada',file=sys.stderr)
                print()
            
            print('Archivos csv en carpeta ../Entrada/ convertidos con exito',file=sys.stderr)
            print()
            
    if len(obj) <1:
        print('No existen archivos csv en carpeta',file=sys.stderr)
        print()