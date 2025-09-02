#Diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35, "Lenguajes": {"Python", "Swift", "Kotlin"}}
print("Diccionario uno: ", my_other_dict)

my_dict = {"Nombre":"Alexander", "Apellido":"Palazuelos", "Edad":20, "Lenguajes": {"Javascript", "Laravel no es un lenguaje :c", "Kotlin"}}
print("Diccionario dos: ",my_dict)

print("Lenguajes en diccionario dos: ", my_dict["Lenguajes"])
print(my_dict.keys())

my_dict["Lenguajes"] = 1

print(my_dict)

print("Alexander" in my_dict.values())