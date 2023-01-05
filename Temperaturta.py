e = str(input("Informe qual escala vai informar a temperatura (C / F): "))

if (e == "F"):
    f = float(input("Digite a temperatura em Fahrenheit: "))
    c = ((5*(f - 32)) / (9))
    print("Temperatura equivalente em Celcius: {:.2f}" .format(c))
elif (e == "C"):
    c = float(input("Digite a temperatura em Celsius: "))
    f = (((9*c) + 160) / 5)
    print("Temperatura equivalente em Celcius: {:.2f}".format(f))
else:
    print("COMANDO INCORRETO. Digite C ou F")
