n = int(input())
coelhos = 0
ratos = 0
sapos = 0
soma = 0
for i in range(1, n+1):
    v, s = input().split()
    v = int(v)
    soma = v+soma
    if s == 'C':
        coelhos += v
    if s == 'R':
        ratos += v
    if s == 'S':
        sapos += v
    pc = (coelhos/soma)*100
    pr = (ratos/soma)*100
    ps = (sapos/soma)*100


print("Total: {} cobaias".format(soma))
print("Total de coelhos: {}".format(coelhos))
print("Total de ratos: {}".format(ratos))
print("Total de sapos: {}".format(sapos))
print("Percentual de coelhos: {:.2f} %".format(pc))
print("Percentual de ratos: {:.2f} %".format(pr))
print("Percentual de sapos: {:.2f} %".format(ps))
