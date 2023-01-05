c = int(input("Digite o codigo do produto (1 a 5): "))
if (c > 0 and c <= 5):
    q = int(input("Informe a quantidade comprada: "))

    x = 5.00
    y = 3.50
    z = 4.80
    a = 8.90
    b = 7.32

    if (c == 1):
        v = x * q
        print("Valor a pagar: R$ {:.2F}".format(v))
    elif (c == 2):
        v = y * q
        print("Valor a pagar: R$ {:.2F}".format(v))
    elif (c == 3):
        v = z * q
        print("Valor a pagar: R$ {:.2F}".format(v))
    elif (c == 4):
        v = a * q
        print("Valor a pagar: R$ {:.2F}".format(v))
    else:
        v = b * q
        print("Valor a pagar: R$ {:.2F}".format(v))
else:
    print("Codigo inexistente!!")
