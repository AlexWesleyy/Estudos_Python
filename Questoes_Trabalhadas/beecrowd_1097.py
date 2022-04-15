i = 0
a = 0.2
for x in range(1, 4):
    j = x
    print('I={:.0f} J={:.0f}'.format(i, j))
while i <= 1.8:
    i = i+a
    for x in range(1, 4):
        j = x+i
        if i == 1.0 or i > 1.8:
            print('I={:.0f} J={:.0f}'.format(i, j))
        else:
            print('I={:.1f} J={:.1f}'.format(i, j))
