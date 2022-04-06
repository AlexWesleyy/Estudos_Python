c=0
while c<1:
    n=int(input())
    count=0
    for i in range(1,n+1): 
        if count == n-1: 
            print(i) 
            count = count+1 
        else: 
            print(i,end=" ") 
            count = count+1 
        if count==n: 
            count=0
    if n==0:
        c+=1