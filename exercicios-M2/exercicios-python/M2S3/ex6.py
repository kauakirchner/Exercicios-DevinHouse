print('---------- Exercício 6 ----------')

nome_usuario = str(input('Insira seu nome: '))
sobrenome_usuario = str(input('Seu sobrenome: '))
idade_usuario = int(input('Sua idade: '))

dicionario_infos = {}

dicionario_infos['nome'] = f'{nome_usuario}'
dicionario_infos['sobrenome'] = f'{sobrenome_usuario}'
dicionario_infos['idade'] = idade_usuario

print(dicionario_infos)
