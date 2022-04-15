sal = float(input())
if sal <= 2000:
    print("Isento")
elif sal <= 3000:
    taxa = (sal-2000)*0.08
    print("R$ {:.2f}".format(taxa))
elif sal <= 4500:
    taxa = (sal-3000)*0.18+1000*0.08
    print("R$ {:.2f}".format(taxa))
else:
    taxa = (sal-4500)*0.28+1500*0.18+1000*0.08
    print("R$ {:.2f}".format(taxa))
