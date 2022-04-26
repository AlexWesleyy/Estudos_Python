par = []
impar = []
c = p = i = 0
while c < 15:
    n = int(input())
    if n % 2 == 0:
        par.append(n)
        p += 1
    else:
        impar.append(n)
        i += 1
    if p > 4:
        for x in range(0, 5):
            print(f'par[{x}] = {par[x]}')
        par.clear()
        p = 0
    if i > 4:
        for x in range(0, 5):
            print(f'impar[{x}] = {impar[x]}')
        impar.clear()
        i = 0
    c += 1
if i > 0:
    for k in range(i):
        print(f'impar[{k}] = {impar[k]}')
if p > 0:
    for j in range(p):
        print(f'par[{j}] = {par[j]}')
