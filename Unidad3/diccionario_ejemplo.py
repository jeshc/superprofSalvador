computadora={"marca":"apple","modelo":"macbook","pantalla":"13",
"cpu":{
    "marca":"intel",
    "velocidad":"2.5ghz",
    "multicpu":True
},
"idioma":"ingles"

}

print(computadora)
print(f"La marca del CPU es: {computadora['cpu']['marca']}")

print("-----------------------------")

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

print(cliente['balance'])
print(cliente['dirección']['colonia'])
print(cliente['nombre']['nombre'][1])

llaves=cliente.keys()
print(llaves)

for x in llaves:
    print(x)

for x in llaves:
    print(cliente[x])

print("---------------")

valores=cliente.values()
print(valores)

for x in valores:
    print(x)

print("---------------")

pares=cliente.items()
print(pares)
print("---------------")
