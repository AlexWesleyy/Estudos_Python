

a=int(input())
b=int(input())
soma=0
if b>a:
    for i in range(a,b+1):
        if i%13!=0:
            soma=soma+i
    print(soma)
else:
    for i in range(b,a+1):
        if i%13!=0:
            soma=soma+i
    print(soma)

    