frutas="uva,manzana,pera,kiwi,mango"
print(frutas)
lista_frutas=frutas.split(',')
print(lista_frutas)
print(lista_frutas[len(lista_frutas)-1])
lista_frutas[0]='fresa'
print(lista_frutas)
del lista_frutas[0]
print(lista_frutas)
lista_frutas.sort()
print(lista_frutas)
lista_frutas.reverse()
print(lista_frutas)

# slicing
print("Slicing")
print(lista_frutas[::])
print(lista_frutas[1:3:])

numeros="1,2,3,4,5,6,7,8,9"
lista_numeros=numeros.split(',')

lista=[lista_frutas,lista_numeros]
print(lista)

lista_numeros.extend(lista_frutas)

print(lista_numeros)

print(lista_numeros*2)

print(lista_numeros)
lista_numeros.append('rojo')
print(lista_numeros)

lista_fw=[1,'132.234.2.3','Activo']
print(lista_fw)
id,ip,status=lista_fw
print(id)
print(ip)
print(status)

print('For sobre una lista')
for val in lista_numeros[::-1]:
    print(val.upper())
