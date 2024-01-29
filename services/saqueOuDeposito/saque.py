from crud import adicionar_registro
from services.saqueOuDeposito.sucessoOperacao import sucessoOperacaoController


textoMenu = '''
----------------------------------
           SAQUE
----------------------------------
Escreva 'voltar' para voltar para o menu principal.

Insira o valor do saque:  '''

def iniciarSaque():
    from services.menuPrincipal import menuPrincipalController
    entradaUsuario = input(textoMenu)
    while True:
        if entradaUsuario.isnumeric():
            adicionar_registro("saque", entradaUsuario)
            sucessoOperacaoController("SAQUE", entradaUsuario)
            break
        elif entradaUsuario == 'voltar':
            menuPrincipalController()
        else:
            print('\n\nvalor inválido. Escreva um numero.\n\n')
            textoDeFalha = '''Escreva 'voltar' para voltar para o menu principal.\n\nInsira o valor do saque:  '''
            entradaUsuario = input(textoDeFalha)
