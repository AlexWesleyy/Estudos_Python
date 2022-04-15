impar = 0
positivo = 0
negativo = 0
par = 0
for x in range(1, 6):
    a = int(input())
    if a % 2 == 0:
        par += 1
    else:
        impar += 1
    if a >= 0:
        positivo += 1
        if a == 0:
            positivo -= 1
    else:
        negativo += 1


print("{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)".format(
    par, impar, positivo, negativo))
