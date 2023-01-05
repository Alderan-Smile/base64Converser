import base64

def decode64(cadena):
    import sys
    import os
    os.system('cls')
    try:
        base64.decode(open('../Entrada/'+cadena+'.txt','rb'),open('../Salida/'+cadena+'.csv','wb'))
        print('Archivo ../Salida/'+cadena+'.csv creado con exito',file=sys.stderr)
        print()
    except FileNotFoundError:
        print('Archivo ../Entrada/'+cadena+'.txt no encontrado',file=sys.stderr)
        print()