A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
delta = (B*B)-4*A*C
if A == 0 or delta < 0:
    print("Impossivel calcular")
else:
    r1 = ((-B)+delta**0.5)/(2*A)
    r2 = ((-B)-delta**0.5)/(2*A)
    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))
