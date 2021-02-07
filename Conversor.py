menu = """

Benvenute ti conversor du moneda

1. Soles a dolares
2. Dolares a soles
3. Soles a euros


"""


opcion = int(input(menu))

valor_dolar = 3.56
valor_euro = 4.10

if opcion == 1:
    
    soles = input("Ingrese la cantidad en soles: ")
    soles = float(soles)

    dolares = soles / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes: $ " + dolares + " Dolares")
 
elif opcion == 2:
    dolares = input("Ingrese la cantidad en Dolares: ")
    dolares = float(dolares)

    soles = dolares * valor_dolar
    soles = round(soles,2)
    soles = str(soles)
    print("Tienes: S/. " + soles + " Nuevo sol")

elif opcion == 3:
    soles = input("Ingrese la cantidad en soles: ")
    soles = float(soles)
    
    euro= soles / valor_euro
    euro = round(euro,2)
    euro = str(euro)
    print("Tienes: E/. " + euro + " euros")

else:
     print('Ingresa una opción correcta porfavor')