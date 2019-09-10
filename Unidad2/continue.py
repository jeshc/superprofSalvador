contador=0

while contador<10:

    contador += 1
    if contador == 2:
        print("estamos en 2")
        #break
    if contador == 3:
        continue
        print("estamos en 3")
    if contador == 5:
        pass
        print("estamos en 5")

    print(contador)
