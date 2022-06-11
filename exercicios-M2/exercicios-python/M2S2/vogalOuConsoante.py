print('Digite uma letra e o oráculo dirá se é vogal ou consoante!')
print('Lembrando que para pausar a execução do programa basta digitar "0"')

while True:

    letraDigitada = input('Digite uma letra: ')

    if letraDigitada == '0':
        print('Até mais!!')
        break

    if letraDigitada != 'a' and 'e' and 'i' and 'o' and  'u' and '0':
        print(letraDigitada, ' É consoante')

    if letraDigitada  == 'a' and 'e' and 'i' and 'o' and  'u':
        print(letraDigitada, ' É vogal')

 