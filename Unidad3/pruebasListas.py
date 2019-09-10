
dias="lunes,martes,miercoles,jueves,viernes,sabado"
lista_dias=dias.split(',')

print(lista_dias)
cadena='%'.join(lista_dias)
print(cadena)

print(dir(lista_dias))
print('----------------------')
print(dir(dias))


texto="Hola,Adios,Amigo"
lista=texto.split(',')
texto2=','.join(lista)
print(texto2)

tupla=tuple(lista)
print(tupla)

alumno=(('id',1),('nombre','jose'))
print('Test:')
print(('id',2) in alumno)

dicAl=dict(alumno)
print(dicAl)

lista_dias[0]='algo'
print(lista_dias)

lista_dias.remove('martes')

print(lista_dias)

lista_dias.sort()
print(lista_dias)
lista_dias.reverse()

print(lista_dias)

numeros=[1,2,3,4,5,6,7,8,9]
print(numeros[::])
print('[::-1]', end=' ')
print(numeros[-1:-9:-1])
print(f"[2:8:1]={numeros[2:7:1]}")

numeros[2:7]=[-4]
print(numeros)
