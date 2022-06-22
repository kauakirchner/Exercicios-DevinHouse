# Construa um método de saque que verifique se o usuário possui saldo e/ou limite para saque. 
# O método deve retornar True/False e convertido em texto para usuário como 
# "Saque liberado" ou "Valor indisponível para saque"

print(' -------- Exercício-5 --------')

class Conta_bancaria:
    def __init__(self, nome_titular, numero, saldo, limite):
        self.nome_titular = nome_titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
  
    
    def saque(self):
        if self.saldo > 0:
            valor_saque = int(input('Qual valor deseja sacar? '))
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
      

conta = Conta_bancaria('Kauã', 1212, 0, 10)
conta.saque()
