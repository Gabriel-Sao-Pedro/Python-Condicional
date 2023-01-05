from math import sqrt

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

d = (b**2) - (4*(a)*(c))
if (d > 0):
    r = sqrt(d)
    x1 = (((-b) + (r)) / (2*a))
    x2 = (((-b) - (r)) / (2*a))

    print("X1 = {:.4f}".format(x1))
    print("X2 = {:.4f}".format(x2))
elif (d == 0):
    x = (-b) / 2*a
    print("X = {:.4f}".format(x))
    print("So existe uma raiz!!")
else:
    print("ESSA EQUAÇÃO NÃO POSSUI RAIZES REAIS")
