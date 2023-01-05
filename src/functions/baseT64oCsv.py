import base64

def decode64(cadena):
    import sys

    cadena_bytes = cadena.encode('utf-8')

    try:
        base64.decode(open('../Entrada/'+cadena+'.txt','rb'),open('../Salida/'+cadena+'.csv','wb'))
    except FileNotFoundError:
        print('Archivo ../Entrada/'+cadena+'.txt no encontrado',file=sys.stderr)