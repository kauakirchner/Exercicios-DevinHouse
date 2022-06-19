# Refatore o código desenvolvido no exercicio três utilizando compreensão de listas (list comprehensions)

# Obs:. É esperado que o retorno seja o mesmo, apenas o que deve mudar é a forma como é declarada a lista. 

vetor_numeros = [x for x in range(1, 21)]
menor_elemento = min(vetor_numeros)
print(f'O menor elemento é: {menor_elemento}. E sua posição na lista é: {vetor_numeros.index(menor_elemento)}')


