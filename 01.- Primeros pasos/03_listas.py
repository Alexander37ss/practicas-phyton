#Listas (Forma de estructura de datos)

mi_lista = list()

mi_lista.append(1) #Insertar elemento en el ultimo espacio de la lista
mi_lista.append(0)
mi_lista.append(7)
print(mi_lista)

mi_lista.clear() #Vaciar lista
print(mi_lista)

mi_lista = [666, 616, 'El pepe'] #En python se puede combinar tipos de datos diferentes en una misma lista!
print(mi_lista.index(616)) #Retorna el indice que corresponde al argumento enviado

mi_lista = [555, 555] 
print(mi_lista.index(555)) #Si hay dos elementos(o más) iguales retorna ambas posiciones
print(mi_lista.count(555)) #Cuantas veces se repite el argumento

mi_lista = [616, 666]
numero_favorito, segundo_numero_favorito = mi_lista #Asigna el valor segun su posicion a la variable correspondiente
print("Primer numero favorito: ",numero_favorito, "\nSegundo numero favorito: ", segundo_numero_favorito)

numero_favorito, segundo_numero_favorito = mi_lista[1], mi_lista[0] #Tambien se puede especificar si tu numero favorito no es 616 :,(
print("Primer numero favorito: ",numero_favorito, "\nSegundo numero favorito: ", segundo_numero_favorito)

nueva_lista = ["Aqui empieza la nueva lista", 3, 1, 6]
print(mi_lista + nueva_lista) #Se pueden sumar listas asi de sencillo

nueva_lista.insert(0, "Hola") #Añadir un valor en cualquier posicion
print(nueva_lista)

nueva_lista.remove(3) #Elimina el primer elemento que coincida con el parametro
print(nueva_lista)

nueva_lista.pop() #Elimina el ultimo elemento de la lista y lo retorna, actuando como si fuera una cola