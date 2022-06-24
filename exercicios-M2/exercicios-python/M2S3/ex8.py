import json

print('---------- Exercício-8 ----------')

dicionario = {'nome': 'Kaua', 'sobrenome': 'Kirchner', 'idade': '17'}
dicionario_json = json.dumps(dicionario)

print(dicionario_json)

def escreve_json():
    nome_usuario = str(input('Insira seu nome: '))
    sobrenome_usuario = str(input('Seu sobrenome: '))
    idade_usuario = str(input('Sua idade: '))

    dict_infos = {}

    dict_infos['nome'] = f'{nome_usuario}'
    dict_infos['sobrenome'] = f'{sobrenome_usuario}'
    dict_infos['idade'] = idade_usuario

    dict_infos_json = json.dumps(dict_infos)
    print(dict_infos_json)

escreve_json()

    