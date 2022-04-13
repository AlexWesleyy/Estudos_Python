
x = list(map(int, input().split()))
i = 1
soma = 0

while x[i] <= 0:
    print(x[i])
    if x[i] <=0:
        i = i + 1
    if x[i] > 0:
        break

for c in range(0,x[i]):
    soma = soma + x[0] + c
   
print(soma)