n=int(input())
if n>1 and n<1000:

    for x in range(1,n+1):
        quadrado=x**2
        cubo=x**3
        print(x,quadrado,cubo)
else: 
    exit


