# 1 - Saque (perguntar valor a ser sacado)
# 2 - Depósito (perguntar valor a ser depositado)
# 3 - Transferência (perguntar valor a ser transferido)
# 4 - Sair (encerrar aplicação)

# E relacione os itens do menu ao programa construído ao longo dos exercícios.
# Como está como aprendizado, inicialize duas contas c1 e c2 com um saldo predefinido para continuar a construção do programa. 
# Considere c1 como a conta manipulada e c2 a conta de um cliente que receberá uma eventual transferência.



print(' -------- Exercício-7 --------')
qual_operacao = str(input(f'O que deseja fazer? Saque[1] Depósito[2] Transferência[3] Sair[4] '))

class Conta_bancaria:
    def __init__(self, nome_titular, numero, saldo, limite):
        self.nome_titular = nome_titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
    

    def saque(self):
        if self.saldo > 0:
            valor_saque = int(input('Qual valor deseja sacar?  '))
            if valor_saque > self.limite:
                print(f'Você não pode realizar um saque de valor superior a seu limite que é: {self.limite}')
                return False
            
            elif valor_saque <= self.limite:
                novo_saldo = self.saldo - valor_saque
                print(f'Você sacou {valor_saque} R$, agora seu saldo é de: {novo_saldo}')
                return True

        if self.saldo <= 0:
            print('Você não possue dinheiro nesta conta, portanto não pode sacar!')
            return False


    def deposito(self):
        valor_deposito = int(input('Quanto deseja depositar?  '))
        novo_saldo = self.saldo + valor_deposito
        print(f'Depósito de {valor_deposito} feito! Seu saldo agora é de: {novo_saldo}')

    def sacar_para_transferencia(self, valor):
        self.saldo = self.saldo - valor

    def depositar_para_transferencia(self, valor):
        self.saldo = self.saldo + valor

    def transferencia(self, conta_1, conta_2):
        valor = int(input('Qual valor deseja transferir?  '))
        if self.saldo > 0 or valor <= self.saldo:
            conta_1.sacar_para_transferencia(valor)
            conta_2.depositar_para_transferencia(valor)
            print(f'Foi transferido {valor} R$ para a conta 2, seu saldo agora é de: {conta_1.saldo}')
            return True

        if self.saldo <= 0:
            print(f'Você não pode realizar uma transferência, pois não há saldo em sua conta.')
            return False
        
        if self.saldo < valor:
            print(f'O valor solicitado é maior que o seu saldo atual. Seu saldo {conta_1.saldo}.')
            return False

    def sair(self):
        print(f'Fim do programa, até mais {self.nome_titular}')

        


c1 = Conta_bancaria('Kauã', 1212, 2000, 919191919)
c2 = Conta_bancaria('José', 1313, 1000, 919191919)

 
if qual_operacao == '1':
    c1.saque()

if qual_operacao == '2':
    c1.deposito()

if  qual_operacao == '3':
    c1.transferencia(c1, c2)

if qual_operacao == '4':
    c1.sair()
