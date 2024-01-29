import sys
import os
from time import sleep
sys.path.append('c:/Users/netoo/OneDrive/Área de Trabalho/projetoCC/CashCrash')
sys.path.append('c:/Users/netoo/OneDrive/Área de Trabalho/projetoCC/CashCrash/services/editarOuCancelar')
from services.despedida import despedidaController
from services.editarOuCancelar.opcoesMenu import menuEditarOuCancelar
from services.extrato.filtro import consultarExtrato
from services.investimentos.menuInvestimentos import menuInvestimentosController
from services.saqueOuDeposito.deposito import iniciarDeposito
from services.saqueOuDeposito.saque import iniciarSaque

textoMenu = '''
----------------------------------
           MENU PRINCIPAL
----------------------------------
Bem-vindo! O que deseja fazer?

[1] - Consultar extrato
[2] - Depositar
[3] - Sacar
[4] - Acessar investimentos
[5] - Editar/Cancelar operação
[6] - Sair

Sua escolha: '''

def menuPrincipalController():
    while True:
        entradaUsuario = input(textoMenu)

        print(f"Você escolheu: {entradaUsuario}")  # Adicionado para debug
        if entradaUsuario == "6":
            despedidaController()
            break
        elif entradaUsuario == "1":
            print("Chamando consultarExtrato")  # Adicionado para debug
            consultarExtrato()
            break
        elif entradaUsuario == "2":
            print("Chamando iniciarDeposito")  # Adicionado para debug
            iniciarDeposito()
            break
        elif entradaUsuario == "3":
            print("Chamando iniciarSaque")  # Adicionado para debug
            iniciarSaque()
            break
        elif entradaUsuario == "4":
            print("Chamando menuInvestimentosController")  # Adicionado para debug
            menuInvestimentosController()
            break
        elif entradaUsuario == "5":
            print("Chamando menuEditarOuCancelar")  # Adicionado para debug
            menuEditarOuCancelar()
            break
        else:
            print("\nESCOLHA INVÁLIDA.\nDigite um número de 1 a 6.\n")
            sleep(4)

if __name__ == "__main__":
    menuPrincipalController()
