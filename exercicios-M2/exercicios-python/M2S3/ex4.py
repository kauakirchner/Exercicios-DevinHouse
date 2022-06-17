# Escreva uma função que tenha a responsabilidade de formatar texto.
#  Esta função deve receber parâmetros necessários para a construção do print e por fim retornar o texto centralizado
# entre caracteres definidos pelo usuarios. Caso o usuário não defina nenhum caracter, mantenha um valor padrão. 

# Retorno esperado: 
# > ------------------------ DEVINHOUSE ------------------------

texto_usuario = str(input('Digite um texto: '))

def formataString(text):
    if(text):
        return f'------------------------ {text} ------------------------'
    
    return '------------------------ Não há texto digitado!! ------------------------'

print(formataString(texto_usuario.upper()))  