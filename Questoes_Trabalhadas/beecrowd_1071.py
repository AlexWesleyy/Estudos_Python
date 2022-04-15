n1=int(input())
n2=int(input())
soma=0
if n1<n2:
    for n1 in range(n1+1,n2):
        if n1 %2!=0:
            soma=soma+n1
        n1+=1
    print(soma)
elif n1>n2:
    a=n1
    n1=n2
    n2=a
    for n1 in range(n1+1,n2):
        if n1 %2!=0:
            soma=soma+n1
        n1+=1
    print(soma)
else:
    print(0)