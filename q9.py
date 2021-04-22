contadorp = 0
contadori = 0

for i in range(1, 11, 1):
    valor = int(input('Escreva um valor inteiro: '))

    if valor % 2 == 0:
        contadorp = contadorp + 1
    else:
        contadori = contadori + 1
print('A quantidade de valores pares foi de: {}'.format(contadorp))
print('A quantidade de valores ímpares foi de: {}'.format(contadori))