import base64
import csv

def decode64(cadena):
    cadena_bytes = cadena.encode('utf-8')
    ##base64.decode(cadena_bytes,open('Salida/decode.csv','wb'))
    base64.decode(open('Entrada/'+cadena+'.txt','rb'),open('Salida/'+cadena+'.csv','wb'))