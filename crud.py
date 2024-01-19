import json

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

def criar_registro(nome, idade):
    return {'nome': nome, 'idade': idade}

def listar_registros():
    dados = ler_dados()
    for i, registro in enumerate(dados, 1):
        print(f"{i}. Nome: {registro['nome']}, Idade: {registro['idade']}")

def adicionar_registro(nome, idade):
    dados = ler_dados()
    novo_registro = criar_registro(nome, idade)
    dados.append(novo_registro)
    salvar_dados(dados)
    print("Registro adicionado com sucesso!")
