
s= "programacion con python 3"

#print(dir(s))
print('--------------------')

print(s.capitalize())

print(s.upper())

print('case fold(lower case agresivo):'+s.casefold())

print('Center:'+s.center(40,'f'))

s= "   programacion con python 3       "
print(s)
print(s.strip())

print("Count:" +s.upper())



#Split
l=s.split()
print(l)
#Slicing
print(s[4:8])  #del caracter 4 al 7, no incluye el limite sup
print(s[4:])   
print(s[:4])
print(s[:])
