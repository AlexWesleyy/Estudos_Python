
x, y = input().split()
x = int(x)
y = int(y)
cont=0
for i in range(1, y+1):
    print(f"{i} ",end="")
    cont += 1
    if cont == x:
        print()
        cont = 0
           