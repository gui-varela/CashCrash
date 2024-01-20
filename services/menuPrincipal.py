from despedida import despedidaController
from time import sleep

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
    else:
      print("\nESCOLHA INVÁLIDA.\nDigite um número de 1 a 6.\n")
      sleep(4)


menuPrincipalController()