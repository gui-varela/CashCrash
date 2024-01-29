from time import sleep

from services.investimentos.filtro import filtroInvestimentosController
from services.investimentos.investir import InvestimentoMenuControler

textoMenu = '''
----------------------------------
           INVESTIMENTOS
----------------------------------
O que você deseja fazer?

[1] - Consultar investimentos
[2] - Investir
[3] - Voltar para o menu principal

Sua escolha: '''

def menuInvestimentosController():
    while True:
        entrada_usuario = input(textoMenu)
        if entrada_usuario == "1":
            filtroInvestimentosController()
            break
        elif entrada_usuario == "2":
            InvestimentoMenuControler()
            break
        elif entrada_usuario == "3":
            from services.menuPrincipal import menuPrincipalController
            menuPrincipalController()
            break
        else:
            print("\nOpção inválida.\nDigite um número de 1 a 3.\n")
            sleep(3)