# Faça um algoritmo que: 

# - Receba dois valores do usuário (X e Y);
# - Retorne o tamanho de cada valor inserido;
# - Concatene os valores inseridos e retorne esse novo valor (Z);
# - Repita o primeiro valor em inserido por tres vezes e retorne esse valor;
# - Valide se X está contido Z e se Y está contido em Z;
# - Imprima a primeira posição de X e a última posição de Y;




x = str(input('Digite um texto: '))
y = str(input('Digite outro texto: '))

print('O tamanho de x é: ', len(x))
print('O tamanho de y é: ', len(y))

z = x + y
print('A concatenção de x e y é: ', z)

print('x está contido em z? ', x in z)

print('A primeira posição de x é: ', x[0])
print('A ultima posição de y é: ', y[-1])
