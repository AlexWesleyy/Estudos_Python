n = int(input())
a = 0
b = 1
soma = 0

print(a, end=' ')
print(b, end=' ')
for i in range(0, n-2):
    soma = a+b
    a=b
    b=soma
    if i==n-3:
         print(soma)
    if i<n-3:
        print(soma, end=' ')
