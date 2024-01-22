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
            sucessoOperacaoController("DEPÓSITO", entradaUsuario)
            break
        elif entradaUsuario == 'voltar':
            menuPrincipalController()
        else:
            print('\n\nvalor inválido. Escreva um numero.\n\n')
            textoDeFalha = '''Escreva 'voltar' para voltar para o menu principal.\n\nInsira o valor do depósito:  '''
            entradaUsuario = input(textoDeFalha)
