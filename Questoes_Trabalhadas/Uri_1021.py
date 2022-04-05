valor = float(input())
# Notas
nota100 = valor//100
resto100 = valor-nota100*100
print("NOTAS:\n{:.0f} nota(s) de R$ 100.00".format(nota100))
nota50 = resto100//50
resto50 = resto100-nota50*50
print("{:.0f} nota(s) de R$ 50.00".format(nota50))
nota20 = resto50//20
resto20 = resto50-nota20*20
print("{:.0f} nota(s) de R$ 20.00".format(nota20))
nota10 = resto20//10
resto10 = resto20-nota10*10
print("{:.0f} nota(s) de R$ 10.00".format(nota10))
nota5 = resto10//5
resto5 = resto10-nota5*5
print("{:.0f} nota(s) de R$ 5.00".format(nota5))
nota2 = resto5//2
resto2 = resto5-nota2*2
print("{:.0f} nota(s) de R$ 2.00".format(nota2))
# Moedas
moeda1 = resto2//1
resto1 = resto2-moeda1*1
print("MOEDAS:\n{:.0f} moeda(s) de R$ 1.00".format(moeda1))
moeda50 = resto1//0.50
resto050 = resto1-moeda50*0.50
print("{:.0f} moeda(s) de R$ 0.50".format(moeda50))

moeda25 = resto050//0.25
resto025 = resto050-moeda25*0.25
print("{:.0f} moeda(s) de R$ 0.25".format(moeda25))

moeda10 = resto025//0.10
resto010 = resto025-moeda10*0.10
print("{:.0f} moeda(s) de R$ 0.10".format(moeda10))

moeda05 = resto010//0.05
resto005 = resto010-moeda05*0.05
print("{:.0f} moeda(s) de R$ 0.05".format(moeda05))

moeda01 = resto005//0.01
print("{:.0f} moeda(s) de R$ 0.01".format(moeda01))
