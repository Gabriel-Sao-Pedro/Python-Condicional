g = float(input("Informe a medida da glicose: "))

if (g <= 100):
    print("CLASSIFICAÇÃO: Normal")
elif (g > 100 and g <= 140):
    print("CLASSIFICAÇÃO: Elevado!!")
else:
    print("CLASSIFICAÇÃO: Diabetes!!!!")
