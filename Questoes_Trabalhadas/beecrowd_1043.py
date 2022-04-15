a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)
ab1=abs(b-c)
ab2=abs(a-c)
ab3=abs(a-b)
if ab1<a and a<b+c and ab2<b and b<a+c and ab3<c and c<a+c:
    p=a+b+c
    print("Perimetro = {:.1f}".format(p))
else:
    a=((a+b)*c)/2
    print("Area = {:.1f}".format(a))