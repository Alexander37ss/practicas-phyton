n = int(input())
monedas = list(map(int, input().split()))

monedas.sort()
hijo_uno = monedas[-1] 
hijo_dos = 0

for i in range(n - 2, -1, -1):
    if hijo_uno >= hijo_dos:
        hijo_dos += monedas[i]
    else:
        hijo_uno += monedas[i]

print(abs(hijo_uno - hijo_dos))