### 6. Estructuras de control iterativas
Sirven para hacer bucles(ejecución repetida de código)
  #### Bucle while
  La sintaxis de la estuctura de control while es la siguiente:
  ```
  while <condición>:
      <sentencias while>
  ```

#### Ejemplo 1:
  ```
  contador=10
  while contador <= 20:
      print(f"Valor de contador:{}")
  ```
#### Ejercicio 1:
  Escribir el código que simule el funcionamiento de la función find() de string.
  ```
  frase1="Si funciona... no lo arregles."
  print(frase1.find('l'))  # 18
  ```
#### Ejemplo 2.- Contar el numero de letras 'a' en la frase 2 que se encuentra a continuación.
  ```
  frase2="Durante mucho tiempo me extrañó el hecho de que algo tan caro y tan vanguardista fuera tan inútil. Y luego pensé que la computadora es una máquina estúpida con la capacidad de hacer cosas increíblemente inteligentes, mientras que los programadores de computadoras son gente inteligente con la capacidad de hacer cosas increíblemente estúpidas. En pocas palabras, son la pareja perfecta.- Linus Torvalds
  longitud=len(frase2)
  contador=0
  frecuencia=0

  while contador < longitud:
      if frase2[contador] == 'a' :
          frecuencia +=1
      contador +=1
  print(f'La frase 2 contiene {frecuencia} letras a')
 ```
#### Ejercicio 2.- Modificar el ejercicio anterior para que la letra a buscar sea obtenida desde teclado.

#### Ejercicio 3.- Escribir un programa que solicite un número entero y que lo imprima en pantalla. Repetir el ciclo hasta que se presione el 0(cero).

### Else While
A diferencia de otros lenguajes, en python la estructura while tiene una sección else:

```
contador=1
while contador < 20:
    print(f"{contador}")
    contador +=1
else:
    print("\nLlegamos a 20")
```

#### Break, contiene y pass
**break** : sale del de la esructura ciclica mas cercana.
**continue** : va inmediatamente a la parte superior del ciclo.

**pass**: no hace nada.


```
while test:
    code statement
    if test:
        break
    if test:
        continue
else:
```



  ## Bucle for
En python un for actua como un iterador sobre una estructura de datos.

```
  for item in object:
    statements to do stuff
```


```
frase="Esta es una frase corta"
for letra in frase:
    print(f"->{letra}<-")
```


### la función range()
La función range sirve para generar una lista en un intervalo especificado por tres valores: Inicio, fin e incremento.


```
range( start, stop, step ).
```
Ejemplo:

```
range(0,5,1) # 0,1,2,3,4
```
No incluye el límite superior.

Ejemplo 2.-

```
range(2,22,2) # 2,4,8,10,12,14,16,18,20
```

#### Variantes
Los dos parámetros finales son opcionales es decir si se envia un sólo párametro, será tomado para stop y start y step por defecto serán 0.

Ejemplo:
```
range(7)  # 0,1,2,3,4,5,6
```

Si se envían sólo dos parámetros seran tomados por start y stop. Step por defecto será 1.


### range() y for

En conbinación la función range() y la estructura for pueden generar bucles del tipo *desde-hasta*.

Ejemplo:

```
for numero in range(1,10,1):
  print(numero, end=',')
```

Resultado:

```
1,2,3,4,5,6,7,8,9,
```

### Strigs, for y range()

Es posible combinar estos elementos para iterar sobre listas (un arreglo tambien es una lista, las listas se ven mas adelante).

Ejemplo, si queremos iterar sobre una lista con la notación [] sería de esta forma:

```
frase="Esta es una frase corta"
for indice in range(len(frase)):
    print(indice, end='-')
```
Resultado:

```
0-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-
```
