#Concatenar distintas variables con buenas practicas
nombre, apellido, edad = 'Arturo', "Ramirez", 41

print("Mi nombre es {} {} y tengo {} años de edad".format(nombre,apellido,edad))
print("Mi nombre es %s %s y tengo %d años de edad" %(nombre, apellido, edad))
print(f"Mi nombre es {nombre} {apellido} y tengo {edad} años de edad")
#Nota: Las tres maneras son correctas, es cuestion de preferencia personal.

#Desempaquetado de caracteres
lenguaje = "Phyton"
a, b, c, d, e, f = lenguaje #A cada variable se le asigna una letra en orden izquierda-derecha
print(a,b,c,d,e,f)

#Manipulacion con slice
lenguaje_slice = lenguaje[1:3]
print(lenguaje_slice)

lenguaje_slice = lenguaje[0:1]
print(lenguaje_slice)

lenguaje_slice = lenguaje[::-1]
print(lenguaje_slice)

#Diversas funciones
print(lenguaje.capitalize())#Primer letra de cada palabra en mayuscula
print(lenguaje.upper())#Mayuscula
print(lenguaje.lower())#Minuscula
print(lenguaje.count("P")) #Cuenta cuantas veces se encuentra un caracter en un string.
print(lenguaje.count("p"))#Discrimina entre minusculas y mayusculas.
