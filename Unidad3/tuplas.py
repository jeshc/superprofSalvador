dias_semana=("lunes","martes")
print(dias_semana)
print(dias_semana[0])


dias="lunes,martes,miercoles"
tupla_dias=tuple(dias.split(","))
print(dias)
print(tupla_dias)



dias_semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
print(dias_semana)
tupla_dias=tuple(dias_semana)
print(tupla_dias)


['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
('lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo')

departamentos="Ventas",
print(departamentos[0])
datos_conexion="localhost",3306,'usrInfo','dios1234'
print(datos_conexion)

colores=("Rojo", "Verde","Azul")
r,g,b=colores
print(r)
print(g)
print(b)




colores=("Rojo", "Verde","Azul")
#print(colores.count())


a="Rojo"
b="Azul"
print(f"a={a} y b={b}")

(a,b)=(b,a)
print(f"a={a} y b={b}")


# COUNT
perros = ('pug','poddle', ('pastor aleman', 'pastor australiano'), ('pastor aleman', 'pastor australiano'), [2, 3])
coincidencias = perros.count(('pastor aleman', 'pastor australiano'))
print("El conteo de ('pastor aleman', 'pastor australiano') es:", coincidencias)

# Conteo de [2,3]
coincidencias = perros.count([2, 3])
print("El conteo de  [2, 3] es:", coincidencias)

print(f"Indice de poddle: {perros.index('poddle')}")
