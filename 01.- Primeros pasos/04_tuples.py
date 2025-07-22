#Tuples o tuplas

mi_tupla = tuple()

mi_tupla = (1, 2.1, "Peru")
print(mi_tupla)
print(type(mi_tupla))

print(mi_tupla.count("Peru"))
print(mi_tupla.index("Peru"))

mi_tupla[2] = "Mexico"
print(mi_tupla) #Va a arrojar un error debido que las tuplas son inmutables, es decir, no pueden ser modificadas
