n=int(input())
x=1
while x<=n:
    a, b = input().split()
    a = float(a)
    b = float(b)
    if b==0:
        print("divisao impossivel")
    else:
        div=a/b
        print("{:.1f}".format(div))
    x+=1
       
