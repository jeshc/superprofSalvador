frase="Esta es una frase corta"
print(frase[0])

for letra in frase:
    print(f"->{letra}<-", end=" ")
print(letra)
#(<inicio=0>,<fin Obligatorio>,<increento=1>)
for numero in range(20):
  print(numero, end=',')

print(range(20))

for indice in range(len(frase)):
    print(f"-{frase[indice]}- ")


lista=[2,5,4,8,9]
for num in lista:
    print(num)

c=0
while c < len(lista):
    print(lista[c])
    c=c+1
