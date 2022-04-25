r = 0
lista = []
listaPar = []
listaImpar = []
while r < 15:
    n = int(input())
    lista.append(n)
    r += 1
for i in range(0, 15):
    if lista[i] % 2 == 0:
        listaPar.append(lista[i])
    else:
        listaImpar.append(lista[i])
for i in range(0, 5):
    if len(listaPar) > 0:
        print(f'par [{i}] = {listaPar[i]}')
for i in range(0, len(listaImpar)):
    if len(listaImpar) > 0:
        print(f'impar [{i}] = {listaImpar[i]}')
while len(listaImpar) > 5:
    del listaImpar[0:5]
    if len(listaImpar) > 5:
        for i in range(0, len(listaImpar)-5):
            print(f'impar [{i}] = {listaImpar[i]}')
    else:
        for i in range(0, len(listaImpar)):
            print(f'impar [{i}] = {listaImpar[i]}')
while len(listaPar) > 5:
    del listaPar[0:5]
    if len(listaPar) > 5:
        for i in range(0, len(listaPar)-5):
            print(f'par [{i}] = {listaPar[i]}')
    else:
        for i in range(0, len(listaPar)):
            print(f'par [{i}] = {listaPar[i]}')
