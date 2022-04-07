from posixpath import split


a,n=input().split()
a=int(a)
n=int(n)
soma=a
for i in range(0,n):
    soma+=i
print(soma+(soma-1))
