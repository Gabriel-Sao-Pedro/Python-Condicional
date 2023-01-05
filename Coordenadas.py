x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

if (x > 0):
    if (y > 0):
        print("Q1")
    elif (y == 0):
        print("EIXO X")
    else:
        print("Q4")
elif (x == 0):
    if (y > 0):
        print("EIXO Y")
    elif (y == 0):
        print("ORIGEM")
    else:
        print("EIXO Y")

else:
    if (y < 0):
        print("Q3")
    elif (y == 0):
        print("EIXO X")
    else:
        print("Q2")
