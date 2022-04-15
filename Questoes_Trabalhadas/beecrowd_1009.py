nome = input()
salario = float(input())
vendas = float(input())
comissao = vendas*0.15
total = salario+comissao
print("TOTAL = R$ {:.2f}".format(total))
