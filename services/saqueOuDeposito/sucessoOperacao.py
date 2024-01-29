from services.despedida import despedidaController
from crud import ler_saldo

def sucessoOperacaoController(nomeOp):
    #atrasar a importação do módulo menuPrincipalController até o momento em que 
    #ele é realmente necessário, evitando assim a importação circular.  ----Credito ChatGPT / stackoverflow
    
    from services.menuPrincipal import menuPrincipalController
    saldo = ler_saldo()
    textoMenu = '''
----------------------------------
           {} REALIZADO!
----------------------------------
{} realizado com sucesso! Saldo após a operação:

R$ {}

[1] - Menu principal

Sua escolha: '''.format(nomeOp, nomeOp.capitalize(), saldo)
    
    while True:
        entradaUsuario = input(textoMenu)
        
        if entradaUsuario == "1":
            menuPrincipalController(isPrimeiroAcesso = False)
            break
        else:
            print("\nESCOLHA INVÁLIDA.\nDigite 1 para voltar ao menu principal.\n")
