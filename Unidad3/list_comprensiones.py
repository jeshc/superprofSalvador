lista_especial=[]
for num in range(1,11):
    if num > 5:
        lista_especial.append(num)
print(lista_especial)


l_e = [x for x in range(1,11) if x > 5]
print(l_e)


archivos = ["archivo"+str(x)+".txt" for x in range(1,11) ]
print(archivos)
