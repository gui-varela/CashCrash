import json
import sys
sys.path.append('services\editarOuCancelar\cancelamento')
import cancelarOperacao
def ler_dados():
    try:
        with open('database/registros.json', 'r') as arquivo:
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

#WIP: cancelar registro
def deletar_registro(dados, id_change):
        index_to_delete = None
        for i, item in enumerate(dados):
            if item.get('id') == id_change:
                index_to_delete = i
                break
        # If the element is found, delete it
        if index_to_delete is not None:
            del dados[index_to_delete]
            print(f'''
----------------------------------
        CANCELADO COM SUCESSO!
----------------------------------
A operação de ID {id_change} foi cancelada e não será realizada!
''')
        else:
            print(f"Elemento com ID {id_change} não encontrado.")
        salvar_dados(dados)

