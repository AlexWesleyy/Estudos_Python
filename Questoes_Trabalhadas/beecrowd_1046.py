inicio, fim = input().split()
inicio = int(inicio)
fim = int(fim)
hora = 0
if fim > inicio:
    for x in range(inicio, fim):
        hora = hora+1
    print("O JOGO DUROU {} HORA(S)".format(hora))
elif inicio > fim:
    horario = 24-inicio+fim
    print("O JOGO DUROU {} HORA(S)".format(horario))
else:
    print("O JOGO DUROU 24 HORA(S)")
