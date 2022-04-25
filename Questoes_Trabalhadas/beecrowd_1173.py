n = int(input())
lista = []
lista.append(n)
print(f'N[0] = {n}')
for i in range(1, 10):
    lista.append(lista[i-1]*2)
    print(f'N[{i}] = {lista[i]}')
