leer = input().split()
m = int(leer[0])
n = int(leer[1])

suma = m + n

if suma < 0:
    suma *= -1

print(suma)