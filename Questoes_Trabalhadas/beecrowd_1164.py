n = int(input())
r = 0
perfeito = 0
while r < n:
    v = int(input())
    for i in range(1, v):
        if v % i == 0:
            perfeito += i
    if perfeito == v:
        print(f'{v} eh perfeito')
    else:
        print(f'{v} nao eh perfeito')
    perfeito = 0
    r += 1
