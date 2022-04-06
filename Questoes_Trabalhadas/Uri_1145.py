x, y = input().split()
x = int(x)
y = int(y)
count = 0
for i in range(1, y+1):
    if count == x-1:
        print(i)
        count = count+1
    else:
        print(i, end=" ")
        count = count+1
    if count == x:
        count = 0
