# Construa um método de transferencia de conta e coloque como parametros de transferencia, 
# o "objeto" relativo a conta que receberá o dinheiro e o valor a ser transferido.
#  Verificar na rotina se a conta1 possui valor a transferir.


print(' -------- Exercício-6 --------')

class Conta_bancaria:
    def __init__(self, nome_titular, numero, saldo, limite):
        self.nome_titular = nome_titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
    
    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        self.saldo = self.saldo - valor

    def transferencia(self, valor, conta_2, conta_1):
        if self.saldo > 0 | valor <= self.saldo:
            self.sacar(valor)
            conta_2.depositar(valor)
            print(f'Foi transferido {valor} R$ para a conta 2, seu saldo agora é de: {conta_1.saldo}')
            return True

        if self.saldo <= 0:
            print(f'Você não pode realizar uma transferência, pois não há saldo em sua conta.')
            return False
        
        if self.saldo < valor:
            print(f'O valor solicitado é maior que o seu saldo atual. Seu saldo {conta_1.saldo}.')
            return False

        


c1 = Conta_bancaria('Kauã', 1212, 3000, 919191919)
c2 = Conta_bancaria('José', 1313, 1000, 919191919)
c1.transferencia(2000, c2, c1)


