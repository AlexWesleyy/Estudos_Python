idade=int(input())
ano=idade//365
restoAno=idade-ano*365
mes=restoAno//30
restoMes=restoAno-mes*30
print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(ano, mes, restoMes))