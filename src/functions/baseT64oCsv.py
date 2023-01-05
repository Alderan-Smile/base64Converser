import base64

def decode64(cadena):
    import sys
    import os

    try:
        base64.decode(open('../Entrada/'+cadena+'.txt','rb'),open('../Salida/'+cadena+'.csv','wb'))
        os.system('cls')
        print()
    except FileNotFoundError:
        os.system('cls')
        print('Archivo ../Entrada/'+cadena+'.txt no encontrado',file=sys.stderr)
        print()