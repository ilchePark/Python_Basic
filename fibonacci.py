def run(ingresante):



    valor_inicial = [0,1]
    #valor_f = valor_inicial[1]
    
    if(ingresante == 1):
        print("0")
    
    #for posicion in range(len(valor_inicial)):
    elif(ingresante == 2):
        print("0")
        print("1")
    else:        
        print("0")
        print("1")
        for x in range(ingresante-2):
            longitud = len(valor_inicial) 
            sumo_1 = longitud - 1
            sumo_2 = longitud - 2
            a_integrar =valor_inicial[sumo_1] + valor_inicial[sumo_2]
            print(a_integrar)
            valor_inicial.append(a_integrar)
        
    #print(cantidad_numero) 
    
          
# 1 1 2 3 5 8 13 21 34 65

ingresante= int(input("Hola porfavor ingrese el Número Límite de fibo:  "))


 
        
if __name__ == "__main__":
    run(ingresante)