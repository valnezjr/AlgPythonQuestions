numero = int(input("Digite um número: "))
palavra =(input("Digite uma palavra de sua preferência em CAIXA ALTA: "))
for i in range(1, 101, 1):
    if i % numero == 0:
        print(palavra, end =" ")
    else:
        print(i, end =" 5")