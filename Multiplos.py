print("Digite dois numeros:")
x = int(input())
y = int(input())

if (x > y):
    m = x % y
else:
    m = y % x

if (m == 0):
    print("SÃO MULTIPLOS")
else:
    print("NÃO SÃO MULTIPLOS")
