#Palindromo una buena practica es empezar con las funciones


def FUNC(nombre):
#ACOMODANDO LAS PALABRAS
    nombre = nombre.lower()
    nombre = nombre.replace(" ","")
    if nombre[0:]==nombre[::-1]:
        return True
    else:
        return False
   
 
nombre = input("digame su nombre : ")

es_palindromo = FUNC(nombre)

if es_palindromo == True:
    print("palindromo")
else:
    print("NO palindromo")







    







