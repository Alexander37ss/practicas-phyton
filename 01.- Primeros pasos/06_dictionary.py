#Los diccionarios son un tipo de estructura donde podemos acceder a sus elementos segun la clave a la que se le haya asignado

mi_diccionario = dict()
print(type(mi_diccionario))

mi_diccionario = {"Nombre": "Alexander", "Apellido": "Palazuelos", "Edad": 19}
print("Mi nombre es %s %s y tengo %d años de edad" %(mi_diccionario["Nombre"],mi_diccionario["Apellido"],mi_diccionario["Edad"]))

mi_diccionario["Ciudad"] = "Lima"
print(mi_diccionario)

del mi_diccionario["Ciudad"]
print("Ciudad" in mi_diccionario)

print(mi_diccionario.items())
print(mi_diccionario.keys())
print(mi_diccionario.values())
#print(mi_diccionario.fromkeys())

nuevo_diccionario = dict.fromkeys(mi_diccionario) #Crea un nuevo diccionario con las claves de otro
print(nuevo_diccionario)


