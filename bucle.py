


def run():
    contador = 1
    LIMITE = 32
    potencia = 2 ** contador
    
    while potencia < LIMITE:
        
        contador=contador+1 
        aa=int(contador)
        bb=int(potencia)

        gg =str(aa)
        hh =str(bb)

        print("2 elevado a: " +  gg + " =  "+ hh)
        potencia = 2 ** contador
         



run()