frase1="Si funciona... no lo arregles."
print(frase1.find('l'))  # 18

contador=0
longitud=len(frase1)
while contador < longitud:
    if frase1[contador]=='l' :
        print(f" la letra l esta en la posicion {contador}")
        break
    contador += 1 # contador=contador +1

print("--------------------------------------")
frase2="Durante mucho tiempo me extrañó el hecho de que algo tan caro y tan vanguardista fuera tan inútil. Y luego pensé que la computadora es una máquina estúpida con la capacidad de hacer cosas increíblemente inteligentes, mientras que los programadores de computadoras son gente inteligente con la capacidad de hacer cosas increíblemente estúpidas. En pocas palabras, son la pareja perfecta.- Linus Torvalds"
longitud=len(frase2)
contador=0
frecuencia=0
letra=input("ingresa la letra a buscar:")
while contador < longitud:
    if frase2[contador] == letra :
        frecuencia +=1
    contador +=1
print(f'La frase 2 contiene {frecuencia} letras {letra}')
