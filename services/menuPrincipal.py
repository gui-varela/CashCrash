import sys
import os
from time import sleep

from services.despedida import despedidaController
from services.editarOuCancelar.opcoesMenu import menuEditarOuCancelar
from services.extrato.filtro import consultarExtrato
from services.investimentos.menuInvestimentos import menuInvestimentosController
sys.path.append('services\editarOuCancelar')
#import opcoesMenu
#from opcoesMenu import menuEditarOuCancelar
<<<<<<< HEAD
=======
sys.path.append('services\editarOuCancelar')
>>>>>>> 0ed5591f05e7891031a55789df4e8962896c79b4
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
<<<<<<< HEAD
        entradaUsuario = input(textoMenu)
=======
        entradaUsuario = input(textoMenu.format(
            "Bem-vindo! " if isPrimeiroAcesso else "Olá!"
        ))

>>>>>>> 0ed5591f05e7891031a55789df4e8962896c79b4
        if entradaUsuario == "6":
            despedidaController()
            break
        elif entradaUsuario == "1":
            consultarExtrato()
            break
        elif entradaUsuario == "2":
            iniciarDeposito()
            break
        elif entradaUsuario == "3":
            iniciarSaque()
            break
        elif entradaUsuario == "4":
            menuInvestimentosController()
            break
        elif entradaUsuario == "5":
            menuEditarOuCancelar()
            break
        else:
            print("\nESCOLHA INVÁLIDA.\nDigite um número de 1 a 6.\n")
            sleep(4)
