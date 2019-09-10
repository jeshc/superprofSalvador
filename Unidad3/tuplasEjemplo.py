datos_conexion="localhost",3306,'usrInfo','dios1234',3306
print(datos_conexion)

lista_frutas=['kiwi','manzana']

print(dir(lista_frutas))

print('Cosas que hacen las tuplas')
print(dir(datos_conexion))

print(datos_conexion.count(3306))

print(datos_conexion.index(3306))


alumno1={'id':12,'nombre':'Jose'}
alumno2={'id':42,'nombre':'pedro'}
alumnos={'bd':[alumno1,alumno2],'bdEmpleados':[e1,e2,e3,e4],'contador':2}


print(alumnos)
print(f"Id del alumno 2:{alumnos['bd'][1]['id']}")
