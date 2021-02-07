def run(inicial):    
    for contador in range(0,inicial):
        contando = 0
        for primox in range(1,inicial):            
            primo = contador % primox
            if primo == 0:
                contando = contando + 1
            else:
                continue
        if contando==2:
            print("NUMERO PRIMO: " + str(contador))
  

inicial= int(input("ingrese número límite: "))

run(inicial)