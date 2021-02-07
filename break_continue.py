def run():
    for contador in range(1000):
        if contador % 2  == 0:
            print(str(contador))
            if contador == 4:
                break

run()