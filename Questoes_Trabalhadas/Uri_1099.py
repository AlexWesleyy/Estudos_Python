n=int(input())
soma=0
for x in range(1,n+1):
    a,b=input().split()
    a=int(a)
    b=int(b)
    if b-1==a or a==b:
        print(0)
    if b>a:
        for a in range(a+1,b):
            if a%2!=0:
                soma=soma+a
            if a==b-1:
                print(soma)
                soma=0
    if b<a:
        for b in range(b+1,a):
            if b%2!=0:
                soma=soma+b
            if b==a-1:
                print(soma)
                soma=0
                

        
            
