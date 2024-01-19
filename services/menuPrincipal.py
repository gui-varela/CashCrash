from despedida import despedidaController

entradaUsuario = input('''
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
)

def menuPrincipalController():
  while True:
    if entradaUsuario == "6":
      despedidaController()
      break
    else:
      print("Escolha inválida.\nDigite um número de 1 a 6.")


menuPrincipalController()