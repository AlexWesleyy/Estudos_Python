a=int(input())
b=int(input())
if b>a:
    for i in range(a+1,b):
        if i%5==2 or i%5==3:
            print(i)
else:
    for i in range(b+1,a):
        if i%5==2 or i%5==3:
            print(i)