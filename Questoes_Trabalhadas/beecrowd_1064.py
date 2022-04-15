maior = 0
soma = 0
for x in range(1, 7):
    a = float(input())
    if a > 0:
        maior += 1
        soma = a+soma
print("{} valores positivos\n{:.1f}".format(maior, soma/maior))
