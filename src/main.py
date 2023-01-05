import os
from functions.csvToBase64 import *
from functions.baseT64oCsv import *

os.system('cls')
print('Bienvenido')
print()
print('0=================================================================================0\n\n          Accenture 2023          \nCreado por: Oliver Consterla Araya\n            Leonardo Bueras Valdes\n0=================================================================================0\n\n')

option = input("1 - Convertir base64 a csv\n2 - Convertir csv a base64\n0 - Salir del archivo\nIngrese la opcion que necesita: ")

while(option != "0"):

    print()
    match option:
        case "0":
            exit()
        case "2":
            fileName = input("Nombre de archivo a codificar sin extension .csv: ")
            encode64(fileName)
        case "1":
            cadena64 = str(input("Nombre de archivo a decodificar sin extension .txt: "))
            decode64(cadena64)
    
    print('0=================================================================================0\n\n          Accenture 2023          \nCreado por: Oliver Consterla Araya\n            Leonardo Bueras Valdes\n0=================================================================================0\n\n')
    option = input("1 - Convertir base64 a csv\n2 - Convertir csv a base64\n0 - Salir del archivo\nIngrese la opcion que necesita: ")