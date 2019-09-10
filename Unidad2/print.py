

name = "José"
apellido= "Sosa"

print(name)
print ("Nombre",name)
print ("Nombre:" + name)
print ("Nombre:",name, "Apellido:", apellido)
print (f"Nombre: {name} {apellido}")

#función Format
print ("Nombre:{0} {1}".format(name,apellido))
print ("Nombre:{0} {1}".format(name,"hola"))
print ("Nombre:{0} {1} {2}".format(name,"hola",3))
print ("{0} {1} {2}".format("Hola",name,apellido))

#Caracter de escape \
print(f"\t{name}\n Hola\n\tMundo")
