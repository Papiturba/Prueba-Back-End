from Tecnologia import Tecnologia
from Consola import Consola
from Tv import Tv
from Bicicleta import Bicicleta
from Scooter import Scooter




listatvs = []
listaconsolas = []
listascooters = []
listabicicletas = []


def registrar_tv():
    #Registro de TV
    voltaje = int(input("Ingrese voltaje: "))
    precio = float(input("Ingrese precio: "))
    eficiencia = input("Ingrese eficiencia: ")
    marca = input("Ingrese marca: ")
    tamano = float(input("Ingrese tamaño: "))
    t = Tv(voltaje,precio,eficiencia,marca,tamano)
    listatvs.append(t)
    
        


def registrar_consola():
    #Registro de consola
    voltaje = int(input("Ingrese voltaje: "))
    precio = float(input("Ingrese precio: "))
    eficiencia = input("Ingrese eficiencia: ")
    marca = input("Ingrese marca: ")
    nombre = input("Ingrese nombre: ")
    version = input("Ingrese versión: ")
    c = Consola(voltaje,precio,eficiencia,marca,nombre,version)
    listaconsolas.append(c)
   
    

def registrar_scooter(): 
    #Registro de scooter
    voltaje = int(input("Ingrese voltaje: "))
    precio = float(input("Ingrese precio: "))
    eficiencia = input("Ingrese eficiencia: ")
    marca = input("Ingrese marca: ")   
    aro = float(input("Ingrese número de aro:"))
    velocidad = int(input("Ingrese velocidad: "))
    peso = float(input("Ingrese peso: "))
    s = Scooter(voltaje,precio,eficiencia,marca,aro,velocidad,peso)
    listascooters.append(s)
    
    

def registrar_bicicleta():
    #Registrar bicicleta
    aro = float(input("Ingrese aro: "))
    peso = float(input("Ingrese peso: "))
    precio = float(input("Ingrese precio: "))
    marca = input("Ingrese marca: ")
    b = Bicicleta(aro,peso,precio,marca)
    listabicicletas.append(b)
    

def cotizar_tv():
    voltaje = int(input("Ingrese voltaje: "))
    precio = float(input("Ingrese precio: "))
    eficiencia = input("Ingrese eficiencia: ")
    marca = input("Ingrese marca: ")
    tamano = float(input("Ingrese tamaño: "))
    for tv in listatvs:
        print(tv)
    
    

def cotizar_consola():
    voltaje = int(input("Ingrese voltaje: "))
    precio = float(input("Ingrese precio: "))
    eficiencia = input("Ingrese eficiencia: ")
    marca = input("Ingrese marca: ")
    nombre = input("Ingrese nombre: ")
    version = input("Ingrese versión: ")
    for consola in listaconsolas:
        print(consola)

def cotizar_scooter():
    voltaje = int(input("Ingrese voltaje: "))
    precio = float(input("Ingrese precio: "))
    eficiencia = input("Ingrese eficiencia: ")
    marca = input("Ingrese marca: ")    
    aro = float(input("Ingrese número de aro:"))
    peso = float(input("Ingrese peso: "))
    for scooter in listascooters:
        print(scooter)

def cotizar_bicicleta():
    aro = float(input("Ingrese aro: "))
    peso = float(input("Ingrese peso: "))
    precio = float(input("Ingrese precio: "))
    marca = input("Ingrese marca: ")
    for bici in listabicicletas:
        print(bici)



while True:
    print("1.- Registrar TV")
    print("2.- Registrar Consola")
    print("3.- Registrar Scooter")
    print("4.- Registrar Bicicleta")
    print("5.- Cotizar TV")
    print("6.- Cotizar Consola")
    print("7.- Cotizar Scooter")
    print("8.- Cotizar Bicicleta")
    
    try:
        opcion = int(input("Ingrese una opción: "))
        
    except:
        print("Ingrese un número: ")
    
    if opcion == 1:
        registrar_tv()
    elif opcion == 2:
        registrar_consola()
    elif opcion == 3:
        registrar_scooter()
    elif opcion == 4:
        registrar_bicicleta()
    elif opcion == 5:
        cotizar_tv()
    elif opcion == 6:
        cotizar_consola()
    elif opcion == 7:
        cotizar_scooter()
    elif opcion == 8:
        cotizar_bicicleta()
    else:
        print("Opción no válida")