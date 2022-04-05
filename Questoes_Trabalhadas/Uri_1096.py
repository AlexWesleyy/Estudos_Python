i = 1
j = 8
for x in range(1, 4):
    j -= 1
    print("I={} J={}".format(i, j))
for x in range(1, 4):
    if j ==5:    
        j =10
    j-=1
    print("I={} J={}".format(i+2, j))
for x in range(1, 4):
    if j ==7:    
        j =12
    j-=1
    print("I={} J={}".format(i+4, j))
for x in range(1, 4):
    if j ==9:    
        j =14
    j-=1

    print("I={} J={}".format(i+6, j))
for x in range(1, 4):
    if j ==11:    
        j =16
    j-=1    

    print("I={} J={}".format(i*3*3, j))
