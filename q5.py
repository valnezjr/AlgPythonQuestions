valor = int(input("Digite um número para informarmos a tabuada:"))
for i in range(1, 11, 1):
    print("{0} x {1} = {2}".format(valor, i, valor*i))