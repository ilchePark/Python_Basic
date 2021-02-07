import random
  

def run(numero_ingresado):
    #numero aleatrorio de la pc
    numero_pensado= random.randint(1, 900)
    #----------------------------

    while numero_ingresado != numero_pensado:
        if numero_ingresado < numero_pensado:
            numero_ingresado= int(input("Elige un numero mayor: "))
        else:
            numero_ingresado= int(input("Elige un numero Menor: "))

    print("Ganaste Ilche")


numero_ingresado = int(input("Ingrese un número del 1 al 900: "))
run(numero_ingresado)