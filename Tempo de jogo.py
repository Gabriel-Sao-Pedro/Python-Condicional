x = int(input("Hora inicial: "))
y = int(input("Hora final: "))
if ((x >= 0 and x <= 24) and (y >= 0 and y <= 24)):
    if (x >= y):
        a = 24 - x
        b = y - 0
        t = a + b
        print("O JOGO DUROU {} HORAS".format(t))
    else:
        t = y - x
        print("O JOGO DUROU {} HORAS".format(t))
else:
    print("HORARIO INVALIODO")
