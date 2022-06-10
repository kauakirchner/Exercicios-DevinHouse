while True:

    print('Digite dois números que o oráculo te mostrará o maior deles')

    numeroX = int(input('Digite um número: '))
    numeroY = int(input('Digite outro número: '))
    if numeroX > numeroY:
        print(numeroX, 'É o maior número')

    if numeroY > numeroX:
        print(numeroY, 'É o maior número')


    querContinuar = input('Bora mais uma? S ou N? ')

    if querContinuar == 'N':
        print('Até mais...')
        break


