#archivos

El manejo de archivos en todos los lenguajes es importante, sore todo por que es la mejor forma de almacenar resultados.

En python el manejo de archivos esta simplificado para el manejo de archivos planos, archivos estructurados y de bases de datos.

## Apertura de un archivos

<fileobj> = open( <nombre archivo> , <modo de apertura>)

Donde :
**fileobj** es el objeto que almacenará la referencia al archivo abierto.
**<nombre archivo>** Es la ruta del archivo a abrir. Emplea ruta absoluta o relativa.
**<modo de apertura>** Indica el modo de acceso y esta formado por dos letras, por ejemplo:**'wt'**
El primero puede ser:

- **r**(lectura)
- **w**(escritura)
- **x**(escritura solo si el archivo no existe)
- **a**(appen al final solo si el archivo existe)

El segundo puede ser:
- **t** format texto
- **b** formato binario

## Escritura en archivos
Una vez abierto el archivo podemos escribir datos en el mismo con la función **write()** y la funcion **print**:

```
texto= """ Esto es un texto
Muy largo
Para guardar en el
archivo """


archivo=open('ejemplo.txt','wt')
archivo.write(texto)
archivo.close()

```

La función write regresa el número de **bytes** guardados.

Modificando el ejemplo anterior
```
texto= """ Esto es un texto
Muy largo
Para guardar en el
archivo """


archivo=open('ejemplo.txt','wt')
tam=archivo.write(texto)
print(f"{tam} bytes escritos")  #55 bytes escritos
archivo.close()

```

### diferencia entre write y print

write no agrega espacios extra ni saltos de línea **\n**, a diferencia de **print** que si lo hace.

### read(), readline() y readlines()

##### read() sin argumentos, lee todo el archivo.

```
archivo=open('ejemplo.txt','rt')

salida=archivo.read()
print(salida)
```
##### read() con argumento, lee la cantidad de  bytes.

```
archivo=open('ejemplo.txt','rt')

salida=archivo.read(4)
print(salida)   #  Est
```

La función read(int) almacena un **offset** que corresponde a la última posición de la última lectura, esto permite una lectura secuencia.

```
archivo=open('ejemplo.txt','rt')
for i in range(15):
    salida=archivo.read(5)
    print(f"->{salida}<-")
archivo.close()
```
Resultado:
```
-> Esto<-
-> es u<-
->n tex<-
->to
Mu<-
->y lar<-
->go
Pa<-
->ra gu<-
->ardar<-
-> en e<-
->l
arc<-
->hivo <-
-><-
-><-
-><-
-><-
```

#### readline() lee una linea hasta, es decir hasta el punto que encuentre un salto de línea.

```
archivo=open('ejemplo.txt','rt')
while True:
    salida=archivo.readline()
    print(f"->{salida}<-")
    if not salida:
        break

archivo.close()
```

#### Readlines() lee todo el archivo y una lista con las lineas leidas.

## Archivos de texto estructurados

Las líneas leidas en un archivo pueden contener una estructura, la mas conocida es la estructura delimitada por comas (CSV) **","**. Formato que es utlizado para separar datos dentro de una línea.

También existen los tipos archivos de texto extructurado para el intercambio de información entre sistemas. El formato XML,YAML y JSON.
