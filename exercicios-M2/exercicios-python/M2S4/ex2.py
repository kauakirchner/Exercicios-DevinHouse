# Modifique o exercício 1 e defina que a construção da instância seja feita com o nome do titular, 
# numero, saldo e limite para a conta.

print(' -------- Exercício-2 --------')

class Conta_bancaria:
    def __init__(self, nome_titular, numero, saldo, limite):
        self.nome_titular = nome_titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

conta = Conta_bancaria('Kauã', 1212, 10000000000, 99999999999999999999)
print(f'O nome do titular é: {conta.nome_titular} número da conta: {conta.numero} com saldo de: {conta.saldo} e limite de: {conta.limite}')