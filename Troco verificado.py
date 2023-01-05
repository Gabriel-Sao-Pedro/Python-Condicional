p = float(input("Informe o valor do produto: "))
q = int(input("informe a quantidade comprada: "))
v = float(input("Informe o valor recebido: "))

x = p * q
t = v - x

if (t < 0):
    y = -(t)
    print("Valor insuciente. Faltam {:.2f} reais.".format(y))
elif (t == 0):
    print("NÃO POSSUI TROCO")
else:
    print("Troco = R${:.2f}".format(t))
