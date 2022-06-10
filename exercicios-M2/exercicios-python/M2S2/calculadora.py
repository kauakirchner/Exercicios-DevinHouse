def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y



print('Realize um calculo com uma das 4 operações!!')

while True:
    
    operacao = input('qual operação deseja fazer? soma, subtração, multiplicação ou divisão? ')
    if operacao == 'sair':
        print('Fim do programa')
        break


    primeiroNumero = int(input('Digite um número: '))
    segundoNumero = int(input('Digite outro número: '))

    if operacao == 'soma':
        print('O resultado é: ',soma(primeiroNumero, segundoNumero))

    if operacao == 'subtração':
        print('O resultado é: ',subtracao(primeiroNumero, segundoNumero))

    if operacao == 'multiplicação':
        print('O resultado é: ',multiplicacao(primeiroNumero, segundoNumero))

    if operacao == 'divisão':
        print('O resultado é: ',divisao(primeiroNumero, segundoNumero))


    querContinuar = input('Deseja continuar S ou N? ')
    if querContinuar == 'N':
        print('Fim do programa')
        break


