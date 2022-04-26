n=int(input())
a=input().split()
menor=0
for i in range(len(a)):
    a[i]=(int(a[i]))
menor=a[0]
p=0
for i in range(0,len(a)):
    if a[i]<menor:
        menor=a[i]
        p=i
print(f'Menor valor: {menor}\nPosicao: {p}')