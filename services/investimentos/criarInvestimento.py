from crud import ler_dados, salvar_dados, criarInvestimento

    
def adicionarInvestimento(valor, tipo):
    informacoes = '''
    ----------------------------------
        INVESTIMENTO REALIZADO!
    ----------------------------------
    O investimento de tipo {} foi realizado 
    com sucesso, e pode ser acessado na consulta 
    de investimentos nome menu (opção 4).

    [1] - Investir novamente
    [2] - Menu Principal

    '''.format(tipo)

    dados = ler_dados()
    novoInvestimento = criarInvestimento(valor, tipo)
    dados.append(novoInvestimento)
    salvar_dados(dados)
    while True:
        respUsuario = input(informacoes)
        if respUsuario == '1':
            from services.investimentos.investir import InvestimentoMenuControler
            InvestimentoMenuControler()
            break
        elif respUsuario == "2":
            from services.menuPrincipal import menuPrincipalController
            menuPrincipalController()
            break