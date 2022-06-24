# Crie um arquivo JSON com valores vazios e as chaves contendo os mesmos valores do exercício 6. 

# Leia o arquivo, insira dados nas chaves e imprima no terminal.

# Obs:. Caso possua problemas com diretórios, utilize o os.path para te auxiliar no acesso ao arquivo.

import json

print('---------- Exercício-7 ----------')

nome_usuario = str(input('Insira seu nome: '))
sobrenome_usuario = str(input('Seu sobrenome: '))
idade_usuario = str(input('Sua idade: '))

dicionario_infos = {}

dicionario_infos['nome'] = f'{nome_usuario}'
dicionario_infos['sobrenome'] = f'{sobrenome_usuario}'
dicionario_infos['idade'] = idade_usuario

dicionario_json = json.dumps(dicionario_infos)

print(dicionario_json)