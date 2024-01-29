from time import sleep

from services.investimentos.criarInvestimento import adicionarInvestimento

textoMenu = '''
----------------------------------
           INVESTIR
----------------------------------
Insira o valor a investir: '''

escolhaInvestimento = '''
[1] - CDB (0,039%/dia)
[2] - LCI (0,038%/dia)
[3] - LCA (0,036%/dia)
[4] - Voltar ao menu principal

Escolha um titulo para investir: '''


def InvestimentoMenuControler():
    while True:
        while True:
            valorInvestido = input(textoMenu)
            try:
                float(valorInvestido)
                break
            except:
                print("\n\nNão pode investir um valor vazio.\n")
        entrada_usuario = input(escolhaInvestimento)
        if entrada_usuario == "1":
            tipo = "CDB"
            adicionarInvestimento(valorInvestido, tipo)
            break
        elif entrada_usuario == "2":
            tipo = "LCI"
            adicionarInvestimento(valorInvestido, tipo)
            break
        elif entrada_usuario == "3":
            tipo = "LCA"
            adicionarInvestimento(valorInvestido, tipo)
            break
        elif entrada_usuario == "4":
            from services.menuPrincipal import menuPrincipalController
            menuPrincipalController()
            break
        else:
            print("\nOpção inválida.\nDigite um número de 1 a 4.\n")
            sleep(3)