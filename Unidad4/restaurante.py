def menu_select(mesa,comensal ,entrada, medio, fuerte, postre):
    print(f"La selección del comensal {comensal} de la mesa {mesa}")
    print(f"Entrada: {entrada}")
    print(f"Segundo: {medio}")
    print(f"Fuerte:  {fuerte}")
    print(f"Postre:  {postre}")
    return None

menu_select(3,2,"Ensalada verde","crema de zanahoria","filete","Pastel de elote")

print("-------------------------------------------------------------------------")
menu_select("crema de zanahoria","Ensalada verde","filete","Pastel de elote",3,2)
