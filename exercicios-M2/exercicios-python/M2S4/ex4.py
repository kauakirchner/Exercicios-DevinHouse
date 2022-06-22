# Construa um método de depósito a conta, tendo como argumento necessário o valor a ser depositado.

print(' -------- Exercício-4 --------')

class Conta_bancaria:
    def __init__(self, nome_titular, numero, saldo, limite):
        self.nome_titular = nome_titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
    
    def deposito(self):
        valor_deposito = int(input('Quanto deseja depositar? '))
        novo_saldo = self.saldo - valor_deposito
        print(f'Depósito de {valor_deposito} feito! Seu saldo agora é de: {novo_saldo}')

conta = Conta_bancaria('Kauã', 1212, 10000000000, 99999999999999999999)
conta.deposito()
