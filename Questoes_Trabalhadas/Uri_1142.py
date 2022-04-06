n=int(input())
for i in range(1,n*4+1):
    if i%4!=0:
        print(i,end=" ")
    if i%4==0:
        print("PUM")