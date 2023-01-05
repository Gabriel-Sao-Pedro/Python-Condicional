m = int(input("Informe a quantidade de minutos: "))
p = 50

if (m > 100):
    t = m - 100
    v = 2 * t
    x = p + v
    print("Valor a pagar: R$ {:.2F}".format(x))
else:
    print("Valor a pagar: R$ {:.2F}".format(p))
