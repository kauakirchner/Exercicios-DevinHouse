# Construa um método de extrato que retorne o valor presente na conta manipulada.

print(' -------- Exercício-3 --------')

class Conta_bancaria:
    def __init__(self, nome_titular, numero, saldo, limite):
        self.nome_titular = nome_titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
    
    def extrato(self):
        print(f'Seu saldo é de: {self.saldo}')
        return self.saldo

conta = Conta_bancaria('Kauã', 1212, 10000000000, 99999999999999999999)
conta.extrato()
