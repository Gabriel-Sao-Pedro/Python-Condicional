print("DIGITE TRES DISTANCIAS:")
x = float(input())
y = float(input())
z = float(input())

if (x > y):
    if (x > z):
        print("MAIOR DISTANCIA {}".format(x))
    else:
        print("MAIOR DISTANCIA {}".format(z))
else:
    if (y > z):
        print("MAIOR DISTANCIA {}".format(y))
    else:
        print("MAIOR DISTANCIA {}".format(z))
