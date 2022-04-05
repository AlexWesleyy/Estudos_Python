soma = 0
x = 1
r = 0
while x <= 2:
    n = float(input())
    if n >= 0 and n <= 10:
        soma = soma+n
        media = soma/2
        x += 1
    else:
        print("nota invalida")
print("media = {:.2f}".format(media))
while r < 1:
    print("novo calculo (1-sim 2-nao)")
    escolha = int(input())
    while escolha < 1 or escolha > 2:

        print("novo calculo (1-sim 2-nao)")
        escolha = int(input())
    if escolha == 1:
        soma = 0
        x = 1
        while x <= 2:
            n = float(input())
            if n >= 0 and n <= 10:
                soma = soma+n
                media = soma/2
                x += 1
            else:
                print("nota invalida")
        print("media = {:.2f}".format(media))
    if escolha == 2:
        r += 1
