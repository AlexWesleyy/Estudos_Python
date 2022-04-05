cod, qtd=input().split()
cod=int(cod)
qtd=int(qtd)
if cod==1:
    valor=4.00*qtd
elif cod==2:
    valor=4.50*qtd
elif cod==3:
    valor=5.00*qtd
elif cod ==4:
    valor=2.00*qtd
else:
    valor=1.50*qtd
print("Total: R$ {:.2f}".format(valor))