#Un set es una estructura de datos parecida a la lista con la peculiareidad de que sus elementos siempre estaran en desorden.

mi_set = set()
print(type(mi_set))

mi_set = {"Alexander", "Palazuelos", 19}
print(mi_set)

mi_set.add(777) #Anadir un elemento
print(mi_set)

mi_set.remove(777) #Eliminar un elemento
print(mi_set)

mi_set.clear() #Borra todos los elementos dentro del set
print(mi_set)

mi_set = {"Alexander", "Palazuelos", 19}
mi_otro_set = {"Mexico", "Polonia", "Tailandia", "Marruecos", "Alexander"}
print(mi_otro_set)
mi_otro_set = mi_otro_set.union(mi_set) #Une dos sets sin contar repetidos
print(mi_otro_set.difference(mi_set)) #Retorna los elementos que se encuentran en mi_otro_set y que no se encuentran en mi_set


