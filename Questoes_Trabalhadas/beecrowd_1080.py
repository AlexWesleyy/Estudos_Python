x = 0
for i in range(1, 101):
    a = int(input())
    if a > x:
        maior = a
        posicao = i
        x = a
print(maior)
print(posicao)
