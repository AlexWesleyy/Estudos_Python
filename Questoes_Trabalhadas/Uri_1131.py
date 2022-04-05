a, b = input().split()
a = int(a)
b = int(b)
r = 0
total = 0
if a > b:
    inter = 1
    gremio = 0
    empate = 0
elif b < a:
    gremio = 1
    inter = 0
    empate = 0
else:
    empate = 1
    gremio = 0
    inter = 0
print("Novo grenal (1-sim 2-nao)")
resposta = int(input())
if resposta == 1:
    while r < 1:
        a, b = input().split()
        a = int(a)
        b = int(b)
        if a > b:
            inter += 1
        elif b > a:
            gremio += 1
        else:
            empate += 1
        total += 1
        print("Novo grenal (1-sim 2-nao)")
        resposta = int(input())
        if resposta == 2:
            r += 1
if resposta == 2:
    exit
print("{} grenais".format(total+1))
print("Inter:{}".format(inter))
print("Gremio:{}".format(gremio))
print("Empates:{}".format(empate))
if inter>gremio:
    print("Inter venceu mais")
elif gremio>inter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
