A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
#Letra a)
aTriangulo=(A*C)/2
#letra b)
aCirculo=(C*C)*(3.14159)
#letra c)
aTrapezio=((A+B)*C)/2
#letra d)
aQuadrado=B*B
#letra e)
aRetangulo=A*B
print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}".format(aTriangulo,aCirculo,aTrapezio,aQuadrado,aRetangulo))