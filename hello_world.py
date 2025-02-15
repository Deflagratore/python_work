lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for number in lista:
    print(number)

lista2 = []
n = 1_000_000

for numero in range(1, n + 1):
    lista2.append(numero)

print(min(lista2))
print(max(lista2))
print(sum(lista2))

lista3 = []

for numero in range(1, 21, 2):
    lista3.append(numero)

print(lista3)

lista4 = []

for numero in range(3, 31, 3):
    lista4.append(numero)

print(lista4)

lista5 = []

for numero in range(1, 11):
    lista5.append(numero ** 3)

print(lista5)

lista6 = [valores ** 3 for valores in range(1, 11)]
print(lista6)