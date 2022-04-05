a, b = input().split()
a = int(a)
b = int(b)
while a != b:
    if b > a:
        print("Crescente")
            
    else:
        print("Decrescente")
    a, b = input().split()
    a = int(a)
    b = int(b)
