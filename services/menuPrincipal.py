import sys
import os
from time import sleep

from services.despedida import despedidaController
from services.editarOuCancelar.opcoesMenu import menuEditarOuCancelar
from services.extrato.filtro import consultarExtrato
sys.path.append('services\editarOuCancelar')
#import opcoesMenu
#from opcoesMenu import menuEditarOuCancelar
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
            print("Apertou 4")
            break
        elif entradaUsuario == "5":
            menuEditarOuCancelar()
            break
        else:
            print("\nESCOLHA INVÁLIDA.\nDigite um número de 1 a 6.\n")
            sleep(4)
