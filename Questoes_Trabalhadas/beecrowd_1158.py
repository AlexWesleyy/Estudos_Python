n = int(input())
i = 1
c = 1
soma = 0
while i <= n:  # 1<=1
    x, y = input().split()
    x = int(x)
    y = int(y)
    while c <= y*2:  # 3<=3
        if x % 2 != 0:  # 4/2!=0
            soma += x  # 5
        x += 1
        c += 1
    print('{}'.format(soma))
    i += 1
    c = 1
    soma = 0
