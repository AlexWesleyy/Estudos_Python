while b != 0 or a != 0:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if b > a:
        for a in range(a, b+1):
            soma = soma+a
            print(soma)
            soma = 0
    if b < a:
        for b in range(b, a+1):
            soma = soma+b
            print(soma)