inicio, mi, fim, mf = input().split()
inicio = int(inicio)
mi = int(mi)
fim = int(fim)
mf = int(mf)
hora = 0
minuto = 0
if fim > inicio:
    for x in range(inicio, fim):
        hora = hora+1
    if mf > mi:
        for x in range(mi, mf):
            minuto = minuto+1
    if mi > mf:
        hora=hora-1
        minuto = (60-mi)+mf
    if fim-inicio == 1 and minuto == 59:
        hora = 0
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora, minuto))

elif inicio > fim:
    horario = 24-inicio+fim
    if mf > mi:
        for x in range(mi, mf):
            minuto = minuto+1
    if mi > mf:
        minuto = (60-mi)+mf
        horario=horario-1
    if fim-inicio == 1 and minuto == 59:
        hora = 0
    if fim-inicio == (-1) and minuto == 59:
        horario = horario-1
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horario, minuto))
elif inicio==fim and mi!=mf:
    if mf > mi:
        horario=0
        for x in range(mi, mf):
            minuto = minuto+1
    if mi > mf:
        horario=23
        minuto = (60-mi)+mf
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horario, minuto))
else:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
