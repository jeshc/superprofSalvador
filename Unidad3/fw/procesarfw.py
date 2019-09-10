
import re
import pandas as pd

# Funcion que busca el inicio de las IP
def buscar_inicio(lista):
    indice=0
    for linea in lista:
        if 'IKE Peer:' in linea:
            break
        indice += 1
    return indice

#Funcion que extrae datos independientes y los mete a una serie para pandas
def extrae(lista,index):
    reporte={'id':[],'ip':[]}
    while index <= len(lista)-1:
        lista[index]=re.sub(' +',' ',lista[index])
        separado=lista[index].split(' ')
        #print(separado)
        reporte['id'].append(int(separado[0]))
        reporte['ip'].append(separado[3])
        index +=3
    return reporte


# Funcion que lee el archivo y lo regresa como lista de renglones
def obtener_datos_crudos():
    data=open('C:\\Users\\LABCOM2\\Documents\\clasesPython\\superprofEnrique\\Unidad3\\fw\\ejemplo.txt','r').readlines()
    for index in range(len(data)):
        data[index]=data[index].strip()
    return data

# main
crudos=obtener_datos_crudos()
resultado=extrae(crudos,buscar_inicio(crudos))
#Panda
df = pd.DataFrame(resultado,index=resultado['id'])
print(df)
print((df.groupby('ip').size()).to_string())
print('----------------------------------------------')
#print(resultado)
