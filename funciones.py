def funcion_bienvenida(opcion):
    print("Hola como estás bienvenido al área")
    print("Número")
    print(opcion)

opcion = int(input("Elija un numero de área: 1,2,3 "))

if opcion==1:
    funcion_bienvenida(opcion)
elif opcion==2:
     funcion_bienvenida(opcion) 
elif opcion==3:
     funcion_bienvenida(opcion)     
else:
    print("elija una opcion correcta")