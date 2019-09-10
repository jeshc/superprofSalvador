alumno={'id':12,'nombre':'Jose'}
print(alumno)
print(f"Id del alumno: {alumno['id']}")


obj={"nombre":{
                "primerNombre":"Mario",
                "segundoNombre":None,
                "apellidoPaterno":"Pérez",
                "apellidoMaterno":"García"
              }
    }

print(type(obj))

# Todos los tips de datos
cliente={
  "numCliente": 1234,
  "nombre":{
            "nombre":["Luis","Fernando"],
            "apellidoPaterno":"Pérez",
            "apellidoMaterno":"García"
          },
  "telefonos":("04455-2345-2344","55-3987-3432","(721)33221212"),
  "direccion":{
                "calle":"Bosques de Africa",
                "numeroExt":"23-B",
                "colonia":"Bosques de Aragón",
                "cp":57127,
                "estado":{
                        "idEstado":15,
                        "nombreCorto":"EdoMex",
                        "nombre":"Estado de México"
                        }
              },
   "activo":True,
   "balance":231521.89,
   "prestamos":None
}

print(cliente)
print(f"Colonia: {cliente['direccion']['colonia']}")
print(f"Info del estado: {cliente['direccion']['estado']}")
print(f"Nombre corto del estado: {cliente['direccion']['estado']['nombreCorto']}")

# Colonia en mayusculas
print(f"Colonia: {cliente['direccion']['colonia'].upper()}")

# Existe nombre luis?
print(cliente['nombre']['nombre'])
print(f"{'Luis' in cliente['nombre']['nombre']}")



# cambiar balance
cliente['balance']=221000.0
print(cliente)

#cambiar Estado
cliente['direccion']['estado']={
        "idEstado":7,
        "nombreCorto":"CdMX",
        "nombre":"Ciudad de México"
        }
print(cliente)


# Agregar
cliente['otro_campo']="algun valor"
print("-----------------------")
print(cliente)


#print(dir(cliente))
print(cliente.keys())
print(cliente.values())
print(cliente.items())


edades={'jose':12, 'pedro':10, 'juan':13}
otros_datos={'jose':22, 'maria':10}
edades.update(otros_datos)
print(edades)


#combinar
mi_lista = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
mi_diccionario=dict(mi_lista)
print(mi_diccionario)


mi_lista = [ ['a', 'b'], ['c', ['d','e']], ['f', 'g'] ]
mi_diccionario=dict(mi_lista)
print(mi_diccionario)  # {'a': 'b', 'c': 'd', 'e': 'f'}
