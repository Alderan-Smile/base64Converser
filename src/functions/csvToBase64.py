import base64

def encode64(filename):
    import sys
    import os
    os.system('cls')
    try:
        base64.encode(open('../Entrada/'+filename+'.csv','rb'),open('../Salida/'+filename+'.txt','wb'))
        print('Archivo ../Salida/'+filename+'.txt creado con exito',file=sys.stderr)
        print()
    except FileNotFoundError:
        print('Archivo ../Entrada/'+filename+'.csv no encontrado',file=sys.stderr)
        print()
