import crud

def executaApp():
    while True:
        print("\n1. Listar Registros")
        print("2. Adicionar Registro")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            crud.listar_registros()
        elif escolha == '2':
            nome = input("Digite o nome: ")
            idade = input("Digite a idade: ")
            crud.adicionar_registro(nome, idade)
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

executaApp()
