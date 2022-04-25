lista = []
lista2 = []
for i in range(0, 20):
    lista.append(int(input()))
lista2 = lista[::-1]
for i in range(0, 20):
    print(f'N[{i}] = {lista2[i]}')
