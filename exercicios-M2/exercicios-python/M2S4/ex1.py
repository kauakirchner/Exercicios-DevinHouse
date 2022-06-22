# Utilizando conceitos de POO, crie um programa bancário que a cada nova declaração seja criada uma
# **instância** de uma conta de banco.

print(' -------- Exercício-1 --------')
class Conta:
    def __init__(self, conta, agencia):
        self.conta = conta
        self.agencia = agencia

conta = Conta(111, 222)

        
