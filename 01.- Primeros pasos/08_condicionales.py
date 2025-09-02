#Condicionales

dinero = 1000
sexo = "masculino"
deuda = True

if sexo == "femenino" and deuda == False:
    print("Buen dia señorita, su balance de dinero es de ", dinero, " pesos mexicanos. Ninguna deuda pendiente")
elif deuda == False:
    print("Buen dia señor, su balance de dinero es de ", dinero, " pesos mexicanos. Ninguna deuda pendiente")

print("Deuda pendiente, error al intentar acceder a su cuenta bancaria.")
