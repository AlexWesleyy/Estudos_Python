import math
from posixpath import split


x1, y1 = input().split()
x2, y2 = input().split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
p1 = ((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1))
Distancia = math.sqrt(p1)
print("{:.4f}".format(Distancia))
