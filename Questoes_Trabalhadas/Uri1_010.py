import os

os.system("cls")
code1, number1, price1 = input().split()
code2, number2, price2 = input().split()
code1 = int(code1)
code2 = int(code2)
number1 = int(number1)
number2 = int(number2)
price1 = float(price1)
price2 = float(price2)

valor = (number1 * price1) + (number2 * price2)
print('VALOR A PAGAR: R$ %.2f' % valor)
