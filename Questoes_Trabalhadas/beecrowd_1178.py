n=float(input())
lista=[]
lista.append(n)
for i in range(1,100):
    lista.append(lista[i-1]/2)
for i in range(0,100):
    print(f'N[{i}] = {lista[i]:.4f}')