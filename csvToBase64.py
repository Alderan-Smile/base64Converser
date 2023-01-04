import base64

def encode64(filename):
    base64.encode(open('Entrada/'+filename+'.csv','rb'),open('Salida/'+filename+'.txt','wb'))