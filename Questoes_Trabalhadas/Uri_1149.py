soma=0
c=0
while c<1:
    a,n=input().split()
    a=int(a)
    n=int(n)
    if n>0:
        c+=1
for i in range(0,n):
    soma=a+i
print(soma+a)
