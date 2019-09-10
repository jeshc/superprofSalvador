



# Python unidad 1


### 1.- Breve historia de Python
Origen en los 80s y principios de los 90s por Guido Van Rossum como continuación al lenguaje ABC en un centro de investigación holandes.
El origen del nombre del lenguaje es por que a Guido le gustaba un grupo de nombre Monty Python.

En octubre de 2000 se libera Python 2.0 con  nuevas características, entre ellas sobresale la recolección de basura y  soporte a Unicode.


### 2. Carasterísticas de Python

- Lenguaje de propósito general.
- Es un lenguaje interpretado, no compilado.
- Usa tipado dinámico, fuertemente tipado.
- Multiplataforma.
- Lenguaje milti-paradigma:  POO, estructurada,  imperativa, en menor medida, programación funcional.
- Código estructurado por indentación.



##### Principios Zen de Python
Los programadores Python publicaron en la página oficial del proyecto una lista de principios de diseño cuano se escribe código en Python, Estos principios fueron los que guiaron la arquitectura del lenguaje en sí.

[Original de los principios Zen Python](https://github.com/python/peps/blob/master/pep-0020.txt)

 Principios Zen de Python
  1. Bello es mejor que feo.
    Centrada en tener una sintaxis clara lo más parecido al lenguaje natural posible (inglés).

  1. Explícito es mejor que implícito.
  1. Simple es mejor que complejo.
  1. Complejo es mejor que complicado.
  1. Plano es mejor que anidado.
  1. Espaciado es mejor que denso.
  1. La legibilidad es importante.
  1. Los casos especiales no son lo suficientemente especiales como para romper las reglas.
  1. Sin embargo la practicidad le gana a la pureza.
  1. Los errores nunca deberían pasar silenciosamente.
  1. A menos que se silencien explícitamente.
  1. Frente a la ambigüedad, evitar la tentación de adivinar.
  1. Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
  1. A pesar de que esa manera no sea obvia a menos que seas Holandés.
  1. Ahora es mejor que nunca.
  1. A pesar de que nunca es muchas veces mejor que ahora mismo.
  1. Si la implementación es difícil de explicar, es una mala idea.
  1. Si la implementación es fácil de explicar, puede que sea una buena idea.
  1. Los espacios de nombres son una gran idea, ¡tengamos más de esos!

## Hola mundo python 3
Es una tradición hacer el clásico programa hola mundo con python

```
>>> print("Hola mundo de programación Python")
Hola mundo de programación Python
>>> print('hola','mundo')
hola mundo
>>> print('hola','mundo', ',soy jesus')
hola mundo ,soy jesus
```
ejercicio 2.
Declarar una variable que almacene tu nombre:
```
nombre="Juan"
>>> print('{0} chatea con {1}'.format(nombre, 'jesus'))
Juan chatea con jesus
>>> print('{1} chatea con {0}'.format(nombre, 'jesus'))
jesus chatea con Juan
>>>
```
#### Print y caracter de escape
Se pueden usar los caracteres de escape:
 - \n   salto de linea
 - \t   tabulador
 - \\\\  escape
 - \'    comilla simple
 - \"    comilla doble
 - \a    beep
 - \b    BS Backspace, elimina el último caracter
 - \uxxxx    unicode 16 bits Hexadecimal
 - \Uxxxxxxxx     unicode 32 bits Hexadecimal

```
print("H\tola mu\\nndo \U00DD")
```
#### print y fin de impresion, operador 'end='
Por defecto un la función print tiene establecido el salto del linea al final, es decir el parametro end='\n'. (Salto de línea heredado de C y C++). En otras palabras por defecto print funciona asi:
```
print("Hola")
print("mundo")
print("python")
print("3")
# y esto es equivalente
print("Hola",end='\n')
print("mundo",end='\n')
print("python",end='\n')
print("3",end='\n')
```

### 3.  Python 2 y Python 3

#### función print

###### Print py2
```
print 'Versión', python_version()
print 'Esto es una linea'
print('esta , también!')
print "Se pueden ", ; print 'varios print con ;'
```
###### Print py3

```
import platform
print ('Versión', platform.python_version())
print ('Esto es una linea')
print ('esta , también!')
print ("Se pueden,", end=" ")
print (En una linea)
print 'Esto marca error en Py3'
```

#### Soporte unicode

######  py3 tiene soporte completo unicode
https://unicode-table.com/es/

```
>>> print('\u00DE')
Þ
>>> print('\u00DD')
Ý
```

#### División de enteros
En python 2.x la división entre enteros da como resultado enteros, sin embargo por cuestiones de facilidad de uso se cambió la regla a que la división entre enteros da como resultado un valor de punto flotante. Por ejemplo la división de 3 / 2 da como resultado 1.5

###### py2 división
```
print '3 / 2 =', 3 / 2      # da 1
print '3 // 2 =', 3 // 2    # da  1
print '3 / 2.0 =', 3 / 2.0  # da 1.5
print '3 // 2.0 =', 3 // 2.0  # da 1.0
```

###### py3 división
```
print '3 / 2 =', 3 / 2      # da 1.5
print '3 // 2 =', 3 // 2    # da  1
print '3 / 2.0 =', 3 / 2.0  # da 1.5
print '3 // 2.0 =', 3 // 2.0  # da 1.0
```

#### input

###### py2 input y raw_input
En python 2.x existían 2 tipos de funciones para la captura de entrada de usuario.
input() que regresaba valores segun el tipo de dato capturado por el usuario. Es decir si el usuario capturaba un 10, input regresaba un entero de valor 10 y si el usuario capturaba un 'abc', la función regresaba un string.
La función raw_input() regresaba siempre un string.

```
>>> mi_input = input("ingresar un numero: ")
ingresar un numero: 123
>>> type(mi_input)
<type 'int'>
>>> mi_input = raw_input("ingresar un numero: ")
ingresar un numero: 123
>>>type(mi_input)
<type 'str'>

```


###### py3 input
En Python 3 sólo existe la funcion input que siempre regresa un string.

ejemplos:
```
>>> var = input("ingresa un entero:")
ingresa un entero:23
>>> type(var)
<class 'str'>
>>>
```

# Romper lineas con +\
