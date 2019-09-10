# Tuplas  ()
Una tupla es una estructura de datos en python son las mismas caracerísticas que las listas, sin embargo estas son **INMUTABLES** por lo cual las operaciones y métodos que mutan una lista no estan disponibles en la  tupla.

### Las caracerísticas de las tuplas son.
- Puede contener 0 ó mas elementos, ( )
- son **inmutables**
- Por lo tanto usan menos espacio.
- No puedes Eliminar valores por error.
- Son buenas para almacenar datos y consultarlos.
- Los elementos pueden ser de diferentes tipos. (¿"Manzana", 12.9,"10")
- Pueden ser anidados y crear estructuras de datos mas complejas. (manzana,("Melón chino","Melón valenciano ","Melón galia", ))
- Estructura secuencial.
- Los argumentos a una función se pasan como tuplas.

# ¿Cuando usar tuplas?
Las tuplas no se usan tanto como las listas, inclusive se usan menos que los diccionarios, la respuesta a la pregunta es: en aquellos casos que se requiera un conjunto de datos que no se modifiquen y **cumplan la función de catálogo de datos** y cuando quieras proteger información de cambios.

# Crear una tupla
#### con ()
```
escala=(10,9,8,7,6,"NA","NP")
print(escala)
```
#### A partir de una lista
```

dias_semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
print(dias_semana)  # ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

tupla_dias=tuple(dias_semana)
print(tupla_dias)     #('lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo')
```


#### A partir de una cadena y el método split.
```
dias="lunes,martes,miercoles"
print(dias)         # "lunes,martes,miercoles"

tupla_dias=tuple(dias.split(","))
print(tupla_dias)   # ('lunes', 'martes', 'miercoles')

```
#### Con "," sin necesidad de ()
```
departamentos="Ventas",
print(departamentos)

datos_conexion="localhost",3306,'usrInfo','dios1234'
print(datos_conexion)
```

# Ejemplos de Tuplas


## Operaciones con Tuplas



## tuple unpacking
Se refiere a mapear los elementos de una tupla a variables independientes.
El unpacking debe tener el mismo número de elementos en ambos lados de la asignación.

```
colores=("Rojo", "Verde","Azul")
r,g,b=colores
print(r)
print(g)
print(b)
```


#  Count

```
perros = ('pug','poddle', ('pastor aleman', 'pastor australiano'), ('pastor aleman', 'pastor australiano'), [2, 3])
coincidencias = perros.count(('pastor aleman', 'pastor australiano'))
print("El conteo de ('pastor aleman', 'pastor australiano') es:", coincidencias)

# Conteo de [2,3]
coincidencias = perros.count([2, 3])
print("El conteo de  [2, 3] es:", coincidencias)
```

# index of
perros.index('poddle') # 1

```
print(f"Indice de poddle: {perros.index('poddle')}")
```

# value swap
Intercambio de valores sin uso de una variable temporal.
```
a="Rojo"
b="Azul"
print(f"a={a} y b={b}")  # a=Rojo y b=Azul

(a,b)=(b,a)
print(f"a={a} y b={b}")  # a=Azul y b=Rojo
```
