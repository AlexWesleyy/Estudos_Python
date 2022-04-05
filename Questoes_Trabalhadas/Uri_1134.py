n = int(input())
alcool = 0
gasolina = 0
disel = 0
c=0
while c <1:
    if n == 1:
        alcool = alcool+1
    elif n == 2:
        gasolina += 1
    elif n == 3:
        disel += 1
    n = int(input())
    if n==4:
        c=c+1
print("MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}".format(alcool, gasolina, disel))
