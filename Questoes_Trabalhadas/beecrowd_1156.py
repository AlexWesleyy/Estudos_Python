s = 1
b = 1
for i in range(3, 40, 2):
    a = i
    b = b*2
    s = s+(a/b)
print('{:.2f}'.format(s))
