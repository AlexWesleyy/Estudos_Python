diaInicial = input().split()
horaInicial = input().split()
diaFinal = input().split()
horaFinal = input().split()
di, df = int(diaInicial[1]), int(diaFinal[1])
hi, mi, si = int(horaInicial[0]), int(horaInicial[2]), int(horaInicial[4])
hf, mf, sf = int(horaFinal[0]), int(horaFinal[2]), int(horaFinal[4])

minuto_seg = 60 #1min em segundos
hora_seg = minuto_seg * 60  #1 hora em segundos
dia_seg = hora_seg * 24 #1 dia em segundos
i = si + mi*minuto_seg + hi*hora_seg + di*dia_seg #convertendo tudo em segundos
f = sf + mf*minuto_seg + hf*hora_seg + df*dia_seg
if i < f:   #2 1 10 10
            #4 2 20 20
    tempo = f - i
    dias = int(tempo/dia_seg)
    tempo = tempo%dia_seg
    horas = int(tempo/hora_seg)
    tempo = tempo%hora_seg
    minutos = int(tempo/minuto_seg)
    tempo = tempo%minuto_seg
    segundos = tempo
    print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dias, horas, minutos, segundos))