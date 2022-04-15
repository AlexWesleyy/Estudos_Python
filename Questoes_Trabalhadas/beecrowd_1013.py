
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
MaiorAB = (a+b+abs(a-b))/2
MaiorABC=(c+MaiorAB+abs(c-MaiorAB))/2
print("{:.0f} eh o maior".format(MaiorABC))
