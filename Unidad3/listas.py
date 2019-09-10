
lista1=[]
print(lista1)

lista2=list()
print(lista2)


lista1.append("Pera")
lista1.append("Kiwi")
lista1.append("Naranja")
lista1.append("Manzana")

print("Naranja" in lista1)
lista1=['Kiwi', 'Manzana', 'Naranja', 'Pera']
print(lista1.sort())
print("Lista:" , lista1)
lista1.clear()
print("Lista:" , lista1)


fecha= ['12', '05', '2019']
d,m,a=fecha
print(d)
print(m)

print(lista1)

print("-------------------------")


dias_semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
tmp=dias_semana[1]
dias_semana[1]=dias_semana[0]
dias_semana[0]=tmp

print(dias_semana)
dias_semana.remove("martes")
print(dias_semana)

dias_semana.reverse()
print(dias_semana)



print('-------------------')
fecha='12/05/2019'
fecha_separada=fecha.split('/')
print(".-.-")
print(fecha_separada)






autos=["Mazda","Honda","VW", "Akura","Ford"]
motocicletas=["Suzuki", "Vento","BMW", "Kawasaki", "Ducatti"]
bicicletas=["Benotto","Alubike"]
vehiculos=[autos,motocicletas,bicicletas]
print(vehiculos)

print(vehiculos[1])   # ?
#print(vehiculos[3]) # ?
print(vehiculos[2][1]) # ?
print(vehiculos[0][3]) # ?
print(vehiculos[1][3]) # ?
print(vehiculos[1][1:4])   # ?



## Slicing avanzado
numeros=[0,1,2,3,4,5,6,7,8,9]
print(numeros[::])
print(numeros[::-1])
print(numeros[::2])
print(numeros[:6:])
print("inverso:",numeros[-4:-9:-1])


# extend
numeros=[0,1,2,3,4,5,6,7,8,9]
dias_semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
numeros.extend(dias_semana)
print(numeros) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

# +=

numeros=[0,1,2,3,4,5,6,7,8,9]
dias_semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
numeros += dias_semana
print(numeros)
print('--------   +        -------------')


# append
numeros=[0,1,2,3,4,5,6,7,8,9]
dias_semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
dias_semana.append(numeros)
print(numeros)


# for
dias_semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
for dia in dias_semana:
    print(dia.upper())
print("Count: ",dias_semana.count("martes"))

print("numeros", numeros  )

print("','.join(str(numeros)): ",''.join(str(numeros)))
strnumeros=str(numeros)
print("str(numeros)",strnumeros)
print(','.join(dias_semana))


a = [1, 2, 3]
b = a
print(a)
print(b)
a[0]='surprise'
print(a)
print(b)
b[0]='oo'
print(a)
print(b)

dias_semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]

dias_semana[0]="un dia"
print(dias_semana)  # ['un dia', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']



numeros=[0,1,2,3,4,5,6,7,8,9]
numeros[2:7]=[-4]
print(numeros)
