from csvToBase64 import *
from baseT64oCsv import *

print('0=================================================================================0')
print()
print('Creado por: Oliver Consterla Araya')
print('            Leonardo Bueras Valdes')
print()
print('0=================================================================================0')
print()
print()

option = input("1 - Convertir base64 a csv\n2 - Convertir csv a base64\n0 - Salir del archivo\nIngrese la opcion que necesita: ")

while(option != "0"):

    match option:
        case "0":
            exit()
        case "2":
            fileName = input("Nombre de archivo a decodificar sin extension .csv: ")
            encode64(fileName)
        case "1":
            cadena64 = str(input("Nombre de archivo a decodificar sin extension .txt: "))
            decode64(cadena64)
    

    option = input("1 - Convertir base64 a csv\n2 - Convertir csv a base64\n0 - Salir del archivo\nIngrese la opcion que necesita: ")
    print()