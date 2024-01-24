import json
from crud import adicionar_registro
from services.saqueOuDeposito.sucessoOperacao import sucessoOperacaoController


textoMenu = '''
----------------------------------
           DEPÓSITO
----------------------------------
Escreva 'voltar' para voltar para o menu principal.

Insira o valor do depósito:  '''

def iniciarDeposito():
    from services.menuPrincipal import menuPrincipalController
    entradaUsuario = input(textoMenu)
    while True:
        if entradaUsuario.isnumeric():
            adicionar_registro("deposito", entradaUsuario)
            sucessoOperacaoController("DEPOSITO")
            break
        elif entradaUsuario == 'voltar':
            menuPrincipalController(isPrimeiroAcesso = False)
        else:
            print('\n\nvalor inválido. Escreva um numero.\n\n')
            textoDeFalha = '''Escreva 'voltar' para voltar para o menu principal.\n\nInsira o valor do depósito:  '''
            entradaUsuario = input(textoDeFalha)
