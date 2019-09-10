archivo = open('ejemplo.txt','rt')
lista=archivo.readlines()
print(lista)
for elem in lista:
    print(elem.strip(),end='')
