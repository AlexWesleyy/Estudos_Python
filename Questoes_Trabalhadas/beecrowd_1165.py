n=int(input())
r=0
while r<n:
    c=0
    v=int(input())
    for i in range(1,v+1):
        if v%i==0:
            c+=1
    if c==2:
        print(f'{v} eh primo')
    else:
      print(f'{v} nao eh primo')  
    r+=1
    