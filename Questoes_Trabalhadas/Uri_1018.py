
valor = int(input())
print(valor)
nota100 = valor//100  # valor notas
n100 = valor-nota100*100  # troco
print("{} nota(s) de R$ 100,00".format(nota100))
nota50 = n100//50
n50 = n100-nota50*50
print("{} nota(s) de R$ 50,00".format(nota50))
nota20 = n50//20
n20 = n50-nota20*20
print("{} nota(s) de R$ 20,00".format(nota20))
nota10 = n20//10
n10 = n20-nota10*10
print("{} nota(s) de R$ 10,00".format(nota10))
nota5 = n10//5
n5 = n10-nota5*5
print("{} nota(s) de R$ 5,00".format(nota5))
nota2 = n5//2
n2 = n5-nota2*2
print("{} nota(s) de R$ 2,00".format(nota2))
nota1 = n2//1
n1 = n2-nota1*1
print("{} nota(s) de R$ 1,00".format(nota1))
