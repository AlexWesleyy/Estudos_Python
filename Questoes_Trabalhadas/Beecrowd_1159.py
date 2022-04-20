n = int(input())
for i in range(1, n+1):
    c = 0
    pa, pb, g1, g2 = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)
    while pb >= pa:
        pa = int(pa*(1+g1/100))
        pb = int(pb*(1+g2/100))
        c += 1
        if c >= 101:
            print('Mais de 1 seculo.')
            break
    if c <= 100:
        c = int(c)
        print('{} anos.'.format(c))
