def run():
    mi_diccionario={
        'Argentia' : 11515151,
        'Bolivia' : 212131,
        'Peru' : 30000,
    }
    #print(mi_diccionario['Argentia'])
    #print(mi_diccionario['Bolivia'])
    #print(mi_diccionario['Peru'])

#VALUES Y VALUES SE PUEDE CAMBIAR POR KEYS

    #for pais in mi_diccionario.values():
     #   print(pais)

#ITEMS
    for pais, poblacion in mi_diccionario.items():
       print(pais, poblacion)



if __name__ == "__main__":
    run()
