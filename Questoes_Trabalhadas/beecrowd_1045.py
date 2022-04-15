
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a > b and a > c:
    a = a
    if b > c:
        b = b
        c = c
    else:
        e = b
        b = c
        c = e
elif b > a and b > c:
    e = b
    f = a
    if a > c:
        b = a
        a = e
    else:
        b = c
        a = e
        c = f
elif c > a and c > b:  # 2 3 4
    e = a

    if a > b:
        a = c
        c = b
        b = e
    else:
        a = c
        c = e
elif a == b and a == c:
    a = a
    b = b
    c = c

if a >= b+c:
    print("NAO FORMA TRIANGULO")
else:
    if (a*a) == (b*b)+(c*c):
        print("TRIANGULO RETANGULO")
    if (a*a) > (b*b)+(c*c):
        print("TRIANGULO OBTUSANGULO")
    if (a*a) < (b*b)+(c*c):
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if a == b and a != c or b == c and b != a or a == c and a != b:  # 757
        print("TRIANGULO ISOSCELES")
