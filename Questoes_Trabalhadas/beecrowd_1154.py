r=0
soma=0
contador=0
while r<1:
    n=int(input())
    if n<0:
        r+=1
    if n>=0:
        soma+=n
        contador+=1
media=soma/contador
print('{:.2f}'.format(media))