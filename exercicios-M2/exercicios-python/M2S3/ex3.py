# Faça um algoritmo que leia um vetor N[20]. A seguir, encontre o menor elemento do vetor N e a sua posição dentro da lista, mostrando:
#  “O menor elemento de N é”, M, “e sua posição dentro da lista é:”,P.
# Output esperado:

# > "O menor elemento de N é {numero} e a sua posição dentro da lista é  {posicao}"

# Obs:. Utilize um dos métodos de formatação de strings vistos em sala de aula

vetor_numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
menor_elemento = min(vetor_numeros)

print(f'O menor elemento é {menor_elemento} e sua posição na lista é: {vetor_numeros.index(menor_elemento)}')
