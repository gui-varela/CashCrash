import sys
import os
from time import sleep

from services.despedida import despedidaController
from services.editarOuCancelar.opcoesMenu import menuEditarOuCancelar
sys.path.append('services\editarOuCancelar')
from services.saqueOuDeposito.deposito import iniciarDeposito
from services.saqueOuDeposito.saque import iniciarSaque

textoMenu = '''
----------------------------------
           MENU PRINCIPAL
----------------------------------
{}O que deseja fazer?

[1] - Consultar extrato
[2] - Depositar
[3] - Sacar
[4] - Acessar investimentos
[5] - Editar/Cancelar operação
[6] - Sair

Sua escolha: '''

def menuPrincipalController(isPrimeiroAcesso = True):
    while True:
        entradaUsuario = input(textoMenu.format(
            "Bem-vindo! " if isPrimeiroAcesso else "Olá!"
        ))

        if entradaUsuario == "6":
            despedidaController()
            break
        elif entradaUsuario == "2":
            iniciarDeposito()
            break
        elif entradaUsuario == "3":
            iniciarSaque()
            break
        elif entradaUsuario == "5":
            menuEditarOuCancelar()
            break
        else:
            print("\nESCOLHA INVÁLIDA.\nDigite um número de 1 a 6.\n")
            sleep(3)
