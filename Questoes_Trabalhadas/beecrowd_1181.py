from random import randint
matriz=[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]
o=int(input())
s=str(input()).upper()
soma=media=0
for l in range(0,12):
    for c in range(0,12):
        matriz[l][c]=float(input())
for c in range(0,12):
    soma+=matriz[o][c]
    if s=='M':
        media=soma/12  
if s=='S':
    print(f'{soma:.1f}')
if s=='M':
        print(f'{media:.1f}')
