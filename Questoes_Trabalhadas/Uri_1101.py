a, b = input().split()
soma = 0
soma2 =0
a = int(a)
b = int(b)
while a > 0 and b > 0:
    if b > a:
        for a in range(a, b+1):
            soma = soma+a
            print(a, end=" ")
            if a == b:
                print("Sum={}".format(soma))
                soma = 0
    if b < a:
        soma2 = 0
        for b in range(b, a+1):
            soma2 = soma2+b
            print(b, end=" ")
            if b == a:
                # print(a)
                print("Sum={}".format(soma2))
    a, b = input().split()
    a = int(a)
    b = int(b)
