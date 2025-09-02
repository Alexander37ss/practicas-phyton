#Sets

my_set = set()
my_other_set = {}

#print(type(my_set))
#print(type(my_other_set))

my_other_set = {"Azul", "Rojo", "Amarillo", "Verde", 1, 2 ,3}

print(type(my_other_set))
print(len(my_other_set))
print(my_other_set) #El orden de los elementos es aleatorio

my_other_set.add("hola") #La estructura de datos "Set" no admite elementos repetidos
my_other_set.add("hola")
my_other_set.remove("hola")
my_other_set.clear

my_set.add(1)
my_set.add(2)
print(my_other_set.intersection(my_set)) #Imprime los elementos compartidos entre dos Sets



