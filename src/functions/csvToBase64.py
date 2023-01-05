import base64

def encode64(filename):
    import sys

    try:
        base64.encode(open('../Entrada/'+filename+'.csv','rb'),open('../Salida/'+filename+'.txt','wb'))
    except FileNotFoundError:
        print('Archivo ../Entrada/'+filename+'.csv no encontrado',file=sys.stderr)
