s = int(input("Informe o salario da pessoa: "))

if (s <= 1000):
    a = s * 0.2
    n = s + a
    print("Novo salario = {}" .format(n))
    print("Aumento = {}" .format(a))
    print("Porcentagem = 20%")
elif (s > 1000 and s <= 3000):
    a = s * 0.15
    n = s + a
    print("Novo salario = {}" .format(n))
    print("Aumento = {}" .format(a))
    print("Porcentagem = 15%")
elif (s > 3000 and s <= 8000):
    a = s * 0.1
    n = s + a
    print("Novo salario = {}" .format(n))
    print("Aumento = {}" .format(a))
    print("Porcentagem = 10%")
else:
    a = s * 0.05
    n = s + a
    print("Novo salario = {}" .format(n))
    print("Aumento = {}" .format(a))
    print("Porcentagem = 5%")
