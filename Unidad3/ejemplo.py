frutas="Uva,Manzana,Pera,Kiwi,Mango"
print(frutas)
lista_frutas=frutas.split(',')
print(lista_frutas)
print(lista_frutas[len(lista_frutas)-1])
lista_frutas[0]='Fresa'
print(lista_frutas)

del lista_frutas[0]
print(lista_frutas)

lista_frutas.sort()
print(lista_frutas)
lista_frutas.reverse()
print(lista_frutas)

#slicing
print(lista_frutas[::])

numeros="1,2,3,4,5,6,7,8,9"
lista_numeros=numeros.split(',')
print(lista_numeros[2:6:])
print(lista_numeros[::2])
print(lista_numeros[:5:])
print(lista_numeros[::-1])
print(lista_numeros[:-4:-1])

lista=[lista_frutas,lista_numeros]
print(lista)
print(lista[1][1])
lista[1][1]='22'
print(lista[1][1])

lista_numeros.extend(lista_frutas)
print (lista_numeros)

lista_numeros.append("rojo")
lista_numeros.extend(("morado","violeta"))
var=lista_numeros.pop()

print(lista_numeros)
print(var)

lista_fw=[1,"172.16.1.1","Activo"]
id,ip,status=lista_fw
print(id)
print(ip)
print(status)
