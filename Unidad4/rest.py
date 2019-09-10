def menu_select(mesa,comensal ,entrada, medio, fuerte, postre):
   print(f"La selección del comensal {comensal} de la mesa {mesa}")
   print(f"Entrada: {entrada}")
   print(f"Segundo: {medio}")
   print(f"Fuerte:  {fuerte}")
   print(f"Postre:  {postre}")
   return None

menu_select(3,2,"Ensalada verde","crema de zanahoria","filete","Pastel de elote")

menu_select(entrada="crema de zanahoria",medio="Ensalada verde",fuerte="filete",postre="Pastel de elote",mesa=3,comensal=2)
