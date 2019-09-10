a=0
b=0

def sumar(a,b):
    c=a+b
    if c == 0:
        print('Nada')
    else:
        print(c)


sumar(a,b)
print("-------------")

print("Argumentos posicionales:")
def menu_select3(**comanda):
    print (comanda.keys())
    for x in comanda:
        print (f"{x.upper()}: {comanda[x]}")

    #print(f'Comanda:{comanda}')
    return None

menu_select3(mesa=3,comensal=2,entrada="Ensalada verde", medio="crema de z" +\
"anahoria",fuerte="filete",adicionales="Filete término medio, la ensalada sin" +\
"ningun tipo de semilla, Adereso Ranch")


def funcion_externa(nombre):
    def funcion_interna(v):
        print(v[::-1])
    nombre=nombre.upper()
    funcion_interna(nombre)
funcion_externa('José José, El príncipe de la canción mexicana')

"""
->Costo total a cobrar al cliente
->Preguntar cuantos productos va a comprar
->Preguntar si los va a recoger o no

Cada producto tiene un costo de $450.0
Cuando se consumen de entre 3 y 5 productos el precio unitario es de $425.0
Arriba de 5 piezas el producto cuesta: $400.0
El IVA a cobrar es de 16%.
Gastos de envío: $29.0 por pieza y $0 si el cliente va por ellos a la tienda.
"""
num_productos=input("Ingrese la cantidad de productos a comprar: ")
envio=input("Recoge el pedido? : 0 para no, 1 para si")
envio=int(envio)
num_productos=int(num_productos)

def precio_producto (np,en):
    def iva_int(cst):
        cst=cst*1.16
        return cst

    def env(ct):
        tot=0
        tot=29.0*ct
        return tot

    if np <3:
        costo=450*np
    elif np >= 3 and np <=5:
        costo=425*np
    else :
        costo=400*np

    if en==1:
        v=env(np)
        costo=costo+v
        print(costo)


    return iva_int(costo)










print(precio_producto(num_productos,envio))
