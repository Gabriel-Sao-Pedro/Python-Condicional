n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))

m = n1 + n2

if (m >= 60.00):
    print("NOTA FINAL = {:.1f}".format(m))
    print("APROVADO!!")
else:
    print("NOTA FINAL = {:.1f}".format(m))
    print("REPROVADO")
