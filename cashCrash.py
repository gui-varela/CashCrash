import json
ID = 0
def ler_dados():
    try:
        with open('registros.json', 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = []
    
    return dados

def salvar_dados(dados):
    with open('registros.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=2)

def criar_registro(ID, nome, idade):
    return {'ID':ID,'nome': nome, 'idade': idade}

def listar_registros():
    dados = ler_dados()
    for i, registro in enumerate(dados, 1):
        print(f"{i}. ID:{registro['ID']} Nome: {registro['nome']}, Idade: {registro['idade']}")

def adicionar_registro(ID, nome, idade):
    dados = ler_dados()
    novo_registro = criar_registro(ID, nome, idade)
    dados.append(novo_registro)
    salvar_dados(dados)
    print("Registro adicionado com sucesso!")

def deletar_registro(dados, index_delete):
        index_to_delete = None
        for i, item in enumerate(dados):
            if item.get('ID') == index_delete:
                index_to_delete = i
                break
        # If the element is found, delete it
        if index_to_delete is not None:
            del dados[index_to_delete]
        else:
            print(f"Element with ID {index_delete} not found.")
        salvar_dados(dados)
# Exemplo de utilização
while True:
    print("\n1. Listar Registros")
    print("2. Adicionar Registro")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        listar_registros()
    elif escolha == '2':
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        ID = ID + 1
        adicionar_registro(ID, nome, idade)
    elif escolha == '3':
        index_delete = int(input("Insira o ID da entrada que deseja remover"))
        ler_dados()
        try:
            with open('registros.json', 'r') as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            dados = []        
        deletar_registro(dados, index_delete)
    elif escolha == '5':
        break
    else:
        print("Opção inválida. Tente novamente.")
