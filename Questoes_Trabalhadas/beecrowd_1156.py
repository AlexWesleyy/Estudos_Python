s=1+(3/2)+(5/4)+(7/8)
for i in range(9,40,2):
    j=i+1
    s=s+(i/j)
print('{:.2f}'.format(s))