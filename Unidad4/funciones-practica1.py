#Escribe una función que reciba una lista de tres números enteros y regrese el mayor de ellos.¶
#ejemplo:
#Llamada: maximo([12,2,3])
#salida: El 12 es el numero mayor
"""

v1=input("Ingresa el primer numero: ")
v2=input("Ingresa el segundo numero: ")
v3=input("Ingresa el tercer numero: ")
v1=int(v1)
v2=int(v2)
v3=int(v3)
lista_num=[]
lista_num.extend((v1,v2,v3))
"""
lista_num=[]
for index in range (3):
    lista_num.append(int(input("Ingresa el numero: ")))

print (lista_num)


def maximo (lista):
    contador=0
    for x in lista:
        if x>contador:
            contador=x
    print (f"El numero maximo es: {contador}")
    return contador

maximo(lista_num)

#Escribe una función que sume los numeros de una lista y retorne el resultado.

def sumalista (lista2):
    v=0
    for x in lista2:
        v=x+v
    print(f"La suma de la lista es: {v}")

sumalista (lista_num)


#Escribe una función en python que reciba un String y lo regrese en orden inverso.

def stringrev (palabra):
    print(palabra[::-1])

txt="Hola"
stringrev(txt)

#Escribir una función que reciba una lista y la regrese con elementos únicos:
#Ejempo de entrada : [1,2,3,3,3,3,4,5,5,5,1]
#Ejemplo de salida : [1, 2, 3, 4, 5]
rep=[1,2,3,3,3,3,4,5,5,5,1]

def uniquek (lista3):
    cadena=[]
    for x in lista3:
        if x not in cadena:
            cadena.append(x)
    print (cadena)

uniquek(rep)

#Escribir una función en python que dada una lista de entrada, regrese una lista con los elementos pares ordenados.¶
#Ejemplo de entrada: [1, 2, 3, 4, 5, 6, 7, 8, 9,11,13,44]
#Ejemplo de salida: [2, 4, 6, 8, 44]

numeros_desorden=[1,2,3,4,5,9,7,13,21,55,84,99]

def par_orden (lista4):
    nueva_lista=[]
    for x in lista4:
        v=x%2

        if v == 0:
            nueva_lista.append(x)
    print(nueva_lista)

par_orden(numeros_desorden)

#Considera la sigueinte lista:
x = [2, 3, 4, 5, 10, 20, 30]
#Define una función que calcule la función matemática f(x) = 5x-2x+1

def fnmat (x):
    b=(5*x)-(2*x)+1
    print (b)

for num in x:
    fnmat(num)


#Dado el diccionario "pedido" como ejemplo, escribir una función que reciba el diccionario e imprima en pantalla
#el recibo formateado, sin olvidar imprimir el subtotal y calcular el IVA del 16%.
pedido = {'id':1212 ,
          'idCliente': 'CSM12',
          'nombre':'Juan Pérez',
          'productos':[{'id':'SKU501','nombre':'Audifonos Bluethot' ,'precio':230.3,'cantidad':100},
                       {'id':'SKU352','nombre':'USB 256 GB' , 'precio':330.50,'cantidad':20}],
          'fecha':"12/06/2019"
         }

def comanda (pedido):
    print (f"El ID del pedido es: {pedido['id']}")
    print (f"El ID del client es: {pedido['idCliente']} y su nombre es: {pedido['nombre']}")
    v=0
    for x in pedido['productos']:
        v= x['precio']*x['cantidad']+v
    print (f"El subtotal es: {v}")
    iva=v*1.16
    iva="%.2f" % iva
    print(f"Gran Total es: ${iva}")
comanda(pedido)
