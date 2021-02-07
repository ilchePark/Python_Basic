 
 #estoy imprimiendo mi nombre con los caracteres en mayuscula con for
 
def run():
    nombre = input("Escribre tu nombre: ")
    for letra in nombre:
        print(letra.upper())


run()