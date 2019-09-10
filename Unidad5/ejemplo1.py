archivo=open('ejemplo.txt','rt')
while True:
    salida=archivo.readline()
    print(f"->{salida}<-")
    if not salida:
        break

archivo.close()
