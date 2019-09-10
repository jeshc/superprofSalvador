# Comprehensions
Son una forma de generar listas a partir de raglas o funciones usando iteradores y condiciones.

Imagina que quieres hacer una lista con los siguientes requisitos:

- Numeros entre 1 y 10
- pero de ese rango solo utilizar los que son mayores a 5

Por lo tanto podrias diseñar la lista con un for loop de la forma:

```
lista_especial=[]
for num in range(1,11):
    if num > 5:
        lista_especial.append(num)
print(lista_especial) # [6, 7, 8, 9, 10]
```
Lo cual requiere 4 líneas de código, sin embargo

Principio ZEN 9: **  Sin embargo la practicidad le gana a la pureza.**

Para ello existen los list Comprehensions, cuya sintaxis es la siguiente:

# Sintaxis
##### nueva_lista = [<expresion_de_x>       <for_sobre_x>    <condicion_de_x>]

Con lo cuál se puede escribir lo mismo en una simple línea.

```
l_e = [x for x in range(1,11) if x > 5]
print(l_e)  # [6, 7, 8, 9, 10]
```

#### ejercicio:
Generar una lista del 6 al 15 en una sola linea empleando Comprehensions.

##### Ejemplo 2
Imagina que vas a abrir archivos con el formato "Archivo1.txt", "Archivo2.txt", hasta "Archivo20.txt".

Lo puedes hacer con Comprehensions de la forma:
```
archivos = ["archivo"+str(x)+".txt" for x in range(1,21) ]
print(archivos)
```
