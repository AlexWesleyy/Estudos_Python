matriz=[]
r=0
while r<12:
    matriz.append([0,0,0,0,0,0,0,0,0,0,0,0])
    r+=1
for l in range(0,12):
    for c in range(0,12):
        matriz[l][c]=randint(0,9)
for l in range(0,12):
    for c in range(0,12):
        print(f'\nO valor na posição [{l}][{c}]: {matriz[l][c]}',end='')
    print()   
