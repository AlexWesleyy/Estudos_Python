fibonacci=[]
fibonacci.append(0)
fibonacci.append(1)
r=0
n=int(input())
for i in range(2,1000):
    fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
while r<n:
    u=int(input())
    for p,v in enumerate(fibonacci):
        if p==u:
            print(f'Fib({u}) = {v}')
    r+=1
