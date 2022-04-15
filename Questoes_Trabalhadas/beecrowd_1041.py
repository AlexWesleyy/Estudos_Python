p1, p2 = input().split()
p1 = float(p1)
p2 = float(p2)
if p1 > 0 and p2 > 0:
    print('Q1')
elif p1 > 0 and p2 < 0:
    print('Q4')
elif p1 < 0 and p2 > 0:
    print('Q2')
elif p1 < 0 and p2 < 0:
    print('Q3')
elif p1 == 0:
    if p2 == 0:
        print('Origem')
    else:
        print("Eixo Y")
elif p2 == 0:
    if p1 != 0:
        print("Eixo X")
