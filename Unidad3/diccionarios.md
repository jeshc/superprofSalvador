# Diccionarios

Los diccionarios son estructuras de datos no ordenadas que almacenan información en pares de ```llave:valor```, la estructura esta organizada por medio de llaves ``` {} ```.
- Formada por pares de {llave:valor}
- En donde valor puede ser de cualquier tipo(int, str,Boolean, lista, tupla), inclusive otro diccionario.
- No se pueden seleccionar por offset [0] o [n].
- Se seleccionan por nombre de llave. ['idCliente']
- Son **mutables**

## Creación de un diccionario.

```
alumno={'id':12,'nombre':'Jose'}
print(alumno)
print(f"Id del alumno: {alumno['id']}") #
```

Desde una lista usando dict()
```
mi_lista = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
mi_diccionario=dict(mi_lista)
print(mi_diccionario)  # {'a': 'b', 'c': 'd', 'e': 'f'}
```

## Ejercicio:
1. Hacer un diccionario que defina tu computadora.
2. Imprimirlo en pantalla.

## Se pueden anidar
En la declaración de un diccionario no aplica la estructura de indentación.

```
obj={"nombre":{
                "primerNombre":"Mario",
                "segundoNombre":None,
                "apellidoPaterno":"Pérez",
                "apellidoMaterno":"García"
              }
    }
```

## Valores
La parte de valor puede ser de cualquier tipo:
- str
- int
- float
- Boolean
- list
- tuple
- dict


Ejemplo:
```
cliente={
  "numCliente": 1234,
  "nombre":{
            "nombre":["Luis","Fernando"],
            "apellidoPaterno":"Pérez",
            "apellidoMaterno":"García"
          },
  "telefonos":("04455-2345-2344","55-3987-3432","(721)33221212"),
  "dirección":{
                "calle":"Bosques de Africa",
                "numeroExt":"23-B",
                "colonia":"Bosques de Aragón",
                "cp":57127
              },
   "activo":True,
   "balance":231521.89,
   "prestamos":None
}

```
Ejemplos.
```
#imprimir la colonia
print(f"Colonia: {cliente['direccion']['colonia']}")

# imprimir info del estado
print(f"Info del estado: {cliente['direccion']['estado']}")

Imprimir nombre corto del estado
print(f"Nombre corto del estado: {cliente['direccion']['estado']['nombreCorto']}")
```
## invocar métodos propios de los valores.
```
# Colonia en mayusculas
print(f"Colonia: {cliente['direccion']['colonia'].upper()}")
print(f"")

# Existe nombre Luis?
print(cliente['nombre']['nombre'])
print(f"{'Luis' in cliente['nombre']['nombre']}")

```

## Modificar Valores
```
# modificar el balance del cliente.
cliente['balance']=221000.0
print(cliente)

# Cambiar Estado
cliente['direccion']['estado']={
        "idEstado":7,
        "nombreCorto":"CdMX",
        "nombre":"Ciudad de México"
        }
print(cliente)

```

## Agregar Valores

```
cliente['otro_campo']="algun valor"
print(cliente) # ...  'prestamos': None, 'otro_campo': 'algun valor'}
```


## Métodos de un diccionario

## keys()
Regresa una **lista** con todos las llaves base del diccionario.

## values()
Regresa una **lista** con todos los valores base del diccionario.
## items()
Regresa **una lista** de **tuplas** con los pares ```llave:valor```

## Combinar tuplas con update()
```
edades={'jose':12, 'pedro':10, 'juan':13}
otros_datos={'jose':22, 'maria':10}
edades.update(otros_datos)
print(edades)
```
