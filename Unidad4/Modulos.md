# Modulos
Un módulo es un archivo de Python cuyos objetos (funciones, clases, excepciones, listas, tuplas, diccionarios...) pueden ser accedidos desde otro archivo.

En python a un conjunto de funciones declaradas en el mismo lugar, con la posibilidad de ser importado y usado desde otros códigos, **se le da el nombre de módulo**.

Ejemplo:


```
# mimodulo.py

def mi_print( valor ):
    print(f"El valor recibido es: {valor} ")

def otro_print( valor ):
    print( (str(valor)).upper() )

```

#### Uso

```
import mimodulo

mimodulo.mi_print("Hola")
```

o importando solamente la función requerida:

```
from mimodulo import mi_print

mi_print("Mundo")

#recuperar el módulo base
print(mi_print.__module__)

```

El el ejemplo anterior se puede observar que se puede importar una función en especifico, tambien puedes incluir todas con ** import \* ** de la forma:

```
from mimodulo import *
```
#### Ejercicio:
- Hacer un módulo de nombre aritmética que contenga las funciones sumar, restar, dividir y multiplicar.
- Importar el módulo desde otro programa python y realizar operaciones aritmeticas.

## Con un alias
También es posible importar módulo con un alias para así accede a las funciones por medio del mismo alias.

```
import mimodulo as mm

mm.mi_print("Hola de nuevo")
```


** La forma como importes las funciones no afecta la forma en la que  trabajan los módulos**


# Módulo sys

Obtener información del  módulo sys:
```
import sys
dir(sys)

```

Rutas de ejecución y búsqueda de módulos

```
>>> sys.path
['',
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip',
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7',
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload',
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages']

```



```
>>> sys.version
'3.7.1 (v3.7.1:e09359112e, Jun  28 2019, 14:54:52) \n[Clang 6.0 (clang-600.0.57)]'
```
