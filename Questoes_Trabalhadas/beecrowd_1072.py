n=int(input())
x=0
c=0
o=0
for x in range(x,n):
    v=int(input())
    if v>=10 and v<=20:
        c+=1
    else:
        o+=1
print("{} in\n{} out".format(c,o))
