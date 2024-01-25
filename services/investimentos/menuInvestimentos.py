from anyio import sleep


textoMenu = '''
----------------------------------
           INVESTIMENTOS
----------------------------------
O que você deseja fazer?

[1] - Consultar investimentos
[2] - Investir
[3] - Voltar para o menu principal
'''

def menuPrincipalController():
    while True:
        entradaUsuario = input(textoMenu)
        if entradaUsuario == "1":
            print("Apertou 1")
            #despedidaController()
            break
        elif entradaUsuario == "2":
            print("Apertou 2")
            #iniciarDeposito()
            break
        elif entradaUsuario == "3":
            from services.menuPrincipal import menuPrincipalController
            menuPrincipalController()
            break
        else:
            print("\nESCOLHA INVÁLIDA.\nDigite um número de 1 a 3.\n")
            sleep(4)