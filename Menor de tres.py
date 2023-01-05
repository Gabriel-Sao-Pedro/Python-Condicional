x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
z = int(input("Digite o terceiro valor: "))

if (x > y):
    if (y > z):
        print("MENOR = {}".format(z))
    else:
        print("MENOR = {}".format(y))
elif (y > x):
    if (x > z):
        print("MENOR = {}".format(z))
    else:
        print("MENOR = {}".format(x))
else:
    if (x > y):
        print("MENOR = {}".format(y))
    else:
        print("MENOR = {}".format(x))
