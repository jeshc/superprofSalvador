def sumar(a, b):
    c=a+b
    return c

x=sumar(4,6)
print(f"4 + 6 = {x}")

print("********** ------------------------++++++++++")
def sumar(a, b):
    print(f"{a} + {b} = {a+b}")
    return None

#Llamada
sumar(4,6)

########### None ###############

def multiplica(valor, veces):
    if valor == None:
        print(' Nada que imprimir')
    else:
        print(veces*valor)

multiplica('a',5)
multiplica(None,5)
multiplica(10,6)
multiplica("josé",3)

########### Posicio de argumentos ###############
def menu_select(mesa,comensal ,entrada, medio, fuerte, postre):
    print(f"La selección del comensal {comensal} de la mesa {mesa}")
    print(f"Entrada: {entrada}")
    print(f"Segundo: {medio}")
    print(f"Fuerte:  {fuerte}")
    print(f"Postre:  {postre}")
    return None

menu_select(3,2,"Ensalada verde","crema de zanahoria","filete","Pastel de elote")

menu_select("crema de zanahoria","Ensalada verde","filete","Pastel de elote",3,2)

menu_select(medio="crema de zanahoria",entrada="Ensalada verde",fuerte="filete",postre="Pastel de elote",mesa=3,comensal=2)

########### Valores por defecto ###############
print("valores por defecto:")
def menu_select(mesa,comensal ,entrada, medio, fuerte, postre='Gelatina de limón'):
   print(f"La selección del comensal {comensal} de la mesa {mesa}")
   print(f"Entrada: {entrada}")
   print(f"Segundo: {medio}")
   print(f"Fuerte:  {fuerte}")
   print(f"Postre:  {postre}")
   return None

menu_select(medio="crema de zanahoria",entrada="Ensalada verde",fuerte="filete",mesa=3,comensal=2)

#!!!!!!!!!!!!!!!!  OJO con valores por defecto !!!!!!!!!!!!!!!!

def registro_impuestos(impuesto_a_cobrar,lista_impuestos=[]):
    lista_impuestos.append(impuesto_a_cobrar)
    print(lista_impuestos)

registro_impuestos(16)  ## [16]
registro_impuestos(30)  ## [30]????

################# Argumentos poscicionales   #######


def imprime_argumentos( *argumentos ):
    print("Estos son los argumentos recibidos:",argumentos)

imprime_argumentos()        # ()
imprime_argumentos(1,2,3)   # (1, 2, 3)
imprime_argumentos("hola",10,12.1,True,("esto","es una", "tupla"), ["una","lista"],{'id':1,'desc':'un diccionario'})


###########  argumentos posicionales * tuplas ###############
print("Argumentos posicionales:")
def menu_select2(mesa,comensal ,entrada, medio, fuerte,*adicionales):
   print(f"La selección del comensal {comensal} de la mesa {mesa}")
   print(f"Entrada: {entrada}")
   print(f"Segundo: {medio}")
   print(f"Fuerte:  {fuerte}")
   print(f"Instrucciones adicionales:{adicionales}")
   return None

menu_select2(3,2,"Ensalada verde", "crema de zanaHoria","filete", "Filete término medio","la ensalada sin ningun tipo de semilla","Adereso Ranch")




###########  argumentos posicionales ** Diccionarios ###############
print("Argumentos posicionales:")
def menu_select2(**comanda):
    print(f"\tDetalle:")
    llaves=comanda.keys()
    for llave in llaves:
        print(f"\t{llave.upper()}:{str(comanda[llave]).lower().capitalize()}")

    return None

menu_select2(mesa=3,comensal=2,entrada="Ensalada verde", medio="crema de zanahoria",fuerte="filete",adicionales="Filete término medio, la ensalada sin ningun tipo de semilla, Adereso Ranch")

######### first class funtions ###########
#Básico
print("Probando first class function")
def mi_print(funcion):
    funcion("Hola")

mi_print(print)


#intermedio
def saludar(cadena):
    print(f"Hola {cadena }, buenos días!")

def ejecutar_saludo(nombre,paterno, materno, funcion):
    c=f" {nombre} {paterno} {materno}"
    funcion(c)

ejecutar_saludo('Jose','Garcia', 'perez', saludar)


# avanzado
def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def calculadora(opernado1, operando2, operacion):
    print(operacion(opernado1,operando2))


calculadora(5,3,sumar)
calculadora(5,3,restar)
calculadora(5,3,multiplicar)


############## inner
#### ejemplo 1

def funcion_externa(nombre):
    def funcion_interna(v):
        print(v[::-1])
    nombre=nombre.upper()
    funcion_interna(nombre)
funcion_externa('José José, El príncipe de la canción mexicana')

### ejemplo 2
def calcular_venta(num_productos,envio_paqueteria):
    print('Iniciando venta')
    def calcular_descuentos(cantidad):
        total=0.0
        if cantidad > 0 and cantidad < 3:
            print('kllkjkljl')
            total =cantidad*450.0
        elif cantidad >= 3 and cantidad <=5:
            total=cantidad*425.0
        elif cantidad > 5:
            total=cantidad*400.0
        else:
            print("Error, valor no válido")
        print(total)
        return total
    def calcular_envio(cantidad,paqueteria):
        costos_envio=0.0
        if(paqueteria):
            costos_envio=cantidad*29.0
        return costos_envio

    return (calcular_descuentos(num_productos)+calcular_envio(num_productos,envio_paqueteria))*1.16

print(f"Total:{'%.3f'%calcular_venta(3,True)}")
