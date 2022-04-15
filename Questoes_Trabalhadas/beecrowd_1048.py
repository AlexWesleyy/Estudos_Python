valor = float(input())
if valor >= 0 and valor <= 400.00:
    nvalor = valor*1.15
    reajuste = valor*0.15
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 15 %".format(
        nvalor, reajuste))
elif valor > 400 and valor <= 800.00:
    nvalor = valor*1.12
    reajuste = valor*0.12
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 12 %".format(
        nvalor, reajuste))
elif valor > 800 and valor <= 1200.00:
    nvalor = valor*1.10
    reajuste = valor*0.10
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 10 %".format(
        nvalor, reajuste))
elif valor > 1200 and valor <= 2000.00:
    nvalor = valor*1.07
    reajuste = valor*0.07
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 7 %".format(
        nvalor, reajuste))
else:
    nvalor = valor*1.04
    reajuste = valor*0.04
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 4 %".format(
        nvalor, reajuste))
