import random

def generar_contrasena():

    mayusculas = ['A','B','C','D','E']
    minusculas = ['a','b','c','d','e']
    simbolos = ['♘','✇','♜','%','〠']
    simbolos_B = ['《》','₡','圎','圜','円','௹','₯','₳']

    
    caracteres = mayusculas + minusculas + simbolos +simbolos_B
    contrasena = []


    for i in range(20):
        caracter_ramdom = random.choice(caracteres)
        contrasena.append(caracter_ramdom)

    contrasena="".join(contrasena)
    return contrasena
 

def run():
    contrasena = generar_contrasena()
    print("Tu nueva contrasena es:   " + contrasena)
    

if __name__ == "__main__":
    run()