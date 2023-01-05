import os
from functions.csvToBase64 import *
from functions.baseT64oCsv import *
from functions.b64Carpeta import *
from functions.csvCarpeta import *

os.system('cls')
print('Bienvenido')
print()
print('0=================================================================================0\n\n          Accenture 2023          \nCreado por: Oliver Consterla Araya\n            Leonardo Bueras Valdes\n0=================================================================================0\n\n')

try:
    if not os.path.exists('../Entrada/'):
        os.makedirs('../Entrada/')
    if not os.path.exists('../Salida/'):
        os.makedirs('../Salida/')
    
    option = input("1 - Convertir base64 a csv\n2 - Convertir csv a base64\n3 - Convertir todos los csv de la carpeta a base64\n4 - Convertir todos los base64 de la carpeta a csv\n0 - Salir del archivo\nIngrese la opcion que necesita: ")

    while(option.isnumeric):
        print()
        match option:
            case "0":
                os.system('cls')
                print('Hasta pronto')
                exit()
            case "2":
                fileName = input("Nombre de archivo a codificar sin extension .csv: ")
                encode64(fileName)
            case "1":
                cadena64 = str(input("Nombre de archivo a decodificar sin extension .txt: "))
                decode64(cadena64)
            case "3":
                encode64dir()
            case "4":
                decode64dir()
        
        print('0=================================================================================0\n\n          Accenture 2023          \nCreado por: Oliver Consterla Araya\n            Leonardo Bueras Valdes\n0=================================================================================0\n\n')
        option = input("1 - Convertir base64 a csv\n2 - Convertir csv a base64\n3 - Convertir todos los csv de la carpeta a base64\n4 - Convertir todos los base64 de la carpeta a csv\n0 - Salir del archivo\nIngrese la opcion que necesita: ")

except KeyboardInterrupt:
    os.system('cls')
    print('Hasta pronto')