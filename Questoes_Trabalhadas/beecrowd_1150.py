x=int(input())
z=int(input())
r=0
soma=0
j=1
cont=0
while r<1:
    if z<=x:
        z=int(input())
    else:
        r+=1
for i in range(x,z):
    soma=soma+i
    cont=cont+j
    if soma>z:
        break
print(cont)
