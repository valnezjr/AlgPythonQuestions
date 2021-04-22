comeco = int(input('Escreva um valor inteiro para começara sequência: '))
final = int(input('Escreva o último número inteiro da sequência: '))

if comeco < final:
    for i in range(comeco, final +1, 1):
        print(i, end = " ")
else:
    for i in range(comeco, final -1, -1):
        print(i, end = " ")